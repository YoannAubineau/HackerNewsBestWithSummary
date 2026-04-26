import statistics
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path

import httpx
import structlog
import typer

from app.config import get_settings
from app.storage import load

log = structlog.get_logger()

_FEEDLY_STREAM_URL = "https://cloud.feedly.com/v3/streams/contents"


@dataclass(frozen=True)
class Measurement:
    short_hash: str
    title: str
    our_published_at: datetime
    crawled_at: datetime
    delta: timedelta


class FeedlyAuthError(Exception):
    """Feedly rejected the developer token (HTTP 401 / 403)."""


def _fetch_feedly_items(
    *, feed_url: str | None, count: int, token: str
) -> list[dict]:
    """Pure HTTP helper. Raises ``FeedlyAuthError`` on 401/403, propagates
    other ``httpx.HTTPError`` subclasses untouched."""
    settings = get_settings()
    target_url = feed_url or settings.feed_self_url
    stream_id = f"feed/{target_url}"
    response = httpx.get(
        _FEEDLY_STREAM_URL,
        params={"streamId": stream_id, "count": count},
        headers={"Authorization": f"OAuth {token}"},
        timeout=settings.http_timeout,
    )
    if response.status_code in (401, 403):
        raise FeedlyAuthError(f"HTTP {response.status_code}")
    response.raise_for_status()
    return response.json().get("items") or []


def fetch_feedly_origin_ids(
    *, feed_url: str | None = None, count: int = 100
) -> set[str] | None:
    """Set of ``originId`` values Feedly currently has for our feed.

    Returns ``None`` when the call could not complete (no token, auth
    error, network error, HTTP 5xx). Returns a (possibly empty) set
    otherwise. Callers should treat ``None`` as "Feedly state unknown"
    and behave conservatively — typically by skipping the work that
    depends on that state, so a Feedly outage does not waste LLM calls.
    """
    settings = get_settings()
    token = settings.feedly_dev_token
    if not token:
        return None
    try:
        items = _fetch_feedly_items(feed_url=feed_url, count=count, token=token)
    except FeedlyAuthError as exc:
        log.warning("feedly_origin_ids_auth_failed", error=str(exc))
        return None
    except httpx.HTTPError as exc:
        log.warning("feedly_origin_ids_http_failed", error=str(exc))
        return None
    return {
        item["originId"]
        for item in items
        if isinstance(item, dict) and item.get("originId")
    }


def compute_lag(*, feed_url: str | None = None, count: int = 50) -> list[Measurement]:
    settings = get_settings()
    token = settings.feedly_dev_token
    if not token:
        typer.echo(
            "FEEDLY_DEV_TOKEN is not set. Generate one at "
            "https://feedly.com/v3/auth/dev and add it to .env.",
            err=True,
        )
        raise typer.Exit(code=1)

    try:
        items = _fetch_feedly_items(feed_url=feed_url, count=count, token=token)
    except FeedlyAuthError as exc:
        typer.echo(
            f"Feedly API rejected the token ({exc}). "
            "Generate a fresh one at https://feedly.com/v3/auth/dev.",
            err=True,
        )
        raise typer.Exit(code=1) from None

    measurements: list[Measurement] = []
    for item in items:
        origin_id = item.get("originId")
        crawled_ms = item.get("crawled")
        if not origin_id or crawled_ms is None:
            continue
        path = _find_by_short_hash(origin_id)
        if path is None:
            log.info("feedly_lag_unmatched", origin_id=origin_id)
            continue
        article, _ = load(path)
        crawled_at = datetime.fromtimestamp(crawled_ms / 1000, tz=UTC)
        measurements.append(
            Measurement(
                short_hash=origin_id,
                title=article.rewritten_title or article.title,
                our_published_at=article.our_published_at,
                crawled_at=crawled_at,
                delta=crawled_at - article.our_published_at,
            )
        )
    measurements.sort(key=lambda m: m.crawled_at, reverse=True)
    return measurements


def _find_by_short_hash(short_hash_value: str) -> Path | None:
    settings = get_settings()
    if not settings.articles_dir.exists():
        return None
    target = f"{short_hash_value}.md"
    for match in settings.articles_dir.rglob(target):
        return match
    return None


def print_report(measurements: list[Measurement]) -> None:
    if not measurements:
        print("No matching articles between Feedly and the local repo.")
        return

    title_width = 50
    header = f"{'crawled (UTC)':<20}  {'our pub (UTC)':<20}  {'delta':>10}  title"
    print(header)
    print("-" * len(header))
    for m in measurements:
        print(
            f"{_fmt_dt(m.crawled_at):<20}  "
            f"{_fmt_dt(m.our_published_at):<20}  "
            f"{_fmt_delta(m.delta):>10}  "
            f"{_truncate(m.title, title_width)}"
        )

    deltas = [m.delta for m in measurements]
    print()
    print(f"items matched: {len(measurements)}")
    print(f"min delay:     {_fmt_delta(min(deltas))}")
    print(f"median delay:  {_fmt_delta(_median_timedelta(deltas))}")
    print(f"mean delay:    {_fmt_delta(_mean_timedelta(deltas))}")
    print(f"max delay:     {_fmt_delta(max(deltas))}")


def _fmt_dt(dt: datetime) -> str:
    return dt.astimezone(UTC).strftime("%Y-%m-%d %H:%M:%S")


def _fmt_delta(delta: timedelta) -> str:
    total = int(delta.total_seconds())
    sign = "-" if total < 0 else ""
    total = abs(total)
    hours, rem = divmod(total, 3600)
    minutes, seconds = divmod(rem, 60)
    if hours:
        return f"{sign}{hours}h{minutes:02d}m"
    if minutes:
        return f"{sign}{minutes}m{seconds:02d}s"
    return f"{sign}{seconds}s"


def _truncate(s: str, width: int) -> str:
    if len(s) <= width:
        return s
    return s[: width - 1] + "…"


def _median_timedelta(deltas: list[timedelta]) -> timedelta:
    return timedelta(seconds=statistics.median(d.total_seconds() for d in deltas))


def _mean_timedelta(deltas: list[timedelta]) -> timedelta:
    return timedelta(seconds=statistics.mean(d.total_seconds() for d in deltas))
