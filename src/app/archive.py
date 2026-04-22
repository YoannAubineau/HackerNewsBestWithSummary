"""Generate a static HTML archive of every summarized article.

Rendered alongside the feed (`artefacts/archive.html`) so readers can
browse articles that have rotated out of the 200-item window. The table
is sortable client-side by three timestamps:

- HN submission date (``source_published_at``)
- First-seen-in-``/best`` date (``our_published_at``)
- Entered-our-feed date (``summarized_at``)
"""

from datetime import datetime
from html import escape
from pathlib import Path

from app.config import get_settings
from app.models import Article
from app.storage import iter_summarized

_ARCHIVE_FILENAME = "archive.html"


def write_archive() -> Path:
    """Generate the archive page and return its filesystem path."""
    settings = get_settings()
    articles = [article for _path, article, _body in iter_summarized()]
    path = settings.artefacts_dir / _ARCHIVE_FILENAME
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(_render(articles), encoding="utf-8")
    return path


def _render(articles: list[Article]) -> str:
    rows = "\n".join(_render_row(a) for a in articles)
    count = len(articles)
    return _TEMPLATE.format(count=count, rows=rows)


def _render_row(article: Article) -> str:
    title = article.rewritten_title or article.title
    return (
        '<tr>'
        f'<td><a href="{escape(article.hn_url)}">{escape(title)}</a>'
        f' <a class="ext" href="{escape(article.url)}" '
        f'title="Original article" rel="noopener">↗</a></td>'
        f"{_date_cell(article.summarized_at)}"
        f"{_date_cell(article.our_published_at)}"
        f"{_date_cell(article.source_published_at)}"
        "</tr>"
    )


def _date_cell(when: datetime | None) -> str:
    if when is None:
        return '<td data-iso=""></td>'
    return f'<td data-iso="{when.isoformat()}">{_format(when)}</td>'


def _format(when: datetime) -> str:
    return when.strftime("%Y-%m-%d %H:%M")


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
  header {{
    max-width: 64rem;
    margin: 0 auto 1.5rem;
  }}
  h1 {{ margin: 0 0 0.25rem; font-size: 1.4rem; }}
  header p {{ margin: 0.25rem 0; color: var(--muted); }}
  a {{ color: var(--accent); text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  a.ext {{ color: var(--muted); font-size: 0.85em; }}
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
    cursor: pointer;
    user-select: none;
    font-weight: 600;
    color: var(--muted);
    white-space: nowrap;
  }}
  th[aria-sort="ascending"]::after {{ content: " ↑"; }}
  th[aria-sort="descending"]::after {{ content: " ↓"; }}
  td:nth-child(n+2), th:nth-child(n+2) {{
    white-space: nowrap;
    color: var(--muted);
    width: 1%;
  }}
  tbody tr:nth-child(even) {{ background: var(--row-alt); }}
  @media (max-width: 640px) {{
    th:nth-child(4), td:nth-child(4) {{ display: none; }}
  }}
</style>
</head>
<body>
<header>
  <h1>Archive</h1>
  <p><span id="count">{count}</span> summarised articles. Click a column header to sort.</p>
  <p><a href="feed.fr.xml">← Back to the feed</a></p>
</header>
<table id="archive">
  <thead>
    <tr>
      <th data-sort="text">Title</th>
      <th data-sort="date" aria-sort="descending">Entered our feed</th>
      <th data-sort="date">Entered /best</th>
      <th data-sort="date">Submitted to HN</th>
    </tr>
  </thead>
  <tbody>
{rows}
  </tbody>
</table>
<script>
(() => {{
  const table = document.getElementById('archive');
  const tbody = table.tBodies[0];
  const headers = table.tHead.rows[0].cells;
  const compare = (kind, dir) => (a, b) => {{
    const i = [...headers].findIndex(h => h.getAttribute('aria-sort'));
    const av = cellValue(a, i, kind);
    const bv = cellValue(b, i, kind);
    if (av < bv) return -dir;
    if (av > bv) return dir;
    return 0;
  }};
  const cellValue = (row, idx, kind) => {{
    const cell = row.cells[idx];
    return kind === 'date' ? cell.dataset.iso : cell.textContent.toLowerCase();
  }};
  [...headers].forEach((th, idx) => th.addEventListener('click', () => {{
    const kind = th.dataset.sort;
    const current = th.getAttribute('aria-sort');
    const dir = current === 'ascending' ? -1 : 1;
    [...headers].forEach(h => h.removeAttribute('aria-sort'));
    th.setAttribute('aria-sort', dir === 1 ? 'ascending' : 'descending');
    const rows = [...tbody.rows].sort(compare(kind, dir));
    rows.forEach(r => tbody.appendChild(r));
  }}));
}})();
</script>
</body>
</html>
"""
