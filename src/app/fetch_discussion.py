import html
import re
from collections.abc import Iterable, Iterator
from dataclasses import dataclass

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
_BLOCK_BREAK_RE = re.compile(r"</(p|div|pre|blockquote|li)\s*>", re.IGNORECASE)
_LINE_BREAK_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)
_BLANK_LINES_RE = re.compile(r"\n{3,}")
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


def fetch_discussion(hn_item_id: int) -> Discussion | None:
    payload = _fetch_algolia_item(hn_item_id)
    if payload is None:
        return None
    settings = get_settings()
    comments = list(_iter_comments(payload, settings.discussion_budget))
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
    )


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


def _iter_comments(root: AlgoliaItem, budget: int) -> Iterator[dict]:
    """Walk the comment tree with a recursive, degressive comment budget.

    A "branch node" is a comment that has at least one direct reply. Non-pinned
    branch nodes are included only if the budget reaches them; the budget at
    each level is split triangularly across qualifying children (the
    highest-ranked child gets the largest share).

    Submitter comments (author == story author) and their full ancestor chain
    are "pinned": always included, regardless of budget, and without consuming
    budget that would otherwise be spent on non-pinned siblings.
    """
    pinned = _collect_pinned(root, root.author) if root.author else set()
    yield from _distribute_children(root, budget, pinned, depth=0)


def _walk(
    node: AlgoliaItem, budget: int, pinned: set[int], depth: int
) -> Iterator[dict]:
    is_pinned = id(node) in pinned
    has_reply = bool(node.children)
    if not (is_pinned or (budget > 0 and has_reply)):
        return
    if node.text:
        yield {
            "author": node.author or "?",
            "points": node.points,
            "text": _strip_html(node.text),
            "depth": depth,
        }
    remaining = budget if is_pinned else max(0, budget - 1)
    yield from _distribute_children(node, remaining, pinned, depth + 1)


def _distribute_children(
    parent: AlgoliaItem, budget: int, pinned: set[int], depth: int
) -> Iterator[dict]:
    children = parent.children
    alloc_map: dict[int, int] = {}
    if budget > 0:
        non_pinned_qualifying = [
            c for c in children if id(c) not in pinned and c.children
        ]
        allocations = _degressive_split(budget, len(non_pinned_qualifying))
        alloc_map = {
            id(c): a for c, a in zip(non_pinned_qualifying, allocations, strict=True)
        }
    for child in children:
        if id(child) in pinned:
            yield from _walk(child, 0, pinned, depth)
        elif (alloc := alloc_map.get(id(child), 0)) > 0:
            yield from _walk(child, alloc, pinned, depth)


def _collect_pinned(root: AlgoliaItem, author: str) -> set[int]:
    """Return the set of id()s for (a) every comment posted by ``author`` and
    (b) each of its ancestors up to the story root."""
    pinned: set[int] = set()
    _mark_pinned(root, author, pinned, ancestors=[])
    return pinned


def _mark_pinned(
    node: AlgoliaItem,
    author: str,
    pinned: set[int],
    ancestors: list[AlgoliaItem],
) -> None:
    if node.author == author and node.text:
        pinned.add(id(node))
        for anc in ancestors:
            pinned.add(id(anc))
    for child in node.children:
        _mark_pinned(child, author, pinned, ancestors + [node])


def _degressive_split(budget: int, n: int) -> list[int]:
    """Triangular split: weight[i] = n-i. First slot gets the largest share."""
    if n <= 0 or budget <= 0:
        return []
    weights = list(range(n, 0, -1))
    total_weight = sum(weights)
    allocs = [budget * w // total_weight for w in weights]
    residue = budget - sum(allocs)
    allocs[0] += residue
    return allocs


def _strip_html(text: str) -> str:
    return html.unescape(_TAG_RE.sub("", text))


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


def _render_comments(comments: Iterable[dict]) -> str:
    parts: list[str] = []
    for c in comments:
        indent = "  " * c["depth"]
        points = f", {c['points']} pts" if c["points"] is not None else ""
        parts.append(f"{indent}[{c['author']}{points}] {c['text'].strip()}")
    return "\n".join(parts)


_WHITESPACE_RE = re.compile(r"\s+")
_HN_ITEM_URL = "https://news.ycombinator.com/item?id={id}"
_MARKDOWN_SPECIAL_RE = re.compile(r"([\\\[\]()*_`#<>])")


def _escape_markdown(text: str) -> str:
    """Backslash-escape Markdown control characters.

    Commenters control both their handle and their text. Without this,
    an author named ``[admin](https://evil)`` or a comment whose text
    contains ``[clic ici](https://evil)`` would inject an active link
    into the rendered Markdown — and into the upstream LLM context, which
    receives this same string before producing the discussion summary.
    """
    return _MARKDOWN_SPECIAL_RE.sub(r"\\\1", text)


def _is_retryable_hn_error(exc: BaseException) -> bool:
    """Retry HN HTML fetches on transient errors only.

    HN HTTP 429 is the dominant failure mode (shared GitHub Actions IPs
    get rate-limited even on a single request). Connection-level
    timeouts and resets are also transient. Any other HTTP error
    (404, 5xx, malformed response) is treated as terminal.
    """
    if isinstance(exc, httpx.HTTPStatusError):
        return exc.response.status_code == 429
    return isinstance(exc, (httpx.ConnectError, httpx.ReadTimeout))


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=2, min=2, max=10),
    retry=retry_if_exception(_is_retryable_hn_error),
    reraise=True,
)
def _fetch_hn_html(hn_item_id: int) -> str:
    settings = get_settings()
    response = httpx.get(
        _HN_STORY_URL.format(id=hn_item_id),
        timeout=settings.http_timeout,
        headers={"User-Agent": settings.user_agent},
    )
    response.raise_for_status()
    return response.text


def _fetch_hn_html_via_proxy(hn_item_id: int) -> str:
    """Single attempt against HN through the Webshare residential proxy.

    Each request comes from a fresh rotating residential IP, which
    bypasses HN's IP-based rate limiting on shared GitHub Actions
    runners. Caller is responsible for checking that proxy credentials
    are configured before invoking this. Raises ``httpx.HTTPError`` on
    failure.
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

    Transient HN failures (HTTP 429, connection resets) are retried up
    to three times with exponential backoff, since GitHub Actions
    runners share IPs and tend to trip HN's rate limit even on a single
    request. When the direct retries are exhausted and Webshare proxy
    credentials are configured, one last attempt routes through the
    residential proxy pool already used by the YouTube transcript path
    — that gives us a fresh IP per request and bypasses HN's
    IP-based throttling entirely. If everything fails, the caller falls
    back to an empty ``top_comments_markdown`` rather than crashing the
    pipeline.
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
        cleaned = _WHITESPACE_RE.sub(" ", _strip_html(node.text)).strip()
        if not cleaned:
            continue
        if len(cleaned) > max_chars:
            cleaned = cleaned[: max_chars - 1].rstrip() + "\u2026"
        picked.append(TopComment(id=cid, author=node.author, text=cleaned))
    return picked


def render_top_comments(comments: list[TopComment]) -> str:
    if not comments:
        return ""
    lines = ["**Commentaires les plus plébiscités** :", ""]
    for c in comments:
        url = _HN_ITEM_URL.format(id=c.id)
        author = _escape_markdown(c.author)
        text = _escape_markdown(c.text)
        lines.append(f"- [{author}]({url}) : « {text} »")
    return "\n".join(lines)
