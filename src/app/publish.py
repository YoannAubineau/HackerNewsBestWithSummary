import json
from datetime import UTC, datetime
from pathlib import Path

from feedgen.feed import FeedGenerator
from markdown_it import MarkdownIt

from app.config import get_settings
from app.models import Article, ContentSource
from app.storage import iter_summarized, short_hash

_LAST_REFRESH_PATH = Path("artifacts/last-refresh.json")

# html=False escapes any raw HTML that sneaks into the LLM output (prompt
# injection via a crafted article could otherwise emit <script> tags that
# slip through to the feed <description>).
_md = MarkdownIt(options_update={"html": False})


def build_feed() -> bytes:
    settings = get_settings()
    articles = _collect_articles()
    fg = FeedGenerator()
    fg.load_extension("media")
    fg.id(settings.feed_self_url)
    fg.title(settings.feed_title)
    # The plain <link> points at HN's "best" page rather than at our own
    # feed URL on purpose: most readers (Feedly, Reeder, …) fetch that URL
    # and extract its favicon as the feed's icon. hnrss.org/best uses the
    # same trick. <atom:link rel="self"> carries the canonical feed URL
    # for validators and dedup logic. Order matters here — feedgen picks
    # the *last* link without `rel` as the RSS <link>, so rel="self" must
    # be declared first.
    fg.link(href=settings.feed_self_url, rel="self")
    fg.link(href=settings.channel_site_url)
    fg.description(settings.feed_description)
    fg.language("fr")
    fg.generator("hn-best-summary")
    fg.ttl(settings.feed_ttl_minutes)
    for article, body in articles:
        _add_entry(fg, article, body)
    return _inject_xsl_stylesheet(fg.rss_str(pretty=True))


def _inject_xsl_stylesheet(rss_bytes: bytes) -> bytes:
    """Insert a <?xml-stylesheet?> PI so browsers render the feed via feed.xsl.

    feedgen has no built-in way to declare a processing instruction; we just
    splice it right after the `<?xml ... ?>` declaration.
    """
    pi = b'<?xml-stylesheet type="text/xsl" href="feed.xsl"?>\n'
    xml_decl_end = rss_bytes.find(b"?>") + 2
    return rss_bytes[:xml_decl_end] + b"\n" + pi + rss_bytes[xml_decl_end + 1 :]


def write_feed() -> Path:
    settings = get_settings()
    data = build_feed()
    settings.feed_output_path.parent.mkdir(parents=True, exist_ok=True)
    settings.feed_output_path.write_bytes(data)
    _write_last_refresh()
    return settings.feed_output_path


def _write_last_refresh() -> None:
    """Write a shields.io endpoint JSON with the current UTC timestamp.

    Consumed by the README badge; updated only when the feed is rewritten,
    so the badge reflects the actual content refresh time.
    """
    now = datetime.now(tz=UTC).strftime("%Y-%m-%d %H:%M UTC")
    payload = {
        "schemaVersion": 1,
        "label": "Last feed refresh",
        "message": now,
        "color": "blue",
    }
    _LAST_REFRESH_PATH.parent.mkdir(parents=True, exist_ok=True)
    _LAST_REFRESH_PATH.write_text(json.dumps(payload) + "\n", encoding="utf-8")


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
    entry.description(_display_url(link))
    entry.content(content=_md.render(body), type="CDATA")
    if article.image_url:
        # `media` is attached to FeedEntry at runtime by fg.load_extension("media");
        # pyright cannot see this dynamic attribute.
        entry.media.thumbnail({"url": article.image_url})  # type: ignore[attr-defined]


def _display_url(url: str) -> str:
    for prefix in ("https://", "http://"):
        if url.startswith(prefix):
            url = url[len(prefix) :]
            break
    return url.split("?", 1)[0]
