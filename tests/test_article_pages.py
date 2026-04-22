from datetime import UTC, datetime

from app.article_pages import write_article_pages
from app.models import Article, ContentSource, Status
from app.storage import save, short_hash


def _make_article(
    guid: str,
    *,
    hn_item_id: int,
    title: str = "Titre original",
    rewritten_title: str | None = None,
) -> Article:
    return Article(
        guid=guid,
        url="https://example.com/a",
        hn_url=f"https://news.ycombinator.com/item?id={hn_item_id}",
        hn_item_id=hn_item_id,
        title=title,
        rewritten_title=rewritten_title,
        source_published_at=datetime(2026, 4, 20, 8, 0, tzinfo=UTC),
        our_published_at=datetime(2026, 4, 21, 9, 0, tzinfo=UTC),
        status=Status.SUMMARIZED,
        content_source=ContentSource.EXTRACTED,
        summarized_at=datetime(2026, 4, 21, 9, 5, tzinfo=UTC),
    )


def test_writes_one_page_per_summarized_article(isolated_settings):
    save(_make_article("g1", hn_item_id=1), "## Résumé\n\nCorps.")
    save(_make_article("g2", hn_item_id=2), "## Résumé\n\nAutre corps.")
    assert write_article_pages() == 2
    out = isolated_settings.artefacts_dir / "a"
    assert (out / f"{short_hash('g1')}.html").exists()
    assert (out / f"{short_hash('g2')}.html").exists()


def test_page_renders_markdown_body_to_html(isolated_settings):
    save(
        _make_article("g1", hn_item_id=1),
        "## Résumé\n\n- premier point\n- second point\n",
    )
    write_article_pages()
    html = (
        isolated_settings.artefacts_dir / "a" / f"{short_hash('g1')}.html"
    ).read_text(encoding="utf-8")
    assert "<h2>Résumé</h2>" in html
    assert "<li>premier point</li>" in html
    assert "<li>second point</li>" in html


def test_page_uses_rewritten_title_when_present(isolated_settings):
    save(
        _make_article(
            "g1",
            hn_item_id=1,
            title="Brouillon",
            rewritten_title="Titre réécrit",
        ),
        "Corps",
    )
    write_article_pages()
    html = (
        isolated_settings.artefacts_dir / "a" / f"{short_hash('g1')}.html"
    ).read_text(encoding="utf-8")
    assert "<h1>Titre réécrit</h1>" in html
    # Original title is shown as a secondary line.
    assert "Brouillon" in html


def test_page_links_to_original_and_hn(isolated_settings):
    save(_make_article("g1", hn_item_id=42), "Corps")
    write_article_pages()
    html = (
        isolated_settings.artefacts_dir / "a" / f"{short_hash('g1')}.html"
    ).read_text(encoding="utf-8")
    assert 'href="https://example.com/a"' in html
    assert 'href="https://news.ycombinator.com/item?id=42"' in html


def test_page_escapes_raw_html_in_body(isolated_settings):
    save(_make_article("g1", hn_item_id=1), "<script>boom()</script>")
    write_article_pages()
    html = (
        isolated_settings.artefacts_dir / "a" / f"{short_hash('g1')}.html"
    ).read_text(encoding="utf-8")
    assert "<script>boom()</script>" not in html
    assert "&lt;script&gt;" in html
