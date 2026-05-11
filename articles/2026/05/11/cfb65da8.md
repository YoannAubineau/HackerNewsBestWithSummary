---
article_fetched_at: '2026-05-11T07:07:50.568293Z'
attempts: 0
content_source: extracted
discussion_comment_count: 104
discussion_fetched_at: '2026-05-11T07:07:49.378082Z'
error: null
guid: https://news.ycombinator.com/item?id=48090029
hn_item_id: 48090029
hn_url: https://news.ycombinator.com/item?id=48090029
image_url: https://blog.k10s.dev/static/og-image.png
is_ask_or_show_hn: false
llm_input_tokens: 16450
llm_latency_ms: 12877
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1160
our_published_at: '2026-05-11T06:58:47Z'
rewritten_title: Retour à la programmation manuelle après avoir expérimenté le code
  généré par IA
source_published_at: '2026-05-11T01:23:51Z'
status: summarized
summarized_at: '2026-05-11T07:08:09.958650Z'
title: I'm going back to writing code by hand
url: https://blog.k10s.dev/im-going-back-to-writing-code-by-hand/
---

## Résumé de l'article

Un développeur décrit son expérience de construction d'un outil Kubernetes (k10s) en laissant l'IA générer la majorité du code, et explique pourquoi cette approche a finalement échoué. Après sept mois de développement rapide, la base de code s'est effondrée sous son propre poids à cause de défauts architecturaux que l'IA reproduisait systématiquement.

- L'IA excelle à générer des fonctionnalités isolées mais échoue à concevoir une architecture solide ; elle gravitera toujours vers des godObjects simples à générer plutôt que vers des structures modulaires
- Le sentiment trompeur de vélocité incite à élargir le scope du projet indéfiniment (« c'est facile, ajoutons ceci aussi »), ce qui accumule la complexité de manière invisible
- Cinq principes clés permettent de limiter les dégâts : écrire l'architecture avant le code, imposer des règles d'ownership strictes via un fichier CLAUDE.md, maintenir des structures de données typées plutôt que des tableaux positionnels, limiter le scope du projet, et garantir que seule la boucle principale peut muter l'état visible
- L'absence de garde-fou dans les directives au modèle IA aboutit à des antipatterns (état partagé non synchronisé, récursion de conditionnelles, fuites de données entre vues)
- La réécriture sera faite en mettant d'abord par écrit les décisions architecturales concrètes, plutôt que de laisser l'IA les inventer au fur et à mesure

## Discussion sur Hacker News (104 commentaires)

**Avis positifs** :
- La conception architecturale en amont (avant le code) est essentielle : les décisions architecturales doivent être prises consciemment et documentées avant de laisser l'IA générer le code, plutôt que de laisser l'IA improviser l'architecture.
- L'IA peut gagner du temps significatif (50-100%) quand elle est encadrée : avec une architecture claire, des règles définies et une revue attentive, l'IA reste un outil productif pour implémenter plutôt que concevoir.
- Mieux vaut viser des itérations petites et précises : plutôt qu'un one-shot généraliste, discuter avec l'IA au niveau technique granulaire (service par service, binding par binding) produit de meilleurs résultats.
- Les tests automatisés sont cruciaux pour valider le code généré : des tests fonctionnels complets permettent de faire confiance aux refactorisations et modifications sans relire chaque ligne.
- Le langage avec lequel on est à l'aise importe plus que la syntaxe objective : la familiarité personnelle permet de détecter les « odeurs » architecturales et les bugs que l'IA peut produire, quelle que soit la complexité syntaxique.

**Avis négatifs** :
- Le titre est trompeur : l'auteur n'écrit pas vraiment « à la main », il conçoit l'architecture et laisse toujours l'IA générer le code, ce qui n'est qu'une variation du même problème.
- Documenter une architecture exhaustive en amont est irréaliste pour la plupart des projets : on découvre souvent l'architecture correcte qu'après avoir écrit du code, itéré et échoué ; documenter tout avant était impraticable historiquement et le reste.
- L'IA génère du code plausible mais défectueux difficile à valider : même avec des revues multiples, les agents passent à côté de détails cruciaux (distinction réplica/primaire, conditions ORDER BY oubliées, etc.), rendant la confiance inévitablement compromise.
- La lecture exhaustive de tout le code généré est impossible à l'échelle et tue l'utilité de l'outil : vouloir comprendre et valider chaque ligne annule les gains de productivité et revient à coder manuellement.
- Le problème n'était pas le langage mais la naïveté du vibe-coding sans révision : sept mois sans lire aucun code n'est pas une limite structurelle de l'IA, c'est un choix de non-engagement qui aurait échoué avec n'importe quel outil.

**Top commentaires** :

- [baddash](https://news.ycombinator.com/item?id=48091332) : I've set a few rules for working with coding agents: 1. If I use a coding agent to generate code, it should be something I am absolutely confident I can code correctly myself given the time \(gun to my head test\). 2. If it isn't, I can't move on until I completely understand what it is that has been…
- [snowe2010](https://news.ycombinator.com/item?id=48090600) : « The other change is simpler: I'm doing the design work myself, by hand, before any code gets written. Not a vague doc. Concrete interfaces, message types, ownership rules. » That’s the hard part of coding. If you have an architecture then writing the code is dead simple. If you aren’t writing the…
- [plastic041](https://news.ycombinator.com/item?id=48090429) : Title says \> back to writing code by hand But what they are doing is \> doing the \_\_design work\_\_ myself, by hand, before any code gets written. So... Claude still is generating the code I guess? And seriously, I can't understand that they thought their vibe coded project works fine and even bought…

---

[Article original](https://blog.k10s.dev/im-going-back-to-writing-code-by-hand/) · [Discussion HN](https://news.ycombinator.com/item?id=48090029)
