---
article_fetched_at: '2026-05-14T19:32:43.303847Z'
attempts: 0
content_source: extracted
discussion_comment_count: 82
discussion_fetched_at: '2026-05-14T19:32:41.331436Z'
error: null
guid: https://news.ycombinator.com/item?id=48137145
hn_item_id: 48137145
hn_url: https://news.ycombinator.com/item?id=48137145
image_url: https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/macos-egpu.jpg
is_ask_or_show_hn: false
llm_input_tokens: 22441
llm_latency_ms: 13339
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1038
our_published_at: '2026-05-14T18:55:21Z'
rewritten_title: 'Connecter un RTX 5090 à un MacBook Air M4 pour jouer: faisabilité
  et performance'
source_published_at: '2026-05-14T15:47:31Z'
status: summarized
summarized_at: '2026-05-14T19:33:42.123262Z'
title: 'RTX 5090 and M4 MacBook Air: Can It Game?'
url: https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/
---

## Résumé de l'article

Un développeur a réussi à connecter une carte graphique NVIDIA RTX 5090 via Thunderbolt à un MacBook Air M4, en contournant les limitations de macOS par une machine virtuelle Linux avec passthrough PCIe. Le projet démontre qu'il est techniquement possible de jouer à des jeux modernes sur Mac avec cette configuration, mais au prix d'une complexité extrême.

- **Configuration technique complexe** : utilisation d'une machine virtuelle ARM64 Linux, passthrough PCIe du GPU via Thunderbolt, création d'un périphérique DMA virtuel dans QEMU, et patches du noyau pour contourner les limites matérielles (plateau de mappings DART limité à 64k, plafond d'allocation de 1,5 Go).

- **Performance en jeu** : le M4 Air + RTX 5090 peut faire tourner Cyberpunk 2077 en 4K avec ray-tracing à 27 fps (111 fps avec DLSS framegen), contre 3 fps en natif. Cependant, un PC gaming classique avec le même GPU est 2 à 4 fois plus rapide en raison de l'émulation x86 (FEX) et de la virtualisation.

- **Avantage clair pour l'inférence IA** : le gain de performance est spectaculaire pour les modèles de langage (100x plus rapide pour le traitement des prompts, ~155 tokens/s contre ~22 en natif), car CUDA s'exécute nativement en ARM64 sans émulation x86.

- **Limitations majeures** : certains jeux (Horizon Zero Dawn) dépassent les limites de mapping DART et ne peuvent pas démarrer; stabilité insuffisante (crashes Steam fréquents, minutes de démarrage); nécessite une entitlement spéciale d'Apple encore en attente.

- **Complexité de mise en place** : ce projet reste un prototype de recherche plutôt qu'une solution pratique; l'intégration upstream dans QEMU est en cours mais pas finalisée.

## Discussion sur Hacker News (82 commentaires)

**Avis positifs** :
- Le projet démontre une véritable ingénierie créative et des modifications QEMU impressionnantes, loin des stéréotypes sur l'IA ; c'est du vrai hacking technique
- Les résultats en inférence IA sont remarquables : accélération 120x sur le traitement des prompts (TTFT) et amélioration drastique de la vitesse de génération, offrant une solution pratique pour l'exécution locale de modèles
- L'absence de support GPU NVIDIA sur Mac pro était effectivement une opportunité manquée majeure pour Apple dans les marchés professionnel et datacenter
- Les LLM restent utiles comme outil de vérification rapide et point de départ, même imparfaits, tant qu'on ne les suit pas aveuglément

**Avis négatifs** :
- Les LLM affichent des failles chroniques : informations obsolètes, incapacité à intégrer les corrections apportées (redonnant les mêmes erreurs), limitation due aux dates de cut-off du training
- Pour les jeux, la compatibilité reste le vrai blocage sur macOS et Apple Silicon, bien plus que la puissance GPU ; une eGPU ne résout pas ce problème fondamental
- Le surengagement marketing des entreprises IA sur la disruption économique massive crée des attentes irréalistes et une hystérie collective disproportionnée par rapport aux capacités réelles
- Une eGPU via Thunderbolt n'offre que 4 lanes PCIe contre les 16+ disponibles sur x86, et Apple améliorera probablement les capacités TTFT directement en silicium (M5/M6) sans besoin d'accessoires externes

**Top commentaires** :

- [matthewfcarlson](https://news.ycombinator.com/item?id=48137817) : I have been bothering the VM team for years for VM GPU pass through. I worked on the Apple Silicon Mac Pro and it would have made way more sense if you could run a linux VM and pass through the GPU that goes inside the case! Sadly, as you can tell, they have not taken me up on my requests. Awesome…
- [Aurornis](https://news.ycombinator.com/item?id=48138265) : Excellent article. The game benchmarks are fun but the LLM improvements are where this gets really interesting for practical use. I love Apple platforms as an approachable way to run local models with a lot of RAM, but their relatively slow prompt processing speed is often overlooked. \> Here you ca…
- [djmips](https://news.ycombinator.com/item?id=48139049) : « Because OpenGL is not well-supported anymore on macOS, the game is completely unplayable there, even with CrossOver. Ironically, it plays totally fine on a Windows PC, but this is a game you literally can’t play on Mac without this eGPU setup. » I understand that this is true it seems that Doom d…

---

[Article original](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/) · [Discussion HN](https://news.ycombinator.com/item?id=48137145)
