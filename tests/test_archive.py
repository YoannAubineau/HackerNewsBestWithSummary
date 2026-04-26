from datetime import UTC, datetime

from app.archive import write_archive
from app.models import Article, ContentSource, Status
from app.storage import save, short_hash


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
    assert f"/{short_hash('g1')}.md" in html
    assert f"/{short_hash('g2')}.md" in html
    assert "github.com/YoannAubineau/HackerNewsBestWithSummary/blob/main" in html


def test_archive_url_matches_storage_partition(isolated_settings):
    # Link must mirror path_for(): partition by our_published_at, not
    # source_published_at — otherwise the GitHub blob URL 404s.
    save(_make_article("g1", hn_item_id=1), "body")
    html = write_archive().read_text(encoding="utf-8")
    assert "/artefacts/articles/2026/04/21/" in html
    assert "/artefacts/articles/2026/04/20/" not in html


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


def test_archive_wires_simple_datatables(isolated_settings):
    save(_make_article("g1", hn_item_id=1), "body")
    html = write_archive().read_text(encoding="utf-8")
    # CSS from jsDelivr.
    assert (
        'https://cdn.jsdelivr.net/npm/simple-datatables@10/dist/style.css' in html
    )
    # JS bundle from jsDelivr.
    assert 'https://cdn.jsdelivr.net/npm/simple-datatables@10' in html
    # Table is initialised and the title column (index 4) is flagged non-sortable.
    assert 'new simpleDatatables.DataTable("#archive"' in html
    assert 'select: 4, sortable: false' in html
    # "Entered our feed" (index 3) drives the default sort indicator.
    assert 'select: 3, sort: "desc"' in html


def test_archive_rows_sorted_by_summarized_at_desc(isolated_settings):
    older = _make_article(
        "g-older",
        hn_item_id=1,
        summarized_at=datetime(2026, 4, 20, 10, 0, tzinfo=UTC),
    )
    newer = _make_article(
        "g-newer",
        hn_item_id=2,
        summarized_at=datetime(2026, 4, 22, 10, 0, tzinfo=UTC),
    )
    save(older, "body")
    save(newer, "body")
    html = write_archive().read_text(encoding="utf-8")
    assert html.index(short_hash("g-newer")) < html.index(short_hash("g-older"))


def test_archive_emits_single_file_only(isolated_settings):
    save(_make_article("g1", hn_item_id=1), "body")
    write_archive()
    out = isolated_settings.artefacts_dir
    assert (out / "archive.html").exists()
    # No more pre-sorted variants.
    assert not (out / "archive-best.html").exists()
    assert not (out / "archive-hn.html").exists()
    assert not list(out.glob("archive-*.html"))
