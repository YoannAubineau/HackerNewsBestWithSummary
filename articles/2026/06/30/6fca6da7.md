---
article_fetched_at: '2026-06-30T14:50:51.373841Z'
attempts: 0
content_source: extracted
discussion_comment_count: 44
discussion_fetched_at: '2026-06-30T14:50:49.587466Z'
error: null
guid: https://news.ycombinator.com/item?id=48722052
hn_item_id: 48722052
hn_url: https://news.ycombinator.com/item?id=48722052
image_url: https://opengraph.githubassets.com/8d13b2221abc9b866b68d78e49a57df2251e8ba34f6270e11e95b52e70308e1a/deepreinforce-ai/Ornith-1
is_ask_or_show_hn: false
llm_input_tokens: 7388
llm_latency_ms: 12654
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 969
our_published_at: '2026-06-30T14:42:01Z'
rewritten_title: 'Ornith-1.0 : modèles open-source auto-améliorants pour le codage
  agentique'
source_published_at: '2026-06-29T17:16:17Z'
status: summarized
summarized_at: '2026-06-30T14:51:10.712981Z'
title: 'Ornith-1.0: self-improving open-source models for agentic coding'
url: https://github.com/deepreinforce-ai/Ornith-1
---

## Résumé de l'article

Ornith-1.0 est une famille de modèles de langage open-source (9B à 397B paramètres) conçue pour le codage agentique et l'automatisation de tâches de développement. Basée sur Gemma 4 et Qwen 3.5, elle utilise un cadre d'apprentissage par renforcement qui optimise conjointement les stratégies de recherche et les solutions générées.

- Quatre variantes de modèles : 9B Dense, 31B Dense, 35B MoE et 397B MoE, avec support d'une fenêtre de contexte de 256K tokens et compatibilité OpenAI
- Performance de pointe sur les benchmarks de codage (Terminal-Bench 2.1, SWE-Bench, NL2Repo, OpenClaw) parmi les modèles open-source de taille comparable
- Architecture à raisonnement explicite avec blocs `<think>` intégrés et support natif des appels d'outils pour les agents de codage
- Licence MIT sans restrictions régionales, déploiement sur vLLM, SGLang, llama.cpp ou Ollama
- Intégration native avec frameworks d'agents standards (OpenHands, OpenClaw) via l'interface OpenAI-compatible

## Discussion sur Hacker News (44 commentaires)

**Avis positifs** :
- Le modèle montre des performances réelles intéressantes en pratique : plus rapide que Qwen 3.6 (jusqu'à 3x), meilleure gestion des tâches de codage agentic, et réduit les boucles de doom-looping comparé aux alternatives
- Acceptation positive dans la communauté locale : premier fine-tune Qwen largement recommandé, offrant des solutions créatives aux problèmes de codage avec un bon compromis qualité/ressources
- L'approche d'apprentissage par renforcement pour générer à la fois les solutions et les harnais spécifiques au problème représente une innovation méthodologique intéressante dans l'entraînement
- Performance compétitive pour son poids : le modèle 35B rivalise avec des modèles plus grands et offre des résultats utiles pour des tâches de codage réelles sur des projets de taille moyenne

**Avis négatifs** :
- Le titre 'self-improving' est trompeur : le modèle ne s'améliore pas à l'usage, c'est uniquement le processus d'entraînement qui utilise l'RL, pas les poids déployés
- Les benchmarks sont suspects : classement incohérent (Kimi K2.6/K2.7 et Gemma 4 mal positionnés), soupçons de 'benchmarking' optimisé et graphiques biaisés favorisant Ornith
- Modèle instable et limité : hallucine beaucoup lors des appels d'outils, échoue sur des tâches plus complexes (implémentations kernel), provient simplement d'un fine-tuning de Qwen/Gemma sans innovation substantielle
- Manque de transparence : le modèle 31B dense annoncé n'existe nulle part, poids et benchmarks manquants, et la provenance exacte (combinaison Qwen + Gemma) reste floue
- Communauté locale saturée par le hype et les marketeurs : beaucoup considèrent ce modèle comme du 'slop', l'accueil réel est mitigé malgré la publicité agressive

**Top commentaires** :

- [CharlesW](https://news.ycombinator.com/item?id=48723122) : Previously: https://news.ycombinator.com/item?id=48709744 https://swelljoe.com/post/will-it-mythos/: "Poor performer here, only found the one bug that almost every model found, despite its performance on other benchmarks being excellent for its size. \[…\] It also performs poorly in a chat without to…
- [lhl](https://news.ycombinator.com/item?id=48732119) : I've been testing Ornith-1.0 35B \(my own FP8-block quant\) and I like it. It runs at \>200 tok/s w/ vLLM on an RTX PRO 6000 \(sm120\), I've run \>140M cached tokens of agentic coding work on it over the past few days. It seems to about somewhere between Qwen 3.6 35B-A3B and 27B, but the good thing: it o…
- [ricardobayes](https://news.ycombinator.com/item?id=48724416) : This is the first Qwen fine-tune that is not immediately rejected by the local LLM community, and in some cases even being recommended. Based on my limited usage, it is good, gives creative solutions to coding problems. I don't expect 9-35B models to one-click create full apps. Most people who were…

---

[Article original](https://github.com/deepreinforce-ai/Ornith-1) · [Discussion HN](https://news.ycombinator.com/item?id=48722052)
