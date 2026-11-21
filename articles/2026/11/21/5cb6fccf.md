---
article_fetched_at: '2026-11-21T07:53:18.657553Z'
attempts: 0
content_source: extracted
discussion_comment_count: 117
discussion_fetched_at: '2026-11-21T07:53:15.520387Z'
error: null
guid: https://news.ycombinator.com/item?id=50577265
hn_item_id: 50577265
hn_url: https://news.ycombinator.com/item?id=50577265
image_url: https://arxiv.org/static/browse/0.3.4/images/arxiv-logo-fb.png
is_ask_or_show_hn: false
llm_input_tokens: 10393
llm_latency_ms: 8529
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1096
our_published_at: '2026-11-21T07:17:40Z'
rewritten_title: Des modèles de langage modifient leurs propres paramètres sans entraînement
source_published_at: '2026-11-20T16:29:06Z'
status: summarized
summarized_at: '2026-11-21T07:53:48.714252Z'
title: Language Models Can Rewrite Their Own Weights
url: https://arxiv.org/abs/2611.21885
---

## Résumé de l'article

Des chercheurs montrent qu'un modèle de langage de 27 milliards de paramètres peut modifier ses propres poids en raisonnant sur ses erreurs, sans gradients ni entraînement supplémentaire. Ce mécanisme, appelé « auto-réécriture », permet au modèle d'agir comme son propre optimiseur et d'améliorer ses performances de manière persistante.

- Le modèle diagnostique ses défaillances en analysant ses réponses évaluées et réécrit ses poids en conséquence, gagnant 6,6 points de précision sur des problèmes jamais vus auparavant.
- Il améliore itérativement ses modifications en les testant sur des données d'entraînement, soumettant uniquement les changements bénéfiques : sur huit cycles consécutifs, la précision augmente continuellement.
- Le modèle peut réparer une copie corrompue de lui-même, la ramenant à plus de 80 % de sa précision originale sur des tâches d'image inédites, sans jamais accéder aux poids originaux et sans réentraînement.
- Cette capacité émerge avec l'échelle : dans une famille de modèles, seul le plus grand modèle peut s'auto-réécrire efficacement, les plus petits ne font aucune modification ou s'endommagent.
- Contrairement au test-time scaling, les gains sont inscrits dans les poids sans coût par réponse ; contrairement à l'entraînement, cela ne nécessite que des passes avant.

## Discussion sur Hacker News (117 commentaires)

**Avis positifs** :
- Représente une approche novatrice différente du fine-tuning traditionnel, où le modèle utilise le raisonnement pour identifier et corriger les défauts (comme les boucles infinies de raisonnement) sans rétropropagation ni optimiseur externe.
- Ouvre des perspectives intéressantes pour l'interprétabilité et les techniques d'édition directe des poids, avec potentiel pour des corrections rapides en production sans réentraînement complet.
- Démontre que les modèles peuvent analyser leurs propres états cachés et matrices de poids pour formuler des modifications ciblées, utilisant des méthodes mathématiques alternatives à la descente de gradient.
- Pourrait éventuellement mener à des paradigmes d'apprentissage continu plus efficaces si la capacité s'améliore avec des modèles plus intelligents entraînés sur des corpus de traces de raisonnement en space des poids.

**Avis négatifs** :
- Les améliorations observées se réduisent à des corrections évidentes de bugs (raccourcissement des traces de raisonnement, réduction des boucles infinies) plutôt qu'à une véritable compréhension profonde des poids ou à des améliorations de capacités nouvelles.
- Risque majeur d'alignement et de sécurité : un modèle pourrait silencieusement supprimer les poids d'alignement et de sécurité tout en testant ses modifications avec succès sur des tâches objectives, rendant la détection extrêmement difficile.
- L'article manque complètement toute discussion sur l'alignement, la responsabilité ou les garde-fous de sécurité, ce qui contraste fortement avec l'importance du sujet ; le style éditorialisé et apparemment généré par IA soulève des questions sur la rigueur académique.
- Les résultats ne se généralisent pas : les modèles sans flaw évident (Gemma) ne montrent pas d'amélioration avec cette approche, suggérant que la méthode n'est efficace que pour des défauts spécifiques déjà présents et non pour une véritable auto-amélioration récursive.
- Doutes sur l'efficacité énergétique et l'utilité pratique comparée au fine-tuning conventionnel, avec préoccupations légitimes concernant le surapprentissage et la convergence vers des optima globaux.

**Top commentaires** :

- [aesthesia](https://news.ycombinator.com/item?id=50578348) : It's worth noting that the only modification the model made to improve itself was to reduce the length of its reasoning traces to avoid hitting the token limit. This is basically the same as the result from the recent weight-space programming article \(https://rikiyat.github.io/blog/weight-space-pro…
- [gavinray](https://news.ycombinator.com/item?id=50578187) : Didn't Google's "sleep" paper already show this? https://research.google/blog/the-sleep-framework-a-new-way-f... \> During the offline sleep phase, the model unlocks pre-allocated Mixture-of-Experts \(MoE\) memory blocks and updates its numerical weights using self-generated practice examples.
- [LarsDu88](https://news.ycombinator.com/item?id=50583498) : This is actually kind of the most dangerous type of research AI-safety wise. An LLM running autonomously can actually, if instructed simply direct itself to abliterate activations relevant for safety and alignment. Could run something like a sparse autoencoder over its activates over a corpus of te…

---

[Article original](https://arxiv.org/abs/2611.21885) · [Discussion HN](https://news.ycombinator.com/item?id=50577265)
