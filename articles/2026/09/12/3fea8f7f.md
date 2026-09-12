---
article_fetched_at: '2026-09-12T11:49:30.381845Z'
attempts: 0
content_source: extracted
discussion_comment_count: 227
discussion_fetched_at: '2026-09-12T11:49:28.133247Z'
error: null
guid: https://news.ycombinator.com/item?id=49658311
hn_item_id: 49658311
hn_url: https://news.ycombinator.com/item?id=49658311
image_url: https://earendil.com/static/og/posts/measuring-code-sloppiness.png
is_ask_or_show_hn: false
llm_input_tokens: 25305
llm_latency_ms: 13319
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1071
our_published_at: '2026-09-12T11:23:32Z'
rewritten_title: Mesurer la qualité défaillante du code généré par les LLM
source_published_at: '2026-09-11T13:42:28Z'
status: summarized
summarized_at: '2026-09-12T11:50:00.142873Z'
title: Measuring the sloppiness of code
url: https://earendil.com/posts/measuring-code-sloppiness/
---

## Résumé de l'article

Les modèles de langage génèrent du code formellement correct, mais souvent peu structuré et inefficace. L'article explore différentes méthodes pour quantifier cette « sloppiness » (négligence) du code : évaluation par IA (peu fiable), jugement humain (non scalable), ou métriques objectives comme le nombre de lignes de code, la verbosité et l'érosion.

- Les LLM produisent du code syntaxiquement valide mais introduisent des abstractions inutiles, duplications et mauvaises décisions architecturales, ce qui complique la maintenance à grande échelle
- Trois approches d'évaluation : (1) demander aux IA d'évaluer leur propre code (inefficace et volatile), (2) jugement humain (fiable mais non scalable), (3) métriques mécaniques
- Les métriques SlopCodeBench (verbosité et érosion) révèlent que le code d'agents IA est en moyenne deux fois plus verbeux et concentré en fonctions complexes que le code humain de référence
- Dans un benchmark avec itérations et contexte effacé entre checkpoints (plus réaliste), même les meilleurs modèles actuels atteint 0 % de taux de passage complet, signalant une accumulation de mauvaises décisions
- L'évaluation de la sloppiness reste partiellement subjective et basée sur l'intuition humaine, malgré les tentatives de métriques objectives

## Discussion sur Hacker News (227 commentaires)

**Avis positifs** :
- Les métriques quantitatives (LOC, complexité cyclomatique, churn) capturent intuitivement ce que beaucoup savent déjà : les agents accumulent de la dette technique et produisent du code verbeux et inefficace au fil des itérations.
- SlopCodeBench offre une évaluation plus réaliste que les benchmarks actuels en simulant des processus itératifs avec effacement du contexte, montrant que même les modèles SOTA n'atteindent 0% de taux de réussite stricte.
- Des métriques mesurables et des boucles de rétroaction bien conçues pourraient permettre aux modèles d'optimiser la qualité du code rapidement, comme ils l'ont fait pour la correction.
- La compression et la modularité sous-tendent à la fois l'intelligence humaine et l'apprentissage des modèles, suggérant que code moins verbeux et mieux organisé bénéficie à tous les systèmes intelligents.
- Historiquement, une grande partie du code humain en entreprise était de mauvaise qualité, donc comparer les agents à des références mediocres n'a pas de sens ; la vraie question est si les agents dépassent les bons développeurs.

**Avis négatifs** :
- Le codage n'est pas réellement résolu : correctness est le minimum ; la véritable qualité exige efficiency, sécurité, maintenabilité, fiabilité et extensibilité, où les modèles actuels sont clairement insuffisants.
- Les agents luttent structurellement : ils ne comprennent pas la conception globale d'une codebase, perdent le contexte architectural, accumulent des duplicatas sans les nettoyer et prennent de mauvaises décisions qui s'amplifient au fil du temps.
- Goodhart's Law menace tout métrique utilisée comme fonction de récompense ; optimiser uniquement sur LOC ou complexité cyclomatique risque de créer du code qui contourne la métrique sans améliorer la qualité réelle.
- Les agents manquent de capacités humaines clés : comprension du problème global, planification à long terme, réflexion architecturale holistique, et incapacité à savoir où faire les changements dans une codebase existante.
- Le coût des tokens demeure prohibitif pour des boucles itératives en production ; le mythe de la « résolution du codage » ignore les contraintes économiques et pratiques réelles du déploiement d'agents autonomes.

**Top commentaires** :

- [dang](https://news.ycombinator.com/item?id=49661927) : All: please don't post generic reflexive reactions to titles. That's covered by this guideline, among others, in https://news.ycombinator.com/newsguidelines.html: "Please don't pick the most provocative thing in an article or post to complain about in the thread. Find something interesting to respo…
- [dherman](https://news.ycombinator.com/item?id=49660089) : Really glad to see folks looking into quantitative approaches to give agents feedback on code quality. This post looks like a good start! My main feedback for the authors would be, the most important problems for sloppiness are global properties, not local ones. In my experience an agent, like a hu…
- [conqrr](https://news.ycombinator.com/item?id=49659478) : Coding is not just the program running in memory, its also the process of distributing the mental model of understanding among the team. If humans increasingly are kept out of coding, then who holds the mental model? If AI holds the mental model, by definition human prompts will be over lossy chann…

---

[Article original](https://earendil.com/posts/measuring-code-sloppiness/) · [Discussion HN](https://news.ycombinator.com/item?id=49658311)
