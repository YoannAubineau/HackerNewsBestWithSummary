import re
import sys
from dataclasses import dataclass

import httpx
import structlog

from app.config import get_settings

log = structlog.get_logger()

_OPENROUTER_MODELS_URL = "https://openrouter.ai/api/v1/models"
_VERSION_RE = re.compile(r"^(?P<family>.+?)-(?P<version>\d+(?:\.\d+)*)$")


@dataclass(frozen=True)
class _ModelRef:
    slug: str
    family: str
    version: tuple[int, ...]


def _parse_slug(slug: str) -> _ModelRef | None:
    base = slug.split(":", 1)[0]
    match = _VERSION_RE.match(base)
    if match is None:
        return None
    version_str = match.group("version")
    try:
        version = tuple(int(part) for part in version_str.split("."))
    except ValueError:
        return None
    return _ModelRef(slug=slug, family=match.group("family"), version=version)


def _fetch_model_ids(timeout: float) -> list[str]:
    response = httpx.get(_OPENROUTER_MODELS_URL, timeout=timeout)
    response.raise_for_status()
    data = response.json()
    items = data.get("data") or []
    return [item["id"] for item in items if isinstance(item, dict) and "id" in item]


def check_llm_versions() -> int:
    """Return 0 when the configured primary model is the newest of its family
    on OpenRouter, 1 when a newer version is published. Writes a human-readable
    report to stdout either way.
    """
    settings = get_settings()
    current = _parse_slug(settings.openrouter_model)
    if current is None:
        print(
            f"Cannot parse a version from current model slug {settings.openrouter_model!r}; "
            "skipping check."
        )
        return 0
    try:
        slugs = _fetch_model_ids(settings.http_timeout)
    except httpx.HTTPError as exc:
        print(f"Failed to fetch OpenRouter model list: {exc}")
        return 0
    newer: list[_ModelRef] = []
    for slug in slugs:
        ref = _parse_slug(slug)
        if ref is None or ref.family != current.family:
            continue
        if ref.version > current.version:
            newer.append(ref)
    if not newer:
        print(
            f"No newer model available for family {current.family!r}. "
            f"Current: {settings.openrouter_model}."
        )
        return 0
    newer.sort(key=lambda ref: ref.version, reverse=True)
    lines = [
        f"Newer model(s) available for {current.family} "
        f"(current: {settings.openrouter_model}):"
    ]
    lines.extend(f"  - {ref.slug}" for ref in newer)
    lines.append("")
    lines.append(
        "To bump, edit `openrouter_model` in src/app/config.py and verify "
        "the output quality on a few articles before merging."
    )
    print("\n".join(lines))
    return 1


def main() -> None:
    sys.exit(check_llm_versions())
