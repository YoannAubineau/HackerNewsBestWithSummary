---
article_fetched_at: '2026-06-23T17:34:38.547636Z'
attempts: 0
content_source: extracted
discussion_comment_count: 84
discussion_fetched_at: '2026-06-23T17:34:35.549420Z'
error: null
guid: https://news.ycombinator.com/item?id=48643426
hn_item_id: 48643426
hn_url: https://news.ycombinator.com/item?id=48643426
image_url: https://opengraph.githubassets.com/8fadd2c3bece958fc158986a189569fdb49d39475f7fee9b758c82c5acbb2368/baidu/Unlimited-OCR
is_ask_or_show_hn: false
llm_input_tokens: 11013
llm_latency_ms: 17474
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 956
our_published_at: '2026-06-23T17:28:04Z'
rewritten_title: 'Unlimited OCR: modèle de reconnaissance de documents et images sur
  un horizon long'
source_published_at: '2026-06-23T11:35:05Z'
status: summarized
summarized_at: '2026-06-23T17:35:59.781364Z'
title: 'Unlimited OCR: One-Shot Long-Horizon Parsing'
url: https://github.com/baidu/Unlimited-OCR
---

## Résumé de l'article

Unlimited-OCR est un modèle d'intelligence artificielle conçu pour l'extraction et le parsing de texte dans des images de documents et des PDF, capable de traiter des contenus de très grande longueur. Le modèle étend les capacités de Deepseek-OCR et est disponible via Hugging Face et ModelScope.

- Supporte le traitement single-image et multi-page/PDF avec deux configurations : « gundam » (base_size=1024, image_size=640) et « base » (image_size=1024)
- Offre deux modes d'inférence : via transformers Hugging Face directement sur GPU NVIDIA, ou via serveur SGLang compatible avec l'API OpenAI
- Permet le traitement par lot d'images ou de PDF avec contrôle de concurrence (jusqu'à 8 requêtes parallèles testées)
- Requiert Python 3.12.3 + CUDA 12.9 et spécifie des versions précises de torch, transformers, et pymupdf
- Utilise un processeur de logits personnalisé (no_repeat_ngram) et accepte des contextes jusqu'à 32768 tokens

## Discussion sur Hacker News (84 commentaires)

**Avis positifs** :
- Les approches basées sur les LLM avec contexte améliorent significativement la reconnaissance de scripts complexes (CJK, arabe, vietnamien, thaï) où l'OCR traditionnel échoue, et gèrent mieux la variance typographique et les contenus hétérogènes
- L'innovation du Reference Sliding Window Attention résout un problème réel : la croissance linéaire du cache KV rend actuellement les longs documents coûteux en mémoire et nécessite du découpage artificiel des PDF en pages
- Les utilisateurs rapportent des succès concrets avec les modèles de vision (Claude, Mistral) pour transcription à grande échelle de documents complexes, y compris reconnaissance d'écritures manuscrites et gestion contextuelle sophistiquée
- L'approche est modulaire et applicable au-delà de l'OCR : conversations longues, traitement documentaire, et potentiellement génération d'images
- La transparence des chercheurs vis-à-vis de leurs sources d'inspiration (DeepSeek-OCR, PaddleOCR) démontre une pratique scientifique responsable

**Avis négatifs** :
- L'OCR traditionnel reste plus rapide, moins coûteux et plus fiable pour les cas d'usage standards, contrairement aux affirmations de certains commentateurs; les solutions commerciales (Textract, Document Intelligence) sont préférées malgré leurs limitations imprévisibles
- La fenêtre locale de génération (~128 mots) pourrait être insuffisante pour les documents très complexes et riches en tokens (images, tableaux), limitant l'efficacité contextuelle réelle
- Les modèles de vision produisent toujours des artefacts d'hallucination (traductions non désirées, confusions multi-langue) qui les rendent inutilisables en production critique sans post-traitement lourd
- Le problème de la distinction entre reconnaissance certaine et hypothèse contextuelle reste non résolu : il n'y a pas de mécanisme pour signaler quand le modèle fait une supposition plutôt que de lire les caractères effectifs
- Absence de comparaison objective avec les benchmarks établis (Infinity Parser 2, Finereader) et aucune évaluation quantitative rigoureuse permettant d'affirmer la supériorité réelle

**Top commentaires** :

- [robotswantdata](https://news.ycombinator.com/item?id=48643871) : Very interesting. The way I understand this works is that the researchers found a clever architectural hack to stop AI from hoarding memory when reading long documents. Normally, when an AI transcribes a 100 page PDF, it tries to remember every single word it has already ingested. This short-term m…
- [peatmoss](https://news.ycombinator.com/item?id=48644574) : I recently bought a tablet for sheet music, mostly to replace a stack of jazz "Real Books" at jam sessions. And the phone camera scans I made are okay, but fixed in size and have a lot of artifacts. And it would be great to transpose on the fly for e.g. Bb or Eb instruments, but being a scan this i…
- [KitN](https://news.ycombinator.com/item?id=48643958) : "We would like to thank Deepseek-OCR, Deepseek-OCR-2, PaddleOCR for their valuable models and ideas." Class Act.

---

[Article original](https://github.com/baidu/Unlimited-OCR) · [Discussion HN](https://news.ycombinator.com/item?id=48643426)
