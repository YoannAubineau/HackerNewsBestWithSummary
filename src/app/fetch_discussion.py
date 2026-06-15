import html
import re
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from datetime import datetime

import httpx
import structlog
from pydantic import BaseModel, ConfigDict, Field, ValidationError
from tenacity import (
    RetryError,
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)
from youtube_transcript_api.proxies import WebshareProxyConfig

from app.config import get_settings

_ALGOLIA_URL = "https://hn.algolia.com/api/v1/items/{id}"
_HN_STORY_URL = "https://news.ycombinator.com/item?id={id}"
_TAG_RE = re.compile(r"<[^>]+>")
_LINK_RE = re.compile(r"<a\b[^>]*>(.*?)</a>", re.IGNORECASE | re.DOTALL)
_BLOCK_BREAK_RE = re.compile(r"</?(p|div|pre|blockquote|li)\s*>", re.IGNORECASE)
_LINE_BREAK_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)
_BLANK_LINES_RE = re.compile(r"\n{3,}")
_WHITESPACE_RE = re.compile(r"\s+")
_BLOCKQUOTE_LINE_RE = re.compile(r"^>\s?")
_COMMENT_ROW_RE = re.compile(
    r'class="athing comtr" id="(\d+)"[^>]*?>.*?indent="(\d+)"',
    re.DOTALL,
)

log = structlog.get_logger()


class AlgoliaItem(BaseModel):
    """Schema of Algolia HN items.

    All fields are optional: we only rely on ``author``, ``text`` and
    ``children`` during traversal, and the API has historically drifted
    in minor ways. Unknown fields are ignored rather than rejected.
    """

    model_config = ConfigDict(extra="ignore")

    id: int | None = None
    author: str | None = None
    text: str | None = None
    url: str | None = None
    points: int | None = None
    title: str | None = None
    created_at: datetime | None = None
    children: list["AlgoliaItem"] = Field(default_factory=list)


AlgoliaItem.model_rebuild()


@dataclass
class TopComment:
    id: int
    author: str
    text: str


@dataclass
class Discussion:
    comment_count: int
    text: str
    top_comments_markdown: str
    url: str | None
    canonical_dupe_id: int | None = None
    title: str | None = None
    source_published_at: datetime | None = None


def fetch_discussion(hn_item_id: int) -> Discussion | None:
    payload = _fetch_algolia_item(hn_item_id)
    if payload is None:
        return None
    canonical_dupe_id = find_dupe_canonical_id(payload)
    if canonical_dupe_id is None:
        canonical_dupe_id = _find_single_comment_redirect(payload)
    if canonical_dupe_id is not None:
        # The current entry was flagged as a duplicate by the first commenter;
        # the caller will substitute or drop it, so skip the HN HTML scrape
        # for top-comment ranking that we are about to throw away.
        return Discussion(
            comment_count=0,
            text="",
            top_comments_markdown="",
            url=None,
            canonical_dupe_id=canonical_dupe_id,
            title=payload.title,
            source_published_at=payload.created_at,
        )
    comments = list(_iter_comments(payload))
    if comments:
        ordered_ids = _fetch_hn_display_order(hn_item_id)
        top_comments = _select_top_comments(payload, ordered_ids)
        text = _render_comments(comments)
        top_comments_markdown = render_top_comments(top_comments)
    else:
        text = ""
        top_comments_markdown = ""
    return Discussion(
        comment_count=len(comments),
        text=text,
        top_comments_markdown=top_comments_markdown,
        url=payload.url,
        title=payload.title,
        source_published_at=payload.created_at,
    )


_DUPE_LINK_RE = re.compile(
    r"https?://news\.ycombinator\.com/item\?id=(\d+)",
    re.IGNORECASE,
)


def find_dupe_canonical_id(payload: AlgoliaItem) -> int | None:
    """Return the HN item id this discussion was marked as a dupe of, or None.

    Detects the moderator (and occasionally regular-user) pattern where the
    first child comment carries a pointer like
    ``dupe: https://news.ycombinator.com/item?id=NNN``. Algolia HTML-escapes
    forward slashes (``&#x2F;``), so we ``html.unescape`` before matching.
    The ``dupe`` keyword is required to avoid false positives on first
    comments that legitimately link to a related HN thread.
    """
    if not payload.children:
        return None
    first = payload.children[0]
    if not first.text:
        return None
    decoded = html.unescape(first.text)
    if "dupe" not in decoded.lower():
        return None
    match = _DUPE_LINK_RE.search(decoded)
    if match is None:
        return None
    canonical_id = int(match.group(1))
    if canonical_id == payload.id:
        return None
    return canonical_id


def _find_single_comment_redirect(payload: AlgoliaItem) -> int | None:
    """Detect a discussion whose only comment links to another HN thread.

    When moderators merge discussions, the original is left with a single
    comment containing a bare link to the canonical thread — without the
    ``dupe`` keyword that ``find_dupe_canonical_id`` requires. The
    single-comment constraint avoids false positives on comments that
    legitimately reference a related thread among many other comments.
    """
    children_with_text = [c.text for c in payload.children if c.text]
    if len(children_with_text) != 1:
        return None
    decoded = html.unescape(children_with_text[0])
    match = _DUPE_LINK_RE.search(decoded)
    if match is None:
        return None
    canonical_id = int(match.group(1))
    if canonical_id == payload.id:
        return None
    return canonical_id


def fetch_submitter_text(hn_item_id: int) -> str:
    """Return the HTML-stripped text the HN submitter posted with the story.

    Used for Ask HN / Tell HN entries, where the interesting "article" content
    is the submitter's own post rather than an external URL. Empty string on
    any HTTP or validation error, or when the root item has no body.
    """
    payload = _fetch_algolia_item(hn_item_id)
    if payload is None or not payload.text:
        return ""
    return _strip_html_preserving_paragraphs(payload.text)


def _fetch_algolia_item(hn_item_id: int) -> AlgoliaItem | None:
    settings = get_settings()
    try:
        response = httpx.get(
            _ALGOLIA_URL.format(id=hn_item_id),
            timeout=settings.http_timeout,
            headers={"User-Agent": settings.user_agent},
        )
        response.raise_for_status()
    except httpx.HTTPError:
        return None
    try:
        return AlgoliaItem.model_validate(response.json())
    except ValidationError as exc:
        log.warning("algolia_payload_invalid", hn_item_id=hn_item_id, error=str(exc))
        return None


def _iter_comments(root: AlgoliaItem) -> Iterator[dict]:
    """Walk the comment tree depth-first and yield every comment with text."""
    for child in root.children:
        yield from _walk(child, depth=0)


def _walk(node: AlgoliaItem, depth: int) -> Iterator[dict]:
    if node.text:
        yield {
            "author": node.author or "?",
            "points": node.points,
            "text": _strip_html(node.text),
            "depth": depth,
        }
    for child in node.children:
        yield from _walk(child, depth + 1)


def _strip_html(text: str) -> str:
    return html.unescape(_TAG_RE.sub("", text))


def _link_text_ratio(raw_html: str, cleaned_length: int) -> float:
    if cleaned_length == 0:
        return 0.0
    total = 0
    for m in _LINK_RE.finditer(raw_html):
        inner = _WHITESPACE_RE.sub(" ", _strip_html(m.group(1))).strip()
        total += len(inner)
    return total / cleaned_length


def _strip_html_preserving_paragraphs(text: str) -> str:
    """Like ``_strip_html`` but keeps block boundaries as blank lines.

    HN submitter posts are typically wrapped in ``<p>...</p>`` blocks; the
    plain tag-strip would glue consecutive paragraphs into a single run
    (``Para 1Para 2``), which the summarization LLM then parses as one
    mashed token. Converting block-level closers and ``<br>`` into
    newlines before stripping keeps the prose readable.
    """
    text = _BLOCK_BREAK_RE.sub("\n\n", text)
    text = _LINE_BREAK_RE.sub("\n", text)
    text = _TAG_RE.sub("", text)
    text = html.unescape(text)
    return _BLANK_LINES_RE.sub("\n\n", text).strip()


def _wrap_initial_blockquote(text: str) -> str:
    """Wrap a leading ``>``-quoted excerpt in French guillemets.

    HN comments commonly start by quoting a prior comment or article
    excerpt with the markdown ``>`` prefix. After paragraph collapse and
    whitespace squashing, the literal ``>`` survives but the end of the
    quoted span becomes invisible, so readers cannot tell where the
    excerpt stops and the reply begins. This helper extracts the
    contiguous leading quoted paragraphs (each line non-empty and starting
    with ``>``), drops the ``>`` prefixes, and wraps the whole excerpt in
    ``« … »`` so the boundary is explicit. Returns ``text`` unchanged when
    no leading blockquote is detected.
    """
    paragraphs = text.split("\n\n")
    quoted_lines: list[str] = []
    consumed = 0
    for para in paragraphs:
        para_lines = [line for line in para.splitlines() if line.strip()]
        if not para_lines:
            break
        if not all(line.startswith(">") for line in para_lines):
            break
        for line in para_lines:
            quoted_lines.append(_BLOCKQUOTE_LINE_RE.sub("", line))
        consumed += 1
    if consumed == 0:
        return text
    quoted = " ".join(quoted_lines).strip()
    if not quoted:
        return text
    rest = "\n\n".join(paragraphs[consumed:])
    if rest:
        return f"« {quoted} »\n\n{rest}"
    return f"« {quoted} »"


def _render_comments(comments: Iterable[dict]) -> str:
    parts: list[str] = []
    for c in comments:
        indent = "  " * c["depth"]
        points = f", {c['points']} pts" if c["points"] is not None else ""
        parts.append(f"{indent}[{c['author']}{points}] {c['text'].strip()}")
    return "\n".join(parts)


_HN_ITEM_URL = "https://news.ycombinator.com/item?id={id}"
_MARKDOWN_SPECIAL_RE = re.compile(r"([\\\[\]()*_`#<>])")


def escape_markdown(text: str) -> str:
    """Backslash-escape Markdown control characters in untrusted plain text.

    HN users control comment and submitter text. Without this, text such as
    ``[clic ici](https://evil)`` would inject an active link into rendered
    Markdown. Backslash escaping preserves the displayed text.
    """
    return _MARKDOWN_SPECIAL_RE.sub(r"\\\1", text)


def _is_retryable_hn_direct_error(exc: BaseException) -> bool:
    """Retry the direct HN fetch only on connection-level transients.

    HN's 429 on a shared GitHub Actions IP typically lasts longer than
    the 2-10 s exponential backoff covers, and we would just hit the
    same throttled IP. Falling through immediately to the Webshare proxy
    path — where each retry draws a fresh residential IP — is strictly
    more productive than burning seconds on the local IP. Connection-
    level transients (timeouts, resets) remain worth retrying on the
    same IP. Any other HTTP error (404, 5xx, malformed response) is
    treated as terminal.
    """
    return isinstance(exc, (httpx.ConnectError, httpx.ReadTimeout))


def _is_retryable_hn_proxy_error(exc: BaseException) -> bool:
    """Retry the proxy HN fetch on 429 and connection-level transients.

    Webshare rotates the egress IP on every request, so a 429 from one
    attempt does not predict a 429 from the next — each retry draws a
    fresh address that independently sidesteps HN's IP throttling.
    """
    if isinstance(exc, httpx.HTTPStatusError):
        return exc.response.status_code == 429
    return isinstance(exc, (httpx.ConnectError, httpx.ReadTimeout))


def _log_hn_response_block(
    resp: httpx.Response, *, hn_item_id: int, via_proxy: bool
) -> None:
    """Diagnostic warning for HN HTML 4xx responses.

    Temporary instrumentation: the cycle workflow has been logging
    ``hn_display_order_proxy_failed`` warnings almost every hour, ~88 % of
    them on the same item, while that item responds 200 OK from a
    residential IP. We want to capture HN's ``Retry-After`` (if any) and a
    snippet of the 4xx body to tell whether HN signals a documented TTL,
    whether 403 vs 429 mean different things, and whether the Webshare
    pool sees the same body as the direct path. Remove once we have a few
    days of samples and have decided on a long-term remediation.
    """
    if not (400 <= resp.status_code < 500):
        return
    body_snippet = _WHITESPACE_RE.sub(" ", resp.text).strip()[:200] if resp.text else ""
    log.warning(
        "hn_html_blocked",
        hn_item_id=hn_item_id,
        status=resp.status_code,
        retry_after=resp.headers.get("retry-after"),
        body_snippet=body_snippet,
        via_proxy=via_proxy,
    )


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=2, min=2, max=10),
    retry=retry_if_exception(_is_retryable_hn_direct_error),
    reraise=True,
)
def _fetch_hn_html(hn_item_id: int) -> str:
    settings = get_settings()
    response = httpx.get(
        _HN_STORY_URL.format(id=hn_item_id),
        timeout=settings.http_timeout,
        headers={"User-Agent": settings.user_agent},
    )
    _log_hn_response_block(response, hn_item_id=hn_item_id, via_proxy=False)
    response.raise_for_status()
    return response.text


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=2, min=2, max=10),
    retry=retry_if_exception(_is_retryable_hn_proxy_error),
    reraise=True,
)
def _fetch_hn_html_via_proxy(hn_item_id: int) -> str:
    """Up to three attempts against HN through the Webshare residential pool.

    Each request comes from a fresh rotating residential IP, which
    bypasses HN's IP-based rate limiting on shared GitHub Actions
    runners. Because Webshare rotates the IP on every HTTP request,
    retrying here is meaningful: each attempt draws a different IP and
    independently avoids any throttled address. Caller is responsible
    for checking that proxy credentials are configured before invoking
    this. Raises ``httpx.HTTPError`` on failure.
    """
    settings = get_settings()
    proxy_url = WebshareProxyConfig(
        proxy_username=settings.webshare_proxy_username,
        proxy_password=settings.webshare_proxy_password,
    ).url
    response = httpx.get(
        _HN_STORY_URL.format(id=hn_item_id),
        timeout=settings.http_timeout,
        headers={"User-Agent": settings.user_agent},
        proxy=proxy_url,
    )
    _log_hn_response_block(response, hn_item_id=hn_item_id, via_proxy=True)
    response.raise_for_status()
    return response.text


def _fetch_hn_display_order(hn_item_id: int) -> list[int]:
    """Return top-level comment IDs in HN's own display order.

    Per-comment scores are not exposed by Algolia or Firebase, and
    Algolia's ``/items/{id}`` returns children in chronological order
    (by ID), which does not reflect HN's "best" ranking. The HN HTML
    page is the only public source of truth for that ordering, so we
    fetch it and pick out each ``<tr class="athing comtr">`` with
    ``indent="0"``.

    Connection-level transients (``ConnectError``, ``ReadTimeout``) are
    retried up to three times directly. A 429, on the other hand, is
    not retried on the direct path: HN's rate-limit window is far
    longer than the 2-10 s exponential backoff covers, and the same
    shared GitHub Actions IP would just hit the same throttle. Instead,
    we fall through immediately to Webshare when credentials are
    configured. There the retries do pay off: each request draws a
    fresh rotating residential IP, so a 429 on one attempt does not
    predict a 429 on the next. If everything fails, the caller falls
    back to an empty ``top_comments_markdown`` rather than crashing
    the pipeline.
    """
    try:
        text = _fetch_hn_html(hn_item_id)
    except (httpx.HTTPError, RetryError) as direct_exc:
        settings = get_settings()
        if not (
            settings.webshare_proxy_username and settings.webshare_proxy_password
        ):
            log.warning(
                "hn_display_order_fetch_failed",
                hn_item_id=hn_item_id,
                error=str(direct_exc),
            )
            return []
        try:
            text = _fetch_hn_html_via_proxy(hn_item_id)
        except httpx.HTTPError as proxy_exc:
            log.warning(
                "hn_display_order_proxy_failed",
                hn_item_id=hn_item_id,
                direct_error=str(direct_exc),
                proxy_error=str(proxy_exc),
            )
            return []
        log.info(
            "hn_display_order_fetched", hn_item_id=hn_item_id, via_proxy=True
        )
    return [
        int(cid)
        for cid, indent in _COMMENT_ROW_RE.findall(text)
        if indent == "0"
    ]


def _select_top_comments(
    root: AlgoliaItem,
    ordered_ids: list[int],
    n: int = 3,
    max_chars: int = 300,
) -> list[TopComment]:
    """Pick the first ``n`` valid comments from ``ordered_ids``.

    ``ordered_ids`` is HN's display order (see ``_fetch_hn_display_order``);
    their text and author live in the Algolia tree. Deleted/dead comments
    (missing ``author`` or ``text``) and IDs not present in the tree are
    skipped in place. Text is HTML-stripped, internal whitespace
    collapsed, and truncated to ``max_chars`` with a single ``…`` on
    overflow.
    """
    if not ordered_ids:
        return []
    by_id: dict[int, AlgoliaItem] = {
        child.id: child for child in root.children if child.id is not None
    }
    picked: list[TopComment] = []
    for cid in ordered_ids:
        if len(picked) == n:
            break
        node = by_id.get(cid)
        if node is None or node.author is None or node.text is None:
            continue
        with_paragraphs = _strip_html_preserving_paragraphs(node.text)
        wrapped = _wrap_initial_blockquote(with_paragraphs)
        cleaned = _WHITESPACE_RE.sub(" ", wrapped).strip()
        if not cleaned:
            continue
        if _link_text_ratio(node.text, len(cleaned)) > 0.5:
            continue
        if len(cleaned) > max_chars:
            cleaned = cleaned[: max_chars - 1].rstrip() + "\u2026"
        if wrapped is not with_paragraphs and "\u00bb" not in cleaned:
            cleaned = cleaned.rstrip("\u2026").rstrip()
            cleaned = cleaned[: max_chars - 3].rstrip() + " \u00bb\u2026"
        picked.append(TopComment(id=cid, author=node.author, text=cleaned))
    return picked


def render_top_comments(comments: list[TopComment]) -> str:
    if not comments:
        return ""
    lines = ["**Top commentaires** :", ""]
    for c in comments:
        url = _HN_ITEM_URL.format(id=c.id)
        author = escape_markdown(c.author)
        text = escape_markdown(c.text)
        lines.append(f"- [{author}]({url}) : {text}")
    return "\n".join(lines)
