from dataclasses import dataclass

import httpx
import trafilatura

from app.config import get_settings
from app.models import ContentSource

_FETCHABLE_CONTENT_TYPES = ("text/html", "application/xhtml+xml")


@dataclass
class ArticleContent:
    text: str
    source: ContentSource


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

    extracted = trafilatura.extract(
        response.text,
        include_comments=False,
        include_tables=False,
        favor_precision=True,
    )
    if extracted and extracted.strip():
        return ArticleContent(text=extracted.strip(), source=ContentSource.EXTRACTED)
    return ArticleContent(text=feed_fallback.strip(), source=ContentSource.FEED_FALLBACK)
