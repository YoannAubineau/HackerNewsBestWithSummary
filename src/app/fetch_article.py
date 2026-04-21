from dataclasses import dataclass
from html.parser import HTMLParser
from urllib.parse import urljoin

import httpx
import trafilatura

from app.config import get_settings
from app.models import ContentSource

_FETCHABLE_CONTENT_TYPES = ("text/html", "application/xhtml+xml")


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
