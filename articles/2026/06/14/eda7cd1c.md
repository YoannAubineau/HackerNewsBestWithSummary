---
article_fetched_at: '2026-06-14T10:57:33.400038Z'
attempts: 0
content_source: extracted
discussion_comment_count: 87
discussion_fetched_at: '2026-06-14T10:57:32.567287Z'
error: null
guid: https://news.ycombinator.com/item?id=48515454
hn_item_id: 48515454
hn_url: https://news.ycombinator.com/item?id=48515454
is_ask_or_show_hn: false
llm_input_tokens: 11928
llm_latency_ms: 11566
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1004
our_published_at: '2026-06-14T10:47:04Z'
rewritten_title: Configuration dual GPU RTX 5080 et RTX 3090 pour atteindre 80 tokens
  par seconde avec Qwen 3.6 Q8
source_published_at: '2026-06-13T09:55:32Z'
status: summarized
summarized_at: '2026-06-14T10:57:51.468210Z'
title: 'RTX 5080 and RTX 3090 Setup: 80 Tok/s on Qwen 3.6 27B Q8'
url: https://imil.net/blog/posts/2026/rtx-5080-+-rtx-3090-setup-80+-tok-s-on-qwen-3.6-27b-q8/
---

## Résumé de l'article

Guide technique complet pour configurer deux cartes graphiques NVIDIA (RTX 5080 et RTX 3090) en parallèle sur une même machine afin d'exécuter localement le modèle de langage Qwen 3.6 quantifié en Q8, atteignant 80+ tokens/seconde.

- Configuration matérielle requise : carte mère Asus Prime X570-Pro (pour split PCIe 16x en 2x8), DDR4, SSD, et câble riser PCIe 4 de qualité pour la RTX 5080
- Configuration BIOS critique : désactiver CSM, activer Above 4G Decoding et ReSize BAR Support, configurer les deux slots PCIe en Gen 4
- Installation du driver NVIDIA : utiliser nvidia-open driver pour cartes de générations différentes (Ampere RTX 3090 et Blackwell RTX 5080), configuration kernel avec support des deux architectures (86 et 120)
- Optimisations llama.cpp : utiliser quantization Q8 pour le cache KV, spéculative decoding multi-GPU (MTP), allocation 2/3 cartes, contexte 229k tokens
- Performance atteinte : 80-91 tokens/seconde selon la tâche avec taux d'acceptation des drafts de 77%

## Discussion sur Hacker News (87 commentaires)

**Avis positifs** :
- Les modèles open-source comme Qwen 3.6 27B offrent des performances suffisantes pour de nombreuses tâches (codage, exploration), avec des modes d'échec plus simples et plus lisibles que les modèles propriétaires, facilitant la maintenance du code généré
- L'inférence locale garantit la confidentialité, le contrôle total (logprobs, samplers, fine-tuning), et l'indépendance vis-à-vis des conditions commerciales changeantes et des régulations potentielles sur l'utilisation des LLM
- Avec les optimisations récentes (MTP, speculative decoding), les performances locales se rapprochent ou égalent celles des services cloud, tandis que le coût électrique reste prévisible et amortissable sur plusieurs années
- La richesse de la communauté (Hugging Face, llama.cpp, Discord) produit des guides, des modèles quantifiés optimisés et des harnesses (Pi, OpenCode) permettant d'améliorer considérablement la performance des modèles locaux

**Avis négatifs** :
- L'article manque d'analyse théorique sur les divisions optimales de charge, la bande passante mémoire réelle atteinte et les problèmes de pilotes existants ; la bande passante observée (720 GB/s vs 936 GB/s théorique) suggère une marge d'amélioration substantielle non exploitée
- L'investissement initial (2000+ euros pour le matériel, électricité continue) et le coût électrique (1kW consommé) rendent cette approche non compétitive face aux services cloud (~3$/1M tokens) en Californie, même sur plusieurs années
- Les modèles locaux demeurent nettement inférieurs pour les tâches complexes, non-triviales et les chaînes de raisonnement longues (CoT) ; les grands modèles propriétaires conservent un avantage substantiel malgré le bruit de marché autour des performances des petits modèles
- La complexité du stack logiciel (compatibilité des drivers, versioning de llama.cpp, instabilité des dépôts) et les bruit/chaleur générés constituent des obstacles pratiques non négligeables pour un usage de hobby durable

**Top commentaires** :

- [sieste](https://news.ycombinator.com/item?id=48518481) : That's almost exactly my setup and I'm very happy with its performance. I noticed recently that I started to prefer my local Qwen3.6 35B A3B and pi agent over Claude Code. Both fail at different tasks, and Qwen more so than Claude. But the way Qwen fails is much more straightforward. In writing tas…
- [DiabloD3](https://news.ycombinator.com/item?id=48521025) : The recommended values for Qwen 3.6 in thinking mode is \`--temp 1.0 --top-p 0.95 --top-k 20 --min-p 0.00\`, and \`--temp 0.6 --top-p 0.95 --top-k 20 --min-p 0.00\` for coding/tool calling tasks, and for non-thinking, \`--temp 0.7 -top-p 0.8 --top-k 20 --presence-penalty 1.5 --min-p 0.00\`. The options l…
- [ydj](https://news.ycombinator.com/item?id=48518772) : 80tp/s with 5080 3090 combo is wild. I’ve been working with a 4090 and two Tenstorrent p150 cards, and manage only about 30 tps utilizing all three for qwen3.6 27b q8. Guess I got more optimization to do. Would like to see the perf of their setup with and without mtp and ngram speculative decoding…

---

[Article original](https://imil.net/blog/posts/2026/rtx-5080-+-rtx-3090-setup-80+-tok-s-on-qwen-3.6-27b-q8/) · [Discussion HN](https://news.ycombinator.com/item?id=48515454)
