import re
from dataclasses import dataclass

from app.llm import complete

_ARTICLE_SYSTEM = """Tu es un rédacteur francophone. Tu reçois le texte d'un article.

Ton travail a deux parties :

1. Un titre réécrit de 6 à 15 mots qui énonce factuellement ce que l'article \
apprend au lecteur. Évite tout style putaclic, toute question, toute promesse vague \
("ce qu'il faut savoir", "ce qui va changer"). Pas de majuscule partout, pas de point final. \
Si le titre original est déjà factuel et informatif, réutilise-le tel quel.

2. Un résumé structuré en Markdown :
   - commence par une à deux phrases de synthèse factuelle (sans préfixe "TL;DR" \
ou autre étiquette),
   - saute une ligne,
   - puis donne 3 à 5 bullets synthétiques (préfixe "- ") avec les points clés.

Format de réponse EXACT, sans rien d'autre :

## Titre
<ton titre ici, une seule ligne>

## Résumé
<ton résumé markdown ici>"""

_DISCUSSION_SYSTEM = """Tu synthétises en français une discussion Hacker News.
Produis exactement deux blocs Markdown :

**Confirmations** :
- 3 à 5 bullets concis regroupant les commentaires qui confirment, appuient ou \
complètent les thèses de l'article.

**Réfutations** :
- 3 à 5 bullets concis regroupant les commentaires qui contredisent, nuancent \
fortement ou réfutent les thèses de l'article.

Résume les positions dominantes, pas les échanges individuels. Si un angle ou nuance inattendu \
domine la discussion, glisse-le dans la liste concernée. N'ajoute aucun autre titre ni \
préambule."""


@dataclass
class ArticleSummary:
    rewritten_title: str | None
    summary_markdown: str
    model: str


def summarize_article(text: str, title: str) -> ArticleSummary:
    user = f"Titre original : {title}\n\nContenu :\n{text}"
    result = complete(_ARTICLE_SYSTEM, user)
    rewritten, summary = _split_title_and_summary(result.text)
    return ArticleSummary(
        rewritten_title=rewritten,
        summary_markdown=summary,
        model=result.model,
    )


def summarize_discussion(text: str, title: str) -> tuple[str, str]:
    """Return (summary markdown, model name)."""
    user = f"Titre : {title}\n\nCommentaires (indentation = fil de réponse) :\n{text}"
    result = complete(_DISCUSSION_SYSTEM, user)
    return result.text, result.model


def compose_body(
    *,
    article_summary: str | None,
    discussion_summary: str | None,
    url: str,
    hn_url: str,
) -> str:
    parts: list[str] = []
    if article_summary:
        parts.append("## Résumé de l'article\n\n" + article_summary.strip())
    if discussion_summary:
        parts.append("## Discussion sur Hacker News\n\n" + discussion_summary.strip())
    parts.append(f"---\n\n[Article original]({url}) · [Discussion HN]({hn_url})")
    return "\n\n".join(parts) + "\n"


_TITLE_HEADING_RE = re.compile(r"^\s*#{1,3}\s*Titre\s*$", re.IGNORECASE | re.MULTILINE)
_SUMMARY_HEADING_RE = re.compile(r"^\s*#{1,3}\s*Résumé\s*$", re.IGNORECASE | re.MULTILINE)


def _split_title_and_summary(text: str) -> tuple[str | None, str]:
    """Parse LLM output. On unexpected format: title=None, summary=raw text."""
    title_match = _TITLE_HEADING_RE.search(text)
    summary_match = _SUMMARY_HEADING_RE.search(text)
    if not title_match or not summary_match or summary_match.start() < title_match.end():
        return None, text.strip()
    raw_title = text[title_match.end() : summary_match.start()].strip()
    title = raw_title.splitlines()[0].strip() if raw_title else ""
    summary = text[summary_match.end() :].strip()
    return (title or None), summary
