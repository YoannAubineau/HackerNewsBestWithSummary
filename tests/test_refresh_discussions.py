from datetime import UTC, datetime, timedelta

import pytest

from app import refresh_discussions as rd
from app.fetch_discussion import Discussion
from app.llm import AllModelsFailedError, LLMCallResult
from app.models import Article, ContentSource, Status
from app.storage import load, save, short_hash
from app.summarize import compose_body


def _make_summarized_article(
    guid: str,
    *,
    our_published_at: datetime,
    summarized_at: datetime | None,
    title: str = "Titre",
    discussion_comment_count: int = 42,
) -> Article:
    return Article(
        guid=guid,
        url="https://example.com/a",
        hn_url=f"https://news.ycombinator.com/item?id={abs(hash(guid)) % 10000}",
        hn_item_id=abs(hash(guid)) % 10000,
        title=title,
        rewritten_title=None,
        source_published_at=our_published_at,
        our_published_at=our_published_at,
        status=Status.SUMMARIZED,
        content_source=ContentSource.EXTRACTED,
        summarized_at=summarized_at,
        discussion_comment_count=discussion_comment_count,
        llm_models_used=["anthropic/claude-haiku-4.5"],
        llm_input_tokens=100,
        llm_output_tokens=50,
        llm_latency_ms=1000,
    )


def _initial_body(*, comment_count: int = 42) -> str:
    return compose_body(
        article_summary="Résumé original de l'article.",
        discussion_summary=(
            "**Avis positifs** :\n- Original positif\n\n"
            "**Avis négatifs** :\n- Original négatif"
        ),
        discussion_comment_count=comment_count,
        top_comments_markdown="**Top commentaires** :\n- @alice (orig)",
        url="https://example.com/a",
        hn_url="https://news.ycombinator.com/item?id=1",
    )


def _save_summarized(
    isolated_settings,
    *,
    guid: str,
    summarized_minutes_ago: int,
    published_minutes_ago: int = 60,
    comment_count: int = 42,
):
    now = datetime.now(UTC)
    article = _make_summarized_article(
        guid,
        our_published_at=now - timedelta(minutes=published_minutes_ago),
        summarized_at=now - timedelta(minutes=summarized_minutes_ago),
        discussion_comment_count=comment_count,
    )
    body = _initial_body(comment_count=comment_count)
    path = save(article, body)
    return article, path, body


_SENTINEL = object()


def _patch_helpers(
    monkeypatch,
    *,
    seen_ids=_SENTINEL,
    discussion_factory=None,
    summary_text: str = (
        "**Avis positifs** :\n- Nouveau positif\n\n"
        "**Avis négatifs** :\n- Nouveau négatif"
    ),
    today_spend_value=None,
):
    """Default mocks for the dependencies of step_refresh_discussions."""
    if seen_ids is _SENTINEL:
        seen_ids = set()
    monkeypatch.setattr(rd, "fetch_feedly_origin_ids", lambda count=100: seen_ids)
    monkeypatch.setattr(rd, "today_spend", lambda: today_spend_value)
    monkeypatch.setattr(rd, "time", _NoSleep())

    def default_discussion(_hn_item_id: int) -> Discussion:
        return Discussion(
            comment_count=99,
            text="raw comments",
            top_comments_markdown="**Top commentaires** :\n- @bob (new)",
            url="https://example.com/a",
        )

    monkeypatch.setattr(
        rd, "fetch_discussion", discussion_factory or default_discussion
    )

    def fake_summarize(_text: str, _title: str):
        return summary_text, LLMCallResult(
            content=summary_text,
            model="anthropic/claude-haiku-4.5",
            input_tokens=10,
            output_tokens=20,
            latency_ms=300,
        )

    monkeypatch.setattr(rd, "summarize_discussion", fake_summarize)


class _NoSleep:
    """Replacement for the `time` module: avoids the llm_sleep_seconds wait."""

    def sleep(self, _seconds: float) -> None:
        return None


def test_no_token_skips_step(isolated_settings, monkeypatch):
    isolated_settings.feedly_dev_token = ""
    _, path, body = _save_summarized(
        isolated_settings, guid="guid-a", summarized_minutes_ago=120
    )

    def boom(*_args, **_kwargs):
        raise AssertionError("must not be called when token is empty")

    monkeypatch.setattr(rd, "fetch_feedly_origin_ids", boom)
    monkeypatch.setattr(rd, "fetch_discussion", boom)
    monkeypatch.setattr(rd, "summarize_discussion", boom)

    refreshed = rd.step_refresh_discussions(datetime.now(UTC))

    assert refreshed == 0
    assert path.read_text(encoding="utf-8").endswith(body)


def test_refresh_skipped_when_feedly_already_has_article(isolated_settings, monkeypatch):
    isolated_settings.feedly_dev_token = "tok"
    article, path, body = _save_summarized(
        isolated_settings, guid="guid-b", summarized_minutes_ago=120
    )

    def boom(*_args, **_kwargs):
        raise AssertionError("LLM/fetch must not run when Feedly already has it")

    _patch_helpers(monkeypatch, seen_ids={short_hash(article.guid)})
    monkeypatch.setattr(rd, "fetch_discussion", boom)
    monkeypatch.setattr(rd, "summarize_discussion", boom)

    refreshed = rd.step_refresh_discussions(datetime.now(UTC) - timedelta(minutes=10))

    assert refreshed == 0
    reloaded, reloaded_body = load(path)
    assert reloaded_body == body.rstrip("\n")
    assert reloaded.discussion_comment_count == 42


def test_refresh_replaces_discussion_block_when_feedly_missing(
    isolated_settings, monkeypatch
):
    isolated_settings.feedly_dev_token = "tok"
    article, path, body = _save_summarized(
        isolated_settings, guid="guid-c", summarized_minutes_ago=120
    )
    _patch_helpers(monkeypatch, seen_ids=set())

    refreshed = rd.step_refresh_discussions(
        datetime.now(UTC) - timedelta(minutes=30)
    )

    assert refreshed == 1
    reloaded, new_body = load(path)
    assert "Résumé original de l'article" in new_body
    assert "[Article original](https://example.com/a)" in new_body
    assert "Original positif" not in new_body
    assert "Nouveau positif" in new_body
    assert "Nouveau négatif" in new_body
    assert "@bob (new)" in new_body
    assert "@alice (orig)" not in new_body
    assert "## Discussion sur Hacker News (99 commentaires)" in new_body
    assert "## Discussion sur Hacker News (42 commentaires)" not in new_body
    assert reloaded.discussion_comment_count == 99
    assert reloaded.discussion_fetched_at is not None
    assert reloaded.llm_input_tokens == 110
    assert reloaded.llm_output_tokens == 70
    assert reloaded.llm_latency_ms == 1300


def test_refresh_skipped_for_articles_summarized_in_same_cycle(
    isolated_settings, monkeypatch
):
    isolated_settings.feedly_dev_token = "tok"
    cycle_started_at = datetime.now(UTC) - timedelta(minutes=5)
    _save_summarized(
        isolated_settings,
        guid="guid-d",
        summarized_minutes_ago=2,
    )

    def boom(*_args, **_kwargs):
        raise AssertionError("must not refresh in the same cycle")

    _patch_helpers(monkeypatch, seen_ids=set())
    monkeypatch.setattr(rd, "fetch_discussion", boom)
    monkeypatch.setattr(rd, "summarize_discussion", boom)

    refreshed = rd.step_refresh_discussions(cycle_started_at)

    assert refreshed == 0


def test_refresh_skipped_for_articles_older_than_max_age(
    isolated_settings, monkeypatch
):
    isolated_settings.feedly_dev_token = "tok"
    _save_summarized(
        isolated_settings,
        guid="guid-old",
        summarized_minutes_ago=60 * 30,
        published_minutes_ago=60 * 30,
    )

    def boom(*_args, **_kwargs):
        raise AssertionError("must not refresh articles past _MAX_AGE")

    _patch_helpers(monkeypatch, seen_ids=set())
    monkeypatch.setattr(rd, "fetch_discussion", boom)
    monkeypatch.setattr(rd, "summarize_discussion", boom)

    refreshed = rd.step_refresh_discussions(datetime.now(UTC) - timedelta(minutes=10))

    assert refreshed == 0


def test_refresh_skipped_when_discussion_is_dupe(isolated_settings, monkeypatch):
    isolated_settings.feedly_dev_token = "tok"
    _, path, body = _save_summarized(
        isolated_settings, guid="guid-dupe", summarized_minutes_ago=120
    )

    def dupe_discussion(_hn_item_id: int) -> Discussion:
        return Discussion(
            comment_count=0,
            text="",
            top_comments_markdown="",
            url=None,
            canonical_dupe_id=999,
        )

    _patch_helpers(monkeypatch, seen_ids=set(), discussion_factory=dupe_discussion)
    monkeypatch.setattr(
        rd, "summarize_discussion", lambda *_a, **_k: pytest.fail("LLM must not run")
    )

    refreshed = rd.step_refresh_discussions(datetime.now(UTC) - timedelta(minutes=30))

    assert refreshed == 0
    _, reloaded_body = load(path)
    assert reloaded_body == body.rstrip("\n")


def test_refresh_skipped_when_discussion_below_threshold(
    isolated_settings, monkeypatch
):
    isolated_settings.feedly_dev_token = "tok"
    isolated_settings.min_discussion_comments = 20
    _, path, body = _save_summarized(
        isolated_settings, guid="guid-thin", summarized_minutes_ago=120
    )

    def thin_discussion(_hn_item_id: int) -> Discussion:
        return Discussion(
            comment_count=5,
            text="raw",
            top_comments_markdown="",
            url=None,
        )

    _patch_helpers(monkeypatch, seen_ids=set(), discussion_factory=thin_discussion)
    monkeypatch.setattr(
        rd, "summarize_discussion", lambda *_a, **_k: pytest.fail("LLM must not run")
    )

    refreshed = rd.step_refresh_discussions(datetime.now(UTC) - timedelta(minutes=30))

    assert refreshed == 0
    _, reloaded_body = load(path)
    assert reloaded_body == body.rstrip("\n")


def test_refresh_continues_when_one_article_llm_fails(
    isolated_settings, monkeypatch
):
    isolated_settings.feedly_dev_token = "tok"
    _, path_bad, body_bad = _save_summarized(
        isolated_settings,
        guid="guid-bad",
        summarized_minutes_ago=120,
        published_minutes_ago=60,
    )
    article_good, path_good, _ = _save_summarized(
        isolated_settings,
        guid="guid-good",
        summarized_minutes_ago=180,
        published_minutes_ago=120,
    )

    calls: list[int] = []

    def fake_summarize(_text: str, _title: str):
        calls.append(1)
        if len(calls) == 1:
            raise AllModelsFailedError("all upstream LLMs failed")
        return (
            "**Avis positifs** :\n- ok\n\n**Avis négatifs** :\n- ok",
            LLMCallResult(
                content="",
                model="anthropic/claude-haiku-4.5",
                input_tokens=10,
                output_tokens=20,
                latency_ms=200,
            ),
        )

    _patch_helpers(monkeypatch, seen_ids=set())
    monkeypatch.setattr(rd, "summarize_discussion", fake_summarize)

    refreshed = rd.step_refresh_discussions(datetime.now(UTC) - timedelta(minutes=30))

    assert refreshed == 1
    _, body_bad_after = load(path_bad)
    assert body_bad_after.rstrip("\n") == body_bad.rstrip("\n")
    _, body_good_after = load(path_good)
    assert "ok" in body_good_after
    assert path_bad.exists()
    assert not isolated_settings.failed_dir.exists() or not list(
        isolated_settings.failed_dir.rglob("*.md")
    )


def test_refresh_skipped_when_body_lacks_discussion_section(
    isolated_settings, monkeypatch
):
    isolated_settings.feedly_dev_token = "tok"
    article, path, _ = _save_summarized(
        isolated_settings, guid="guid-noform", summarized_minutes_ago=120
    )
    legacy_body = compose_body(
        article_summary="Just an article summary, no discussion.",
        discussion_summary=None,
        url="https://example.com/a",
        hn_url="https://news.ycombinator.com/item?id=1",
    )
    save(article, legacy_body)

    _patch_helpers(monkeypatch, seen_ids=set())

    refreshed = rd.step_refresh_discussions(datetime.now(UTC) - timedelta(minutes=30))

    assert refreshed == 0
    _, reloaded_body = load(path)
    assert reloaded_body.rstrip("\n") == legacy_body.rstrip("\n")


def test_refresh_skipped_when_feedly_unavailable(isolated_settings, monkeypatch):
    """fetch_feedly_origin_ids returns None on HTTP / auth failure.

    We then skip the entire step rather than treat "unknown Feedly state"
    as "missing from Feedly" (which would burn LLM calls on every recent
    article every cycle while Feedly is down).
    """
    isolated_settings.feedly_dev_token = "tok"
    _, path, body = _save_summarized(
        isolated_settings, guid="guid-outage", summarized_minutes_ago=120
    )

    def boom(*_args, **_kwargs):
        raise AssertionError("must not run when Feedly state is unknown")

    _patch_helpers(monkeypatch, seen_ids=None)
    monkeypatch.setattr(rd, "fetch_discussion", boom)
    monkeypatch.setattr(rd, "summarize_discussion", boom)

    refreshed = rd.step_refresh_discussions(datetime.now(UTC) - timedelta(minutes=30))

    assert refreshed == 0
    _, body_after = load(path)
    assert body_after.rstrip("\n") == body.rstrip("\n")


def test_cost_breaker_short_circuits_step(isolated_settings, monkeypatch):
    isolated_settings.feedly_dev_token = "tok"
    isolated_settings.daily_cost_limit_usd = 2.0
    _save_summarized(
        isolated_settings, guid="guid-cost", summarized_minutes_ago=120
    )

    def boom(*_args, **_kwargs):
        raise AssertionError("must not be called when cost limit is breached")

    _patch_helpers(monkeypatch, seen_ids=set(), today_spend_value=2.5)
    monkeypatch.setattr(rd, "fetch_feedly_origin_ids", boom)
    monkeypatch.setattr(rd, "fetch_discussion", boom)
    monkeypatch.setattr(rd, "summarize_discussion", boom)

    refreshed = rd.step_refresh_discussions(datetime.now(UTC) - timedelta(minutes=30))

    assert refreshed == 0
