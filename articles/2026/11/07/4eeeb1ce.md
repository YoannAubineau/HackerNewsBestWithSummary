---
article_fetched_at: '2026-11-07T15:59:17.316303Z'
attempts: 0
content_source: extracted
discussion_comment_count: 125
discussion_fetched_at: '2026-11-07T15:58:48.101197Z'
error: null
guid: https://news.ycombinator.com/item?id=50403052
hn_item_id: 50403052
hn_url: https://news.ycombinator.com/item?id=50403052
is_ask_or_show_hn: false
llm_input_tokens: 9162
llm_latency_ms: 8033
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 814
our_published_at: '2026-11-07T15:55:12Z'
rewritten_title: Need for Speed Underground 2 jouable en ligne dans le navigateur
  avec contrôles personnalisables
source_published_at: '2026-11-07T09:36:36Z'
status: summarized
summarized_at: '2026-11-07T16:00:18.799722Z'
title: Need for Speed Underground 2 online in the browser
url: https://nfsu2.xyz/
---

## Résumé de l'article

Need for Speed Underground 2 est un jeu de course arcade sorti en 2004, ici rendu jouable dans un navigateur web avec support multijoueur en ligne. La plateforme permet de sauvegarder sa progression localement ou dans le cloud, de synchroniser les données entre appareils, et d'accéder à des mods créés par la communauté.

- Les sauvegardes s'effectuent via le menu Garage (Échap ou Start) et se synchonisent automatiquement via le cloud entre appareils
- Les contrôles tactiles, à la manette ou au clavier sont entièrement personnalisables, avec options de direction inclinée et redimensionnement automatique des boutons
- Les commandes incluent l'accélération, le freinage, la direction, le nitro, le handbrake, les commandes manuelles, les hydrauliques et les éléments d'interaction sociale (chat rapide, messages)
- La caméra, la carte, les messages et le respawn sont accessibles via des raccourcis configurables
- Les mods communautaires (et leurs traductions) sont listés et s'appliquent au redémarrage du jeu

## Discussion sur Hacker News (125 commentaires)

**Avis positifs** :
- La performance est excellente pour un jeu complexe en WebGL/WASM, fonctionnant même sur des appareils anciens (téléphones de 6 ans, tablets) avec des temps de chargement instantanés
- Le concept du multijoueur en ligne avec free roam et les événements chaotiques entre joueurs ajoute une dimension sociale nouvelle et amusante au jeu original
- C'est une solution valable de préservation de jeux abandonnés : EA refuse de revendre NFSU2 (problèmes de droits musicaux) et le jeu n'est disponible nulle part légalement
- La technologie de recompilation WASM permet de revisiter des classiques avec une accessibilité accrue (navigateur, tous appareils) sans les problèmes de compatibilité des versions natives

**Avis négatifs** :
- La légalité est très douteuse : distribution d'assets copyrightés et acceptation de donations, ce qui attirera rapidement les poursuites judiciaires d'EA et des détenteurs de droits musicaux
- Des ralentissements et pauses GC se produisent pendant le jeu malgré la fluidité générale, et WebGPU/WebGL nécessite l'activation de flags 'unsafe' posant des risques de sécurité (débordements mémoire)
- L'expérience de jeu en navigateur n'est pas idéale : manque de contrôles manuels, stabilité inférieure aux versions natives, nécessite Chromium (Firefox non supporté sur mobile)
- Le problème plus large : ces projets pourraient compromettre la préservation de jeux à long terme en incitant les éditeurs à renforcer la répression plutôt que de proposer des solutions officielles

**Top commentaires** :

- [macNchz](https://news.ycombinator.com/item?id=50404449) : I played this when it was new, taking turns at the keyboard of my friend’s gaming PC. Kind of wild to revisit on my phone today and have it work perfectly. I wish the circumstances around abandonware games weren’t so tenuous, there’s so much great stuff out there and reverse engineering with AI unl…
- [popcar2](https://news.ycombinator.com/item?id=50404555) : Been playing it the last few days along with a few races with friends, it's pretty wild that this is even possible. The only downside is that this website isn't legal and now that it's popular it's probably getting a takedown soon. But NFSU2 is abandonware that isn't available anymore so I hope the…
- [rustyhancock](https://news.ycombinator.com/item?id=50404031) : Huge fan of bringing back older games and updating. But I think it's highly dubious to accept let alone solicit donations for copyrighted content.

---

[Article original](https://nfsu2.xyz/) · [Discussion HN](https://news.ycombinator.com/item?id=50403052)
