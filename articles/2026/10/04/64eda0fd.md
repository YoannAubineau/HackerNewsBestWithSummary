---
article_fetched_at: '2026-10-04T06:32:41.945398Z'
attempts: 0
content_source: extracted
discussion_comment_count: 26
discussion_fetched_at: '2026-10-04T06:32:38.080319Z'
error: null
guid: https://news.ycombinator.com/item?id=49946895
hn_item_id: 49946895
hn_url: https://news.ycombinator.com/item?id=49946895
image_url: https://www.phoronix.net/image.php?id=2026&image=timur
is_ask_or_show_hn: false
llm_input_tokens: 3302
llm_latency_ms: 8536
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 859
our_published_at: '2026-10-04T06:31:58Z'
rewritten_title: Timur Kristóf de Valve améliore les anciens GPU AMD sur Linux avec
  le driver AMDGPU
source_published_at: '2026-10-03T19:14:48Z'
status: summarized
summarized_at: '2026-10-04T06:33:16.751653Z'
title: The work by Valve's Timur Kristóf on improving old AMD GPUs on Linux
url: https://www.phoronix.com/news/XDC-2026-Valve-Timur-AMDGPU
---

## Résumé de l'article

Timur Kristóf, ingénieur chez Valve, a réalisé un travail majeur de migration des anciennes cartes graphiques AMD GCN 1.0/1.1 du driver Radeon hérité vers le driver noyau AMDGPU moderne, débloquant l'accès au driver Vulkan RADV et améliorant significativement les performances et les fonctionnalités.

- Migration des GPU AMD Legacy Radeon vers AMDGPU, permettant l'utilisation du driver RADV Vulkan et apportant une amélioration de performance d'environ 30% (Linux 6.19)
- Correction de défauts dans le code d'affichage AMDGPU et résolution de problèmes de gestion de l'énergie pour ces cartes graphiques anciennes
- Ajout du support du soft reset et autres améliorations pour rendre ces GPU plus viables pour le jeu Linux en 2026 et au-delà
- AMD n'ayant pas consacré beaucoup de ressources à ces améliorations, Timur a comblé ce manque au sein de l'équipe Linux de Valve
- Présentation XDC2026 disponible avec diapositives PDF détaillant son expérience et offrant des conseils pour contribuer au développement du driver AMD open-source

## Discussion sur Hacker News (26 commentaires)

**Avis positifs** :
- L'optimisation de vieux matériel AMD par Valve/Timur Kristóf permet de donner une seconde vie à des cartes graphiques obsolètes pour des usages variés (encodage vidéo, post-traitement, machines virtuelles, GPGPU)
- Les performances sous Linux avec des GPUs anciens RDNA 2 et antérieurs sont impressionnantes, notamment grâce au travail sur les pilotes Mesa, et rivalisent ou surpassent celles sous Windows
- Nvidia abandonnerait graduellement le support des anciennes cartes, tandis que AMD/Mesa continuent à les supporter, ce qui démontre l'engagement d'AMD envers la compatibilité retroactive
- Le travail de Valve sur les drivers bénéficie largement à l'écosystème au-delà du Steam Deck, permettant à des outils comme Llama.cpp et GGML d'être plus efficaces

**Avis négatifs** :
- Les vieux GPUs manquent des capacités matérielles critiques (FP4/FP8) et de mémoire suffisante, limitant sérieusement leur viabilité pour l'inférence LLM moderne comparé aux solutions gratuites en ligne
- Les améliorations incrémentielles ne suffiront pas : il faudrait une innovation architecturale majeure pour que ces anciennes cartes soient vraiment utiles pour des tâches exigeantes, ce qui n'est pas à l'horizon
- AMD n'investit pas suffisamment en ingénierie dédiée comparé à Nvidia, qui a tiré des bénéfices massifs (estimés en centaines de milliards) de son support matériel universel grâce au crypto et à l'IA

**Top commentaires** :

- [LaurensBER](https://news.ycombinator.com/item?id=49948486) : I just bought a used Ayaneo 2 handheld, it has an old\(er\) mobile RDNA 2 GPU and I was blown away by how well this thing performed under Linux. Almost everything \(that's not a recent AAA game\) runs beautiful and a lot faster/smoother than it does under Windows. The experience has been so good that I…
- [gary\_0](https://news.ycombinator.com/item?id=49949075) : Direct link to the talk, with timestamp: https://youtu.be/j5W5ErEMnvM?t=21385
- [bugake](https://news.ycombinator.com/item?id=49950851) : Some other benefits of older GPUs: Use as a dedicated GPU for encoding and decoding video. Post processing like frame interpolation or superresolution. Use for GPGPU workloads. Run additional monitors independently. Use for GPU passthrough to virtual machines. Use as a backup GPU for troubleshootin…

---

[Article original](https://www.phoronix.com/news/XDC-2026-Valve-Timur-AMDGPU) · [Discussion HN](https://news.ycombinator.com/item?id=49946895)
