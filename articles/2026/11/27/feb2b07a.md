---
article_fetched_at: '2026-11-27T01:19:16.466744Z'
attempts: 0
content_source: extracted
discussion_comment_count: 254
discussion_fetched_at: '2026-11-27T01:19:14.225442Z'
error: null
guid: https://news.ycombinator.com/item?id=50652527
hn_item_id: 50652527
hn_url: https://news.ycombinator.com/item?id=50652527
is_ask_or_show_hn: false
llm_input_tokens: 19951
llm_latency_ms: 8587
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1014
our_published_at: '2026-11-27T00:50:27Z'
rewritten_title: OpenAI réduit les coûts de ses modèles Astra et Sol au détriment
  de la performance
source_published_at: '2026-11-26T07:33:12Z'
status: summarized
summarized_at: '2026-11-27T01:20:28.502177Z'
title: OpenAI may be in cost control mode
url: https://micjm.com/blog/openai-is-in-cost-control-mode/
---

## Résumé de l'article

OpenAI a apparemment optimisé ses modèles Astra 6.2 et Sol 6.2 pour réduire les coûts d'exploitation. L'analyse des données montre une diminution significative des tokens de raisonnement et des tokens de sortie par rapport aux versions précédentes, ce qui entraîne une baisse de la qualité des réponses.

- Les modèles Astra 6.2 et Sol 6.2 consomment moins de tokens de raisonnement et de tokens de sortie que leurs prédécesseurs, selon l'analyse comparative
- Les réductions sont statistiquement significatives (p-value de 0,0055 pour Sol et 0,022 pour Astra sur la sortie ; p-value de 0,00013 pour Sol et 0,0064 pour Astra sur le raisonnement)
- Ces changements positionnent les nouveaux modèles comme des « sous-penseurs » comparés à leurs concurrents, ce qui se traduit par une performance inférieure mesurée par les scores Elo
- Les réceptions initiales de ces versions ont été négatives, reflétant probablement cette baisse de qualité liée aux économies de coûts

## Discussion sur Hacker News (254 commentaires)

**Avis positifs** :
- OpenAI optimise ses modèles pour le rapport coût/performance, ce qui peut être justifié dans un marché compétitif où les entreprises surveillent étroitement les benchmarks de rentabilité.
- La réduction des tokens de sortie et de raisonnement peut refléter une meilleure efficacité plutôt qu'une dégradation : un modèle plus intelligent atteint ses conclusions avec moins de détours.
- Les cycles d'optimisation des coûts suivis de croissance sont naturels dans le développement logiciel et l'évolution technologique, comparables à l'élagage dans un jardin.
- Plusieurs commentateurs rapportent que certains modèles OpenAI (notamment Astra 6.2) surpassent Claude dans des tâches spécifiques comme le développement web ou le codage structuré.
- Le contrôle des coûts est nécessaire pour construire une entreprise durable, et OpenAI doit devenir rentable avant une introduction en bourse.

**Avis négatifs** :
- Sol 6.2 affiche une dégradation catastrophique des performances en coding : seulement 73 victoires sur 213 batailles contre des modèles nettement plus faibles (DeepSeek, Qwen), ce qui dépasse largement l'optimisation de coûts raisonnable.
- Le timing suspect (sortie rapide d'Astra 6.2 contre l'IPO d'Anthropic) et les problèmes de facturation (OpenAI a dû reconnaître une surcharge de 20%) suggèrent une gestion chaotique plutôt qu'une stratégie délibérée.
- Les données de rentabilité réelle (AgentDuel) contredisent les benchmarks marketing : Claude domine 65-83% de la courbe de Pareto tandis qu'aucun modèle OpenAI n'y apparaît, remettant en question les affirmations de supériorité.
- L'expérience utilisateur s'est dégradée notablement : les modèles génèrent du code illisible (aucune ligne vide, variables mal nommées) et se comportent « paresseusement » en interrompant les sessions longues.
- OpenAI perd du talent vers Anthropic et a échoué à lever les 30 milliards prévus (n'en obtenant que 15), signalant une perte de confiance du marché malgré les affirmations de santé financière.

**Top commentaires** :

- [stillpointlab](https://news.ycombinator.com/item?id=50659214) : Hard to say how concerning this is. I've been thinking about software dev like gardening to try to wrap my head around what this transition to agent-centric dev has meant. In a tortured analogy, agent-centric dev feels like having fertilizer and now all of a sudden my garden is heavily over-grown a…
- [torginus](https://news.ycombinator.com/item?id=50660438) : Personally I wouldn't read too deeply into this. Astra 6.2 was a timed release, scheduled to go against the ANT IPO. The model might be undercooked. They really look like they went for cost savings, and they probably gave up some performance in exchange, even though they might've improved on their…
- [ac29](https://news.ycombinator.com/item?id=50659291) : The most obvious explanation is that they are tuning to be on the pareto frontier of cost/intelligence on benchmarks. If those benchmarks are good enough proxies for the work you're doing and you're paying API rates, its a compelling place to be

---

[Article original](https://micjm.com/blog/openai-is-in-cost-control-mode/) · [Discussion HN](https://news.ycombinator.com/item?id=50652527)
