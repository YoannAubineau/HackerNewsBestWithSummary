import json
from dataclasses import dataclass

from app.llm import LLMCallResult, complete

_ARTICLE_SYSTEM = """Tu es un rédacteur francophone. Tu reçois le texte d'un article, \
ou la transcription d'une vidéo.

Ton travail a deux parties :

1. Un titre réécrit en français de 6 à 15 mots qui énonce factuellement ce que le contenu \
apprend au lecteur. Évite tout style putaclic, toute question, toute promesse vague \
("ce qu'il faut savoir", "ce qui va changer"). Pas de majuscule partout, pas de point final.

2. Un résumé structuré en Markdown :
   - commence par une à deux phrases de synthèse factuelle (sans préfixe "TL;DR" \
ou autre étiquette),
   - saute une ligne,
   - puis donne 3 à 5 bullets synthétiques (préfixe "- ") avec les points clés.

Réponds uniquement par un objet JSON valide avec exactement deux champs string :
- "title" : le titre réécrit, une seule ligne, sans préfixe ni en-tête.
- "summary" : le résumé Markdown (les sauts de ligne et les bullets doivent être \
échappés correctement dans la chaîne JSON).

Aucun texte hors du JSON, pas de bloc de code, pas de commentaire."""

_TITLE_TRANSLATION_SYSTEM = """Tu reçois un titre d'article en anglais \
(ou dans une autre langue). Traduis-le fidèlement en français. Ne réécris pas, \
ne reformule pas, ne synthétise pas : traduis aussi littéralement que possible \
tout en produisant un français naturel. Pas de majuscule partout, pas de point \
final. Si le titre est déjà en français, réutilise-le tel quel. Réponds \
uniquement par le titre traduit, sur une seule ligne."""

_DISCUSSION_SYSTEM = """Tu synthétises en français une discussion Hacker News.
Produis exactement deux blocs Markdown :

**Avis positifs** :
- 3 à 5 bullets concis regroupant les commentaires qui confirment, appuient ou \
complètent les thèses de l'article.

**Avis négatifs** :
- 3 à 5 bullets concis regroupant les commentaires qui contredisent, nuancent \
fortement ou réfutent les thèses de l'article.

Résume les positions dominantes, pas les échanges individuels. Si un angle ou nuance inattendu \
domine la discussion, glisse-le dans la liste concernée. N'ajoute aucun autre titre ni \
préambule."""


@dataclass
class ArticleSummary:
    rewritten_title: str | None
    summary_markdown: str


def summarize_article(text: str, title: str) -> tuple[ArticleSummary, LLMCallResult]:
    user = f"Titre original : {title}\n\nContenu :\n{text}"
    result = complete(_ARTICLE_SYSTEM, user, json=True)
    rewritten, summary = _parse_article_response(result.content)
    return ArticleSummary(rewritten_title=rewritten, summary_markdown=summary), result


def translate_title(title: str) -> tuple[str | None, LLMCallResult]:
    result = complete(_TITLE_TRANSLATION_SYSTEM, title)
    raw = result.content.strip()
    translated = raw.splitlines()[0].strip() if raw else ""
    return (translated or None), result


def summarize_discussion(text: str, title: str) -> tuple[str, LLMCallResult]:
    user = f"Titre : {title}\n\nCommentaires (indentation = fil de réponse) :\n{text}"
    result = complete(_DISCUSSION_SYSTEM, user)
    return result.content, result


def compose_body(
    *,
    article_summary: str | None,
    discussion_summary: str | None,
    discussion_comment_count: int | None = None,
    url: str,
    hn_url: str,
) -> str:
    parts: list[str] = []
    if article_summary:
        parts.append("## Résumé de l'article\n\n" + article_summary.strip())
    if discussion_summary:
        heading = "## Discussion sur Hacker News"
        if discussion_comment_count:
            word = "commentaire" if discussion_comment_count == 1 else "commentaires"
            heading += f" ({discussion_comment_count} {word} analysé"
            heading += "s)" if discussion_comment_count > 1 else ")"
        parts.append(f"{heading}\n\n" + discussion_summary.strip())
    parts.append(f"---\n\n[Article original]({url}) · [Discussion HN]({hn_url})")
    return "\n\n".join(parts) + "\n"


def _parse_article_response(text: str) -> tuple[str | None, str]:
    """Parse the LLM's JSON article response.

    On any malformed JSON, missing key, or wrong type: return
    ``(None, text.strip())`` so the article still publishes with the
    original title and the raw model output as the body.
    """
    try:
        data = json.loads(_strip_code_fence(text))
    except json.JSONDecodeError:
        return None, text.strip()
    if not isinstance(data, dict):
        return None, text.strip()
    raw_title = data.get("title")
    raw_summary = data.get("summary")
    if not isinstance(raw_summary, str):
        return None, text.strip()
    title = raw_title.strip() if isinstance(raw_title, str) else ""
    summary = raw_summary.strip()
    return (title or None), summary


def _strip_code_fence(text: str) -> str:
    """Drop a surrounding ```json ... ``` markdown fence if the LLM added one."""
    s = text.strip()
    if not s.startswith("```"):
        return s
    first_nl = s.find("\n")
    if first_nl == -1:
        return s
    s = s[first_nl + 1 :]
    if s.endswith("```"):
        s = s[:-3]
    return s.strip()
