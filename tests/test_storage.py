from datetime import UTC, datetime
from itertools import islice

import frontmatter

from app.models import Article, ContentSource, Status
from app.storage import (
    clear_sidecars,
    find_existing,
    iter_by_status,
    iter_summarized,
    load,
    migrate_partitions,
    move_to_failed,
    path_for,
    read_sidecar,
    save,
    short_hash,
    sidecar_path,
    write_sidecar,
)


def _make_article(
    guid: str = "https://news.ycombinator.com/item?id=1",
    *,
    source_published_at: datetime = datetime(2026, 4, 21, 8, 30, tzinfo=UTC),
    our_published_at: datetime = datetime(2026, 4, 22, 9, 0, tzinfo=UTC),
) -> Article:
    return Article(
        guid=guid,
        url="https://example.com/a",
        hn_url="https://news.ycombinator.com/item?id=1",
        hn_item_id=1,
        title="Titre",
        source_published_at=source_published_at,
        our_published_at=our_published_at,
    )


def test_short_hash_stable():
    assert short_hash("abc") == short_hash("abc")
    assert len(short_hash("abc")) == 8
    assert short_hash("abc") != short_hash("abd")


def test_path_for_partitions_by_our_published_at(isolated_settings):
    # source_published_at is 2026-04-21, our_published_at is 2026-04-22 —
    # the file must land in the 2026/04/22 partition.
    article = _make_article()
    p = path_for(article.guid, article.our_published_at)
    assert p.parts[-4:] == ("2026", "04", "22", f"{short_hash(article.guid)}.md")
    assert p.is_absolute() or str(isolated_settings.articles_dir) in str(p)


def test_save_and_load_roundtrip(isolated_settings):
    article = _make_article()
    article.status = Status.SUMMARIZED
    article.content_source = ContentSource.EXTRACTED
    article.summarized_at = datetime(2026, 4, 21, 9, 5, tzinfo=UTC)
    article.llm_models_used = ["deepseek/deepseek-chat-v3:free"]
    body = "## Résumé\n\nCorps markdown."
    path = save(article, body)
    assert path.exists()
    loaded, loaded_body = load(path)
    assert loaded.guid == article.guid
    assert loaded.status == Status.SUMMARIZED
    assert loaded.content_source == ContentSource.EXTRACTED
    assert loaded.llm_models_used == ["deepseek/deepseek-chat-v3:free"]
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


def _make_summarized(
    hn_item_id: int,
    our_date: datetime,
    *,
    source_date: datetime | None = None,
) -> Article:
    article = Article(
        guid=f"https://news.ycombinator.com/item?id={hn_item_id}",
        url=f"https://example.com/{hn_item_id}",
        hn_url=f"https://news.ycombinator.com/item?id={hn_item_id}",
        hn_item_id=hn_item_id,
        title=f"t-{hn_item_id}",
        source_published_at=source_date or our_date,
        our_published_at=our_date,
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


def test_iter_summarized_sorts_within_day_by_our_published_at_desc(isolated_settings):
    # hn_item_id order is 101, 105, 103, 110; our_published_at order is
    # the reverse. The returned order must follow our_published_at.
    base_day = datetime(2026, 4, 20, 0, 0, tzinfo=UTC)
    pairs = [
        (101, base_day.replace(hour=20)),
        (105, base_day.replace(hour=15)),
        (103, base_day.replace(hour=10)),
        (110, base_day.replace(hour=5)),
    ]
    for hid, when in pairs:
        save(_make_summarized(hid, when))
    ids = [a.hn_item_id for _, a, _ in iter_summarized()]
    assert ids == [101, 105, 103, 110]


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
            our_date=datetime(2026, 4, 10 + i, 12, 0, tzinfo=UTC),
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


def test_find_existing_returns_active_match(isolated_settings):
    article = _make_article("guid-active")
    path = save(article)
    assert find_existing("guid-active") == path


def test_find_existing_returns_failed_match(isolated_settings):
    article = _make_article("guid-failed")
    article.status = Status.PENDING
    path = save(article)
    failed_path = move_to_failed(path, article, "body")
    assert find_existing("guid-failed") == failed_path


def test_find_existing_returns_none_when_absent(isolated_settings):
    assert find_existing("guid-missing") is None


def test_find_existing_finds_across_any_partition(isolated_settings):
    # A file in 2026/04/19 is findable even though the caller no longer
    # knows which our_published_at it was saved under.
    article = _make_summarized(77, datetime(2026, 4, 19, 12, 0, tzinfo=UTC))
    path = save(article)
    assert find_existing(article.guid) == path


def test_migrate_partitions_moves_file_to_our_published_at_folder(isolated_settings):
    article = _make_article(
        "guid-migrate",
        source_published_at=datetime(2026, 4, 19, 8, 0, tzinfo=UTC),
        our_published_at=datetime(2026, 4, 22, 9, 0, tzinfo=UTC),
    )
    # Simulate the pre-migration layout: the file currently lives under
    # its source_published_at partition.
    legacy_dir = isolated_settings.articles_dir / "2026" / "04" / "19"
    legacy_dir.mkdir(parents=True, exist_ok=True)
    legacy_path = legacy_dir / f"{short_hash(article.guid)}.md"
    post = frontmatter.Post(
        "body",
        **article.model_dump(mode="json", exclude_none=True),
    )
    legacy_path.write_text(frontmatter.dumps(post) + "\n", encoding="utf-8")

    moved = migrate_partitions()
    assert moved == 1

    expected = (
        isolated_settings.articles_dir / "2026" / "04" / "22"
        / f"{short_hash(article.guid)}.md"
    )
    assert expected.exists()
    assert not legacy_path.exists()
    # The now-empty 2026/04/19 directory is pruned up to the articles root.
    assert not legacy_dir.exists()


def test_migrate_partitions_is_idempotent(isolated_settings):
    article = _make_article(
        "guid-idem",
        source_published_at=datetime(2026, 4, 19, 8, 0, tzinfo=UTC),
        our_published_at=datetime(2026, 4, 22, 9, 0, tzinfo=UTC),
    )
    save(article)  # saved directly in the new-style partition
    assert migrate_partitions() == 0


def test_migrate_partitions_moves_sidecars(isolated_settings):
    article = _make_article(
        "guid-side",
        source_published_at=datetime(2026, 4, 19, 8, 0, tzinfo=UTC),
        our_published_at=datetime(2026, 4, 22, 9, 0, tzinfo=UTC),
    )
    # Place the .md plus two sidecars in the legacy folder.
    legacy_dir = isolated_settings.articles_dir / "2026" / "04" / "19"
    legacy_dir.mkdir(parents=True, exist_ok=True)
    stem = short_hash(article.guid)
    legacy_path = legacy_dir / f"{stem}.md"
    post = frontmatter.Post(
        "body",
        **article.model_dump(mode="json", exclude_none=True),
    )
    legacy_path.write_text(frontmatter.dumps(post) + "\n", encoding="utf-8")
    (legacy_dir / f"{stem}.raw.article.txt").write_text("raw article")
    (legacy_dir / f"{stem}.raw.discussion.txt").write_text("raw discussion")

    assert migrate_partitions() == 1

    target_dir = isolated_settings.articles_dir / "2026" / "04" / "22"
    assert (target_dir / f"{stem}.md").exists()
    assert (target_dir / f"{stem}.raw.article.txt").read_text() == "raw article"
    assert (target_dir / f"{stem}.raw.discussion.txt").read_text() == "raw discussion"
    assert not legacy_dir.exists()


def test_migrate_partitions_preserves_failed_flag(isolated_settings):
    article = _make_article(
        "guid-fail-mig",
        source_published_at=datetime(2026, 4, 19, 8, 0, tzinfo=UTC),
        our_published_at=datetime(2026, 4, 22, 9, 0, tzinfo=UTC),
    )
    article.status = Status.FAILED
    # Drop the file into _failed/2026/04/19 directly.
    legacy_failed_dir = isolated_settings.failed_dir / "2026" / "04" / "19"
    legacy_failed_dir.mkdir(parents=True, exist_ok=True)
    legacy_path = legacy_failed_dir / f"{short_hash(article.guid)}.md"
    post = frontmatter.Post(
        "body",
        **article.model_dump(mode="json", exclude_none=True),
    )
    legacy_path.write_text(frontmatter.dumps(post) + "\n", encoding="utf-8")

    assert migrate_partitions() == 1

    target = (
        isolated_settings.failed_dir / "2026" / "04" / "22"
        / f"{short_hash(article.guid)}.md"
    )
    assert target.exists()
    assert not legacy_path.exists()
