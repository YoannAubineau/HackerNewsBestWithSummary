import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from html.parser import HTMLParser
from urllib.parse import urljoin

import httpx
import trafilatura

from app.config import get_settings
from app.models import ContentSource

_FETCHABLE_CONTENT_TYPES = ("text/html", "application/xhtml+xml")
_JS_NOTICE_SIMILARITY_THRESHOLD = 0.9


@dataclass
class ArticleContent:
    text: str
    source: ContentSource
    image_url: str | None = None


def fetch_article(url: str, feed_fallback: str) -> ArticleContent:
    """Fetch and extract the URL's main content, falling back to the feed's summary."""
    settings = get_settings()
    try:
        response = httpx.get(
            url,
            timeout=settings.http_timeout,
            headers={"User-Agent": settings.user_agent},
            follow_redirects=True,
        )
        response.raise_for_status()
    except httpx.HTTPError:
        return ArticleContent(text=feed_fallback.strip(), source=ContentSource.FEED_FALLBACK)

    content_type = response.headers.get("content-type", "").split(";")[0].strip().lower()
    if content_type and not any(content_type.startswith(t) for t in _FETCHABLE_CONTENT_TYPES):
        return ArticleContent(text=feed_fallback.strip(), source=ContentSource.FEED_FALLBACK)

    image_url = _extract_image_url(response.text, url)

    extracted = trafilatura.extract(
        response.text,
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
        text=feed_fallback.strip(),
        source=ContentSource.FEED_FALLBACK,
        image_url=image_url,
    )


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
