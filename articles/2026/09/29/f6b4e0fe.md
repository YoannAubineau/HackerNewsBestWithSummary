---
article_fetched_at: '2026-09-29T00:47:31.165793Z'
attempts: 0
content_source: extracted
discussion_comment_count: 74
discussion_fetched_at: '2026-09-29T00:47:29.347767Z'
error: null
guid: https://news.ycombinator.com/item?id=49883844
hn_item_id: 49883844
hn_url: https://news.ycombinator.com/item?id=49883844
image_url: https://opengraph.githubassets.com/09e4abc0b1f3a764333729f9127153da7a195c1e47281f310be3affd7e651501/firelex/jeff
is_ask_or_show_hn: false
llm_input_tokens: 9750
llm_latency_ms: 15211
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1109
our_published_at: '2026-09-29T00:28:10Z'
rewritten_title: Jeff, modèles de décision compatibles Jev entraînés localement, décisions
  en 30 ms
source_published_at: '2026-09-28T20:23:36Z'
status: summarized
summarized_at: '2026-09-29T00:48:30.954077Z'
title: Jeff – Jev-compatible 0.8B decision models, trained at home, ~30 ms
url: https://github.com/firelex/jeff
---

## Résumé de l'article

Jeff est un ensemble de petits modèles de classification zéro-shot basés sur Qwen et Gemma, fins versions d'0,8 B à 2 B de paramètres, conçus pour prendre des décisions rapides et bien calibrées entre des options décrites en langage naturel. Entraîné entièrement sur du matériel local sans GPU cloud, Jeff utilise le même format de requête que Jev mais n'y est pas affilié.

- Les modèles répondent en 22-28 ms par décision sur GPU haut de gamme, permettant une intégration directe dans du code local sans accès réseau
- Zéro-shot : les catégories n'ont pas besoin d'apparaître dans les données d'entraînement; on les décrit en langage naturel et Jeff affecte une probabilité calibrée à chaque option
- Sur les benchmarks publics (4 599 questions), Jeff approche ou égale la performance de Jev sur les tâches de classification et de grounding, mais reste en retrait sur les tâches lourdes en raisonnement (BBH, JudgeBench)
- L'entraînement fin sur des exemples spécifiques au domaine (~11k exemples) améliore drastiquement la précision: une fine-tune voice-navigation a porté la précision de 31,7% à 95,8% en moins d'une demi-heure sur un GPU
- Trois types de questions supportées (choix unique, oui/non, évaluation sur échelle); les poids des modèles sont publiés sous licence Apache 2.0 et le code sous MIT

## Discussion sur Hacker News (74 commentaires)

**Avis positifs** :
- Jeff démontre qu'il est possible de construire des modèles de décision performants en open-source et auto-hébergés sans infrastructure massive, offrant une alternative viable à Jev pour certains cas d'usage.
- La vitesse d'inférence (28-40ms) et la capacité à fonctionner localement sur du matériel standard (MacBook, RTX) ouvrent de nouveaux cas d'usage (navigation vocale, routage de requêtes en temps réel) où l'API centralisée n'est pas adaptée.
- Les petits modèles de classification ont des avantages pratiques : rapidité extrême (<1ms avec embeddings+classifieur), économies de coût et de ressources, et flexibilité pour l'ajustement fin sur des données spécifiques.
- Ce type d'approche System 1 (jugement rapide sans génération de texte) représente une branche complémentaire durable aux LLM généralisés, adaptée aux applications nécessitant des décisions rapides et nombreuses.

**Avis négatifs** :
- Jeff affiche des performances de classification inférieures à Jev (70% vs 94% rapporté par certains utilisateurs) et perd significativement sur des tâches de raisonnement multi-étapes (64-68% sur BBH vs 94% pour Jev), ce qui limite fortement son utilité sans fine-tuning.
- La comparaison de benchmarks est problématique : Jeff utilise des ensembles de test différents et des tâches axées classification là où Jev excelle en raisonnement; les scores ne sont donc pas directement comparables.
- Jev offre déjà une valeur majeure par sa capacité zero-shot sans ajustement, tandis que Jeff nécessite un fine-tuning pour atteindre des performances acceptables, changeant fondamentalement la proposition de valeur et les coûts opérationnels.
- L'utilité réelle reste incertaine par rapport aux alternatives simples : des classifieurs traditionnels (ModernBERT 0.4B) ou l'approche embeddings+logistic regression obtiennent des résultats comparables ou supérieurs avec moins de complexité.
- Les préoccupations éthiques augmentent avec la démocratisation de modèles de classification rapides et optimisés pour la décision en temps réel, ouvrant les portes à la surveillance de masse et aux systèmes d'armes autonomes.

**Top commentaires** :

- [adrithmetiqa](https://news.ycombinator.com/item?id=49885037) : Forgive my lack of understanding but how long before Jev type functionality is just built straight into all frontier models?
- [AgentMasterRace](https://news.ycombinator.com/item?id=49884862) : I compared it to Jev in my current use cases and it's very inaccurate. 70% vs 94% . for classification, it's unacceptable.
- [trebligdivad](https://news.ycombinator.com/item?id=49885443) : What proportion of commercial LLM use is classification? I'm just wondering what happens to business AI spending/data centre usage when they realise they don't need full LLMs.

---

[Article original](https://github.com/firelex/jeff) · [Discussion HN](https://news.ycombinator.com/item?id=49883844)
