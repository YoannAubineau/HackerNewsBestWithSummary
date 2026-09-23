---
article_fetched_at: '2026-09-23T21:54:51.460224Z'
attempts: 0
content_source: extracted
discussion_comment_count: 190
discussion_fetched_at: '2026-09-23T21:54:23.316714Z'
error: null
guid: https://news.ycombinator.com/item?id=49812769
hn_item_id: 49812769
hn_url: https://news.ycombinator.com/item?id=49812769
image_url: https://www.nobodywho.ai/assets/images/blog/2026/jev-in-25-lines/jev.png
is_ask_or_show_hn: false
llm_input_tokens: 15918
llm_latency_ms: 12095
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 989
our_published_at: '2026-09-23T21:28:46Z'
rewritten_title: Implémenter Jev en 25 lignes de Python avec un modèle de langage
  local
source_published_at: '2026-09-23T07:26:23Z'
status: summarized
summarized_at: '2026-09-23T21:57:58.931438Z'
title: Jev in 25 Lines of Python
url: https://www.nobodywho.ai/posts/jev-in-25-lines/
---

## Résumé de l'article

Jev est un modèle de prise de décision qui classe des entrées en assignant des probabilités à des options prédéfinies, sans faire appel à des APIs externes ni entraînement personnalisé. Cet article montre comment implémenter une version minimale de Jev en Python en chargeant un modèle GGUF local, en préparant un prompt avec des choix, puis en convertissant les logits du modèle en probabilités calibrées.

- Charger un modèle GGUF (Qwen3-0.6B utilisé ici) avec la bibliothèque llama-cpp-python et définir les options de classification
- Générer les logits du modèle en lui faisant évaluer le prompt contenant les choix
- Convertir les logits bruts en probabilités logarithmiques puis en probabilités normalisées via softmax
- Le résultat est une classification rapide, locale et sans envoi de données externes (contrairement aux approches basées sur API ou entraînement par renforcement)
- L'implémentation montre que Jev est essentiellement un mécanisme de classification probabiliste fondé sur les tokens finaux du modèle

## Discussion sur Hacker News (190 commentaires)

**Avis positifs** :
- Le concept fondamental est légitime : montrer comment extraire des probabilités fiables à partir de modèles de langage pour des tâches de classification est pédagogiquement valide et aide à démystifier la technologie.
- Les modèles locaux et open-source peuvent accomplir des tâches similaires avec des avantages (latence réduite, coûts nuls, pas de dépendance à une API), notamment Qwen ou Gemma, rendant les approches accessibles.
- Le positionnement du post en tant que parodie légale est approprié et transparent, puisque Jev distingue sa valeur par l'entraînement spécialisé en calibration des probabilités, pas juste par l'architecture.
- Des techniques pratiques pour améliorer les résultats sont confirmées empiriquement : placer les options avant le corps du texte, répéter les instructions et utiliser des sorties structurées améliorent significativement la précision.

**Avis négatifs** :
- L'article omet des éléments critiques : absence de comparaisons de latence, comparaison d'erreurs, évaluation de la conformité du format de sortie et benchmark rigoureux avec Jev sur des métriques standardisées.
- La calibration des probabilités n'est pas triviale pour les LLMs génériques : les logprobs bruts d'un modèle standard ne sont pas calibrés, tandis que Jev revendique une calibration spécialisée après entraînement en RL, une différence qualitative majeure.
- Qwen 0.6B quantifié n'est pas de l'intelligence frontière : réduire Jev à une simple inférence sur un petit modèle quantifié ignore l'effort d'entraînement post-training et les optimisations qui le distinguent du simple appel d'un modèle existant.
- Le problème de fond : des implémentations open-source existantes (Laya, OpenJev) font déjà cela sans hype ; le post trivialise le travail derrière ces systèmes en prétendant que 25 lignes de Python suffisent, ce qui est trompeur.
- Absence de benchmark sur l'exactitude et la généralisation inter-domaines ; les modèles LLM utilisés ne sont généralement pas optimisés pour la classification et échouent sur les cas ambigus, ce que les réducteurs du problème ne testent pas.

**Top commentaires** :

- [sigmoid10](https://news.ycombinator.com/item?id=49813052) : Going directly for the logprobs is always icky when you use a chat model as base, because they are trained to write prose as output. So your "choice" tokens and thus their probabilities might get diluted in whatever else it wanted to say. If you have to do it in the same way as this post, at least…
- [antirez](https://news.ycombinator.com/item?id=49813417) : Because of masked attention in LLMs, if you put the options before the body \(the email to analyze\), the transformer already knows what it needs to look for, and can use more tokens to create state to address that specific task \(BERT has no mask in the attention, so tokens attend also to next tokens…
- [iamflimflam1](https://news.ycombinator.com/item?id=49822726) : The number of - “I did/invented Jev last year”, or, “here’s a version of Jev I vibed up last night” is getting a bit ridiculous. Especially ridiculous is how the hacker news crowd seems to be taking these at face value… There was one the other day with a compelling demo. But when you looked closely…

---

[Article original](https://www.nobodywho.ai/posts/jev-in-25-lines/) · [Discussion HN](https://news.ycombinator.com/item?id=49812769)
