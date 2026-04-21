from datetime import UTC, datetime
from itertools import islice

from app.models import Article, ContentSource, Status
from app.storage import (
    clear_sidecars,
    iter_by_status,
    iter_summarized,
    load,
    move_to_failed,
    path_for,
    read_sidecar,
    save,
    short_hash,
    sidecar_path,
    write_sidecar,
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


def test_sidecar_roundtrip(isolated_settings):
    article = _make_article("guid-sidecar")
    path = save(article)
    write_sidecar(path, "article", "raw content")
    write_sidecar(path, "discussion", "raw discussion")
    assert read_sidecar(path, "article") == "raw content"
    assert read_sidecar(path, "discussion") == "raw discussion"
    assert read_sidecar(path, "missing") is None


def test_clear_sidecars_removes_all_transient_files(isolated_settings):
    article = _make_article("guid-clear")
    path = save(article)
    write_sidecar(path, "article", "raw content")
    write_sidecar(path, "discussion", "raw discussion")
    assert sidecar_path(path, "article").exists()
    assert sidecar_path(path, "discussion").exists()
    clear_sidecars(path)
    assert not sidecar_path(path, "article").exists()
    assert not sidecar_path(path, "discussion").exists()
    # The article .md itself stays untouched.
    assert path.exists()


def _make_summarized(hn_item_id: int, source_date: datetime) -> Article:
    article = Article(
        guid=f"https://news.ycombinator.com/item?id={hn_item_id}",
        url=f"https://example.com/{hn_item_id}",
        hn_url=f"https://news.ycombinator.com/item?id={hn_item_id}",
        hn_item_id=hn_item_id,
        title=f"t-{hn_item_id}",
        source_published_at=source_date,
        our_published_at=source_date,
        status=Status.SUMMARIZED,
    )
    return article


def test_iter_summarized_yields_newest_day_first(isolated_settings):
    older = _make_summarized(100, datetime(2026, 4, 19, 12, 0, tzinfo=UTC))
    newer = _make_summarized(200, datetime(2026, 4, 21, 12, 0, tzinfo=UTC))
    middle = _make_summarized(150, datetime(2026, 4, 20, 12, 0, tzinfo=UTC))
    for a in (older, newer, middle):
        save(a)
    ids = [a.hn_item_id for _, a, _ in iter_summarized()]
    assert ids == [200, 150, 100]


def test_iter_summarized_sorts_within_day_by_hn_item_id_desc(isolated_settings):
    same_day = datetime(2026, 4, 20, 8, 0, tzinfo=UTC)
    for hid in (101, 105, 103, 110):
        save(_make_summarized(hid, same_day))
    ids = [a.hn_item_id for _, a, _ in iter_summarized()]
    assert ids == [110, 105, 103, 101]


def test_iter_summarized_skips_non_summarized(isolated_settings):
    summarized = _make_summarized(200, datetime(2026, 4, 21, 12, 0, tzinfo=UTC))
    pending = _make_summarized(150, datetime(2026, 4, 20, 12, 0, tzinfo=UTC))
    pending.status = Status.PENDING
    save(summarized)
    save(pending)
    ids = [a.hn_item_id for _, a, _ in iter_summarized()]
    assert ids == [200]


def test_iter_summarized_skips_failed_tree(isolated_settings):
    ok = _make_summarized(200, datetime(2026, 4, 21, 12, 0, tzinfo=UTC))
    doomed = _make_summarized(199, datetime(2026, 4, 21, 12, 0, tzinfo=UTC))
    save(ok)
    doomed_path = save(doomed)
    move_to_failed(doomed_path, doomed, "body")
    ids = [a.hn_item_id for _, a, _ in iter_summarized()]
    assert ids == [200]


def test_iter_summarized_is_lazy_and_stops_on_early_break(isolated_settings):
    # Ten summarized articles across different days; consuming only the top
    # two must not load the rest (indirectly verified: islice terminates and
    # returns the two newest without raising or scanning further).
    for i in range(10):
        save(_make_summarized(
            hn_item_id=1000 + i,
            source_date=datetime(2026, 4, 10 + i, 12, 0, tzinfo=UTC),
        ))
    ids = [a.hn_item_id for _, a, _ in islice(iter_summarized(), 2)]
    assert ids == [1009, 1008]


def test_iter_by_status_skips_failed_tree(isolated_settings):
    article = _make_article("guid-skip")
    article.status = Status.PENDING
    original = save(article)
    move_to_failed(original, article, "body")
    results = list(iter_by_status(Status.FAILED))
    assert results == []
