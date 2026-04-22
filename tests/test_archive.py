from datetime import UTC, datetime

from app.archive import write_archive
from app.models import Article, ContentSource, Status
from app.storage import save


def _make_article(
    guid: str,
    *,
    hn_item_id: int,
    rewritten_title: str | None = None,
    title: str = "Titre original",
    source_published_at: datetime | None = None,
    our_published_at: datetime | None = None,
    summarized_at: datetime | None = None,
) -> Article:
    return Article(
        guid=guid,
        url="https://example.com/a",
        hn_url=f"https://news.ycombinator.com/item?id={hn_item_id}",
        hn_item_id=hn_item_id,
        title=title,
        rewritten_title=rewritten_title,
        source_published_at=source_published_at
        or datetime(2026, 4, 20, 8, 0, tzinfo=UTC),
        our_published_at=our_published_at
        or datetime(2026, 4, 21, 9, 0, tzinfo=UTC),
        status=Status.SUMMARIZED,
        content_source=ContentSource.EXTRACTED,
        summarized_at=summarized_at or datetime(2026, 4, 21, 9, 5, tzinfo=UTC),
    )


def test_archive_lists_every_summarized_article(isolated_settings):
    save(_make_article("g1", hn_item_id=10), "body")
    save(_make_article("g2", hn_item_id=20), "body")
    path = write_archive()
    html = path.read_text(encoding="utf-8")
    assert html.count("<tr>") == 3  # header + 2 articles
    assert "item?id=10" in html
    assert "item?id=20" in html


def test_archive_prefers_rewritten_title(isolated_settings):
    save(
        _make_article("g1", hn_item_id=1, rewritten_title="Titre réécrit"),
        "body",
    )
    html = write_archive().read_text(encoding="utf-8")
    assert "Titre réécrit" in html
    assert "Titre original" not in html


def test_archive_falls_back_to_original_title(isolated_settings):
    save(_make_article("g1", hn_item_id=1, title="Le vrai"), "body")
    html = write_archive().read_text(encoding="utf-8")
    assert "Le vrai" in html


def test_archive_emits_iso_timestamps_for_sorting(isolated_settings):
    article = _make_article(
        "g1",
        hn_item_id=1,
        source_published_at=datetime(2026, 1, 2, 3, 4, tzinfo=UTC),
        our_published_at=datetime(2026, 2, 3, 4, 5, tzinfo=UTC),
        summarized_at=datetime(2026, 3, 4, 5, 6, tzinfo=UTC),
    )
    save(article, "body")
    html = write_archive().read_text(encoding="utf-8")
    # Every sortable date column carries a data-iso attribute.
    assert 'data-iso="2026-01-02T03:04:00+00:00"' in html
    assert 'data-iso="2026-02-03T04:05:00+00:00"' in html
    assert 'data-iso="2026-03-04T05:06:00+00:00"' in html


def test_archive_ignores_non_summarized_articles(isolated_settings):
    summarized = _make_article("g1", hn_item_id=1)
    pending = _make_article("g2", hn_item_id=2)
    pending.status = Status.PENDING
    save(summarized, "body")
    save(pending, "body")
    html = write_archive().read_text(encoding="utf-8")
    assert "item?id=1" in html
    assert "item?id=2" not in html


def test_archive_escapes_html_in_title(isolated_settings):
    article = _make_article("g1", hn_item_id=1, title="<script>boom()</script>")
    save(article, "body")
    html = write_archive().read_text(encoding="utf-8")
    assert "<script>boom()</script>" not in html
    assert "&lt;script&gt;" in html
