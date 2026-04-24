from datetime import UTC, datetime

from app import pipeline
from app.llm import LLMCallResult
from app.models import Article, ContentSource, Status
from app.pipeline import (
    _record_attempt,
    run_cycle,
    step_fetch_articles,
    step_fetch_discussions,
    step_fetch_feed,
)
from app.rss_in import FeedEntry
from app.storage import load, move_to_failed, read_sidecar, save, sidecar_path, write_sidecar
from app.summarize import ArticleSummary


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


def _make_ask_hn_article(hn_item_id: int = 42) -> Article:
    return Article(
        guid=f"https://news.ycombinator.com/item?id={hn_item_id}",
        url=f"https://news.ycombinator.com/item?id={hn_item_id}",
        hn_url=f"https://news.ycombinator.com/item?id={hn_item_id}",
        hn_item_id=hn_item_id,
        title="Ask HN: what's your X?",
        source_published_at=datetime(2026, 4, 21, 8, 0, tzinfo=UTC),
        our_published_at=datetime(2026, 4, 21, 9, 0, tzinfo=UTC),
        status=Status.PENDING,
        is_ask_or_show_hn=True,
    )


def test_record_attempt_first_failure_keeps_article_in_place(isolated_settings):
    isolated_settings.max_attempts = 3
    article = _make_article()
    path = save(article)
    failures: list[tuple[str, str]] = []
    moved = _record_attempt(path, article, "body", "network glitch", failures)
    assert moved is False
    assert failures == []
    assert path.exists()
    reloaded, _ = load(path)
    assert reloaded.attempts == 1
    assert reloaded.error == "network glitch"
    assert reloaded.status == Status.PENDING  # unchanged until we exhaust retries


def test_record_attempt_moves_to_failed_at_last_attempt(isolated_settings):
    isolated_settings.max_attempts = 3
    article = _make_article()
    path = save(article)
    failures: list[tuple[str, str]] = []
    assert _record_attempt(path, article, "body", "fail 1", failures) is False
    reloaded_1, _ = load(path)
    assert _record_attempt(path, reloaded_1, "body", "fail 2", failures) is False
    reloaded_2, _ = load(path)
    assert _record_attempt(path, reloaded_2, "body", "fail 3", failures) is True
    assert not path.exists()
    failed_files = list(isolated_settings.failed_dir.rglob("*.md"))
    assert len(failed_files) == 1
    recovered, _ = load(failed_files[0])
    assert recovered.status == Status.FAILED
    assert recovered.attempts == 3
    assert recovered.error == "fail 3"
    assert failures == [(article.guid, "fail 3")]


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
    monkeypatch.setattr(pipeline, "step_fetch_articles", lambda _failures=None: 0)
    monkeypatch.setattr(pipeline, "step_fetch_discussions", lambda _failures=None: 0)
    monkeypatch.setattr(pipeline, "step_summarize", lambda _failures=None: summarize_count)
    monkeypatch.setattr(pipeline, "step_publish", lambda: calls.append("publish") or "")
    return calls


def test_run_cycle_publishes_even_when_nothing_new(isolated_settings, monkeypatch):
    # Always republishing lets publish-side code changes propagate on the
    # next cycle without waiting for a fresh HN submission.
    calls = _neutralize_steps(monkeypatch, summarize_count=0)
    isolated_settings.feed_output_path.write_text("<rss/>", encoding="utf-8")
    run_cycle()
    assert calls == ["publish"]


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


def test_run_cycle_returns_empty_failures_when_all_steps_clean(
    isolated_settings, monkeypatch
):
    _neutralize_steps(monkeypatch, summarize_count=0)
    isolated_settings.feed_output_path.write_text("<rss/>", encoding="utf-8")
    result = run_cycle()
    assert result.failures == []


def test_run_cycle_collects_failures_from_steps(isolated_settings, monkeypatch):
    isolated_settings.feed_output_path.write_text("<rss/>", encoding="utf-8")

    def fake_fetch_articles(failures=None):
        if failures is not None:
            failures.append(("guid://a", "boom a"))
        return 0

    def fake_fetch_discussions(failures=None):
        if failures is not None:
            failures.append(("guid://b", "boom b"))
        return 0

    monkeypatch.setattr(pipeline, "step_fetch_feed", lambda: 0)
    monkeypatch.setattr(pipeline, "step_fetch_articles", fake_fetch_articles)
    monkeypatch.setattr(pipeline, "step_fetch_discussions", fake_fetch_discussions)
    monkeypatch.setattr(pipeline, "step_summarize", lambda _failures=None: 0)
    monkeypatch.setattr(pipeline, "step_publish", lambda: "")

    result = run_cycle()
    assert result.failures == [("guid://a", "boom a"), ("guid://b", "boom b")]


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


def test_step_fetch_articles_writes_submitter_sidecar_for_ask_hn(
    isolated_settings, httpx_mock
):
    article = _make_ask_hn_article(hn_item_id=42)
    path = save(article)
    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/42",
        json={
            "author": "op",
            "text": "<p>First paragraph.</p><p>Second paragraph.</p>",
            "children": [],
        },
    )

    assert step_fetch_articles() == 1

    sidecar = sidecar_path(path, "article")
    assert sidecar.exists()
    assert sidecar.read_text(encoding="utf-8") == "First paragraph.\n\nSecond paragraph."
    reloaded, _ = load(path)
    assert reloaded.status == Status.ARTICLE_FETCHED
    assert reloaded.content_source == ContentSource.ASK_SHOW_HN


def test_step_fetch_articles_skips_sidecar_when_submitter_text_empty(
    isolated_settings, httpx_mock
):
    article = _make_ask_hn_article(hn_item_id=43)
    path = save(article)
    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/43",
        json={"author": "op", "text": None, "children": []},
    )

    assert step_fetch_articles() == 1

    assert not sidecar_path(path, "article").exists()
    reloaded, _ = load(path)
    assert reloaded.status == Status.ARTICLE_FETCHED
    assert reloaded.content_source == ContentSource.ASK_SHOW_HN


def test_step_fetch_discussions_writes_top_comments_sidecar(
    isolated_settings, httpx_mock, monkeypatch
):
    from app import fetch_discussion as fd

    article = _make_article("guid-top-comments")
    article.status = Status.ARTICLE_FETCHED
    article.content_source = ContentSource.EXTRACTED
    article.hn_item_id = 500
    path = save(article)

    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/500",
        json={
            "id": 500,
            "children": [
                {
                    "id": 501,
                    "author": "alice",
                    "text": "winner comment",
                    "points": 42,
                    "children": [
                        {
                            "id": 502,
                            "author": "bob",
                            "text": "reply",
                            "points": 10,
                            "children": [],
                        },
                    ],
                },
            ],
        },
    )
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [501])

    assert step_fetch_discussions() == 1

    sidecar = sidecar_path(path, "top_comments")
    assert sidecar.exists()
    content = sidecar.read_text(encoding="utf-8")
    assert content.startswith("**Commentaires les plus plébiscités** :")
    assert "[alice](https://news.ycombinator.com/item?id=501)" in content


def test_step_summarize_reads_and_clears_top_comments_sidecar(
    isolated_settings, monkeypatch
):
    isolated_settings.llm_sleep_seconds = 0
    article = _make_article("guid-top-flow")
    article.status = Status.DISCUSSION_FETCHED
    article.content_source = ContentSource.EXTRACTED
    path = save(article)
    write_sidecar(path, "article", "raw article")
    write_sidecar(path, "discussion", "raw discussion")
    top_md = (
        "**Commentaires les plus plébiscités** :\n\n"
        "- [alice](https://news.ycombinator.com/item?id=501) : « hi »"
    )
    write_sidecar(path, "top_comments", top_md)

    def fake_summarize_article(text, title):
        return ArticleSummary(
            rewritten_title=None, summary_markdown="- s"
        ), LLMCallResult(content="", model="m", input_tokens=1, output_tokens=1,
                         latency_ms=1)

    def fake_summarize_discussion(text, title):
        return "**Avis positifs** :\n- ok", LLMCallResult(
            content="", model="m", input_tokens=1, output_tokens=1, latency_ms=1,
        )

    monkeypatch.setattr(pipeline, "summarize_article", fake_summarize_article)
    monkeypatch.setattr(pipeline, "summarize_discussion", fake_summarize_discussion)
    monkeypatch.setattr(pipeline, "today_spend", lambda: None)

    assert pipeline.step_summarize() == 1

    _, final_body = load(path)
    assert "**Commentaires les plus plébiscités**" in final_body
    assert "[alice](https://news.ycombinator.com/item?id=501)" in final_body
    assert read_sidecar(path, "top_comments") is None


def test_step_summarize_records_llm_metrics(isolated_settings, monkeypatch):
    isolated_settings.llm_sleep_seconds = 0
    article = _make_article("guid-metrics")
    article.status = Status.DISCUSSION_FETCHED
    article.content_source = ContentSource.EXTRACTED
    path = save(article)
    write_sidecar(path, "article", "raw article")
    write_sidecar(path, "discussion", "raw discussion")

    def fake_summarize_article(text, title):
        return ArticleSummary(
            rewritten_title="titre réécrit",
            summary_markdown="- point",
        ), LLMCallResult(
            content="ignored",
            model="anthropic/claude-haiku-4.5",
            input_tokens=1000,
            output_tokens=200,
            latency_ms=1500,
        )

    def fake_summarize_discussion(text, title):
        return "**Avis positifs** :\n- ok", LLMCallResult(
            content="ignored",
            model="z-ai/glm-4.6:free",
            input_tokens=300,
            output_tokens=80,
            latency_ms=900,
        )

    monkeypatch.setattr(pipeline, "summarize_article", fake_summarize_article)
    monkeypatch.setattr(pipeline, "summarize_discussion", fake_summarize_discussion)
    monkeypatch.setattr(pipeline, "today_spend", lambda: None)

    assert pipeline.step_summarize() == 1

    reloaded, _ = load(path)
    assert reloaded.status == Status.SUMMARIZED
    assert reloaded.llm_models_used == [
        "anthropic/claude-haiku-4.5",
        "z-ai/glm-4.6:free",
    ]
    assert reloaded.llm_input_tokens == 1300
    assert reloaded.llm_output_tokens == 280
    assert reloaded.llm_latency_ms == 2400


def _make_feed_entry(guid: str, hn_item_id: int = 42) -> FeedEntry:
    return FeedEntry(
        guid=guid,
        title="t",
        url="https://example.com/a",
        hn_url=f"https://news.ycombinator.com/item?id={hn_item_id}",
        hn_item_id=hn_item_id,
        source_published_at=datetime(2026, 4, 21, 8, 0, tzinfo=UTC),
        feed_summary="",
        is_ask_or_show_hn=False,
        observed_at=datetime(2026, 4, 22, 9, 0, tzinfo=UTC),
    )


def test_step_fetch_feed_skips_already_seen_guid(isolated_settings, monkeypatch):
    # An existing article saved under a DIFFERENT our_published_at than the
    # feed's observed_at must still be recognised as already-seen. The
    # former bug: path-based check with source_published_at happened to
    # work because source_published_at is stable; with our_published_at
    # based partitioning, only a guid-wide lookup works.
    existing = _make_article("guid-seen")
    save(existing)
    entry = _make_feed_entry(
        "guid-seen",
        hn_item_id=1,
    )
    # Feed's observed_at is a different day than the saved our_published_at.
    entry.observed_at = datetime(2026, 5, 1, 12, 0, tzinfo=UTC)
    monkeypatch.setattr(pipeline, "fetch_source_feed", lambda: [entry])
    assert step_fetch_feed() == 0


def test_step_fetch_feed_skips_failed_guid(isolated_settings, monkeypatch):
    article = _make_article("guid-prev-failed")
    article.status = Status.PENDING
    path = save(article)
    move_to_failed(path, article, "body")
    entry = _make_feed_entry("guid-prev-failed", hn_item_id=1)
    monkeypatch.setattr(pipeline, "fetch_source_feed", lambda: [entry])
    assert step_fetch_feed() == 0


def test_step_fetch_feed_creates_new_pending(isolated_settings, monkeypatch):
    entry = _make_feed_entry("guid-fresh", hn_item_id=777)
    monkeypatch.setattr(pipeline, "fetch_source_feed", lambda: [entry])
    assert step_fetch_feed() == 1


def test_step_summarize_breaker_disabled_when_limit_is_zero(isolated_settings, monkeypatch):
    isolated_settings.daily_cost_limit_usd = 0.0

    def boom():
        raise AssertionError("today_spend should not be probed when the breaker is off")

    monkeypatch.setattr(pipeline, "today_spend", boom)
    monkeypatch.setattr(pipeline, "iter_by_status", lambda _status: iter(()))
    assert pipeline.step_summarize() == 0
