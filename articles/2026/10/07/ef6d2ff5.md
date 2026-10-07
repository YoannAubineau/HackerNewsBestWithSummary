---
article_fetched_at: '2026-10-07T06:43:24.294975Z'
attempts: 0
content_source: extracted
discussion_comment_count: 109
discussion_fetched_at: '2026-10-07T06:43:22.440994Z'
error: null
guid: https://news.ycombinator.com/item?id=49984025
hn_item_id: 49984025
hn_url: https://news.ycombinator.com/item?id=49984025
image_url: https://developers.openai.com/og/api/docs/guides/decisions.png
is_ask_or_show_hn: false
llm_input_tokens: 10908
llm_latency_ms: 11266
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 910
our_published_at: '2026-10-07T06:39:54Z'
rewritten_title: L'API Decisions d'OpenAI est en bêta publique avec le modèle gpt-6-luna
source_published_at: '2026-10-06T20:57:25Z'
status: summarized
summarized_at: '2026-10-07T06:44:20.347265Z'
title: Decisions API is in public beta
url: https://developers.openai.com/api/docs/guides/decisions
---

## Résumé de l'article

L'API Decisions est une nouvelle interface d'OpenAI qui évalue du texte, des images ou les deux pour retourner rapidement des réponses typées : probabilités, choix parmi des options fixes, ou scores contre une grille d'évaluation. Elle fonctionne 10 fois plus vite que l'API Responses et est conçue pour classer du contenu, router des requêtes et prioriser des tâches dans les applications.

- Trois types de questions disponibles : predicate (probabilité qu'une condition soit vraie), choice (sélection parmi des catégories fixes) et score (évaluation selon des niveaux ordonnés)
- Accès via un endpoint POST dédié /v1/decisions ; seul le modèle gpt-6-luna est actuellement disponible
- Tarification de $0,10 par million de tokens d'entrée uniquement, sans frais de cache ou de sortie
- Supporte l'analyse d'images en base64 inline avec du texte dans la même requête, et les questions multiples indépendantes
- Bêta publique actuellement, disponibilité générale prévue dans les prochaines semaines ; supporte Zero Data Retention et HIPAA pour les clients éligibles

## Discussion sur Hacker News (109 commentaires)

**Avis positifs** :
- OpenAI a réagi rapidement à la menace de Jev en lançant un concurrent crédible, validant la viabilité du marché des modèles de décision
- L'API Decisions supporte les images en entrée contrairement à Jev, comblant une lacune importante et offrant une vraie multimodalité
- Pour les entreprises ayant déjà des contrats avec OpenAI, l'intégration est économiquement plus simple que d'onboarder un nouveau fournisseur (facteur de stickiness réel)
- La vitesse de latence (160-175ms en moyenne) et l'absence de coûts pour les tokens de sortie rendent le produit attrayant pour les cas d'usage à l'échelle
- L'API définit potentiellement un standard de facto que d'autres fournisseurs adopteront, accélérant l'adoption du marché

**Avis négatifs** :
- Jev reste 2-3x moins cher avec des performances supérieures, notamment en calibration des probabilités et précision sur des domaines variés
- Le produit semble sous-développé : latence plus lente que Jev, coût 3x plus élevé, taux d'erreur plus haut (4 défaillances vs 0 pour Jev), probablement précipité pour réagir à la hype
- La fondation du modèle d'affaires sur une course au prix n'est pas durable ; sans réelle différenciation, OpenAI court le risque d'une commoditisation complète
- Le produit ne résout que des cas d'usage simples ; les décisions du monde réel complexes perdent de la cohérence avec plusieurs appels indépendants
- OpenAI semble réagir en mode 'me-too' plutôt que d'innover, symptôme d'absence réelle de moat : les modèles open-source locaux deviennent viables et même les alternatives tarifaires font disparaître progressivement l'avantage compétitif

**Top commentaires** :

- [simonw](https://news.ycombinator.com/item?id=49985035) : curl https://api.openai.com/v1/decisions \\ -H "Authorization: Bearer $\(llm keys get openai\)" \\ -H "Content-Type: application/json" \\ --data ' { "model": "gpt-6-luna", "input": \[{ "role": "user", "content": \[ {"type": "input\_text", "text": "I am angry about the new product feature"} \] }\], "questions…
- [TSiege](https://news.ycombinator.com/item?id=49985015) : The response to Jev should be the nail in the coffin over whether or not the AI business is a commodity market. Out of no where Jev appeared as the next round of the price wars. Jev showed the value of System One models. A fast yes/no/confidence score not only is cheaper but also often all people w…
- [Topfi](https://news.ycombinator.com/item?id=49985095) : Ran my decisions evals \(still rudimentary, less than 600 calls \(UI component selection, chat charting, tag selection, PKM stuff\)\) on this via OpenRouter against Jev and Mercury Decide. Jev because it has replaced my mt0 efforts by sheer force of affordability \(more importantly, the limits running o…

---

[Article original](https://developers.openai.com/api/docs/guides/decisions) · [Discussion HN](https://news.ycombinator.com/item?id=49984025)
