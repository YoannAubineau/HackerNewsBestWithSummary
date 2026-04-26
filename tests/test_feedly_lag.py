from datetime import UTC, datetime

import pytest
import typer

from app.feedly_lag import compute_lag
from app.models import Article, Status
from app.storage import save, short_hash


def _make_article(
    guid: str,
    *,
    our_published_at: datetime,
    title: str = "Titre",
    rewritten_title: str | None = None,
) -> Article:
    return Article(
        guid=guid,
        url="https://example.com/a",
        hn_url=f"https://news.ycombinator.com/item?id={abs(hash(guid)) % 10000}",
        hn_item_id=abs(hash(guid)) % 10000,
        title=title,
        rewritten_title=rewritten_title,
        source_published_at=our_published_at,
        our_published_at=our_published_at,
        status=Status.SUMMARIZED,
    )


def test_compute_lag_matches_local_articles_and_skips_unknown(
    isolated_settings, httpx_mock
):
    isolated_settings.feedly_dev_token = "test-token"
    isolated_settings.feed_self_url = "https://example.com/feed.fr.xml"

    pub_a = datetime(2026, 4, 26, 10, 0, tzinfo=UTC)
    pub_b = datetime(2026, 4, 26, 11, 0, tzinfo=UTC)
    article_a = _make_article(
        "https://news.ycombinator.com/item?id=1",
        our_published_at=pub_a,
        rewritten_title="A rewritten",
    )
    article_b = _make_article(
        "https://news.ycombinator.com/item?id=2",
        our_published_at=pub_b,
    )
    save(article_a, "body A")
    save(article_b, "body B")

    crawled_a_ms = int((pub_a.timestamp() + 600) * 1000)  # +10 min
    crawled_b_ms = int((pub_b.timestamp() + 1800) * 1000)  # +30 min

    httpx_mock.add_response(
        json={
            "items": [
                {"originId": short_hash(article_a.guid), "crawled": crawled_a_ms},
                {"originId": short_hash(article_b.guid), "crawled": crawled_b_ms},
                {"originId": "deadbeef", "crawled": crawled_a_ms},
            ]
        }
    )

    measurements = compute_lag(count=10)

    assert len(measurements) == 2
    by_hash = {m.short_hash: m for m in measurements}
    assert by_hash[short_hash(article_a.guid)].title == "A rewritten"
    assert by_hash[short_hash(article_a.guid)].delta.total_seconds() == 600
    assert by_hash[short_hash(article_b.guid)].title == "Titre"
    assert by_hash[short_hash(article_b.guid)].delta.total_seconds() == 1800


def test_compute_lag_exits_when_token_missing(isolated_settings):
    isolated_settings.feedly_dev_token = ""
    with pytest.raises(typer.Exit) as exc_info:
        compute_lag(count=5)
    assert exc_info.value.exit_code == 1


def test_compute_lag_exits_on_unauthorized(isolated_settings, httpx_mock):
    isolated_settings.feedly_dev_token = "expired-token"
    httpx_mock.add_response(status_code=401, json={"errorMessage": "expired"})
    with pytest.raises(typer.Exit) as exc_info:
        compute_lag(count=5)
    assert exc_info.value.exit_code == 1


def test_compute_lag_handles_negative_delta(isolated_settings, httpx_mock):
    isolated_settings.feedly_dev_token = "test-token"
    pub = datetime(2026, 4, 26, 12, 0, tzinfo=UTC)
    article = _make_article(
        "https://news.ycombinator.com/item?id=99",
        our_published_at=pub,
    )
    save(article, "body")

    crawled_ms = int((pub.timestamp() - 60) * 1000)  # crawled 60s before our pub
    httpx_mock.add_response(
        json={
            "items": [
                {"originId": short_hash(article.guid), "crawled": crawled_ms},
            ]
        }
    )

    measurements = compute_lag(count=5)
    assert len(measurements) == 1
    assert measurements[0].delta.total_seconds() == -60
