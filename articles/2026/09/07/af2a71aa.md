---
article_fetched_at: '2026-09-07T16:54:57.961795Z'
attempts: 0
content_source: ask_show_hn
discussion_comment_count: 231
discussion_fetched_at: '2026-09-07T16:54:48.273945Z'
error: null
guid: https://news.ycombinator.com/item?id=49589914
hn_item_id: 49589914
hn_url: https://news.ycombinator.com/item?id=49589914
is_ask_or_show_hn: true
llm_input_tokens: 21464
llm_latency_ms: 7648
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 587
our_published_at: '2026-09-07T16:40:05Z'
source_published_at: '2026-09-06T19:27:10Z'
status: summarized
summarized_at: '2026-09-07T16:56:21.149812Z'
title: 'Ask HN: How do you manage skills files?'
url: https://news.ycombinator.com/item?id=49589914
---

How do you find skills, keep them organized, and make sure they actually work? Do you keep improving them over time?

I believe skills will eventually be eating by model capabilities, but until then I'm just looking for a better way to manage things.

## Discussion sur Hacker News (231 commentaires)

**Avis positifs** :
- Les skills spécifiques à un projet ou une organisation sont précieuses pour encoder des processus, des conventions et des workflows personnalisés que les modèles ne connaissent pas, économisant tokens et évitant les erreurs répétées.
- Les skills fonctionnent comme du caching déterministe : éviter que le modèle ne réinvente la roue à chaque session en documentant comment utiliser les outils propriétaires, CLI, ou processus métier spécifiques.
- Bien gérées via git et symlinks, les skills permettent de syncer des instructions cohérentes entre plusieurs machines et membres d'équipe, améliorant la consistance et réduisant les réapprentissages.
- Combiner skills avec scripts Python ou bash offre un équilibre puissant : les tâches déterministes restent en code, les tâches non-triviales délèguent au modèle avec contexte préparé.
- Les skills documentent non pas des capacités génériques mais des décisions d'équipe (style de commit, patterns d'architecture, conventions de nommage) qui maintiennent la qualité du code généré.

**Avis négatifs** :
- Les skills génériques téléchargées sur internet (design critique, review de code) sont rapidement obsolètes et remplacées par les améliorations des modèles, ce qui rend leur curation coûteuse en temps.
- Accumuler trop de skills sans discipline crée de la dette technique : chargement inutile de contexte, confusion sur lesquelles utiliser, et maintenance difficile quand les modèles évoluent.
- Les skills ne garantissent pas le comportement : les modèles les ignorent ou ne les suivent pas fidèlement, nécessitant des tests constants et des ajustements frustrants.
- Pour la plupart des tâches générales, un bon README ou AGENTS.md avec des instructions claires suffit ; les skills complexes peuvent être un signe de surengineering plutôt qu'une vraie nécessité.
- La tendance à nommer et packager tout comme « skill » crée une confusion marketing : une simple instruction en markdown n'est pas magique, et trop compter sur elles détourne de solutions réelles (déterminisme via code, hooks, MCP).

**Top commentaires** :

- [picklenerd](https://news.ycombinator.com/item?id=49599924) : I don’t find skills. I write my own skills based on things I do frequently and repeatably. I keep them version controlled locally and in GitHub, and I symlink that folder to my various agent skill folders so they all stay up to date. I feel like downloading a bunch of skills is another one of those…
- [avaer](https://news.ycombinator.com/item?id=49595780) : Skills are mostly snake oil, the way people use them \(the aspiration to download kung foo from a celebrity\). There was a time when maybe it mattered \(last year\), but with good repos and good prompts today's agents can find exactly what they need without any skills. "Skills" as developer macros can…
- [theahura](https://news.ycombinator.com/item?id=49598910) : First, a lot of people in thread are saying you don't need skills. This is pretty wrong. There is a lot of alpha in using any set of skills that implements SPACE \(search, plan, assert, code, evaluate\). See: https://open.substack.com/pub/theahura/p/agentics-using-meta... Second, we share all of our…

---

[Article original](https://news.ycombinator.com/item?id=49589914) · [Discussion HN](https://news.ycombinator.com/item?id=49589914)
