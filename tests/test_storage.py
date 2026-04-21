from datetime import UTC, datetime

from app.models import Article, ContentSource, Status
from app.storage import (
    iter_by_status,
    load,
    move_to_failed,
    path_for,
    save,
    short_hash,
)


def _make_article(guid: str = "https://news.ycombinator.com/item?id=1") -> Article:
    return Article(
        guid=guid,
        url="https://example.com/a",
        hn_url="https://news.ycombinator.com/item?id=1",
        hn_item_id=1,
        title="Titre",
        source_published_at=datetime(2026, 4, 21, 8, 30, tzinfo=UTC),
        our_published_at=datetime(2026, 4, 21, 9, 0, tzinfo=UTC),
    )


def test_short_hash_stable():
    assert short_hash("abc") == short_hash("abc")
    assert len(short_hash("abc")) == 8
    assert short_hash("abc") != short_hash("abd")


def test_path_for_partitions_by_date(isolated_settings):
    article = _make_article()
    p = path_for(article.guid, article.source_published_at)
    assert p.parts[-4:] == ("2026", "04", "21", f"{short_hash(article.guid)}.md")
    assert p.is_absolute() or str(isolated_settings.articles_dir) in str(p)


def test_save_and_load_roundtrip(isolated_settings):
    article = _make_article()
    article.status = Status.SUMMARIZED
    article.content_source = ContentSource.EXTRACTED
    article.summarized_at = datetime(2026, 4, 21, 9, 5, tzinfo=UTC)
    article.model = "deepseek/deepseek-chat-v3:free"
    body = "## Résumé\n\nCorps markdown."
    path = save(article, body)
    assert path.exists()
    loaded, loaded_body = load(path)
    assert loaded.guid == article.guid
    assert loaded.status == Status.SUMMARIZED
    assert loaded.content_source == ContentSource.EXTRACTED
    assert loaded.model == "deepseek/deepseek-chat-v3:free"
    assert loaded_body.strip() == body.strip()


def test_save_is_idempotent_on_same_guid(isolated_settings):
    article = _make_article()
    p1 = save(article)
    p2 = save(article)
    assert p1 == p2


def test_iter_by_status_filters(isolated_settings):
    a = _make_article("guid-a")
    a.status = Status.PENDING
    b = _make_article("guid-b")
    b.status = Status.SUMMARIZED
    save(a)
    save(b)
    pending = list(iter_by_status(Status.PENDING))
    summarized = list(iter_by_status(Status.SUMMARIZED))
    assert len(pending) == 1
    assert len(summarized) == 1
    assert pending[0][1].guid == "guid-a"
    assert summarized[0][1].guid == "guid-b"


def test_move_to_failed_removes_source_and_creates_failed(isolated_settings):
    article = _make_article("guid-fail")
    article.status = Status.PENDING
    original = save(article)
    dest = move_to_failed(original, article, "body")
    assert not original.exists()
    assert dest.exists()
    assert "_failed" in dest.parts
    loaded, _ = load(dest)
    assert loaded.status == Status.FAILED


def test_iter_by_status_skips_failed_tree(isolated_settings):
    article = _make_article("guid-skip")
    article.status = Status.PENDING
    original = save(article)
    move_to_failed(original, article, "body")
    results = list(iter_by_status(Status.FAILED))
    assert results == []
