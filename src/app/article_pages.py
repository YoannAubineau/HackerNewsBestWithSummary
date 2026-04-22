"""Render one static HTML page per summarized article.

Each page lives at ``artefacts/a/{short_hash}.html`` so the archive can
link directly to our own French summary (the article body rendered from
Markdown) rather than sending readers back to the original URL or HN.
"""

from datetime import datetime
from html import escape

from markdown_it import MarkdownIt

from app.config import get_settings
from app.models import Article
from app.storage import iter_summarized, short_hash

# html=False escapes raw HTML that could sneak in via the LLM output.
_md = MarkdownIt(options_update={"html": False})


def write_article_pages() -> int:
    """Regenerate every article page. Returns the count written."""
    settings = get_settings()
    out_dir = settings.artefacts_dir / "a"
    out_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for _path, article, body in iter_summarized():
        html = _render(article, body)
        (out_dir / f"{short_hash(article.guid)}.html").write_text(
            html, encoding="utf-8"
        )
        count += 1
    return count


def _render(article: Article, body: str) -> str:
    title = article.rewritten_title or article.title
    body_html = _md.render(body)
    meta_parts: list[str] = []
    if article.rewritten_title and article.title != article.rewritten_title:
        meta_parts.append(
            f'<p class="original-title">Titre original : '
            f"<em>{escape(article.title)}</em></p>"
        )
    meta_parts.append(
        '<p class="dates">'
        f"Publié sur HN le {_format(article.source_published_at)} · "
        f"Entré dans /best le {_format(article.our_published_at)}"
        + (
            f" · Résumé généré le {_format(article.summarized_at)}"
            if article.summarized_at
            else ""
        )
        + "</p>"
    )
    return _TEMPLATE.format(
        page_title=escape(title),
        title=escape(title),
        meta="\n  ".join(meta_parts),
        body=body_html,
        hn_url=escape(article.hn_url),
        article_url=escape(article.url),
    )


def _format(when: datetime) -> str:
    return when.strftime("%Y-%m-%d %H:%M")


_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page_title} — Hacker News Best with summaries</title>
<style>
  :root {{
    color-scheme: light dark;
    --bg: #fafafa;
    --fg: #222;
    --muted: #666;
    --border: #e5e5e5;
    --accent: #ff6600;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --bg: #1a1a1a;
      --fg: #e5e5e5;
      --muted: #999;
      --border: #333;
    }}
  }}
  body {{
    margin: 0;
    padding: 1.5rem;
    background: var(--bg);
    color: var(--fg);
    font: 15px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }}
  main, nav.top {{
    max-width: 44rem;
    margin: 0 auto;
  }}
  nav.top {{
    margin-bottom: 1rem;
    color: var(--muted);
    font-size: 0.9em;
  }}
  h1 {{ margin: 0.25rem 0 0.75rem; font-size: 1.6rem; line-height: 1.25; }}
  a {{ color: var(--accent); text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  .original-title, .dates {{
    color: var(--muted);
    margin: 0.25rem 0;
    font-size: 0.9em;
  }}
  article {{
    border-top: 1px solid var(--border);
    margin-top: 1rem;
    padding-top: 1rem;
  }}
  article h2 {{ font-size: 1.2rem; margin-top: 1.5rem; }}
  article ul {{ padding-left: 1.25rem; }}
  article li {{ margin: 0.25rem 0; }}
  article blockquote {{
    margin: 0.5rem 0 0.5rem 0;
    padding-left: 1rem;
    border-left: 3px solid var(--border);
    color: var(--muted);
  }}
  footer {{
    max-width: 44rem;
    margin: 2rem auto 0;
    padding-top: 1rem;
    border-top: 1px solid var(--border);
    color: var(--muted);
    font-size: 0.9em;
  }}
  footer a {{ margin-right: 1rem; }}
</style>
</head>
<body>
<nav class="top">
  <a href="../archive.html">← Archive</a> ·
  <a href="../feed.fr.xml">Flux</a>
</nav>
<main>
  <h1>{title}</h1>
  {meta}
  <article>
{body}
  </article>
</main>
<footer>
  <a href="{article_url}" rel="noopener">Article original ↗</a>
  <a href="{hn_url}" rel="noopener">Discussion HN ↗</a>
</footer>
</body>
</html>
"""
