from pathlib import Path

import markdown
from feedgen.feed import FeedGenerator

from app.config import get_settings
from app.models import Article, ContentSource
from app.storage import iter_summarized, short_hash


def build_feed() -> bytes:
    settings = get_settings()
    articles = _collect_articles()
    fg = FeedGenerator()
    fg.id(settings.feed_self_url)
    fg.title(settings.feed_title)
    fg.link(href=settings.feed_self_url, rel="self")
    fg.description(settings.feed_description)
    fg.language("fr")
    for article, body in articles:
        _add_entry(fg, article, body)
    return fg.rss_str(pretty=True)


def write_feed() -> Path:
    settings = get_settings()
    data = build_feed()
    settings.feed_output_path.parent.mkdir(parents=True, exist_ok=True)
    settings.feed_output_path.write_bytes(data)
    return settings.feed_output_path


def _collect_articles() -> list[tuple[Article, str]]:
    settings = get_settings()
    items = [(a, body) for _, a, body in iter_summarized()]
    items.sort(key=lambda pair: pair[0].our_published_at, reverse=True)
    return items[: settings.feed_items_limit]


def _add_entry(fg: FeedGenerator, article: Article, body: str) -> None:
    entry = fg.add_entry(order="append")
    entry.title(article.rewritten_title or article.title)
    link = (
        article.hn_url
        if article.content_source == ContentSource.ASK_SHOW_HN
        else article.url
    )
    entry.link(href=link)
    entry.guid(short_hash(article.guid), permalink=False)
    entry.comments(article.hn_url)
    entry.pubDate(article.our_published_at)
    entry.description(markdown.markdown(body, extensions=["extra"]))
