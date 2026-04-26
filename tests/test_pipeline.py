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
from app.storage import (
    load,
    move_to_failed,
    path_for,
    read_sidecar,
    save,
    short_hash,
    sidecar_path,
    write_sidecar,
)
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
    # step_fetch_discussions runs before step_fetch_articles in the new order,
    # so its failures are collected first.
    assert result.failures == [("guid://b", "boom b"), ("guid://a", "boom a")]


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
    article.status = Status.DISCUSSION_FETCHED
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
    article.status = Status.DISCUSSION_FETCHED
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

    isolated_settings.min_discussion_comments = 0
    article = _make_article("guid-top-comments")
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


def test_step_fetch_discussions_overwrites_url_with_algolia_canonical(
    isolated_settings, httpx_mock
):
    isolated_settings.min_discussion_comments = 0
    article = _make_article("guid-url-canonical")
    article.url = "https://feed.example.com/stale?utm=tracking"
    article.hn_item_id = 600
    path = save(article)

    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/600",
        json={
            "id": 600,
            "url": "https://canonical.example.com/article",
            "children": [],
        },
    )

    assert step_fetch_discussions() == 1

    reloaded, _ = load(path)
    assert reloaded.url == "https://canonical.example.com/article"
    assert reloaded.status == Status.DISCUSSION_FETCHED


def test_step_fetch_discussions_keeps_feed_url_when_algolia_url_missing(
    isolated_settings, httpx_mock
):
    isolated_settings.min_discussion_comments = 0
    article = _make_article("guid-no-canonical")
    article.url = "https://feed.example.com/keep-me"
    article.hn_item_id = 601
    path = save(article)

    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/601",
        json={"id": 601, "children": []},
    )

    assert step_fetch_discussions() == 1

    reloaded, _ = load(path)
    assert reloaded.url == "https://feed.example.com/keep-me"
    assert reloaded.status == Status.DISCUSSION_FETCHED


def test_step_fetch_discussions_keeps_feed_url_when_algolia_unreachable(
    isolated_settings, httpx_mock
):
    article = _make_article("guid-algolia-down")
    article.url = "https://feed.example.com/keep-me"
    article.hn_item_id = 602
    path = save(article)

    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/602",
        status_code=500,
    )

    assert step_fetch_discussions() == 1

    reloaded, _ = load(path)
    assert reloaded.url == "https://feed.example.com/keep-me"
    assert reloaded.status == Status.DISCUSSION_FETCHED


def test_step_fetch_discussions_drains_pre_swap_article_fetched(
    isolated_settings, httpx_mock
):
    isolated_settings.min_discussion_comments = 0
    article = _make_article("guid-in-flight")
    article.url = "https://feed.example.com/old"
    article.status = Status.ARTICLE_FETCHED
    article.hn_item_id = 603
    path = save(article)

    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/603",
        json={
            "id": 603,
            "url": "https://canonical.example.com/in-flight",
            "children": [],
        },
    )

    assert step_fetch_discussions() == 1

    reloaded, _ = load(path)
    assert reloaded.status == Status.DISCUSSION_FETCHED
    assert reloaded.url == "https://canonical.example.com/in-flight"


def _dupe_first_comment_payload(item_id: int, canonical_id: int) -> dict:
    return {
        "id": item_id,
        "title": "Dupe of an earlier post",
        "created_at": "2026-04-24T20:00:30Z",
        "url": "https://feed.example.com/dupe",
        "children": [
            {
                "id": item_id + 1,
                "author": "pingou",
                "text": (
                    f'dupe: <a href="https:&#x2F;&#x2F;news.ycombinator.com'
                    f'&#x2F;item?id={canonical_id}">https:&#x2F;&#x2F;'
                    f'news.ycombinator.com&#x2F;item?id={canonical_id}</a>'
                ),
                "children": [],
            },
        ],
    }


def test_step_fetch_discussions_drops_dupe_when_canonical_already_known(
    isolated_settings, httpx_mock, monkeypatch
):
    from app import fetch_discussion as fd

    canonical_guid = "https://news.ycombinator.com/item?id=700"
    canonical = _make_article(canonical_guid)
    canonical.hn_item_id = 700
    canonical.status = Status.SUMMARIZED
    canonical_path = save(canonical)
    assert canonical_path.exists()

    dupe = _make_article("https://news.ycombinator.com/item?id=701")
    dupe.hn_item_id = 701
    dupe_path = save(dupe)
    write_sidecar(dupe_path, "article", "stale article sidecar from a prior step")

    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/701",
        json=_dupe_first_comment_payload(701, 700),
    )
    monkeypatch.setattr(
        fd,
        "_fetch_hn_display_order",
        lambda _id: (_ for _ in ()).throw(
            AssertionError("HN scrape must be skipped on a dropped dupe"),
        ),
    )

    assert step_fetch_discussions() == 0

    assert not dupe_path.exists()
    assert not sidecar_path(dupe_path, "article").exists()
    # The canonical entry is left untouched (no double-write under its guid).
    assert canonical_path.exists()
    reloaded, _ = load(canonical_path)
    assert reloaded.status == Status.SUMMARIZED


def test_step_fetch_discussions_substitutes_canonical_when_unknown(
    isolated_settings, httpx_mock, monkeypatch
):
    from app import fetch_discussion as fd

    isolated_settings.min_discussion_comments = 0
    dupe_guid = "https://news.ycombinator.com/item?id=801"
    canonical_guid = "https://news.ycombinator.com/item?id=800"

    dupe = _make_article(dupe_guid)
    dupe.hn_item_id = 801
    dupe.title = "Stale dupe title"
    dupe.url = "https://feed.example.com/dupe"
    original_published_at = dupe.our_published_at
    old_path = save(dupe)
    assert old_path.exists()

    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/801",
        json=_dupe_first_comment_payload(801, 800),
    )
    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/800",
        json={
            "id": 800,
            "title": "Canonical original title",
            "created_at": "2026-04-20T10:15:00Z",
            "url": "https://canonical.example.com/article",
            "children": [
                {
                    "id": 8001,
                    "author": "alice",
                    "text": "first canonical comment",
                    "children": [],
                },
            ],
        },
    )
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [])

    assert step_fetch_discussions() == 1

    new_path = path_for(canonical_guid, original_published_at)
    assert not old_path.exists()
    assert new_path.exists()
    assert short_hash(canonical_guid) in new_path.name

    reloaded, _ = load(new_path)
    assert reloaded.hn_item_id == 800
    assert reloaded.guid == canonical_guid
    assert reloaded.hn_url == canonical_guid
    assert reloaded.title == "Canonical original title"
    assert reloaded.source_published_at == datetime(2026, 4, 20, 10, 15, tzinfo=UTC)
    # our_published_at is the partition key and must not move when we substitute.
    assert reloaded.our_published_at == original_published_at
    assert reloaded.url == "https://canonical.example.com/article"
    assert reloaded.status == Status.DISCUSSION_FETCHED
    assert reloaded.discussion_comment_count == 1
    assert read_sidecar(new_path, "discussion") == "[alice] first canonical comment"


def test_step_fetch_discussions_does_not_dedup_when_no_dupe_keyword(
    isolated_settings, httpx_mock, monkeypatch
):
    # First comment legitimately links to another HN thread without the
    # "dupe" marker. Must process normally with the original identity.
    from app import fetch_discussion as fd

    isolated_settings.min_discussion_comments = 0
    article = _make_article("guid-related-link")
    article.hn_item_id = 900
    path = save(article)

    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/900",
        json={
            "id": 900,
            "title": "Real article",
            "created_at": "2026-04-21T12:00:00Z",
            "url": "https://example.com/real",
            "children": [
                {
                    "id": 901,
                    "author": "alice",
                    "text": (
                        'related: <a href="https://news.ycombinator.com/item?id=42">'
                        "older thread</a>"
                    ),
                    "children": [],
                },
            ],
        },
    )
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [])

    assert step_fetch_discussions() == 1

    reloaded, _ = load(path)
    assert reloaded.hn_item_id == 900
    assert reloaded.guid == "guid-related-link"
    assert reloaded.url == "https://example.com/real"
    assert reloaded.status == Status.DISCUSSION_FETCHED


def test_step_fetch_discussions_records_attempt_when_canonical_unavailable(
    isolated_settings, httpx_mock, monkeypatch
):
    from app import fetch_discussion as fd

    isolated_settings.max_attempts = 3
    dupe_guid = "https://news.ycombinator.com/item?id=1001"
    dupe = _make_article(dupe_guid)
    dupe.hn_item_id = 1001
    path = save(dupe)

    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/1001",
        json=_dupe_first_comment_payload(1001, 1000),
    )
    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/1000",
        status_code=500,
    )
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [])

    failures: list[tuple[str, str]] = []
    assert step_fetch_discussions(failures) == 0

    assert path.exists()
    reloaded, _ = load(path)
    assert reloaded.status == Status.PENDING
    assert reloaded.attempts == 1
    assert reloaded.error is not None
    assert "1000" in reloaded.error
    # Below max_attempts: not surfaced as a hard failure yet.
    assert failures == []


def _children_with_text(n: int, base_id: int = 10_000) -> list[dict]:
    return [
        {"id": base_id + i, "author": "u", "text": f"c{i}", "children": []}
        for i in range(n)
    ]


def test_step_fetch_discussions_parks_article_below_threshold(
    isolated_settings, httpx_mock, monkeypatch
):
    from app import fetch_discussion as fd

    article = _make_article("guid-thin-thread")
    article.hn_item_id = 1100
    path = save(article)

    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/1100",
        json={"id": 1100, "children": _children_with_text(3)},
    )
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [])

    # Default threshold is 20; 3 < 20 so the article must stay parked.
    assert step_fetch_discussions() == 0

    assert path.exists()
    reloaded, _ = load(path)
    assert reloaded.status == Status.PENDING
    assert reloaded.attempts == 0
    assert reloaded.error is None
    assert reloaded.discussion_fetched_at is None
    assert reloaded.discussion_comment_count is None
    assert not sidecar_path(path, "discussion").exists()
    assert not sidecar_path(path, "top_comments").exists()
    assert list(isolated_settings.failed_dir.rglob("*.md")) == []


def test_step_fetch_discussions_promotes_after_thread_grows(
    isolated_settings, httpx_mock, monkeypatch
):
    from app import fetch_discussion as fd

    article = _make_article("guid-late-bloomer")
    article.hn_item_id = 1101
    path = save(article)

    isolated_settings.min_discussion_comments = 5
    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/1101",
        json={"id": 1101, "children": _children_with_text(2)},
    )
    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/1101",
        json={"id": 1101, "children": _children_with_text(7)},
    )
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [])

    assert step_fetch_discussions() == 0
    parked, _ = load(path)
    assert parked.status == Status.PENDING

    assert step_fetch_discussions() == 1
    promoted, _ = load(path)
    assert promoted.status == Status.DISCUSSION_FETCHED
    assert promoted.discussion_comment_count == 7
    assert sidecar_path(path, "discussion").exists()


def test_step_fetch_discussions_threshold_is_strict_lower_bound(
    isolated_settings, httpx_mock, monkeypatch
):
    from app import fetch_discussion as fd

    isolated_settings.min_discussion_comments = 5
    article = _make_article("guid-exactly-threshold")
    article.hn_item_id = 1102
    path = save(article)

    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/1102",
        json={"id": 1102, "children": _children_with_text(5)},
    )
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [])

    # 5 == threshold → comparison is `<`, not `<=`, so the article advances.
    assert step_fetch_discussions() == 1
    reloaded, _ = load(path)
    assert reloaded.status == Status.DISCUSSION_FETCHED
    assert reloaded.discussion_comment_count == 5


def test_step_fetch_discussions_parks_substituted_canonical_below_threshold(
    isolated_settings, httpx_mock, monkeypatch
):
    from app import fetch_discussion as fd

    dupe_guid = "https://news.ycombinator.com/item?id=901"
    canonical_guid = "https://news.ycombinator.com/item?id=900"

    dupe = _make_article(dupe_guid)
    dupe.hn_item_id = 901
    dupe.title = "Stale dupe title"
    original_published_at = dupe.our_published_at
    old_path = save(dupe)
    assert old_path.exists()

    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/901",
        json=_dupe_first_comment_payload(901, 900),
    )
    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/900",
        json={
            "id": 900,
            "title": "Canonical original title",
            "created_at": "2026-04-20T10:15:00Z",
            "url": "https://canonical.example.com/article",
            "children": _children_with_text(2, base_id=9000),
        },
    )
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [])

    # Default threshold is 20; canonical has only 2 comments, so the
    # substituted entry must be parked at PENDING under the canonical guid.
    assert step_fetch_discussions() == 0

    new_path = path_for(canonical_guid, original_published_at)
    assert not old_path.exists()
    assert new_path.exists()
    reloaded, _ = load(new_path)
    assert reloaded.status == Status.PENDING
    assert reloaded.hn_item_id == 900
    assert reloaded.guid == canonical_guid
    assert reloaded.hn_url == canonical_guid
    assert reloaded.title == "Canonical original title"
    assert reloaded.source_published_at == datetime(2026, 4, 20, 10, 15, tzinfo=UTC)
    assert reloaded.our_published_at == original_published_at
    assert reloaded.discussion_comment_count is None
    assert reloaded.discussion_fetched_at is None
    assert not sidecar_path(new_path, "discussion").exists()
    assert list(isolated_settings.failed_dir.rglob("*.md")) == []


def test_step_summarize_reads_and_clears_top_comments_sidecar(
    isolated_settings, monkeypatch
):
    isolated_settings.llm_sleep_seconds = 0
    article = _make_article("guid-top-flow")
    article.status = Status.ARTICLE_FETCHED
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
    article.status = Status.ARTICLE_FETCHED
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


def test_step_fetch_feed_skips_flagged_title(isolated_settings, monkeypatch):
    entry = _make_feed_entry("guid-flagged", hn_item_id=778)
    entry.title = "[flagged] Some sensitive post"
    monkeypatch.setattr(pipeline, "fetch_source_feed", lambda: [entry])
    assert step_fetch_feed() == 0


def test_step_fetch_feed_skips_flagged_title_case_insensitive(isolated_settings, monkeypatch):
    entry = _make_feed_entry("guid-flagged-upper", hn_item_id=779)
    entry.title = "[FLAGGED] Another one"
    monkeypatch.setattr(pipeline, "fetch_source_feed", lambda: [entry])
    assert step_fetch_feed() == 0


def test_step_summarize_breaker_disabled_when_limit_is_zero(isolated_settings, monkeypatch):
    isolated_settings.daily_cost_limit_usd = 0.0

    def boom():
        raise AssertionError("today_spend should not be probed when the breaker is off")

    monkeypatch.setattr(pipeline, "today_spend", boom)
    monkeypatch.setattr(pipeline, "iter_by_status", lambda _status: iter(()))
    assert pipeline.step_summarize() == 0
