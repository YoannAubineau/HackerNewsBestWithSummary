---
article_fetched_at: '2026-09-09T00:54:03.810776Z'
attempts: 0
content_source: extracted
discussion_comment_count: 241
discussion_fetched_at: '2026-09-09T00:54:01.237826Z'
error: null
guid: https://news.ycombinator.com/item?id=49610631
hn_item_id: 49610631
hn_url: https://news.ycombinator.com/item?id=49610631
image_url: https://opengraph.githubassets.com/070329ba76853a16d1ca475851cd3b2aac79612a3b52d96046218ad8c3bf148c/ayghri/i-have-adhd
is_ask_or_show_hn: false
llm_input_tokens: 18701
llm_latency_ms: 12229
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 929
our_published_at: '2026-09-09T00:04:42Z'
rewritten_title: 'i-have-adhd: un plugin pour agents de code qui priorise la réponse
  plutôt que les explications'
source_published_at: '2026-09-08T14:13:26Z'
status: summarized
summarized_at: '2026-09-09T00:54:25.676241Z'
title: 'I-have-ADHD: A skill to stop coding agents from burying the answer'
url: https://github.com/ayghri/i-have-adhd
---

## Résumé de l'article

i-have-adhd est un plugin/skill open source pour assistants de code (notamment Claude) qui impose un format de réponse structuré et direct, conçu pour éviter que l'IA ne noie la réponse dans du texte prolixe ou des tangentes.

- Le plugin applique 10 règles : commencer par l'action suivante, numéroter les tâches multi-étapes, terminer par une prochaine étape concrète, étouffer les digressions, limiter les listes à 5 éléments, fournir des estimations de temps précises, et bannir les formules de politesse ("J'espère que cela t'aide")
- Installation via GitHub (ayghri/i-have-adhd) avec support de multiples assistants et instructions disponibles dans AGENTS.md
- S'inspire de la boîte à outils pour adultes ADHD de Ramsay et Rostain, adaptée à la manière dont les LLM devraient répondre plutôt qu'à l'organisation humaine
- Les règles imposent des réponses sans préambule, sans récapitulatif, axées sur les actions concrètes numérotées et les estimations temporelles précises
- Licence MIT, fork et personnalisation encouragés via les fichiers SKILL.md

## Discussion sur Hacker News (241 commentaires)

**Avis positifs** :
- Efficace pour forcer une reformulation concise : de nombreux utilisateurs rapportent que dire simplement « j'ai un TDAH » ou des variantes obtiennent des résumés plus lisibles et structurés que les instructions génériques.
- Résout un problème universel, pas seulement neurotypique : les stratégies d'accessibilité pour le TDAH (BLUF, listes à puces, structure claire) bénéficient à tous, similaire aux rampes d'accès utiles à chacun.
- Meilleur que les alternatives fragmentées : plus robuste et persistent qu'un simple « Soyez concis » ou que les instructions dans CLAUDE.md/AGENTS.md, qui perdent en poids avec l'accroissement du contexte.
- Adresse un défaut récurrent de Claude : notamment Opus 5 souffre d'une verbosité chronique et d'une structure enterrant les réponses, validant le besoin urgent d'un tel outil malgré son usage métaphorique du TDAH.

**Avis négatifs** :
- Efficacité limitée et éphémère : même avec le skill installé, Claude oublie rapidement les directives après quelques tours et revient à sa verbosité habituelle, nécessitant des rappels constants.
- Problématique d'appropriation : l'usage métaphorique du TDAH par ceux sans diagnostic agace les personnes réellement atteintes; le skill perpétue la trivialisation d'un trouble neurodéveloppemental sérieux.
- Solution symptomatique plutôt que racine : le vrai problème est l'entraînement et l'architecture de Claude/Opus 5, pas l'absence d'un skill; patcher le comportement au lieu de corriger le modèle est inefficace.
- Surengineering : un dépôt de 8,7k lignes pour une simple instruction markdown de 140 lignes; un gist ou une simple ligne de prompt suffirait, questionnant l'intérêt réel du format « skill ».

**Top commentaires** :

- [jp57](https://news.ycombinator.com/item?id=49613789) : Let's face it. Claude \(in particular\) is a terrible writer. There's a whole cottage industry of skills and CLAUDE.md instructions trying to push it toward writing better, but each new model iteration seems expressly designed to override all that so that it can load up its writing with unnecessary p…
- [ryandrake](https://news.ycombinator.com/item?id=49613881) : The biggest "Claudism" that I have a hard time getting the LLM to stop doing is its insistence on talking about what it didn't do in addition to what it did. "I edited this.py and that.py but I did not edit README.md and I did not commit." or code comments like "This code invokes foo on bar and ret…
- [sleazebreeze](https://news.ycombinator.com/item?id=49611957) : Claude models are the ones that need this the most and in my experience with this specific skill only maintain the conciseness for a few turns at most before they completely forget and are back to their unfathomable verbosity. That's with it instructed to use it in my sparse global CLAUDE.md and al…

---

[Article original](https://github.com/ayghri/i-have-adhd) · [Discussion HN](https://news.ycombinator.com/item?id=49610631)
