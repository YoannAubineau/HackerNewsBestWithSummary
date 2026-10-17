---
article_fetched_at: '2026-10-17T07:20:54.735917Z'
attempts: 0
content_source: extracted
discussion_comment_count: 286
discussion_fetched_at: '2026-10-17T07:20:53.334536Z'
error: null
guid: https://news.ycombinator.com/item?id=50122951
hn_item_id: 50122951
hn_url: https://news.ycombinator.com/item?id=50122951
image_url: https://claude.dev/blog/solving-code-review-at-anthropic/og.png
is_ask_or_show_hn: false
llm_input_tokens: 27753
llm_latency_ms: 13989
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 999
our_published_at: '2026-10-17T06:26:00Z'
rewritten_title: Comment l'équipe Claude Code pratique la révision de code à grande
  échelle
source_published_at: '2026-10-16T19:04:47Z'
status: summarized
summarized_at: '2026-10-17T07:21:35.342285Z'
title: How the Claude Code team does code review
url: https://claude.dev/blog/solving-code-review-at-anthropic/
---

## Résumé de l'article

L'équipe Claude Code d'Anthropic a réorganisé son processus de révision de code pour gérer le volume de changements générés par les agents IA (passé de 2 500 à 30 000 changements par jour en quelques mois), en déplaçant la majeure partie du travail vers des vérifications automatisées tout en préservant l'examen humain pour les décisions critiques.

- La révision se fait maintenant en continu avant la création d'une pull request, avec Claude vérifiant le code et les tests avant qu'un humain ne l'examine, capturant ainsi les erreurs routinières sans intervention humaine.
- Les vérifications automatisées incluent lint, tests, construction, review de sécurité et une revue Claude qui détecte les bugs et vérifie la conformité aux conventions du projet (via des fichiers CLAUDE.md et REVIEW.md).
- Un système de classification des risques détermine le niveau de révision nécessaire : les changements à faible risque des auteurs de confiance peuvent fusionner avec seule la validation automatisée, tandis que les changements sensibles nécessitent toujours un humain.
- Entre juin et septembre, les pull requests fusionnées ont plus que doublé tandis que les révocations ont baissé de plus de 40 %, démontrant que moins d'examens humains ne signifie pas plus d'incidents si les automatisations capturent les vrais bugs.
- L'équipe a mis en place des garde-fous : les agents reviewer et les agents auteur peuvent créer des boucles infinies, donc les révisions multiples sont limitées ; les incidents deviennent des cas de test pour améliorer les vérificateurs futurs.

## Discussion sur Hacker News (286 commentaires)

**Avis positifs** :
- L'approche d'Anthropic optimise le workflow en automatisant les revues basses risques et en concentrant l'attention humaine sur les décisions architecturales et les changements critiques
- Les modèles récents (Opus 5.5) produisent effectivement du code de bonne qualité et gèrent bien les refactorisations, rendant le vibe coding viable pour certains cas d'usage
- Le système d'évaluation continuellement amélioré par chaque incident crée une boucle d'apprentissage qui renforce progressivement la qualité des revues automatisées
- Cette approche à grande échelle offre une preuve de concept pour l'industrie et permet d'explorer les limites réelles des LLM en production

**Avis négatifs** :
- Le chiffre de 30 000 changements par jour paraît largement gonflé et potentiellement trompeur (refactoring automatique, changements de config mineurs, etc.), relevant davantage du marketing que d'une métrique significative
- Personne n'a réellement compris le code ; les ingénieurs n'ont plus de modèle mental cohérent du système et dépendent entièrement de Claude pour expliquer chaque slice, créant une vulnérabilité existentielle
- Le code généré en vibe-coding accumule duplication, architectures incohérentes et debt technique non intentionnel, masqué par un taux de réversion artificiellement bas
- L'absence de revue humaine réelle pose des risques de conformité (SOC2, audit), de sécurité (injection de prompts, code malveillant) et crée une dépendance dangereuse envers les tokens payants
- Le rythme insoutenable crée du churn plutôt que de l'innovation ; les produits restent instables (bugs UI récurrents, régressions fréquentes) et l'approche n'est pas transposable aux équipes sans ressources illimitées

**Top commentaires** :

- [status\_quo69](https://news.ycombinator.com/item?id=50124637) : No wonder most people at Anthropic believe our jobs are in jeopardy, they've already made a system wherein the machines are treating them like pets. I really don't get the tendency here from Anthropic to describe what's most likely churn? A high pressure amount of changes/PRs a day on a TUI to wrap…
- [avinoth](https://news.ycombinator.com/item?id=50127080) : This is like one of Google’s infrastructure blog. Google scale things are only relevant and appropriate for them. We had lots of bitter lessons from smaller engineering teams following the process with the justification that “this is how Google does it”. Similarly, Anthropic can afford to do this b…
- [mk12](https://news.ycombinator.com/item?id=50124719) : I saw someone say the other day \(in response to another blog post being well written\) that Anthropic employees have a rule against using AI for writing/external comms? That seems clearly not the case here, normal people don't write like this: \> Most of the path is automated; a person's attention go…

---

[Article original](https://claude.dev/blog/solving-code-review-at-anthropic/) · [Discussion HN](https://news.ycombinator.com/item?id=50122951)
