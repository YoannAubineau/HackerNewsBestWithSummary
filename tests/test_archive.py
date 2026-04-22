from datetime import UTC, datetime

from app import archive
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
    # Titles link to the Markdown file rendered on github.com.
    from app.storage import short_hash

    assert f"/{short_hash('g1')}.md" in html
    assert f"/{short_hash('g2')}.md" in html
    assert "github.com/YoannAubineau/HackerNewsBestWithSummary/blob/main" in html


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


def test_archive_formats_dates_as_iso_minute(isolated_settings):
    article = _make_article(
        "g1",
        hn_item_id=1,
        source_published_at=datetime(2026, 1, 2, 3, 4, tzinfo=UTC),
        our_published_at=datetime(2026, 2, 3, 4, 5, tzinfo=UTC),
        summarized_at=datetime(2026, 3, 4, 5, 6, tzinfo=UTC),
    )
    save(article, "body")
    html = write_archive().read_text(encoding="utf-8")
    assert "2026-01-02 03:04" in html
    assert "2026-02-03 04:05" in html
    assert "2026-03-04 05:06" in html


def test_archive_ignores_non_summarized_articles(isolated_settings):
    from app.storage import short_hash

    summarized = _make_article("g1", hn_item_id=1)
    pending = _make_article("g2", hn_item_id=2)
    pending.status = Status.PENDING
    save(summarized, "body")
    save(pending, "body")
    html = write_archive().read_text(encoding="utf-8")
    assert short_hash("g1") in html
    assert short_hash("g2") not in html


def test_archive_shows_hn_id_linking_to_discussion(isolated_settings):
    save(_make_article("g1", hn_item_id=47861270), "body")
    html = write_archive().read_text(encoding="utf-8")
    assert (
        '<a href="https://news.ycombinator.com/item?id=47861270"'
        ' rel="noopener">47861270</a>'
    ) in html


def test_archive_escapes_html_in_title(isolated_settings):
    article = _make_article("g1", hn_item_id=1, title="<script>boom()</script>")
    save(article, "body")
    html = write_archive().read_text(encoding="utf-8")
    assert "<script>boom()</script>" not in html
    assert "&lt;script&gt;" in html


def test_archive_emits_alternative_sort_pages(isolated_settings):
    save(_make_article("g1", hn_item_id=1), "body")
    write_archive()
    assert (isolated_settings.artefacts_dir / "archive.html").exists()
    assert (isolated_settings.artefacts_dir / "archive-best.html").exists()
    assert (isolated_settings.artefacts_dir / "archive-hn.html").exists()


def test_archive_paginates_when_over_page_size(isolated_settings, monkeypatch):
    monkeypatch.setattr(archive, "_PAGE_SIZE", 2)
    for i in range(1, 6):  # 5 articles → ceil(5/2) = 3 pages
        save(_make_article(f"g{i}", hn_item_id=i), "body")
    write_archive()
    out = isolated_settings.artefacts_dir
    assert (out / "archive.html").exists()  # feed view, page 1
    assert (out / "archive-feed-2.html").exists()
    assert (out / "archive-feed-3.html").exists()
    assert not (out / "archive-feed-4.html").exists()
    # Page 1 has pagination links to page 2 for the feed view.
    assert "archive-feed-2.html" in (out / "archive.html").read_text(encoding="utf-8")


def test_archive_column_headers_link_to_matching_view(isolated_settings):
    save(_make_article("g1", hn_item_id=1), "body")
    write_archive()
    feed_page = (isolated_settings.artefacts_dir / "archive.html").read_text(encoding="utf-8")
    best_page = (isolated_settings.artefacts_dir / "archive-best.html").read_text(encoding="utf-8")
    # Each date column header is a link to its own pre-sorted view.
    assert '<a href="archive.html">Entered our feed</a>' in feed_page
    assert '<a href="archive-best.html">Entered /best</a>' in feed_page
    assert '<a href="archive-hn.html">Entered HN</a>' in feed_page
    # The active column carries a dedicated class on its <th>.
    assert '<th class="active"><a href="archive.html">Entered our feed</a></th>' in feed_page
    assert '<th class="active"><a href="archive-best.html">Entered /best</a></th>' in best_page
