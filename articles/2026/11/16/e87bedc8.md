---
article_fetched_at: '2026-11-16T12:27:35.697653Z'
attempts: 0
content_source: extracted
discussion_comment_count: 257
discussion_fetched_at: '2026-11-16T12:27:31.485699Z'
error: null
guid: https://news.ycombinator.com/item?id=50513215
hn_item_id: 50513215
hn_url: https://news.ycombinator.com/item?id=50513215
image_url: https://img.alicdn.com/imgextra/i4/O1CN01OXv3EM1FN8t9W4P79_!!6000000000474-2-tps-80-80.png
is_ask_or_show_hn: false
llm_input_tokens: 24887
llm_latency_ms: 9846
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 963
our_published_at: '2026-11-16T12:15:31Z'
rewritten_title: Qwen4-Max, modèle IA de Alibaba avec 2,4 trillions de paramètres,
  disponible en accès public
source_published_at: '2026-11-16T02:14:44Z'
status: summarized
summarized_at: '2026-11-16T12:28:48.759374Z'
title: Qwen4-Max
url: https://qwen.ai/blog?id=qwen4-max
---

## Résumé de l'article

Qwen4-Max est un modèle de langage de grande taille développé par Alibaba, construit sur une nouvelle architecture avec 2,4 trillions de paramètres, des capacités visuelles natives et une fenêtre de contexte d'un million de tokens. Il est conçu comme un assistant IA polyvalent pour la productivité professionnelle, la création et la recherche scientifique.

- Réductions de coûts significatives : 24-35% de réduction d'utilisation de tokens sur les benchmarks Work360, et 62% de réduction du coût moyen par tâche (de 4,43$ à 1,67$) comparé à Qwen3.8-Max
- Architectures améliorées comprenant GDN (Gated DeltaNet) + Qwen Sparse Attention (QSA), Gated Residual et N-gram Embedding, permettant une meilleure efficacité computationnelle et stabilité d'entraînement
- Capacités démontrées en 3D/jeux vidéo, conception manufacturière automobile, recherche financière, audit juridique, santé critique et découverte scientifique autonome (design de matériaux et molécules de médicaments)
- Agents 24/7 autonomes avec mode « Live Delivery » permettant des itérations continues et la révision en temps réel par l'utilisateur
- Disponible via QwenCloud (API et Token Plan), ainsi que sur QwenWork, Qoder et QwenStudio

## Discussion sur Hacker News (257 commentaires)

**Avis positifs** :
- L'architecture MoE et les optimisations d'efficacité continuent de progresser, promettant des modèles plus petits (27B, Flash) performants pour l'inférence locale.
- Qwen 4 marque des améliorations significatives par rapport à Qwen 3.8 en codage, workflows agentiques et réduction des hallucinations.
- Les modèles chinois maintiennent une parité compétitive dans les tâches pratiques (codage, traitement d'images) malgré une infrastructure GPU plus limitée.
- L'accès via OpenRouter et des interfaces publiques facilite l'expérimentation sans dépendance vis-à-vis des fournisseurs américains.

**Avis négatifs** :
- Le score AA de 43 est bien en-dessous de la frontière (GPT-6.1 Sol à 46), et l'absence de test multi-niveaux de raisonnement rend la comparaison incomplets pour un jugement équitable.
- Artificial Analysis est suspecté de manquer d'indépendance (financements, ajustements fréquents de méthodologie) et d'avantager systématiquement les modèles Anthropic/OpenAI.
- Le coût API ($3.27 par tâche) reste beaucoup plus élevé que DeepSeek V4.1 Flash ($0.36-0.50), limitant l'attrait commercial malgré les performances brutes.
- Les refus systématiques sur questions historiques sensibles (Dalai-Lama, Tiananmen) et l'absence de support image sur certaines variantes (2.4T) constituent des limitations de déploiement.
- Le décalage s'élargit entre les modèles fermés (accès compute 10× supérieur, améliorations rapides) et les poids ouverts, questionnant la capacité long terme de ces derniers à rester compétitifs.

**Top commentaires** :

- [simonw](https://news.ycombinator.com/item?id=50513837) : Qwen4-Max pelicans at four reasoning efforts \(none, low, high, xhigh\): https://tools.simonwillison.net/markdown-svg-renderer?url=ht... For comparison, here's one I got from Qwen3.8 Max \(at default reasoning effort\): https://simonwillison.net/2026/Jul/20/afraid-of-chinese-mode... This inspired me to…
- [maplet](https://news.ycombinator.com/item?id=50513658) : It scores a 43 on Artificial Analysis with an average cost of $3.27 \[1\]. For reference, GPT-6.1 Sol \(medium\) gets a 46 with an average of $0.36. \[1\]: https://artificialanalysis.ai/models/qwen4-max
- [hauntingseaweed](https://news.ycombinator.com/item?id=50516256) : Anthropic deserves to go bankrupt for trying to ban open-weight/open-source competition. I hope their IPO flops.

---

[Article original](https://qwen.ai/blog?id=qwen4-max) · [Discussion HN](https://news.ycombinator.com/item?id=50513215)
