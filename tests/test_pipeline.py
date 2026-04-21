from datetime import UTC, datetime

from app.models import Article, Status
from app.pipeline import _record_attempt
from app.storage import load, save, sidecar_path, write_sidecar


def _make_article(guid: str = "https://news.ycombinator.com/item?id=1") -> Article:
    return Article(
        guid=guid,
        url="https://example.com/a",
        hn_url="https://news.ycombinator.com/item?id=1",
        hn_item_id=1,
        title="t",
        source_published_at=datetime(2026, 4, 21, 8, 0, tzinfo=UTC),
        our_published_at=datetime(2026, 4, 21, 9, 0, tzinfo=UTC),
        status=Status.PENDING,
    )


def test_record_attempt_first_failure_keeps_article_in_place(isolated_settings):
    isolated_settings.max_attempts = 3
    article = _make_article()
    path = save(article)
    _record_attempt(path, article, "body", "network glitch")
    assert path.exists()
    reloaded, _ = load(path)
    assert reloaded.attempts == 1
    assert reloaded.error == "network glitch"
    assert reloaded.status == Status.PENDING  # unchanged until we exhaust retries


def test_record_attempt_moves_to_failed_at_last_attempt(isolated_settings):
    isolated_settings.max_attempts = 3
    article = _make_article()
    path = save(article)
    _record_attempt(path, article, "body", "fail 1")
    reloaded_1, _ = load(path)
    _record_attempt(path, reloaded_1, "body", "fail 2")
    reloaded_2, _ = load(path)
    _record_attempt(path, reloaded_2, "body", "fail 3")
    assert not path.exists()
    failed_files = list(isolated_settings.failed_dir.rglob("*.md"))
    assert len(failed_files) == 1
    recovered, _ = load(failed_files[0])
    assert recovered.status == Status.FAILED
    assert recovered.attempts == 3
    assert recovered.error == "fail 3"


def test_record_attempt_clears_sidecars_when_moving_to_failed(isolated_settings):
    isolated_settings.max_attempts = 1  # fail immediately
    article = _make_article()
    path = save(article)
    write_sidecar(path, "article", "raw article text")
    write_sidecar(path, "discussion", "raw discussion text")
    assert sidecar_path(path, "article").exists()
    assert sidecar_path(path, "discussion").exists()

    _record_attempt(path, article, "body", "boom")

    assert not sidecar_path(path, "article").exists()
    assert not sidecar_path(path, "discussion").exists()


def test_record_attempt_keeps_sidecars_before_final_failure(isolated_settings):
    isolated_settings.max_attempts = 3
    article = _make_article()
    path = save(article)
    write_sidecar(path, "article", "raw")
    _record_attempt(path, article, "body", "first fail")
    # sidecars must still be there — a retry will consume them on the next run
    assert sidecar_path(path, "article").exists()
