---
article_fetched_at: '2026-08-22T21:13:10.492084Z'
attempts: 0
content_source: extracted
discussion_comment_count: 40
discussion_fetched_at: '2026-08-22T21:13:04.433842Z'
error: null
guid: https://news.ycombinator.com/item?id=49389952
hn_item_id: 49389952
hn_url: https://news.ycombinator.com/item?id=49389952
image_url: https://nari-labs.com/blog/qwen3-tts-speed-cost-frontier/assets/image.png
is_ask_or_show_hn: false
llm_input_tokens: 6562
llm_latency_ms: 12959
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1161
our_published_at: '2026-08-22T21:12:42Z'
rewritten_title: Optimisation d'un modèle de synthèse vocale pour réduire la latence
  sous 50 ms
source_published_at: '2026-08-21T15:51:10Z'
status: summarized
summarized_at: '2026-08-22T21:14:20.109132Z'
title: How we made a text-to-speech model respond in sub-50 ms
url: https://nari-labs.com/blog/qwen3-tts-speed-cost-frontier/
---

## Résumé de l'article

Nari Labs a développé une implémentation de Qwen3-TTS 1.7B CustomVoice (un modèle de synthèse vocale basé sur l'apprentissage automatique) qui atteint un temps de réponse inférieur à 50 ms au 95e percentile avec 10 requêtes par seconde sur un seul GPU NVIDIA H100 SXM, tout en produisant environ 630 caractères par seconde à un coût d'environ 2 dollars par million de caractères.

- L'implémentation surpasse cinq autres systèmes existants (vLLM-Omni, SGLang-Omni, VoxServe, M*) en maintenant une latence sub-50 ms jusqu'à 10 requêtes par seconde, tandis que les autres moteurs atteignent environ 100 ms ou plus à partir de 6 requêtes par seconde
- L'optimisation repose sur l'exposition des trois modules du modèle (Talker, Code Predictor, Codec) à un seul planificateur unifié, permettant une priorisation dynamique du travail selon l'urgence plutôt que l'ordre d'exécution fixe
- Des techniques incluent la suppression du silence initial (gain de ~80 ms), l'ajustement de l'accumulation de frames pour équilibrer latence et efficacité, l'utilisation de graphes CUDA pré-compilés, et la mise en cache de l'état du Codec pour éviter le traitement répété de l'historique audio
- Le coût opérationnel (2 $/1M caractères) est significativement inférieur à celui des services concurrents ElevenLabs V3 (100 $/1M) et Cartesia Sonic 3.5 (49 $/1M) avec des latences supérieures
- L'implémentation et les benchmarks sont en open source, utilisant du trafic Poisson sur 5 minutes pour simuler des charges réelles et mesurant la latence perceptible du premier audio et l'absence de ruptures de lecture

## Discussion sur Hacker News (40 commentaires)

**Avis positifs** :
- L'optimisation du temps de réponse (TTFA) en sub-50ms est pertinente pour les applications vocales temps réel et représente une amélioration significative par rapport aux implémentations open-source existantes jugées trop lentes.
- Le modèle fonctionne sur du matériel grand public (RTX 4090) et pas uniquement sur des serveurs H100, rendant la technologie plus accessible aux développeurs et entrepreneurs.
- La capacité à traiter des flux LLM en streaming directement vers le modèle TTS sans attendre la génération complète est une approche élégante pour réduire la latence perçue.
- L'implémentation open-source et les benchmarks détaillés permettent à d'autres développeurs d'itérer et d'améliorer la technologie.
- La qualité de sortie est conservée par rapport à l'implémentation originale de Qwen, ce qui valide que la vitesse n'a pas compromis la performance.

**Avis négatifs** :
- Les exigences matérielles restent prohibitives pour la majorité des cas d'usage grand public (un RTX 4090 coûte 2500-3000$ d'occasion) et aucune démonstration sur matériel mobile ou CPU/iGPU standard n'est fournie.
- Une latence de 50ms trop basse peut créer une sensation d'étrangeté utilisateur car elle ne respecte pas le délai naturel de traitement auditif humain (~200ms), risquant de donner une impression artificielle ou perturbante.
- La latence TTS seule ne résout que partiellement le problème : la latence d'inférence du LLM reste le goulot d'étranglement majeur pour un agent conversationnel complet.
- Peu d'informations sur les tests en conditions réelles (performance lors de pics de charge, comportement avec plusieurs requêtes concurrentes sur matériel moins puissant), et certains utilisateurs rapportent des artefacts en mode websocket.
- L'approche ne répond pas aux besoins d'exécution on-device léger sur mobiles, limiterait donc son impact pour les assistants vocaux vraiment décentralisés.

**Top commentaires** :

- [toebee](https://news.ycombinator.com/item?id=49389953) : time-to-first-audio \(TTFA\) is critical for realtime voice applications. open source implementations \(e.g. vLLM-Omni, SGLang-Omni\) are often too slow for production and can have issues with realtime playback if you push for lower latency. we wanted to fix that. we optimized qwen3-tts, a popular OSS…
- [armcat](https://news.ycombinator.com/item?id=49392664) : Having built my own voice assistant \(https://github.com/acatovic/ova\) and having tried many other services and models, I feel the real win is when this is on-device, and by "on-device" I mean being very inexpensive to run on a phone, and not H100. I've now been using Pocket TTS which is super fast,…
- [pcvetkovski](https://news.ycombinator.com/item?id=49397387) : Sub-50ms on text-to-speech running on an LLM is commendable. We recently shipped text-to-speech and speech-to-text support inside Finsight \(Maxint\). We tapped into the platform’s native speech capabilities, which were integrated with the user’s preferred LLM inference endpoint \(including local on-d…

---

[Article original](https://nari-labs.com/blog/qwen3-tts-speed-cost-frontier/) · [Discussion HN](https://news.ycombinator.com/item?id=49389952)
