---
article_fetched_at: '2026-06-22T18:22:05.457936Z'
attempts: 0
content_source: extracted
discussion_comment_count: 72
discussion_fetched_at: '2026-06-22T18:22:04.539165Z'
error: null
guid: https://news.ycombinator.com/item?id=48620342
hn_item_id: 48620342
hn_url: https://news.ycombinator.com/item?id=48620342
image_url: https://brandur.org/assets/images/minimum-viable-unit/twitter@2x.jpg
is_ask_or_show_hn: false
llm_input_tokens: 10841
llm_latency_ms: 14841
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1250
our_published_at: '2026-06-22T18:20:13Z'
rewritten_title: Établir le seuil minimal de viabilité commerciale d'un logiciel face
  aux LLM
source_published_at: '2026-06-21T16:41:21Z'
status: summarized
summarized_at: '2026-06-22T18:22:59.342311Z'
title: The minimum viable unit of saleable software
url: https://brandur.org/minimum-viable-unit
---

## Résumé de l'article

L'auteur analyse pourquoi construire un logiciel commercial reste viable malgré les modèles de langage, qui rendent la création interne de solutions logicielles moins coûteuse. Il argumente que certains logiciels commercialisés restent rentables car leur prix, leur complexité et leurs besoins de maintenance dépassent ce qu'il est économiquement sensé de construire en interne avec des LLM.

- Les LLM ont drastiquement réduit le coût initial de développement logiciel, mais n'ont pas éliminé les coûts : il faut toujours des ajustements itératifs et une maintenance continue supervisée par un humain.
- Le calcul économique pour reconstruire en interne dépend du coût annuel du logiciel : un outil à 400 $/mois (comme Jira) ne justifie pas une reconstruction, tandis qu'un produit à 25 000 $/mois (comme Salesforce) peut la rendre rentable.
- L'auteur définit une « zone de viabilité » où un logiciel commercial reste préférable à une reconstruction interne : sa complexité doit justifier l'effort de la réimplémentation LLM, et son prix ne doit pas être exorbitant.
- River, un système de file d'attente de tâches pour Go et PostgreSQL, propose une stratégie freemium (fonctionnalités avancées et facturation réservées à la version Pro) et un tarif de 125 $/mois pour les petites équipes.
- L'auteur reconnaît l'incertitude de cette thèse et parie sa subsistance sur le fait que River se situe au-dessus du seuil minimal de viabilité commerciale.

## Discussion sur Hacker News (72 commentaires)

**Avis positifs** :
- Le calcul buy-vs-build a effectivement changé : pour les grandes dépenses SaaS (ex. Salesforce à 25k€/mois), employer 1,5 ingénieur pour construire une alternative devient économiquement viable, surtout avec les LLM réduisant les coûts de développement.
- En B2B, les vraies entreprises sont de plus en plus disposées à acheter plutôt que construire, ce qui crée une opportunité pour les produits bien conçus ; contrairement aux développeurs individuels qui refusent de payer.
- L'architecture et la conception des API constituent des différentiateurs importants : contrairement aux solutions générées par IA, un produit bien pensé peut se démarquer du « AI slop ».
- Le problème réel n'est pas l'impossibilité de construire, mais la maintenance, les risques de conformité, la redondance des talents et les coûts cachés (intégration, formation, support) qui rendent l'achat souvent plus rationnel à long terme.
- Le framing de l'auteur capture bien un moment donné : les LLM permettent effectivement de construire rapidement des MVP, mais ce qui reste coûteux, c'est la spécification, l'itération et le maintien en production.

**Avis négatifs** :
- Les coûts réels d'un build interne sont largement sous-estimés : chaque ligne de code crée de la complexité, il faut plusieurs ingénieurs (minimum 4) pour maintenir quelque chose de durable, gérer la succession des talents, les sauvegardes, la haute disponibilité et la conformité réglementaire (CCPA/GDPR).
- Construire une alternative Jira, Salesforce ou Google Docs masque l'énorme complexité : ces outils ont été développés par des milliers d'ingénieurs sur plus d'une décennie ; les LLM eux-mêmes refusent souvent ces tâches car ils les reconnaissent comme impossibles à décomposer.
- Le risque organisationnel et politique est réel : personne n'est viré pour avoir choisi Salesforce, mais construire une solution interne expose l'entreprise à des défaillances massives si l'équipe clé part ou disparaît ; les vendeurs existants peuvent aussi baisser leurs prix à tout moment.
- Il manque une analyse des coûts d'opportunité : des ingénieurs talentueux consacrés à des problèmes non-core au lieu de générer du revenu direct est un mauvais arbitrage, même si le build semble moins cher à court terme.
- La bureaucratie interne irrationnelle favorise paradoxalement le buy : on peut dépenser 200k€ en salaire sans sourciller mais bloquer des mois pour approuver une licence SaaS à 400€/mois, créant une distorsion des incitations plutôt qu'une vraie économie.

**Top commentaires** :

- [zingar](https://news.ycombinator.com/item?id=48621636) : I have multiple side projects that I would never have contemplated building before but whose utility now exceeds the much lower cost to build. I got a few weeks in to each and then stalled on all of them because the effort and motivation required to extend beyond the crazed early days \_is\_ still mo…
- [ahamilton454](https://news.ycombinator.com/item?id=48621252) : I like that you point out that the cost to build software is still not 0. And in my expirence it’s further from 0 than I would expect. I often find myself thinking I can rebuild a project \(or usually improve upon an existing one\) in just a few days. And yet when it comes down to making anything wel…
- [xyzzy123](https://news.ycombinator.com/item?id=48627218) : I feel like the build threshold discussed is \_extremely\_ optimistic? \> But does that always hold true? Let’s take the other side for a second by examining a much higher-priced SaaS product. Gemini reports that the price of a fully loaded Salesforce seat is ~$500/mo. Say you need 50 seats, that’s $2…

---

[Article original](https://brandur.org/minimum-viable-unit) · [Discussion HN](https://news.ycombinator.com/item?id=48620342)
