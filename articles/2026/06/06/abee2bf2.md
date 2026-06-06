---
article_fetched_at: '2026-06-06T00:33:36.488200Z'
attempts: 0
content_source: extracted
discussion_comment_count: 81
discussion_fetched_at: '2026-06-06T00:33:35.959579Z'
error: null
guid: https://news.ycombinator.com/item?id=48414653
hn_item_id: 48414653
hn_url: https://news.ycombinator.com/item?id=48414653
image_url: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Hero_Visual_Blog.width-1300.png
is_ask_or_show_hn: false
llm_input_tokens: 8896
llm_latency_ms: 13683
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1139
our_published_at: '2026-06-06T00:24:03Z'
rewritten_title: Google lance les modèles Gemma 4 QAT pour compression optimisée sur
  appareils mobiles et ordinateurs
source_published_at: '2026-06-05T16:18:48Z'
status: summarized
summarized_at: '2026-06-06T00:33:56.609702Z'
title: 'Gemma 4 QAT models: Optimizing compression for mobile and laptop efficiency'
url: https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/
---

## Résumé de l'article

Google a publié de nouveaux checkpoints de Gemma 4 (modèle de langage open-source) optimisés avec la Quantization-Aware Training (QAT) pour réduire l'empreinte mémoire tout en préservant la qualité. Cette approche simule la quantization pendant l'entraînement, minimisant la perte de performance comparée à la quantization post-entraînement standard.

- Deux formats de quantization disponibles : Q4_0 (populaire) et un format mobile spécialisé réduisant le modèle Gemma 4 E2B à moins de 1 GB
- Optimisations mobiles incluent activations statiques précalculées, quantization par canal, compression 2-bit des couches génératrices de tokens, et optimisation du cache KV
- Les poids sont accessibles immédiatement sur Hugging Face en formats GGUF et Tensors comprimés pour diverses intégrations
- Support intégré avec llama.cpp, Ollama, LM Studio, vLLM, SGLang, MLX et Transformers.js pour déploiement local et edge
- Possibilité de déployer uniquement les modalités nécessaires (texte seul, sans encodeurs audio/vision) pour réduire davantage l'usage mémoire

## Discussion sur Hacker News (81 commentaires)

**Avis positifs** :
- Les modèles QAT quantifiés (notamment Q4_0) offrent une compression efficace : Gemma 4 12B tient en 6.7GB VRAM, permettant l'exécution sur du matériel grand public (laptops 16GB, téléphones haut de gamme)
- La formation avec quantization-aware training (QAT) réduit significativement la perte de précision comparé aux quantifications post-entraînement simples, tout en maintenant une accuracy proche du modèle non quantifié
- L'écosystème s'accélère rapidement : les modèles QAT multitoken prediction (MTP), GGUFs pour llama.cpp, et intégrations via Unsloth Studio/LM Studio facilitent l'adoption locale et réduisent les coûts cloud
- Les petits modèles (2B-31B) offrent un excellent rapport performance/ressources pour des tâches spécifiques : extraction JSON structurée, recherche web, navigation d'interface, sans requérir des modèles frontier à coûts élevés
- Les démonstrations fonctionnelles montrent une viabilité réelle : multimodal (texte, image, audio), exécution rapide sur Mac/Linux avec seulement quelques GB, et résultats pratico-pratiques pour l'automatisation et les agents locaux

**Avis négatifs** :
- La fragmentation des releases est confuse et génère du travail de maintenance inutile : quatre lancements en trois semaines (2B/4B/E3B/31B, variantes assistant/MTP drafter, 12B, QAT) sans support cohérent dans llama.cpp et les applications locales
- Les petits modèles ont des limitations factuelles sévères : hallucinations impossibles (données météo incohérentes), erreurs massives sur des faits historiques simples, besoin d'agents grondés sur le web pour la fiabilité, ce qui limite l'utilité hors de cas très spécifiques
- Les modèles E2B/E4B se montrent peu fiables pour les agents avec outils : boucles infinies, nécessité d'instructions très spécifiques, mauvaise implémentation des web search tools dans Edge Gallery sur Android, malgré la qualité sur desktop
- Les revendications de Google sur la compatibilité matérielle sont inexactes : Edge Gallery Mac indique Gemma 4 12B non supporté sur 16GB RAM alors que la version quantifiée devrait théoriquement tenir, et le manque de GGUF officiels crée des frictions
- Les petits modèles restent inadéquats pour des tâches complexes : même avec prompts optimisés et retry logic, la performance ne se rapproche pas des modèles frontier pour la plupart des cas réels (sauf automatisation très spécifique ou recommandations simples)

**Top commentaires** :

- [simonw](https://news.ycombinator.com/item?id=48416486) : I just ran one of these locally on a Mac like this: uvx litert-lm run \\ --from-huggingface-repo=litert-community/gemma-4-E2B-it-litert-lm \\ gemma-4-E2B-it.litertlm \\ --backend=gpu \\ --prompt="Generate an SVG of a pelican riding a bicycle" The first time you run that it downloads 3.2GB to ~/.cache/h…
- [satvikpendem](https://news.ycombinator.com/item?id=48415688) : Unsloth's collection as well \[0\], with their results \[1\]. Looks like they can get very close to 100% accuracy compared to the BF16 model that is unquantized, and Unsloth's quants are better than the original Google's QAT as posted in the article. Personal I'm using the 2B model for web search and s…
- [jbarrow](https://news.ycombinator.com/item?id=48417969) : Very impressed with how much the Gemma ecosystem has advanced just this week. Gemma 12B, multitoken prediction, and official quants released. Feels like Google is putting real effort into this string of releases, and I'm very excited to see that!

---

[Article original](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/) · [Discussion HN](https://news.ycombinator.com/item?id=48414653)
