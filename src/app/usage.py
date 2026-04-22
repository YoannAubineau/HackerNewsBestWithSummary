"""Track OpenRouter spend over time and render a 30-day bar chart.

Each cycle calls ``record_usage`` which hits OpenRouter's ``/api/v1/auth/key``
endpoint and stores the current cumulative spend against the date in
``docs/usage-daily.json``. ``generate_chart`` then renders a hand-crafted
SVG bar chart of the last N days' deltas into ``docs/usage-chart.svg``.
The JSON file holds at most one entry per UTC date, so it never grows
without bound.
"""

import json
from datetime import UTC, date, datetime, timedelta
from pathlib import Path

import httpx
import structlog

from app.config import get_settings

log = structlog.get_logger()

_OPENROUTER_KEY_URL = "https://openrouter.ai/api/v1/auth/key"
_DAILY_PATH = Path("docs/usage-daily.json")
_CHART_PATH = Path("docs/usage-chart.svg")
_BADGE_PATH = Path("docs/llm-cost.json")


def record_usage() -> None:
    """Query OpenRouter and store today's cumulative spend."""
    settings = get_settings()
    try:
        response = httpx.get(
            _OPENROUTER_KEY_URL,
            headers={"Authorization": f"Bearer {settings.openrouter_api_key}"},
            timeout=settings.http_timeout,
        )
        response.raise_for_status()
    except httpx.HTTPError as exc:
        log.warning("usage_fetch_failed", error=str(exc))
        return
    payload = response.json().get("data") or {}
    usage = float(payload.get("usage") or 0)
    limit_raw = payload.get("limit")
    limit = float(limit_raw) if limit_raw is not None else None

    today = datetime.now(tz=UTC).date().isoformat()
    entries = _load_daily()
    entries[today] = {"cumulative": usage, "limit": limit}
    _save_daily(entries)
    _write_badge(usage)
    log.info("usage_recorded", date=today, cumulative=usage, limit=limit)


def _write_badge(usage: float) -> None:
    """Emit a shields.io endpoint JSON for the total-cost badge."""
    payload = {
        "schemaVersion": 1,
        "label": "Total LLM cost",
        "message": f"${usage:.2f}",
        "color": "yellow",
    }
    _BADGE_PATH.parent.mkdir(parents=True, exist_ok=True)
    _BADGE_PATH.write_text(json.dumps(payload) + "\n", encoding="utf-8")


def generate_chart(days: int = 30) -> None:
    """Render the last ``days`` UTC days of per-day spend into an SVG."""
    entries = _load_daily()
    today = datetime.now(tz=UTC).date()
    window_start = today - timedelta(days=days - 1)
    dates = [window_start + timedelta(days=i) for i in range(days)]
    daily_spend = _derive_daily_spend(entries, dates)
    limit = _latest_limit(entries)
    svg = _render_svg(daily_spend, limit=limit)
    _CHART_PATH.parent.mkdir(parents=True, exist_ok=True)
    _CHART_PATH.write_text(svg, encoding="utf-8")
    log.info("usage_chart_written", days=days, path=str(_CHART_PATH))


def _load_daily() -> dict[str, dict]:
    if not _DAILY_PATH.exists():
        return {}
    try:
        return json.loads(_DAILY_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def _save_daily(entries: dict[str, dict]) -> None:
    _DAILY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ordered = dict(sorted(entries.items()))
    _DAILY_PATH.write_text(
        json.dumps(ordered, indent=2) + "\n", encoding="utf-8"
    )


def _derive_daily_spend(
    entries: dict[str, dict], dates: list[date]
) -> list[tuple[date, float]]:
    """Compute per-day spend from cumulative snapshots.

    For each target date, daily spend = cumulative(that date) -
    cumulative(previous known date). When no snapshot exists for a date we
    carry the previous cumulative forward (spend reads as zero).
    """
    cumulative_by_date: dict[date, float] = {
        date.fromisoformat(d): v["cumulative"] for d, v in entries.items()
    }
    result: list[tuple[date, float]] = []
    # Seed with the last cumulative known strictly before the window.
    prev = 0.0
    for d in sorted(cumulative_by_date):
        if d < dates[0]:
            prev = cumulative_by_date[d]
    for d in dates:
        cur = cumulative_by_date.get(d, prev)
        result.append((d, max(cur - prev, 0.0)))
        prev = cur
    return result


def _latest_limit(entries: dict[str, dict]) -> float | None:
    if not entries:
        return None
    latest = max(entries)
    value = entries[latest].get("limit")
    return float(value) if value is not None else None


def _render_svg(daily: list[tuple[date, float]], *, limit: float | None) -> str:
    width, height = 720, 260
    margin_top, margin_bottom = 24, 52
    margin_left, margin_right = 52, 12
    plot_w = width - margin_left - margin_right
    plot_h = height - margin_top - margin_bottom
    n = len(daily)
    slot_w = plot_w / n
    bar_w = slot_w * 0.7

    max_spend = max((v for _, v in daily), default=0.0)
    y_max = _nice_ceiling(max_spend) if max_spend > 0 else 0.1

    out: list[str] = []
    out.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        'role="img" aria-label="OpenRouter daily spend over the last 30 days" '
        'style="font:12px -apple-system,BlinkMacSystemFont,Segoe UI,Roboto,'
        'sans-serif">'
    )
    out.append(
        f'<rect width="{width}" height="{height}" fill="#fafafa" stroke="#e5e5e5"/>'
    )
    # gridlines + y-axis labels at quarters
    for i in range(5):
        y = margin_top + plot_h * (1 - i / 4)
        value = y_max * i / 4
        out.append(
            f'<line x1="{margin_left}" y1="{y:.1f}" x2="{width - margin_right}" '
            f'y2="{y:.1f}" stroke="#e5e5e5"/>'
        )
        out.append(
            f'<text x="{margin_left - 6}" y="{y + 4:.1f}" text-anchor="end" '
            f'fill="#666">${value:.2f}</text>'
        )
    # bars
    for i, (_day, value) in enumerate(daily):
        bar_h = plot_h * (value / y_max) if y_max else 0
        x = margin_left + i * slot_w + (slot_w - bar_w) / 2
        y = margin_top + plot_h - bar_h
        out.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" '
            f'height="{bar_h:.1f}" fill="#ff6600" rx="1"/>'
        )
    # x-axis labels every ~5 days
    stride = max(1, n // 6)
    for i, (day, _) in enumerate(daily):
        if i % stride == 0 or i == n - 1:
            x = margin_left + i * slot_w + slot_w / 2
            out.append(
                f'<text x="{x:.1f}" y="{height - margin_bottom + 18}" '
                f'text-anchor="middle" fill="#666">'
                f'{day.strftime("%d/%m")}</text>'
            )
    # footer
    total = sum(v for _, v in daily)
    footer = f"Last {n} days: ${total:.2f}"
    if limit is not None:
        footer += f" · limit ${limit:.2f}"
    out.append(
        f'<text x="{margin_left}" y="{height - 10}" fill="#666">{footer}</text>'
    )
    out.append("</svg>")
    return "\n".join(out)


def _nice_ceiling(value: float) -> float:
    """Round ``value`` up to a human-friendly tick."""
    if value <= 0:
        return 1.0
    if value < 0.1:
        return round(value + 0.02, 2)
    if value < 1:
        return round(value * 1.2 + 0.05, 1)
    if value < 10:
        return float(int(value * 1.2) + 1)
    return float(int(value * 1.15 / 5 + 1) * 5)
