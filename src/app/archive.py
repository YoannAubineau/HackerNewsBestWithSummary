"""Generate a single static HTML archive of every summarized article.

Rendered alongside the feed so readers can browse articles that have
rotated out of the 200-item window. Sorting, pagination, and search
are handled client-side by `simple-datatables <https://github.com/
fiduswriter/simple-datatables>`_ loaded from jsDelivr — we just emit a
plain ``<table>`` with rows pre-sorted by entry-in-our-feed descending.
"""

from datetime import datetime
from html import escape
from pathlib import Path

from app.config import get_settings
from app.models import Article
from app.storage import iter_summarized, short_hash

# GitHub renders committed Markdown files (frontmatter + body) into a nice
# page out of the box, so the archive titles link there directly.
_REPO_BLOB_URL = "https://github.com/YoannAubineau/HackerNewsBestWithSummary/blob/main"


def write_archive() -> Path:
    """Regenerate ``archive.html`` and return its path."""
    settings = get_settings()
    articles = [article for _path, article, _body in iter_summarized()]
    path = settings.artefacts_dir / "archive.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(_render(articles), encoding="utf-8")
    return path


def _render(articles: list[Article]) -> str:
    rows = "\n".join(_render_row(a) for a in articles)
    return _TEMPLATE.format(count=len(articles), rows=rows)


def _render_row(article: Article) -> str:
    title = article.rewritten_title or article.title
    return (
        "<tr>"
        f'<td><a href="{escape(article.hn_url)}" rel="noopener">'
        f"{article.hn_item_id}</a></td>"
        f"{_date_cell(article.source_published_at)}"
        f"{_date_cell(article.our_published_at)}"
        f"{_date_cell(article.summarized_at)}"
        f'<td class="title"><a href="{escape(_summary_url(article))}">'
        f"{escape(title)}</a></td>"
        "</tr>"
    )


def _date_cell(when: datetime | None) -> str:
    if when is None:
        return "<td></td>"
    return f"<td>{when.strftime('%Y-%m-%d %H:%M')}</td>"


def _summary_url(article: Article) -> str:
    """Return the URL of the article's Markdown file rendered on GitHub."""
    when = article.source_published_at
    return (
        f"{_REPO_BLOB_URL}/artefacts/articles/"
        f"{when.year:04d}/{when.month:02d}/{when.day:02d}/"
        f"{short_hash(article.guid)}.md"
    )


_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Archive — Hacker News Best with summaries</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/simple-datatables@10/dist/style.css">
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
  header {{ margin-bottom: 1.5rem; }}
  h1 {{ margin: 0 0 0.25rem; font-size: 1.4rem; }}
  a {{ color: var(--accent); text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  table {{
    width: 100%;
    border-collapse: collapse;
  }}
  th, td {{
    padding: 0.5rem 0.75rem;
    border-bottom: 1px solid var(--border);
    text-align: left;
    vertical-align: top;
  }}
  th {{ font-weight: 600; color: var(--muted); white-space: nowrap; }}
  th, td:not(.title) {{
    white-space: nowrap;
    color: var(--muted);
    width: 1%;
  }}
  td.title, th:last-child {{ width: 100%; color: var(--fg); }}
  tbody tr:nth-child(even) {{ background: var(--row-alt); }}
</style>
</head>
<body>
<header>
  <h1>Archive of {count} articles</h1>
</header>
<table id="archive">
  <thead>
    <tr>
      <th>HN</th>
      <th>Entered HN</th>
      <th>Entered /best</th>
      <th>Entered our feed</th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
{rows}
  </tbody>
</table>
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@10"></script>
<script>
  new simpleDatatables.DataTable("#archive", {{
    searchable: true,
    perPage: 20,
    labels: {{
      perPage: "{{select}} articles per page",
      info: "Showing {{start}} to {{end}} of {{rows}} articles"
    }},
    columns: [
      {{ select: 4, sortable: false }}
    ]
  }});
</script>
</body>
</html>
"""
