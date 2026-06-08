from datetime import UTC, datetime
from pathlib import Path

import pytest

from app import config as config_module
from app import fetch_discussion as fd
from app.models import Article, ContentSource, Status


def make_article(
    guid: str = "https://news.ycombinator.com/item?id=1",
    *,
    url: str = "https://example.com/a",
    hn_item_id: int = 1,
    hn_url: str | None = None,
    title: str = "Titre",
    rewritten_title: str | None = None,
    status: Status = Status.PENDING,
    is_ask_or_show_hn: bool = False,
    content_source: ContentSource | None = None,
    source_published_at: datetime = datetime(2026, 4, 21, 8, 0, tzinfo=UTC),
    our_published_at: datetime = datetime(2026, 4, 21, 9, 0, tzinfo=UTC),
    summarized_at: datetime | None = None,
) -> Article:
    """Single field-assembly point for test articles.

    Each test module wraps this with its own defaults (a PENDING freshly
    ingested item, a fully SUMMARIZED item ready to publish, …) so the
    long ``Article(...)`` field list lives in exactly one place.
    """
    return Article(
        guid=guid,
        url=url,
        hn_url=hn_url or f"https://news.ycombinator.com/item?id={hn_item_id}",
        hn_item_id=hn_item_id,
        title=title,
        rewritten_title=rewritten_title,
        source_published_at=source_published_at,
        our_published_at=our_published_at,
        status=status,
        is_ask_or_show_hn=is_ask_or_show_hn,
        content_source=content_source,
        summarized_at=summarized_at,
    )


@pytest.fixture(autouse=True)
def stub_hn_display_order(monkeypatch: pytest.MonkeyPatch):
    """Default every test to an empty HN order so fetch_discussion never
    tries to hit news.ycombinator.com. Tests that care about top comments
    override this via a local monkeypatch."""
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [])


@pytest.fixture(autouse=True)
def isolated_settings(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-test")
    monkeypatch.chdir(tmp_path)
    config_module.reset_settings()
    settings = config_module.get_settings()
    settings.artifacts_dir = tmp_path / "artifacts"
    settings.artifacts_dir.mkdir(parents=True, exist_ok=True)
    settings.articles_dir = tmp_path / "articles"
    settings.articles_dir.mkdir(parents=True, exist_ok=True)
    # Tests opt in to Wayback explicitly. Leaving it on would force every
    # existing fetch_article test that exercises a failure path to also
    # mock archive.org calls, which is unrelated to what they verify.
    settings.wayback_enabled = False
    # Same rationale as wayback above: tests opt in to the reader fallback
    # explicitly so existing failure-path tests don't have to mock r.jina.ai.
    settings.reader_enabled = False
    # Same rationale: tests opt in to the archive.today fallback explicitly so
    # existing failure-path tests don't have to mock archive.ph.
    settings.archive_today_enabled = False
    yield settings
    config_module.reset_settings()
