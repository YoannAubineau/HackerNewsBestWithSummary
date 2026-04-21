import html
import re
from dataclasses import dataclass

import httpx

from app.config import get_settings

_ALGOLIA_URL = "https://hn.algolia.com/api/v1/items/{id}"
_TAG_RE = re.compile(r"<[^>]+>")


@dataclass
class Discussion:
    comment_count: int
    text: str


def fetch_discussion(hn_item_id: int) -> Discussion | None:
    settings = get_settings()
    try:
        response = httpx.get(
            _ALGOLIA_URL.format(id=hn_item_id),
            timeout=settings.http_timeout,
            headers={"User-Agent": settings.user_agent},
        )
        response.raise_for_status()
    except httpx.HTTPError:
        return None
    payload = response.json()
    comments = list(_iter_comments(payload, settings.discussion_budget))
    if not comments:
        return None
    return Discussion(comment_count=len(comments), text=_render_comments(comments))


def _iter_comments(root: dict, budget: int):
    """Walk the comment tree with a recursive, degressive comment budget.

    A "branch node" is a comment that has at least one direct reply. Non-pinned
    branch nodes are included only if the budget reaches them; the budget at
    each level is split triangularly across qualifying children (the
    highest-ranked child gets the largest share).

    Submitter comments (author == story author) and their full ancestor chain
    are "pinned": always included, regardless of budget, and without consuming
    budget that would otherwise be spent on non-pinned siblings.
    """
    author = root.get("author")
    pinned = _collect_pinned(root, author) if author else set()
    yield from _distribute_children(root, budget, pinned, depth=0)


def _walk(node: dict, budget: int, pinned: set[int], depth: int):
    is_pinned = id(node) in pinned
    has_reply = bool(node.get("children"))
    if not (is_pinned or (budget > 0 and has_reply)):
        return
    if node.get("text"):
        yield {
            "author": node.get("author") or "?",
            "points": node.get("points"),
            "text": _strip_html(node["text"]),
            "depth": depth,
        }
    remaining = budget if is_pinned else max(0, budget - 1)
    yield from _distribute_children(node, remaining, pinned, depth + 1)


def _distribute_children(parent: dict, budget: int, pinned: set[int], depth: int):
    children = parent.get("children") or []
    alloc_map: dict[int, int] = {}
    if budget > 0:
        non_pinned_qualifying = [
            c for c in children if id(c) not in pinned and c.get("children")
        ]
        allocations = _degressive_split(budget, len(non_pinned_qualifying))
        alloc_map = {
            id(c): a for c, a in zip(non_pinned_qualifying, allocations, strict=True)
        }
    for child in children:
        if id(child) in pinned:
            yield from _walk(child, 0, pinned, depth)
        elif (alloc := alloc_map.get(id(child), 0)) > 0:
            yield from _walk(child, alloc, pinned, depth)


def _collect_pinned(root: dict, author: str) -> set[int]:
    """Return the set of id()s for (a) every comment posted by ``author`` and
    (b) each of its ancestors up to the story root."""
    pinned: set[int] = set()
    _mark_pinned(root, author, pinned, ancestors=[])
    return pinned


def _mark_pinned(
    node: dict, author: str, pinned: set[int], ancestors: list[dict]
) -> None:
    if node.get("author") == author and node.get("text"):
        pinned.add(id(node))
        for anc in ancestors:
            pinned.add(id(anc))
    for child in node.get("children") or []:
        _mark_pinned(child, author, pinned, ancestors + [node])


def _degressive_split(budget: int, n: int) -> list[int]:
    """Triangular split: weight[i] = n-i. First slot gets the largest share."""
    if n <= 0 or budget <= 0:
        return []
    weights = list(range(n, 0, -1))
    total_weight = sum(weights)
    allocs = [budget * w // total_weight for w in weights]
    residue = budget - sum(allocs)
    allocs[0] += residue
    return allocs


def _strip_html(text: str) -> str:
    return html.unescape(_TAG_RE.sub("", text))


def _render_comments(comments: list[dict]) -> str:
    parts: list[str] = []
    for c in comments:
        indent = "  " * c["depth"]
        points = f", {c['points']} pts" if c["points"] is not None else ""
        parts.append(f"{indent}[{c['author']}{points}] {c['text'].strip()}")
    return "\n".join(parts)
