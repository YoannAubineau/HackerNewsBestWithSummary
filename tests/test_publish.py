from datetime import UTC, datetime
from xml.etree import ElementTree as ET

from app.models import Article, ContentSource, Status
from app.publish import build_feed
from app.storage import save


def _make_article(
    guid: str,
    *,
    ask_show: bool = False,
    title: str = "Titre",
    rewritten_title: str | None = None,
    url: str = "https://example.com/a",
    hn_item_id: int = 1,
    our_published_at: datetime | None = None,
) -> Article:
    hn_url = f"https://news.ycombinator.com/item?id={hn_item_id}"
    return Article(
        guid=guid,
        url=hn_url if ask_show else url,
        hn_url=hn_url,
        hn_item_id=hn_item_id,
        title=title,
        rewritten_title=rewritten_title,
        source_published_at=datetime(2026, 4, 21, 8, 0, tzinfo=UTC),
        our_published_at=our_published_at or datetime(2026, 4, 21, 9, 0, tzinfo=UTC),
        status=Status.SUMMARIZED,
        is_ask_or_show_hn=ask_show,
        content_source=ContentSource.ASK_SHOW_HN if ask_show else ContentSource.EXTRACTED,
        summarized_at=datetime(2026, 4, 21, 9, 5, tzinfo=UTC),
    )


def _parse(feed_bytes: bytes):
    root = ET.fromstring(feed_bytes)
    return root.findall(".//item")


def test_feed_has_required_fields(isolated_settings):
    article = _make_article("g1", hn_item_id=10)
    save(article, "## Résumé\n\nCorps.")
    items = _parse(build_feed())
    assert len(items) == 1
    item = items[0]
    assert item.findtext("title") == "Titre"
    assert item.findtext("link") == "https://example.com/a"
    assert item.findtext("comments") == "https://news.ycombinator.com/item?id=10"


def test_ask_hn_uses_hn_url_as_link(isolated_settings):
    article = _make_article("g2", ask_show=True, hn_item_id=20, title="Ask HN")
    save(article, "## Discussion\n\nCorps.")
    items = _parse(build_feed())
    assert items[0].findtext("link") == "https://news.ycombinator.com/item?id=20"
    assert items[0].findtext("comments") == "https://news.ycombinator.com/item?id=20"


def test_feed_sorted_by_our_published_at_desc(isolated_settings):
    # Deliberately choose hn_item_id order OPPOSITE to our_published_at
    # order to prove the feed is sorted on the right field.
    first_entered = _make_article(
        "first",
        hn_item_id=200,
        title="Ancien dans notre flux",
        our_published_at=datetime(2026, 4, 21, 8, 0, tzinfo=UTC),
    )
    last_entered = _make_article(
        "last",
        hn_item_id=100,
        title="Récent dans notre flux",
        our_published_at=datetime(2026, 4, 22, 8, 0, tzinfo=UTC),
    )
    save(first_entered, "body")
    save(last_entered, "body")
    items = _parse(build_feed())
    assert [i.findtext("title") for i in items] == [
        "Récent dans notre flux",
        "Ancien dans notre flux",
    ]


def test_pubdate_is_source_published_at(isolated_settings):
    article = _make_article("g1", hn_item_id=1)
    article.source_published_at = datetime(2026, 4, 19, 7, 8, tzinfo=UTC)
    save(article, "body")
    items = _parse(build_feed())
    pub = items[0].findtext("pubDate")
    assert pub is not None
    assert "19 Apr 2026" in pub
    assert "07:08" in pub


def test_feed_items_limit_respected(isolated_settings):
    isolated_settings.feed_items_limit = 2
    for i in range(5):
        article = _make_article(
            f"g{i}",
            hn_item_id=100 + i,
            our_published_at=datetime(2026, 4, 21, i, 0, tzinfo=UTC),
        )
        save(article, "body")
    items = _parse(build_feed())
    assert len(items) == 2


def test_guid_is_short_hash_not_permalink(isolated_settings):
    article = _make_article("some-guid", hn_item_id=42)
    save(article, "body")
    root = ET.fromstring(build_feed())
    guid = root.find(".//item/guid")
    assert guid is not None
    assert guid.attrib.get("isPermaLink") == "false"
    assert guid.text is not None
    assert len(guid.text) == 8


def test_rewritten_title_replaces_original(isolated_settings):
    article = _make_article(
        "g-rw",
        hn_item_id=30,
        title="Ce truc incroyable va changer votre vie",
        rewritten_title="nouvelle méthode de chiffrement basée sur les réseaux de neurones",
    )
    save(article, "body")
    items = _parse(build_feed())
    assert items[0].findtext("title") == (
        "nouvelle méthode de chiffrement basée sur les réseaux de neurones"
    )


def test_original_title_used_when_no_rewrite(isolated_settings):
    article = _make_article("g-orig", hn_item_id=31, title="Titre original")
    save(article, "body")
    items = _parse(build_feed())
    assert items[0].findtext("title") == "Titre original"


_MEDIA_NS = {"media": "http://search.yahoo.com/mrss/"}


def _thumbnail_url(item) -> str | None:
    thumb = item.find(".//media:thumbnail", _MEDIA_NS)
    return thumb.get("url") if thumb is not None else None


def test_media_thumbnail_emitted_when_image_url_set(isolated_settings):
    article = _make_article("g-img", hn_item_id=50)
    article.image_url = "https://cdn.example.com/hero.jpg"
    save(article, "## Résumé\n\nCorps.")
    items = _parse(build_feed())
    assert _thumbnail_url(items[0]) == "https://cdn.example.com/hero.jpg"


def test_channel_ttl_is_fifteen_minutes(isolated_settings):
    article = _make_article("g-ttl", hn_item_id=60)
    save(article, "body")
    root = ET.fromstring(build_feed())
    ttl = root.find(".//channel/ttl")
    assert ttl is not None
    assert ttl.text == "15"


def test_item_source_points_to_hnrss(isolated_settings):
    article = _make_article("g-src", hn_item_id=61)
    save(article, "body")
    items = _parse(build_feed())
    source = items[0].find("source")
    assert source is not None
    assert source.get("url") == isolated_settings.source_feed_url


def test_no_media_thumbnail_when_image_url_absent(isolated_settings):
    article = _make_article("g-noimg", hn_item_id=52)
    save(article, "## Résumé\n\nCorps.")
    items = _parse(build_feed())
    assert _thumbnail_url(items[0]) is None


def test_rendered_body_does_not_inline_the_image(isolated_settings):
    # media:thumbnail is the only channel for the image; the rendered body
    # stays clean and does not contain an <img> tag (which would risk
    # showing up twice in readers that both display the thumbnail and
    # render the body).
    article = _make_article("g-clean", hn_item_id=53)
    article.image_url = "https://cdn.example.com/hero.jpg"
    save(article, "## Résumé\n\nCorps.")
    items = _parse(build_feed())
    content = _content_encoded(items[0])
    assert "<img " not in content
    assert "cdn.example.com" not in content


_CONTENT_NS = {"content": "http://purl.org/rss/1.0/modules/content/"}


def _content_encoded(item) -> str:
    el = item.find("content:encoded", _CONTENT_NS)
    return (el.text or "") if el is not None else ""


def test_content_encoded_contains_rendered_markdown(isolated_settings):
    article = _make_article("g-desc", hn_item_id=7)
    save(article, "## Résumé de l'article\n\n**Note importante.**\n\n- Point 1\n- Point 2")
    items = _parse(build_feed())
    content = _content_encoded(items[0])
    assert "<h2>" in content
    assert "<strong>Note importante.</strong>" in content
    assert "<li>Point 1</li>" in content


def test_raw_html_in_body_is_escaped(isolated_settings):
    # Guards against a prompt-injected LLM output emitting <script> / <iframe>
    # that would slip through to RSS readers. markdown-it-py should treat the
    # raw HTML as literal text (escaped) rather than pass it through.
    article = _make_article("g-xss", hn_item_id=99)
    save(article, "## Résumé\n\n<script>alert('xss')</script>\n\nnormal.")
    raw = build_feed().decode("utf-8")
    assert "<script>" not in raw
    assert "&lt;script&gt;" in raw


def test_description_is_article_url_without_scheme(isolated_settings):
    article = _make_article("g-url", hn_item_id=77, url="https://lwn.net/Articles/1069399/")
    save(article, "## Résumé\n\nCorps.")
    items = _parse(build_feed())
    assert items[0].findtext("description") == "lwn.net/Articles/1069399/"


def test_description_for_ask_hn_uses_hn_url_without_scheme(isolated_settings):
    article = _make_article("g-url-ask", ask_show=True, hn_item_id=78)
    save(article, "## Discussion\n\nCorps.")
    items = _parse(build_feed())
    assert items[0].findtext("description") == "news.ycombinator.com/item"


def test_description_strips_query_string(isolated_settings):
    article = _make_article(
        "g-qs",
        hn_item_id=81,
        url="https://www.justice.gov/usao-sdny/pr/article?bm-verify=ABCDEF123&tracking=x",
    )
    save(article, "## Résumé\n\nCorps.")
    items = _parse(build_feed())
    assert items[0].findtext("description") == "www.justice.gov/usao-sdny/pr/article"


def test_rss_declares_content_namespace(isolated_settings):
    article = _make_article("g-ns", hn_item_id=78)
    save(article, "## Résumé\n\nCorps.")
    raw = build_feed().decode("utf-8")
    assert 'xmlns:content="http://purl.org/rss/1.0/modules/content/"' in raw
    items = _parse(build_feed())
    assert items[0].find("content:encoded", _CONTENT_NS) is not None


def test_feed_declares_xsl_stylesheet_for_browser_rendering(isolated_settings):
    article = _make_article("g-xsl", hn_item_id=88)
    save(article, "body")
    raw = build_feed()
    first_200 = raw[:200].decode("utf-8")
    assert '<?xml-stylesheet type="text/xsl" href="feed.xsl"?>' in first_200
    assert first_200.index("<?xml version") < first_200.index("<?xml-stylesheet")
    assert first_200.index("<?xml-stylesheet") < first_200.index("<rss")
