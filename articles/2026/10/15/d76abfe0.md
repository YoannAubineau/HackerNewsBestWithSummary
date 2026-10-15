---
article_fetched_at: '2026-10-15T20:45:29.791080Z'
attempts: 0
content_source: extracted
discussion_comment_count: 259
discussion_fetched_at: '2026-10-15T20:45:26.539226Z'
error: null
guid: https://news.ycombinator.com/item?id=50107379
hn_item_id: 50107379
hn_url: https://news.ycombinator.com/item?id=50107379
image_url: https://research.meta.ai/articles/muse-spark-open/social/muse-spark-1-2-open-weights-social-v2.webp
is_ask_or_show_hn: false
llm_input_tokens: 19141
llm_latency_ms: 23751
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1086
our_published_at: '2026-10-15T20:09:59Z'
rewritten_title: Muse Spark Open, un modèle IA open-source de 816 milliards de paramètres,
  est désormais disponible
source_published_at: '2026-10-15T17:47:39Z'
status: summarized
summarized_at: '2026-10-15T20:46:55.324318Z'
title: Muse Spark Open
url: https://research.meta.ai/blog/muse-spark-open
---

## Résumé de l'article

Muse Spark Open est un modèle d'IA multimodal open-source publié par Meta, conçu pour les tâches de codage et le travail agentique. Avec 816 milliards de paramètres (42 milliards actifs) et une fenêtre contextuelle d'1 million de tokens, il peut tourner entièrement sur des ordinateurs de bureau, notamment deux Mac Studio équipés de la puce Apple M5 Ultra.

- Le modèle est optimisé pour l'exécution locale grâce à la version récente du framework MLX d'Apple, offrant une bande passante mémoire de 1,2 To/s pour traiter les inférences
- Il est accessible via plusieurs plateformes API (Together AI, Fireworks, Baseten, Modal, Groq, Nebius, OpenRouter) et les poids peuvent être téléchargés sur Hugging Face, Google Cloud et Amazon SageMaker
- Muse Spark Open supporte de nombreux moteurs d'inférence (vLLM, SGLang, TensorRT-LLM, llama.cpp) avec optimisations pour les architectures AMD, Apple, Intel et NVIDIA
- Le modèle a été soumis à un post-entraînement de sécurité renforcée et respecte le cadre Meta Superintelligence Scaling Framework pour les risques majeurs
- Il est publié sous la licence Muse Model License avec conditions commerciales limitées, permettant à de nombreux développeurs une utilisation gratuite

## Discussion sur Hacker News (259 commentaires)

**Avis positifs** :
- Meta démontre un engagement sérieux envers les modèles open-weight, contrairement à OpenAI et Anthropic, ce qui pourrait établir une standardisation autour de l'infrastructure Meta et réduire les coûts à long terme
- Le modèle bénéficie d'un support multiplateforme impressionnant (Unsloth, MLX, ONNX, etc.), maximisant l'accessibilité comparé aux alternatives propriétaires
- La sortie d'un modèle open-weight par un acteur majeur renforce la concurrence et empêche un seul laboratoire de dominer le marché de l'IA, bénéficiant à l'écosystème global
- Pour les cas d'usage de conversion image-HTML et autres tâches spécialisées, Muse Spark Open obtient des résultats impressionnants parmi les modèles open-weight
- L'application Muse agent connaît un succès massif de téléchargement (numéro 1 sur l'App Store), démontrant une adoption consommateur réelle au-delà des cercles techniques

**Avis négatifs** :
- Le modèle ne s'exécute pratiquement que sur du matériel extrêmement onéreux (deux Mac Studios M5 Ultra coûtant ~$30-50k), rendant absurde l'affirmation que 'l'avenir est pour tous'
- Les performances sont inférieures à Muse Spark 1.3 et 1.2, et comparables ou pires que GLM 5.3 Flash et DeepSeek V4.1 Flash, qui sont eux beaucoup moins exigeants en ressources
- La licence n'est pas véritablement 'open-source' : elle restreint la commercialisation directe du modèle et exige un accord séparé avec Meta pour les entreprises générant plus de 20M$ de revenus
- Meta utilise des définitions marketing gonflées ('le meilleur modèle open-weight US') pour masquer que les modèles chinois sont techniquement supérieurs, et la promotion ressemble à du greenwashing corporatif
- Les affirmations sur la 'stickiness' de Muse sont non fondées : c'est simplement OpenClaw rebrandé sans effets réseau véritables, et les téléchargements massifs initiaux s'effondreront probablement rapidement

**Top commentaires** :

- [a11r](https://news.ycombinator.com/item?id=50108293) : Artificial analysis shows this: underperforming Qwen3.8 Flash Next and GLM 5.3 Flash, both of which you can run on a single B300 . I think Meta has a bit of catching up to do in the open-weight space. As an aside, it's really unfortunate that artificial analysis only provides comparison at the high…
- [seizethecheese](https://news.ycombinator.com/item?id=50108164) : Since there are many comments here arguing that this is not open weight, I looked at the license. Basically, you're free to use this except this clause: \> If the Licensee or any of its affiliates provide a third party with access to artificial intelligence models as a product or service, via API or…
- [armcat](https://news.ycombinator.com/item?id=50107063) : They've done considerable effort in making sure this model can run on basically every model runner, from Unsloth to MLX, https://dev.meta.ai/docs/muse-spark-open/deploy

---

[Article original](https://research.meta.ai/blog/muse-spark-open) · [Discussion HN](https://news.ycombinator.com/item?id=50107379)
