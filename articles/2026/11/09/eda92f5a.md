---
article_fetched_at: '2026-11-09T18:02:52.856118Z'
attempts: 0
content_source: tweet
discussion_comment_count: 286
discussion_fetched_at: '2026-11-09T18:02:42.922812Z'
error: null
guid: https://news.ycombinator.com/item?id=50422069
hn_item_id: 50422069
hn_url: https://news.ycombinator.com/item?id=50422069
image_url: https://pbs.twimg.com/media/HWjhsqYWMAALhKb.jpg?name=orig
is_ask_or_show_hn: false
llm_input_tokens: 18734
llm_latency_ms: 7063
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 555
our_published_at: '2026-11-09T17:53:09Z'
rewritten_title: Opus 5.5 a-t-il été affaibli ? Les modèles de réflexion ont changé
  le 3 novembre
source_published_at: '2026-11-09T07:04:25Z'
status: summarized
summarized_at: '2026-11-09T18:04:09.385906Z'
title: Is Opus 5.5 nerfed? Thinking patterns changed on November 3
url: https://twitter.com/shanemelaugh/status/2119192075505893695
---

## Résumé de l'article

Tweet de @shanemelaugh :

> is Opus 5.5 nerfed?
>
> I just had Gemini 4 Argon analyze 1,400 Claude Code sessions and it found that on November 3, something definitely happened.
>
> the model name didn't change, but the way it does reasoning took a sharp turn.

## Discussion sur Hacker News (286 commentaires)

**Avis positifs** :
- Plusieurs utilisateurs signalent une dégradation observable d'Opus 5.5 depuis novembre 3, avec des erreurs répétitives, des oublis d'étapes et une fiabilité réduite dans les tâches habituelles
- Le timing coïncide souvent avec les préparations de sorties de nouveaux modèles, suggérant une réallocation des ressources de calcul pour les versions futures
- Cette pratique de dégradation silencieuse avant une sortie de nouveau modèle améliore artificiellement la perception de supériorité du nouveau modèle par rapport à l'ancien
- Les utilisateurs demandent plus de transparence et de contrôle : les modèles open-source offrent au moins la certitude et la stabilité, contrairement aux services cloud qui changent sans notification

**Avis négatifs** :
- Aucune dégradation mesurable n'apparaît sur les sites de suivi de performance des modèles ; les réclamations reposent sur des impressions subjectives sans données objectives
- Les ingénieurs d'Anthropic et OpenAI nient procéder à des quantifications discrètes ou remplacer les checkpoints ; la variance observée pourrait refléter les variations naturelles des LLM plutôt qu'une dégradation intentionnelle
- Le biais cognitif humain tend à mémoriser sélectivement les cas où les modèles échouent et à les attribuer à des changements de modèle, alors que la variance existe en permanence
- Les utilisateurs qui font tourner des benchmarks réguliers observent une variance inhérente sans corrélation avec des 'nerfs' supposés ; des tests rigoureux manquent pour valider les allégations
- Les utilisateurs d'Azure ou d'autres fournisseurs hébergés rapportent une capacité inchangée, ce qui contredit l'hypothèse d'une dégradation généralisée du modèle lui-même

**Top commentaires** :

- [PaulKeeble](https://news.ycombinator.com/item?id=50426840) : The local Qwen 3.8 27B might not be anywhere near as smart as Claude's models but I never wake up one morning and wonder if I am part of some test model to see if I will accept something somewhat less capable or not trained as well in the tools I am using day to day. Its also not suddenly going to…
- [benwills](https://news.ycombinator.com/item?id=50422643) : I noticed Fable decline in quality a couple weeks ago. And I've noticed Opus drop over the last week, even after bumping to a default of Extra High reasoning for almost everything. Tonight has been maddening with the kinds of absurd mistakes it's repeatedly making. It's so frustrating. I'm the kind…
- [losvedir](https://news.ycombinator.com/item?id=50426297) : Anyone with evals picking up a real signal? I've learned not to trust "vibes". The only one I'm familiar with testing Opus 5.5 specifically over time is https://github.com/ninjahawk/livenerf and it's not showing anything.

---

[Article original](https://twitter.com/shanemelaugh/status/2119192075505893695) · [Discussion HN](https://news.ycombinator.com/item?id=50422069)
