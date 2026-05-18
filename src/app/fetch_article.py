import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from html.parser import HTMLParser
from urllib.parse import parse_qs, urljoin, urlparse

import httpx
import structlog
import trafilatura
from lxml import etree  # pyright: ignore[reportAttributeAccessIssue]
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig

from app.config import get_settings
from app.models import ContentSource

log = structlog.get_logger()

_FETCHABLE_CONTENT_TYPES = (
    "text/html",
    "application/xhtml+xml",
    "application/xml",
    "text/xml",
)
_XML_CONTENT_TYPES = ("application/xml", "text/xml")
_JS_NOTICE_SIMILARITY_THRESHOLD = 0.9
_YOUTUBE_HOSTS = {"youtube.com", "youtu.be"}
_YOUTUBE_HOST_PREFIXES = ("www.", "m.", "music.")
_VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
_YOUTUBE_PATH_VIDEO_ID_RE = re.compile(r"^/(?:shorts|embed|v)/([A-Za-z0-9_-]{11})(?:/|$)")
_TRANSCRIPT_LANGUAGES = ("fr", "en")
_TWITTER_HOSTS = {"x.com", "twitter.com", "mobile.x.com", "mobile.twitter.com"}
_TWEET_PATH_RE = re.compile(r"^/(?P<user>[^/]+)/status/(?P<id>\d+)(?:/.*)?$")


@dataclass
class ArticleContent:
    text: str
    source: ContentSource
    image_url: str | None = None


def fetch_article(url: str) -> ArticleContent:
    """Fetch and extract the URL's main content.

    On any failure (HTTP error, non-HTML content-type, empty extraction,
    YouTube transcript blocked), returns an empty ``text`` with a source
    that records *why* extraction did not produce content. The caller
    must decide what to do with an empty body — we deliberately do not
    fall back to the feed's own summary, which on hnrss is just metadata
    boilerplate (article URL, points, comment count) and would only
    pollute downstream summarization.
    """
    video_id = _extract_youtube_video_id(url)
    if video_id is not None:
        thumbnail = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
        transcript = _fetch_youtube_transcript(video_id)
        if transcript:
            return ArticleContent(
                text=transcript,
                source=ContentSource.VIDEO_TRANSCRIPT,
                image_url=thumbnail,
            )
        return ArticleContent(
            text="",
            source=ContentSource.FEED_FALLBACK,
            image_url=thumbnail,
        )

    tweet_id = _extract_tweet_id(url)
    if tweet_id is not None:
        # X.com / twitter.com block JS-less requests with an in-DOM error
        # page (not a <noscript> block), so the normal trafilatura path is
        # guaranteed to fail. Skip it entirely and use a public tweet API.
        tweet = _fetch_tweet(*tweet_id)
        if tweet is not None:
            return tweet
        return ArticleContent(text="", source=ContentSource.FEED_FALLBACK)

    response = _http_get_with_proxy_fallback(url)
    if response is None:
        return ArticleContent(text="", source=ContentSource.FEED_FALLBACK)

    content_type = response.headers.get("content-type", "").split(";")[0].strip().lower()
    if content_type and not any(content_type.startswith(t) for t in _FETCHABLE_CONTENT_TYPES):
        return ArticleContent(text="", source=ContentSource.FEED_FALLBACK)

    image_url = _extract_image_url(response.text, url)

    if any(content_type.startswith(t) for t in _XML_CONTENT_TYPES):
        html_for_extraction = _xml_to_html(response.content)
        if html_for_extraction is None:
            return ArticleContent(
                text="",
                source=ContentSource.FEED_FALLBACK,
                image_url=image_url,
            )
    else:
        html_for_extraction = response.text

    extracted = trafilatura.extract(
        html_for_extraction,
        include_comments=False,
        include_tables=False,
        favor_precision=True,
    )
    if extracted and extracted.strip():
        if _is_js_required_notice(extracted, response.text):
            return ArticleContent(
                text="",
                source=ContentSource.JS_REQUIRED,
                image_url=image_url,
            )
        return ArticleContent(
            text=extracted.strip(),
            source=ContentSource.EXTRACTED,
            image_url=image_url,
        )
    return ArticleContent(
        text="",
        source=ContentSource.FEED_FALLBACK,
        image_url=image_url,
    )


def _http_get_with_proxy_fallback(url: str) -> httpx.Response | None:
    """GET ``url`` directly, then retry through Webshare on any HTTP error.

    Publishers like nytimes.com, fastcompany.com, openai.com and medium.com
    return 403 to non-browser User-Agents from cloud IP ranges (GitHub
    Actions runners included). Routing the retry through Webshare's
    rotating residential pool — already wired in for YouTube transcripts
    and HN comment-ranking scraping — bypasses those blocks for a tiny
    per-request cost. Returns ``None`` when both attempts fail, or when
    the direct attempt fails and Webshare credentials are not configured.
    """
    settings = get_settings()
    headers = {"User-Agent": settings.user_agent}
    try:
        response = httpx.get(
            url,
            timeout=settings.http_timeout,
            headers=headers,
            follow_redirects=True,
        )
        response.raise_for_status()
        return response
    except httpx.HTTPError as direct_exc:
        if not (
            settings.webshare_proxy_username and settings.webshare_proxy_password
        ):
            return None
        proxy_url = WebshareProxyConfig(
            proxy_username=settings.webshare_proxy_username,
            proxy_password=settings.webshare_proxy_password,
        ).url
        try:
            response = httpx.get(
                url,
                timeout=settings.http_timeout,
                headers=headers,
                follow_redirects=True,
                proxy=proxy_url,
            )
            response.raise_for_status()
        except httpx.HTTPError as proxy_exc:
            log.warning(
                "article_fetch_proxy_failed",
                url=url,
                direct_error=str(direct_exc),
                proxy_error=str(proxy_exc),
            )
            return None
        log.info(
            "article_fetch_via_proxy",
            url=url,
            direct_error=str(direct_exc),
        )
        return response


def _extract_youtube_video_id(url: str) -> str | None:
    try:
        parsed = urlparse(url)
    except ValueError:
        return None
    host = (parsed.hostname or "").lower()
    for prefix in _YOUTUBE_HOST_PREFIXES:
        if host.startswith(prefix):
            host = host[len(prefix):]
            break
    if host not in _YOUTUBE_HOSTS:
        return None
    if host == "youtu.be":
        candidate = parsed.path.lstrip("/").split("/", 1)[0]
        return candidate if _VIDEO_ID_RE.fullmatch(candidate) else None
    if parsed.path == "/watch":
        candidate = (parse_qs(parsed.query).get("v") or [""])[0]
        return candidate if _VIDEO_ID_RE.fullmatch(candidate) else None
    match = _YOUTUBE_PATH_VIDEO_ID_RE.match(parsed.path)
    return match.group(1) if match else None


def _fetch_youtube_transcript(video_id: str) -> str | None:
    settings = get_settings()
    proxy_config = None
    if settings.webshare_proxy_username and settings.webshare_proxy_password:
        proxy_config = WebshareProxyConfig(
            proxy_username=settings.webshare_proxy_username,
            proxy_password=settings.webshare_proxy_password,
        )
    try:
        api = YouTubeTranscriptApi(proxy_config=proxy_config)
        fetched = api.fetch(video_id, languages=_TRANSCRIPT_LANGUAGES)
    except Exception as exc:  # noqa: BLE001
        log.warning(
            "youtube_transcript_failed",
            video_id=video_id,
            exc_type=type(exc).__name__,
            error=str(exc),
        )
        return None
    parts = [snippet.text.strip() for snippet in fetched if snippet.text and snippet.text.strip()]
    return " ".join(parts) if parts else None


def _extract_tweet_id(url: str) -> tuple[str, str] | None:
    try:
        parsed = urlparse(url)
    except ValueError:
        return None
    host = (parsed.hostname or "").lower()
    if host.startswith("www."):
        host = host[len("www."):]
    if host not in _TWITTER_HOSTS:
        return None
    match = _TWEET_PATH_RE.match(parsed.path)
    if match is None:
        return None
    return match.group("user"), match.group("id")


@dataclass
class _Tweet:
    text: str
    author_handle: str
    author_name: str
    image_url: str | None
    quote_text: str | None
    quote_handle: str | None


def _fetch_tweet(user: str, status_id: str) -> ArticleContent | None:
    for fetcher in (_fetch_tweet_via_fxtwitter, _fetch_tweet_via_vxtwitter):
        tweet = fetcher(user, status_id)
        if tweet is not None:
            return ArticleContent(
                text=_render_tweet(tweet),
                source=ContentSource.TWEET,
                image_url=tweet.image_url,
            )
    return None


def _fetch_tweet_via_fxtwitter(user: str, status_id: str) -> _Tweet | None:
    settings = get_settings()
    url = f"https://api.fxtwitter.com/{user}/status/{status_id}"
    try:
        response = httpx.get(
            url,
            timeout=settings.http_timeout,
            headers={"User-Agent": settings.user_agent},
            follow_redirects=True,
        )
        response.raise_for_status()
        payload = response.json()
    except (httpx.HTTPError, ValueError) as exc:
        log.warning("tweet_fetch_failed", provider="fxtwitter", error=str(exc))
        return None
    if not isinstance(payload, dict) or payload.get("code") != 200:
        code = payload.get("code") if isinstance(payload, dict) else None
        log.warning("tweet_fetch_failed", provider="fxtwitter", code=code)
        return None
    tweet_data = payload.get("tweet")
    if not isinstance(tweet_data, dict):
        return None
    text = (tweet_data.get("text") or "").strip()
    author = tweet_data.get("author") or {}
    handle = (author.get("screen_name") or "").strip()
    name = (author.get("name") or "").strip()
    if not text or not handle:
        return None
    image_url = None
    media = tweet_data.get("media") or {}
    photos = media.get("photos") if isinstance(media, dict) else None
    if isinstance(photos, list) and photos:
        first = photos[0]
        if isinstance(first, dict):
            image_url = first.get("url")
    quote_text: str | None = None
    quote_handle: str | None = None
    quote = tweet_data.get("quote")
    if isinstance(quote, dict):
        qt = (quote.get("text") or "").strip()
        qa = quote.get("author") or {}
        qh = (qa.get("screen_name") or "").strip()
        if qt and qh:
            quote_text = qt
            quote_handle = qh
    return _Tweet(
        text=text,
        author_handle=handle,
        author_name=name or handle,
        image_url=image_url,
        quote_text=quote_text,
        quote_handle=quote_handle,
    )


def _fetch_tweet_via_vxtwitter(user: str, status_id: str) -> _Tweet | None:
    settings = get_settings()
    url = f"https://api.vxtwitter.com/{user}/status/{status_id}"
    try:
        response = httpx.get(
            url,
            timeout=settings.http_timeout,
            headers={"User-Agent": settings.user_agent},
            follow_redirects=True,
        )
        response.raise_for_status()
        payload = response.json()
    except (httpx.HTTPError, ValueError) as exc:
        log.warning("tweet_fetch_failed", provider="vxtwitter", error=str(exc))
        return None
    if not isinstance(payload, dict):
        return None
    text = (payload.get("text") or "").strip()
    handle = (payload.get("user_screen_name") or "").strip()
    name = (payload.get("user_name") or "").strip()
    if not text or not handle:
        return None
    image_url = None
    media = payload.get("media_extended")
    if isinstance(media, list) and media:
        first = media[0]
        if isinstance(first, dict):
            image_url = first.get("url")
    quote_text: str | None = None
    quote_handle: str | None = None
    quote = payload.get("qrt")
    if isinstance(quote, dict):
        qt = (quote.get("text") or "").strip()
        qh = (quote.get("user_screen_name") or "").strip()
        if qt and qh:
            quote_text = qt
            quote_handle = qh
    return _Tweet(
        text=text,
        author_handle=handle,
        author_name=name or handle,
        image_url=image_url,
        quote_text=quote_text,
        quote_handle=quote_handle,
    )


def _render_tweet(tweet: _Tweet) -> str:
    body = f"@{tweet.author_handle} ({tweet.author_name}):\n\n{tweet.text}"
    if tweet.quote_text and tweet.quote_handle:
        body += f"\n\n> @{tweet.quote_handle}: {tweet.quote_text}"
    return body


def _xml_to_html(content: bytes) -> str | None:
    """Strip XML namespaces and wrap as HTML for trafilatura.

    Forester-style sources (e.g. forester-notes.org) ship article text
    inside namespaced HTML elements like ``<html:p>`` under custom roots
    like ``<fr:tree><fr:mainmatter>``. trafilatura's heuristics anchor on
    plain ``<html><body>``, so we drop every namespace, then wrap the
    serialized tree in a minimal HTML shell.
    """
    parser = etree.XMLParser(recover=True, resolve_entities=False, no_network=True)
    try:
        root = etree.fromstring(content, parser=parser)
    except etree.XMLSyntaxError:
        return None
    if root is None:
        return None
    for el in root.iter():
        if isinstance(el.tag, str):
            el.tag = etree.QName(el).localname
    etree.cleanup_namespaces(root)
    body = etree.tostring(root, encoding="unicode", method="xml")
    return f"<html><body>{body}</body></html>"


def _is_js_required_notice(extracted: str, html: str) -> bool:
    """True when trafilatura's output matches the raw HTML's <noscript> text."""
    noscript_text = _collect_noscript_text(html)
    if not noscript_text:
        return False
    a = _normalize(extracted)
    b = _normalize(noscript_text)
    if not a or not b:
        return False
    return SequenceMatcher(None, a, b).ratio() >= _JS_NOTICE_SIMILARITY_THRESHOLD


_WHITESPACE_RE = re.compile(r"\s+")


def _normalize(text: str) -> str:
    return _WHITESPACE_RE.sub(" ", text.strip().lower())


def _collect_noscript_text(html: str) -> str:
    collector = _NoscriptCollector()
    try:
        collector.feed(html)
    except Exception:  # noqa: BLE001
        return ""
    return collector.text()


class _NoscriptCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._depth = 0
        self._chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "noscript":
            self._depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "noscript" and self._depth > 0:
            self._depth -= 1

    def handle_data(self, data: str) -> None:
        if self._depth > 0 and data.strip():
            self._chunks.append(data)

    def text(self) -> str:
        return " ".join(chunk.strip() for chunk in self._chunks if chunk.strip())


class _MetaImageExtractor(HTMLParser):
    """Pick up the first og:image (or og:image:url), with twitter:image fallback."""

    def __init__(self) -> None:
        super().__init__()
        self.og_image: str | None = None
        self.twitter_image: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "meta":
            return
        d = {k.lower(): v for k, v in attrs if v is not None}
        content = d.get("content")
        if not content:
            return
        prop = d.get("property", "").lower()
        name = d.get("name", "").lower()
        if prop in ("og:image", "og:image:url") and not self.og_image:
            self.og_image = content
        elif name == "twitter:image" and not self.twitter_image:
            self.twitter_image = content


def _extract_image_url(html: str, base_url: str) -> str | None:
    parser = _MetaImageExtractor()
    try:
        parser.feed(html)
    except Exception:  # noqa: BLE001
        return None
    image = parser.og_image or parser.twitter_image
    if not image:
        return None
    return urljoin(base_url, image.strip())
