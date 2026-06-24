---
article_fetched_at: '2026-06-24T23:24:26.752653Z'
attempts: 0
content_source: extracted
discussion_comment_count: 180
discussion_fetched_at: '2026-06-24T23:24:25.729962Z'
error: null
guid: https://news.ycombinator.com/item?id=48648039
hn_item_id: 48648039
hn_url: https://news.ycombinator.com/item?id=48648039
image_url: https://cdn.sanity.io/images/4zrzovbb/website/b9ba85fd4d8beaf4efe04a4cf6cec14761e52c78-2400x1260.jpg
is_ask_or_show_hn: false
llm_input_tokens: 14066
llm_latency_ms: 9844
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 863
our_published_at: '2026-06-24T23:04:23Z'
rewritten_title: Claude Tag, assistant IA collaboratif pour Slack, disponible en bêta
source_published_at: '2026-06-23T17:09:18Z'
status: summarized
summarized_at: '2026-06-24T23:24:43.115415Z'
title: Claude Tag
url: https://www.anthropic.com/news/introducing-claude-tag
---

## Résumé de l'article

Claude Tag est une nouvelle intégration d'IA développée par Anthropic qui permet aux équipes de travailler avec Claude directement dans Slack. L'assistant peut être mentionné (@Claude) dans les canaux pour accomplir des tâches, accède à des outils et des données configurés par les administrateurs, et se souvient du contexte des conversations au fil du temps.

- Claude Tag fonctionne de manière collaborative et asynchrone : un seul Claude par canal que tous les membres peuvent utiliser, et il peut travailler sur des tâches de façon autonome pendant des heures ou des jours
- L'IA apprend progressivement à partir des informations du canal et peut prendre des initiatives proactives (flagging d'informations pertinentes, suivi des tâches non résolues) si activé
- L'accès aux données et outils est strictement contrôlé par les administrateurs, chaque Claude ayant des identités séparées selon le canal et sans partage de données sensibles entre équipes
- Claude Tag remplace l'application Claude existante pour Slack et est actuellement en bêta pour les clients Claude Enterprise et Team
- Chez Anthropic, 65 % du code produit par l'équipe produit est désormais généré par la version interne de Claude Tag

## Discussion sur Hacker News (180 commentaires)

**Avis positifs** :
- Le modèle collaboratif multiplayer est véritablement innovant : un Claude partagé dans un canal Slack permet à tous les participants de suivre et de reprendre le travail, contrairement aux sessions privées classiques.
- Anthropic démontre une vélocité de mise sur le marché remarquable en étendant son offre au-delà des développeurs vers les équipes métier et l'entreprise, captant des cas d'usage que la concurrence ne couvre pas.
- Le cas d'usage interne d'Anthropic (65% du code produit généré par Claude Tag) montre l'efficacité réelle de l'outil pour des workflows productifs complexes.
- L'intégration native avec des outils d'entreprise (GitHub, Datadog, etc.) via des identités d'agent distinctes offre une flexibilité que les bots génériques ne proposent pas.

**Avis négatifs** :
- Le modèle de sécurité et permissions reste flou et problématique : pas de garantie que les données sensibles ne fuient pas entre canaux, et difficultés à appliquer le principe du moindre privilège dans un contexte multiplayer.
- Slack n'est accessible qu'aux startups et tech companies, tandis que 90% des entreprises utilisent Microsoft Teams, ce qui limite drastiquement le marché réel d'adoption en entreprise.
- L'approche de Slack-only pour une plateforme clé est une erreur stratégique : les produits d'Anthropic manquent d'intégration cohérente (Design, Code, Cowork, Tag en silos) et créent des frictions pour les utilisateurs.
- La facturation basée sur l'usage avec limites de dépense désactivées par défaut favorise l'escalade des coûts en tokens sans que les utilisateurs en aient conscience, contrairement à la transparence des concurrents.

**Top commentaires** :

- [yodon](https://news.ycombinator.com/item?id=48649742) : « Today, 65% of our product team’s code is created by our internal version of Claude Tag. » Yeah, that explains a lot.
- [holografix](https://news.ycombinator.com/item?id=48652360) : Wowza this will be a token guzzler. Assuming Claude is parsing every message posted on multiple slack channels, compacting knowledge etc. Looks like Anthropic is progressing further into platform territory and conquering Agentic use cases left right and centre. If you’re building an agent platform…
- [SweetSoftPillow](https://news.ycombinator.com/item?id=48648503) : The most important difference from other products: \> @Claude is multiplayer. Within a given Slack channel, there’s one Claude that interacts with everyone. This means that anyone can see what it’s working on, and can pick up the conversation from where the last person left off. This makes tagging C…

---

[Article original](https://www.anthropic.com/news/introducing-claude-tag) · [Discussion HN](https://news.ycombinator.com/item?id=48648039)
