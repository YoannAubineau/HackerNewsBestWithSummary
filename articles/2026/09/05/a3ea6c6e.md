---
article_fetched_at: '2026-09-05T20:50:35.796980Z'
attempts: 0
content_source: extracted
discussion_comment_count: 69
discussion_fetched_at: '2026-09-05T20:50:33.303781Z'
error: null
guid: https://news.ycombinator.com/item?id=49576386
hn_item_id: 49576386
hn_url: https://news.ycombinator.com/item?id=49576386
is_ask_or_show_hn: false
llm_input_tokens: 8073
llm_latency_ms: 12586
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1095
our_published_at: '2026-09-05T20:10:54Z'
rewritten_title: La BC-250 d'AMD, une carte de minage reconvertie en PC de jeu à moins
  de 100 dollars
source_published_at: '2026-09-05T13:36:38Z'
status: summarized
summarized_at: '2026-09-05T20:51:29.242907Z'
title: The "$60 Gaming PC" – AMD BC-250 (2025)
url: https://devquasar.com/hardware/the-60-gaming-pc-amd-bc-250/
---

## Résumé de l'article

La BC-250 est une carte informatique conçue à l'origine pour le minage de cryptomonnaies, basée sur un APU (processeur graphique intégré) PS5 défaillant et revendu à bas prix sur le marché de l'occasion. Disponible pour 70 à 100 dollars environ, elle peut faire tourner des jeux modernes comme Cyberpunk 2077 à des cadences acceptables avec des modifications matérielles et logicielles substantielles.

- La BC-250 intègre 6 cœurs Zen 2, une GPU RDNA 2 avec 24 unités de calcul et 16 Go de mémoire GDDR6 partagée — des spécifications réduites par rapport à un APU PS5 standard.
- La configuration exige des modifications destructives (refonte du système de refroidissement, accès à un programmeur EEPROM ou flasheur BIOS personnalisé) et le repartitionnement de la mémoire unifiée pour optimiser les performances de jeu.
- Le système d'exploitation Linux (Manjaro) est recommandé car Windows manque de pilotes graphiques adaptés ; Steam fonctionne nativement sous Linux sur cette plateforme.
- Les utilisateurs rapportent des résultats comparables à un GPU d'entrée de gamme moderne, notamment sur Counter-Strike 2, GTA V et Hitman 3, mais aucune performance haut de gamme.
- Le projet demande des compétences avancées en modding matériel, bricolage 3D et configuration système — ce n'est pas une solution prête à l'emploi.

## Discussion sur Hacker News (69 commentaires)

**Avis positifs** :
- C'est effectivement un excellent matériel repurposé : des puces PS5 défectueuses recyclées intelligemment plutôt que jetées, débloquées pour offrir plus de cœurs GPU/CPU
- Les performances sont impressionnantes pour le prix historique : comparable à une PS5 standard, capable de jouer Cyberpunk 2077 à des réglages similaires à une RX 6700XT, avec une excellente bande passante mémoire (~410 GB/s) utile pour les LLM
- L'écosystème s'est considérablement développé : documentation complète, support Mesa, outils Linux, cas d'impression 3D, et une communauté active continuant à améliorer les performances
- Solution viable pour le cloud gaming domestique : utilisable comme serveur de jeu sans tête en streaming local via Sunshine/Moonlight, parfait pour plusieurs utilisateurs sur un même réseau
- Représente une leçon positive sur le recyclage : ce qui aurait pu être des déchets électroniques devient une opportunité pour les amateurs de bricolage grâce à la diffusion de connaissances

**Avis négatifs** :
- Le prix n'est plus du tout $60 : la plupart des vendeurs demandent $300+ maintenant, et les prix ont explosé après la couverture médiatique (Linus Tech Tips, etc.), rendant le titre trompeur et obsolète
- C'est un projet complexe et coûteux : il faut ajouter alimentation, NVMe, ventilation, adaptateurs vidéo, avec au total ~$300 dépensés, sans compter le temps de configuration Linux et l'ajustement du BIOS
- Expérience console peu soignée : consommation élevée en veille (80W), pas de suspension/reprise automatique, bruit selon la configuration, nécessite des contournements informatiques pour une convivialité basique
- Pas de sortie vidéo native en HDMI : nécessite des adaptateurs ou affichage DisplayPort sur un téléviseur généralement équipé d'HDMI, compliquant l'intégration salon
- Les scams se multiplient : des vendeurs vendent juste les boîtiers imprimés en 3D au prix du PC complet en les catégorisant comme ordinateurs complets sur eBay, trompant les acheteurs inattentifs

**Top commentaires** :

- [nsbk](https://news.ycombinator.com/item?id=49576855) : I built one of these. It is not possible to do so for 60$ anymore since the board itself goes for 150+. On top of that you still need a PSU, NVMe, a high pressure fan, DP to HDMI adapter, possibly BT and Wifi adapters, and a 3d-printed or DIY case. It is also a very hacky build. You need to flash t…
- [jolan](https://news.ycombinator.com/item?id=49579060) : I bought one while waiting to see if my Steam Machine reservation would be fulfilled. I paid ~$186 shipped for the board on eBay 5 weeks ago. I use an ATX power supply and NVMe that I had laying around and I printed a big case for it\[0\]. I seem to have gotten a good one as it has no problems after…
- [monster\_truck](https://news.ycombinator.com/item?id=49576756) : You are \_not\_ getting one of these for less than $300, and because of this post and many like it, there are countless scams selling just cases for them at this price from a dollar or two of filament.

---

[Article original](https://devquasar.com/hardware/the-60-gaming-pc-amd-bc-250/) · [Discussion HN](https://news.ycombinator.com/item?id=49576386)
