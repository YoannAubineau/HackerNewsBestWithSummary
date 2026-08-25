---
article_fetched_at: '2026-08-25T18:25:56.671935Z'
attempts: 0
content_source: extracted
discussion_comment_count: 116
discussion_fetched_at: '2026-08-25T18:25:50.061799Z'
error: null
guid: https://news.ycombinator.com/item?id=49432317
hn_item_id: 49432317
hn_url: https://news.ycombinator.com/item?id=49432317
image_url: https://cdn.modelscope.cn/social-thumbnails/models/Qwen/Qwen3.8-Flash-Next.png
is_ask_or_show_hn: false
llm_input_tokens: 9630
llm_latency_ms: 10919
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 961
our_published_at: '2026-08-25T17:37:35Z'
rewritten_title: Qwen3.8-Flash-Next, modèle multimodal MoE, sera lancé le 26 août
  2026
source_published_at: '2026-08-25T11:49:43Z'
status: summarized
summarized_at: '2026-08-25T18:26:14.998872Z'
title: Qwen 3.8-Flash-Next releasing tomorrow (125B a6B)
url: https://modelscope.cn/models/Qwen/Qwen3.8-Flash-Next
---

## Résumé de l'article

Qwen3.8-Flash-Next est un modèle multimodal basé sur l'architecture de nouvelle génération Qwen4, proposé par Alibaba sur la plateforme ModelScope. Le modèle sera publié en accès ouvert le 26 août 2026 à 15h00 UTC.

- Qwen3.8-Flash-Next utilise une architecture MoE (Mixture of Experts) conçue pour offrir des performances rapides
- Deux versions seront mises à disposition : Qwen3.8-Flash-Next et Qwen3.8-Flash-Next-FP8 (quantifiée)
- Ce lancement anticipé vise à préparer la communauté pour la future famille de modèles Qwen4
- Le modèle sera accessible gratuitement sur la page ModelScope une fois publié

## Discussion sur Hacker News (116 commentaires)

**Avis positifs** :
- Alibaba/Qwen démontre une innovation impressionnante avec une architecture MoE efficace (125B/6B actifs) capable de rivaliser avec les modèles denses bien plus petits en termes de capacités réelles, notamment en codage.
- Le modèle ouvre l'accès local aux utilisateurs avec du matériel grand public (128GB Strix Halo, Mac Studio, DGX Spark), représentant un tournant vers l'IA locale viable pour les workflows sans dépendre d'OpenAI/Anthropic.
- Cette sortie de prévisualisation de Qwen 3.8-Flash-Next permet aux communautés et aux frameworks d'inférence d'optimiser le support des architectures MoE avant la sortie complète de Qwen 4, bénéficiant à tous.
- Les performances rapportées (40-80 tok/s sur Strix Halo estimés, 500+ tok/s sur 5090) suggèrent des vitesses pratiques pour les tâches interactives et autonomes, notamment supérieures à Qwen 3.8-27B dense.
- L'utilisation intelligente de la géométrie MoE (√(125×6) ≈ 27B équivalent) offre un bon équilibre entre capacité cognitive et efficacité d'exécution sur du matériel limité.

**Avis négatifs** :
- Le modèle cible principalement les appareils haute-gamme (128GB+), laissant les utilisateurs avec 64GB (M1/M2 Max, configurations standard) sans options satisfaisantes et déçus de l'absence de 35B dense attendu.
- Les problèmes de préfill persistants sur Strix Halo (~300 tok/s) rendent l'utilisation interactive pénible malgré de bons temps de génération, limitant l'utilité pour les agents et le codage.
- Les frameworks d'inférence (llama.cpp, etc.) manquent encore d'optimisations critiques pour les MoE (pas de cache dynamique d'experts GPU natif selon les RFC), rendant les performances réelles incertaines.
- OpenRouter et autres fournisseurs d'inférence API souffrent de capacité insuffisante et de fiabilité pour les modèles Qwen, poussant les utilisateurs vers l'autohébergement sans service intermédiaire viable.
- Les modèles Qwen 3.8 montrent des problèmes de « doute de soi » nécessitant du prompt engineering supplémentaire, et des dégradations importantes en quantification 4-bit selon les retours utilisateurs.

**Top commentaires** :

- [SwellJoe](https://news.ycombinator.com/item?id=49435021) : Finally, a reason to own a 128GB Strix Halo or GB10 device. Or a reason to consider the new Mac Studio. I have a Strix Halo and dual 32GB GPUs in my desktop, and the latter is pretty much always better for running local models because it's quite a bit faster due to higher memory bandwidth. There si…
- [ddtaylor](https://news.ycombinator.com/item?id=49433980) : I enjoy the Qwen models a lot, but building things on top of them with OpenRouter has been painful. OpenRouter does a lot of great work and I really enjoy being able to use different models so easily. I like when a provider is phasing out an older model that still works for my needs and the price i…
- [notnullorvoid](https://news.ycombinator.com/item?id=49434580) : It will be interesting to see the intersection of this with inference engines like FreeToken which improve distribution of work for MoE models across CPU/RAM and GPU/VRAM. If all it takes for a competitive model to run locally at good speeds is a used 3090 and some DDR4, then we might be in for the…

---

[Article original](https://modelscope.cn/models/Qwen/Qwen3.8-Flash-Next) · [Discussion HN](https://news.ycombinator.com/item?id=49432317)
