from datetime import UTC, datetime

from app import pipeline
from app.models import Article, Status
from app.pipeline import _record_attempt, run_cycle
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


def _neutralize_steps(monkeypatch, *, summarize_count: int = 0) -> list[str]:
    """Replace every pipeline step except publish with a no-op and record
    whether publish was invoked."""
    calls: list[str] = []
    monkeypatch.setattr(pipeline, "step_fetch_feed", lambda: 0)
    monkeypatch.setattr(pipeline, "step_fetch_articles", lambda: 0)
    monkeypatch.setattr(pipeline, "step_fetch_discussions", lambda: 0)
    monkeypatch.setattr(pipeline, "step_summarize", lambda: summarize_count)
    monkeypatch.setattr(pipeline, "step_publish", lambda: calls.append("publish") or "")
    return calls


def test_run_cycle_skips_publish_when_nothing_new(isolated_settings, monkeypatch):
    calls = _neutralize_steps(monkeypatch, summarize_count=0)
    isolated_settings.feed_output_path.write_text("<rss/>", encoding="utf-8")
    run_cycle()
    assert calls == []


def test_run_cycle_publishes_when_new_summaries(isolated_settings, monkeypatch):
    calls = _neutralize_steps(monkeypatch, summarize_count=3)
    isolated_settings.feed_output_path.write_text("<rss/>", encoding="utf-8")
    run_cycle()
    assert calls == ["publish"]


def test_run_cycle_publishes_when_feed_missing(isolated_settings, monkeypatch):
    calls = _neutralize_steps(monkeypatch, summarize_count=0)
    assert not isolated_settings.feed_output_path.exists()
    run_cycle()
    assert calls == ["publish"]


def test_step_summarize_trips_cost_breaker(isolated_settings, monkeypatch):
    isolated_settings.daily_cost_limit_usd = 1.0
    monkeypatch.setattr(pipeline, "today_spend", lambda: 5.0)

    def boom(*args, **kwargs):
        raise AssertionError("iter_by_status should not be called once breaker trips")

    monkeypatch.setattr(pipeline, "iter_by_status", boom)
    assert pipeline.step_summarize() == 0


def test_step_summarize_ignores_breaker_when_unmeasurable(isolated_settings, monkeypatch):
    isolated_settings.daily_cost_limit_usd = 1.0
    monkeypatch.setattr(pipeline, "today_spend", lambda: None)
    monkeypatch.setattr(pipeline, "iter_by_status", lambda _status: iter(()))
    # Fail open: no spend signal means we proceed, which here just finds no work.
    assert pipeline.step_summarize() == 0


def test_step_summarize_breaker_disabled_when_limit_is_zero(isolated_settings, monkeypatch):
    isolated_settings.daily_cost_limit_usd = 0.0

    def boom():
        raise AssertionError("today_spend should not be probed when the breaker is off")

    monkeypatch.setattr(pipeline, "today_spend", boom)
    monkeypatch.setattr(pipeline, "iter_by_status", lambda _status: iter(()))
    assert pipeline.step_summarize() == 0
