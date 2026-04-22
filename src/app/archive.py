"""Generate a paginated static HTML archive of every summarized article.

Rendered alongside the feed so readers can browse articles that have
rotated out of the 200-item window. The set is pre-sorted server-side
into three views — by entry in our feed, by entry in HN's ``/best``,
and by HN submission date — and split into pages of
``_PAGE_SIZE`` articles.

URL layout:

- ``archive.html``           — default (feed sort, page 1)
- ``archive-{view}.html``    — other views, page 1
- ``archive-{view}-N.html``  — page N > 1 (also for the feed view)
"""

from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime
from html import escape
from pathlib import Path

from app.config import get_settings
from app.models import Article
from app.storage import iter_summarized, short_hash

_PAGE_SIZE = 100
_EPOCH = datetime.min.replace(tzinfo=UTC)


@dataclass(frozen=True)
class _View:
    key: str
    label: str
    key_fn: Callable[[Article], datetime]


_VIEWS = (
    _View("feed", "Entered our feed", lambda a: a.summarized_at or _EPOCH),
    _View("best", "Entered /best", lambda a: a.our_published_at),
    _View("hn", "Entered HN", lambda a: a.source_published_at),
)


def write_archive() -> Path:
    """Regenerate every archive page. Returns the path of ``archive.html``."""
    settings = get_settings()
    articles = [article for _path, article, _body in iter_summarized()]
    out_dir = settings.artefacts_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    default_path = out_dir / "archive.html"
    for view in _VIEWS:
        ordered = sorted(articles, key=view.key_fn, reverse=True)
        pages = [ordered[i : i + _PAGE_SIZE] for i in range(0, len(ordered), _PAGE_SIZE)] or [[]]
        for page_index, page_articles in enumerate(pages, start=1):
            path = out_dir / _filename(view.key, page_index)
            html = _render(
                view=view,
                page=page_index,
                total_pages=len(pages),
                articles=page_articles,
                total_articles=len(ordered),
            )
            path.write_text(html, encoding="utf-8")
    return default_path


def _filename(view_key: str, page: int) -> str:
    if view_key == "feed" and page == 1:
        return "archive.html"
    if page == 1:
        return f"archive-{view_key}.html"
    return f"archive-{view_key}-{page}.html"


def _render_row(article: Article) -> str:
    title = article.rewritten_title or article.title
    summary_url = f"a/{short_hash(article.guid)}.html"
    return (
        "<tr>"
        f'<td><a href="{escape(article.hn_url)}" rel="noopener">'
        f"{article.hn_item_id}</a></td>"
        f"{_date_cell(article.source_published_at)}"
        f"{_date_cell(article.our_published_at)}"
        f"{_date_cell(article.summarized_at)}"
        f'<td class="title"><a href="{summary_url}">{escape(title)}</a>'
        f' <a class="ext" href="{escape(article.url)}" '
        f'title="Original article" rel="noopener">↗</a></td>'
        "</tr>"
    )


def _date_cell(when: datetime | None) -> str:
    if when is None:
        return "<td></td>"
    return f"<td>{_format(when)}</td>"


def _format(when: datetime) -> str:
    return when.strftime("%Y-%m-%d %H:%M")


def _render_pagination(view_key: str, page: int, total_pages: int) -> str:
    if total_pages <= 1:
        return ""
    if page > 1:
        prev_link = f'<a href="{_filename(view_key, page - 1)}">← Newer</a>'
    else:
        prev_link = '<span class="disabled">← Newer</span>'
    if page < total_pages:
        next_link = f'<a href="{_filename(view_key, page + 1)}">Older →</a>'
    else:
        next_link = '<span class="disabled">Older →</span>'
    return (
        f'<nav class="pagination">{prev_link}'
        f'<span class="page-indicator">Page {page} / {total_pages}</span>'
        f"{next_link}</nav>"
    )


_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Archive — Hacker News Best with summaries</title>
<style>
  :root {{
    color-scheme: light dark;
    --bg: #fafafa;
    --fg: #222;
    --muted: #666;
    --border: #e5e5e5;
    --accent: #ff6600;
    --row-alt: #f3f3f3;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --bg: #1a1a1a;
      --fg: #e5e5e5;
      --muted: #999;
      --border: #333;
      --row-alt: #222;
    }}
  }}
  body {{
    margin: 0;
    padding: 1.5rem;
    background: var(--bg);
    color: var(--fg);
    font: 14px/1.4 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }}
  header, footer {{
    max-width: 64rem;
    margin: 0 auto;
  }}
  header {{ margin-bottom: 1.5rem; }}
  footer {{ margin-top: 1.5rem; }}
  h1 {{ margin: 0 0 0.25rem; font-size: 1.4rem; }}
  header p {{ margin: 0.25rem 0; color: var(--muted); }}
  a {{ color: var(--accent); text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  a.ext {{ color: var(--muted); font-size: 0.85em; }}
  nav.pagination {{
    margin: 0.75rem 0 0;
    color: var(--muted);
    display: flex; gap: 1rem; align-items: baseline;
  }}
  nav.pagination .disabled {{ color: var(--border); }}
  nav.pagination .page-indicator {{ flex: 1; text-align: center; }}
  table {{
    width: 100%;
    max-width: 64rem;
    margin: 0 auto;
    border-collapse: collapse;
  }}
  th, td {{
    padding: 0.5rem 0.75rem;
    border-bottom: 1px solid var(--border);
    text-align: left;
    vertical-align: top;
  }}
  th {{
    font-weight: 600;
    color: var(--muted);
    white-space: nowrap;
  }}
  th a {{ color: inherit; }}
  th.active {{ color: var(--fg); }}
  th.active::after {{ content: " ↓"; }}
  th, td:not(.title) {{
    white-space: nowrap;
    color: var(--muted);
    width: 1%;
  }}
  td.title {{ color: var(--fg); width: auto; }}
  tbody tr:nth-child(even) {{ background: var(--row-alt); }}
  @media (max-width: 640px) {{
    th:nth-child(2), td:nth-child(2) {{ display: none; }}
  }}
</style>
</head>
<body>
<header>
  <h1>Archive</h1>
  <p><span id="count">{count}</span> summarised articles.
  <a href="feed.fr.xml">← Back to the feed</a>.</p>
  {pagination}
</header>
<table id="archive">
  <thead>
    <tr>
      <th>HN</th>
      <th class="{hn_class}"><a href="archive-hn.html">Entered HN</a></th>
      <th class="{best_class}"><a href="archive-best.html">Entered /best</a></th>
      <th class="{feed_class}"><a href="archive.html">Entered our feed</a></th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
{rows}
  </tbody>
</table>
<footer>
  {pagination}
</footer>
</body>
</html>
"""


def _render(
    *,
    view: _View,
    page: int,
    total_pages: int,
    articles: list[Article],
    total_articles: int,
) -> str:
    rows = "\n".join(_render_row(a) for a in articles)
    return _TEMPLATE.format(
        count=total_articles,
        rows=rows,
        pagination=_render_pagination(view.key, page, total_pages),
        hn_class="active" if view.key == "hn" else "",
        best_class="active" if view.key == "best" else "",
        feed_class="active" if view.key == "feed" else "",
    )
