---
article_fetched_at: '2026-07-05T11:24:29.080751Z'
attempts: 0
content_source: extracted
discussion_comment_count: 50
discussion_fetched_at: '2026-07-05T11:24:25.988157Z'
error: null
guid: https://news.ycombinator.com/item?id=48780865
hn_item_id: 48780865
hn_url: https://news.ycombinator.com/item?id=48780865
image_url: https://opengraph.githubassets.com/49434cefc3911817a75fbf43f0a202ad27a16487569321af69250a8e990bd3fb/FossPrime/Steam-Controller-Auto-Charge
is_ask_or_show_hn: false
llm_input_tokens: 5396
llm_latency_ms: 10329
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 909
our_published_at: '2026-07-05T11:12:36Z'
rewritten_title: Steam Controller Auto-Charge automatise l'amarrage magnétique par
  vision par ordinateur et contrôle haptique
source_published_at: '2026-07-03T22:39:50Z'
status: summarized
summarized_at: '2026-07-05T11:24:46.785538Z'
title: Steam Controller Auto-Charge – pilot to magnetic charging puck using CV
url: https://github.com/FossPrime/Steam-Controller-Auto-Charge
---

## Résumé de l'article

Steam Controller Auto-Charge est une application web open-source qui pilote automatiquement une manette Steam vers son socle de recharge magnétique en utilisant le suivi optique par flux optique et la telémétrie WebHID. Le système détecte visuellement la position de la manette et du socle via une caméra overhead, puis navigue la manette vers sa destination en activant des impulsions haptiques asymétriques à travers les actionneurs linéaires résonnants internes.

- Suivi par flux optique : OpenCV.js suit les points sélectionnés sur la manette et le socle via caméra overhead pour déterminer leur position en temps réel
- Navigation haptique : WebHID se connecte à la manette et envoie des impulsions haptiques de 70 Hz pour la guider ; la fréquence diminue de 50 % à proximité du socle pour assurer un amarrage magnétique en douceur
- Sondage de batterie : lit les rapports de télémétrie (ID 67 et 121) pour confirmer la charge magnétique réussie et afficher le pourcentage de batterie et la tension des cellules
- Installation simple : seul Nix Package Manager est requis comme dépendance de construction ; fonctionne sur Windows, macOS et Linux avec un navigateur compatible WebHID et une webcam overhead
- Détection d'objets en arrière-plan : utilise Rust/WASM compilé pour que la boucle de suivi principale reste fluide sur le thread principal

## Discussion sur Hacker News (50 commentaires)

**Avis positifs** :
- Le projet est ingénieux et fonctionne bien en pratique : le contrôleur se déplace effectivement de manière fluide vers le socle de charge magnétique sans à-coups.
- C'est un projet hobbyiste publié librement sous licence MIT avec du code fonctionnel, ce qui mérite du respect indépendamment de la qualité de la documentation.
- La solution utilise intelligemment les moteurs haptic existants du contrôleur avec une vision par ordinateur, ce qui est créatif et démontre une bonne compréhension du matériel.
- Les mesures de Valve contre le scalping (randomisation des commandes) sont préférables à des alternatives plus restrictives comme le verrouillage par compte ou les plafonds de prix.

**Avis négatifs** :
- La documentation est confuse et peu claire : elle n'explique pas immédiatement que le contrôleur se déplace physiquement par vibration, utilisant plutôt un jargon technique obscur ("Linear Resonant Actuators") sans contexte.
- Le README semble généré par IA avec des formulations maladroites et peu naturelles (ex : "Code like Anthony Fu and Evan You"), ce qui suggère un manque d'effort et de respect envers le lecteur.
- Il existe une critique légitime sur le scalping des Steam Controllers : bien que la randomisation aide, les contrôleurs sont toujours revendus 2-2.5x leur prix, créant une barrière artificielle pour les acheteurs à budget limité.
- Le scalping ne crée pas de valeur réelle mais représente plutôt du parasitisme économique : les revendeurs s'insèrent comme intermédiaires non désirés sans améliorer le produit ni le service.

---

[Article original](https://github.com/FossPrime/Steam-Controller-Auto-Charge) · [Discussion HN](https://news.ycombinator.com/item?id=48780865)
