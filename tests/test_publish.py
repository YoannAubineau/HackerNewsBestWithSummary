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
        model="test/model:free",
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


def test_feed_sorted_by_hn_item_id_desc(isolated_settings):
    older = _make_article("old", hn_item_id=100, title="Ancien")
    newer = _make_article("new", hn_item_id=200, title="Récent")
    save(older, "body")
    save(newer, "body")
    items = _parse(build_feed())
    assert [i.findtext("title") for i in items] == ["Récent", "Ancien"]


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


def test_description_contains_rendered_markdown(isolated_settings):
    article = _make_article("g-desc", hn_item_id=7)
    save(article, "## Résumé de l'article\n\n**Note importante.**\n\n- Point 1\n- Point 2")
    items = _parse(build_feed())
    description = items[0].findtext("description") or ""
    assert "<h2>" in description
    assert "<strong>Note importante.</strong>" in description
    assert "<li>Point 1</li>" in description
