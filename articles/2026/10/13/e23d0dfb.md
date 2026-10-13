---
article_fetched_at: '2026-10-13T01:02:31.678445Z'
attempts: 0
content_source: extracted
discussion_comment_count: 141
discussion_fetched_at: '2026-10-13T01:02:21.177200Z'
error: null
guid: https://news.ycombinator.com/item?id=50052251
hn_item_id: 50052251
hn_url: https://news.ycombinator.com/item?id=50052251
image_url: https://opengraph.githubassets.com/5b5822bae859f86efeb77796bf2f7fe773ab2fd8411897e957fb3a09f050a1c0/snuri00/ps2-web-recomp
is_ask_or_show_hn: false
llm_input_tokens: 13566
llm_latency_ms: 15916
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1171
our_published_at: '2026-10-13T00:34:43Z'
rewritten_title: Jeux PlayStation 2 recompilés statiquement en WebAssembly pour le
  navigateur
source_published_at: '2026-10-12T06:46:53Z'
status: summarized
summarized_at: '2026-10-13T01:04:50.998751Z'
title: 'Show HN: PS2 games statically recompiled to WebAssembly'
url: https://github.com/snuri00/ps2-web-recomp
---

## Résumé de l'article

Un projet de recompilation statique permet de faire fonctionner des jeux PS2 dans le navigateur sans émulateur : le code machine du processeur Emotion Engine est traduit en C++ et compilé en WebAssembly, puis lié à une réimplémentation du système d'exploitation et du matériel PS2 avec rendu WebGPU.

- Les jeux (Gran Turismo 4 et God of War II testés) s'exécutent à pleine vitesse (50-60 fps) avec son, effets et sauvegarde en mémoire sur navigateur, à résolution double ou triple de la PS2
- La recompilation (outil eerecomp) traduit les fonctions du jeu en unités de 16 KiB de code en C++, préservant les quirks du R5900 (registres 128 bits, unités vectorielles, comportement flottant spécifique à PS2)
- Le noyau PS2 est réimplémenté en C++ avec émulation haute niveau des threads, des interruptions, du contrôleur DMA, et un interprétateur R3000 pour le processeur E/S exécutant les modules IRX du jeu
- Les unités vectorielles sont compilées en SIMD C++ avec modélisation des délais de pipeline et des règles flottantes PS2 (pas d'infinis/NaN, débordements plafonnés)
- Le Graphics Synthesizer tourne sur GPU via shaders WebGPU en calcul, conservant la mémoire vidéo native (4 MB) et gérant les effets complexes (textures rendues, palettes relues depuis framebuffers)

## Discussion sur Hacker News (141 commentaires)

**Avis positifs** :
- Accomplissement technique impressionnant : la recompilation statique de jeux PS2 en WebAssembly avec gestion approximative mais fonctionnelle du timing, des interrupts et de la synchronisation via VIF/GIF est un exploit d'ingénierie remarquable
- Implémentation détaillée et réfléchie : gestion bit-exacte des floats PS2, modélisation précise du pipeline VU1 avec drapeaux MAC/status/clip, compilation AOT du code EE avec fallback JIT pour les microprogrammes VU1 non vus en AOT
- Distribution décentralisée et avantageuse : l'utilisateur convertit son propre ISO localement, rien de dérivé du jeu n'est hébergé publiquement, ce qui contourne les problèmes DMCA contrairement aux émulateurs hébergés
- Performance viable : 60fps maintenu en résolution native sur GPU intégré pour God of War 2, avec optimisations intelligentes (batching, caching) contre les goulots d'étranglement initiaux
- Réalisations connexes motivantes : le succès parallèle de recompilations (PSP, Xbox 360 NFS/Forza Horizon) démontre le potentiel et l'impact positif sur l'accès aux jeux via handheld gaming

**Avis négatifs** :
- Prétentions trompeuses sur la recompilation : le projet maintient l'interprétation du CPU IOP (processeur I/O PS1-like), contredisant l'affirmation d'une recompilation complète sans émulation de composants système
- Implications légales graves : distribution de jeux copyrightés sans consentement, malgré les affirmations du développeur sur le respect légal ; historique de takedowns DMCA par Cloudflare démontre la vulnérabilité juridique
- Préoccupations légitimes sur la sécurité et les malveillances : absence de processus de vérification établi pour les binaires générés par IA comparé à l'écosystème d'émulation mature ; difficulté à garantir l'absence de code malveillant injecté
- Mensonges documentés dans les projets de recompilation : plusieurs projets similaires ont gonflé leurs revendications (ex. prétendre 'pas d'émulation' alors qu'ils la conservent), générant de la méfiance justifiée envers les affirmations du secteur
- Impact négatif sur les incitations de création : la facilité accrue de piratage et de distribution gratuite via recompilation affecte les revenus des petits studios indépendants, bien que les impacts sur les AAA restent débattus

**Top commentaires** :

- [aceazzameen](https://news.ycombinator.com/item?id=50057773) : I don't know. There's suddenly so many decomps that run native \(granted this post is about WebAssembly\). Is there no concern about hidden malware? IMO it doesn't have the same level of trust and vetting that the emulator scene has. At least not yet.
- [zuInnp](https://news.ycombinator.com/item?id=50055027) : All of this recomp stuff is pretty amazing. I really don't like how AI changed my profession, but hey at least I get something good from it.
- [Megabinator](https://news.ycombinator.com/item?id=50055373) : What about compiling the compiler to WebAssembly so it can be hosted anywhere and convert a project directly from a browser?

---

[Article original](https://github.com/snuri00/ps2-web-recomp) · [Discussion HN](https://news.ycombinator.com/item?id=50052251)
