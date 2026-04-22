import re
from dataclasses import dataclass
from datetime import UTC, datetime
from time import struct_time

import feedparser
import httpx
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from app.config import get_settings

_HN_ITEM_RE = re.compile(r"[?&]id=(\d+)")


@dataclass
class FeedEntry:
    guid: str
    title: str
    url: str
    hn_url: str
    hn_item_id: int
    source_published_at: datetime
    feed_summary: str
    is_ask_or_show_hn: bool


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=2, min=2, max=10),
    retry=retry_if_exception_type(httpx.HTTPError),
    reraise=True,
)
def fetch_source_feed() -> list[FeedEntry]:
    settings = get_settings()
    response = httpx.get(
        settings.source_feed_url,
        timeout=settings.http_timeout,
        headers={"User-Agent": settings.user_agent},
        follow_redirects=True,
    )
    response.raise_for_status()
    return parse_feed_bytes(response.content)


def parse_feed_bytes(data: bytes) -> list[FeedEntry]:
    parsed = feedparser.parse(data)
    entries: list[FeedEntry] = []
    for entry in parsed.entries:
        mapped = _map_entry(entry)
        if mapped is not None:
            entries.append(mapped)
    return entries


def _map_entry(entry) -> FeedEntry | None:
    guid = entry.get("id") or entry.get("guid") or entry.get("link")
    if not guid:
        return None
    link = entry.get("link") or ""
    comments = entry.get("comments") or ""
    hn_url = comments or link
    match = _HN_ITEM_RE.search(hn_url)
    if not match:
        return None
    hn_item_id = int(match.group(1))
    is_ask_or_show = not comments or link == comments
    return FeedEntry(
        guid=guid,
        title=entry.get("title", "").strip(),
        url=link or hn_url,
        hn_url=hn_url,
        hn_item_id=hn_item_id,
        source_published_at=_parse_published(entry),
        feed_summary=(entry.get("summary") or "").strip(),
        is_ask_or_show_hn=is_ask_or_show,
    )


def _parse_published(entry) -> datetime:
    for key in ("published_parsed", "updated_parsed"):
        value = entry.get(key)
        if isinstance(value, struct_time):
            return datetime(*value[:6], tzinfo=UTC)
    return datetime.now(tz=UTC)
