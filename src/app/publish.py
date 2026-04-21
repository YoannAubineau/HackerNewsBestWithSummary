from pathlib import Path

from feedgen.feed import FeedGenerator
from markdown_it import MarkdownIt

from app.config import get_settings
from app.models import Article, ContentSource
from app.storage import iter_summarized, short_hash

_md = MarkdownIt()


def build_feed() -> bytes:
    settings = get_settings()
    articles = _collect_articles()
    fg = FeedGenerator()
    fg.load_extension("media")
    fg.id(settings.feed_self_url)
    fg.title(settings.feed_title)
    fg.link(href=settings.feed_self_url, rel="self")
    fg.description(settings.feed_description)
    fg.language("fr")
    fg.generator(
        "hn-best-summary 0.1 (https://github.com/YoannAubineau/HackerNewsBestWithSummary)"
    )
    fg.ttl(60)
    fg.image(
        url="https://yoannaubineau.github.io/HackerNewsBestWithSummary/logo.png",
        title=settings.feed_title,
        link=settings.feed_self_url,
    )
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
    limit = settings.feed_items_limit
    items: list[tuple[Article, str]] = []
    for _, article, body in iter_summarized():
        items.append((article, body))
        if len(items) >= limit:
            break
    return items


def _add_entry(fg: FeedGenerator, article: Article, body: str) -> None:
    settings = get_settings()
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
    entry.pubDate(article.source_published_at)
    entry.source(url=settings.source_feed_url, title="Hacker News Best via hnrss.org")
    entry.description(_md.render(body))
    if article.image_url:
        # `media` is attached to FeedEntry at runtime by fg.load_extension("media");
        # pyright cannot see this dynamic attribute.
        entry.media.thumbnail({"url": article.image_url})  # type: ignore[attr-defined]
