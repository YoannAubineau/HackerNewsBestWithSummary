---
article_fetched_at: '2026-09-04T00:33:36.709612Z'
attempts: 0
content_source: extracted
discussion_comment_count: 81
discussion_fetched_at: '2026-09-04T00:33:35.764524Z'
error: null
guid: https://news.ycombinator.com/item?id=49551760
hn_item_id: 49551760
hn_url: https://news.ycombinator.com/item?id=49551760
image_url: https://ifm.ai/blog/k2/assets/k2-horizon-social.webp
is_ask_or_show_hn: false
llm_input_tokens: 10569
llm_latency_ms: 13541
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1191
our_published_at: '2026-09-03T23:49:00Z'
rewritten_title: IFM publie K2 Horizon, une flotte de six modèles ouverts de tailles
  variées
source_published_at: '2026-09-03T15:36:43Z'
status: summarized
summarized_at: '2026-09-04T00:33:57.206189Z'
title: 'K2 Horizon: A connected fleet of six open models'
url: https://ifm.ai/blog/k2/
---

## Résumé de l'article

K2 Horizon est une flotte de six modèles de langage ouverts publiée par IFM, allant de 0,9 milliard à 375 milliards de paramètres, conçus comme une famille cohérente partageant architecture, données d'entraînement et infrastructure. Cette publication est remarquable pour son exhaustivité : IFM divulgue l'intégralité du cycle de développement (pré-entraînement, affinage supervisé, post-entraînement, entraînement d'agents), y compris les points de contrôle intermédiaires, les données ou recettes de données, le code, les configurations et les logs détaillés.

- Les modèles 0,9B, 3,7B et 7B atteignent l'état de l'art dans leurs catégories de taille respectives en raisonnement, mathématiques, codage et tâches d'agents ; les modèles 32B et 375B-A23B figurent parmi les meilleurs de leurs classes
- Le modèle 36B-A4B utilise une nouvelle architecture MoVA (Mixture-of-Value Attention) qui applique la spécialisation d'experts à l'attention, activant seulement ~4 milliards de paramètres par jeton pour une performance proche du modèle dense 32B
- La flotte couvre l'ensemble de la chaîne de déploiement, du 0,9B pour les appareils contraints (montres, lunettes) jusqu'au 375B-A23B pour les données-centers d'entreprise
- ~17% du corpus de pré-entraînement (~10 billions de tokens) consiste en trajectoires de raisonnement synthétique ; plus de 100 millions de tâches uniques ont été générées pour le post-entraînement
- Tous les modèles sont sous licence Apache 2.0 avec support immédiat de vLLM, SGLang et Ollama ; les chercheurs peuvent étudier quand les capacités émergent et comment les comportements non intentionnels (reward hacking) apparaissent au fil de l'entraînement grâce aux points de contrôle intermédiaires publiés

## Discussion sur Hacker News (81 commentaires)

**Avis positifs** :
- La publication complète des données d'entraînement, du code et des méthodologies constitue un progrès significatif vers la transparence, contrairement aux modèles fermés où demeurent des doutes sur les manipulations possibles
- Le modèle 7B offre d'excellentes performances et peut s'exécuter sur téléphone, représentant une avancée notable pour les cas d'usage pratiques et l'accessibilité locale
- La pile complètement ouverte, incluant le processus d'entraînement et les données synthétiques, est aussi précieuse que les poids eux-mêmes pour permettre la reproduction et l'amélioration continue
- Cette initiative rejoint les rares autres projets véritablement ouverts comme OLMo, et démontre que le financement d'alternatives réellement ouvertes aux géants fermés est possible
- La disponibilité de ces modèles offre une résilience critique : leur existence locale s'avère précieuse lors des pannes des services fermés

**Avis négatifs** :
- Les modèles 32B et 36B underperforment significativement par rapport aux alternatives comme Qwen 3.8 27B selon les benchmarks, rendant la publication prématurée pour ces tailles
- Les données d'entraînement restent en quantités bien inférieures (dizaines de To contre centaines ou milliers de To pour OpenAI/Anthropic), limitant potentiellement la qualité globale
- Le petit modèle 3.7B montre des faiblesses en programmation avec hallucinations et boucles infinies sur des tâches basiques, ne pouvant être considéré comme fiable pour le code
- L'accès initial au site était verrouillé derrière une authentification et les graphiques manquaient de lisibilité, contredisant le message 'radicalement ouvert' et révélant des lacunes en UX
- La vraie ouverture reste limitée : sans données d'entraînement avec licences permissives et sans résoudre les enjeux de droit d'auteur, l'idéal d'ouverture complète reste techniquement difficile à atteindre

**Top commentaires** :

- [jjordan](https://news.ycombinator.com/item?id=49552578) : Fully open models really need to be a big part of the AI future. That includes all source code, open training data, how it's organized, fed to the model, processed, etc. Until that becomes a thing you're always going to be left wondering what exactly lies underneath the closed model you are using,…
- [a11r](https://news.ycombinator.com/item?id=49553249) : It is great to see another player introduce a fully open stack. Nvidia's Nemotron is the only other prominent one I know of. All that said, the headline claims do not match the self-reported performance. For example, the dense 32B model is significantly behind Qwen3.8 27B \(chart towards the bottom…
- [cogman10](https://news.ycombinator.com/item?id=49555008) : My quick review of the 3.7B model \(because I was interested\) is that it's not to be trusted for coding. It failed my basic test I like to ask models and generated incorrect code. When prompted about the bug, it preceded to start hallucinating non-existent APIs. After doing that it got caught in a l…

---

[Article original](https://ifm.ai/blog/k2/) · [Discussion HN](https://news.ycombinator.com/item?id=49551760)
