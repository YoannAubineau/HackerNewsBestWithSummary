---
article_fetched_at: '2026-09-04T14:38:31.506906Z'
attempts: 0
content_source: extracted
discussion_comment_count: 114
discussion_fetched_at: '2026-09-04T14:38:28.211966Z'
error: null
guid: https://news.ycombinator.com/item?id=49550375
hn_item_id: 49550375
hn_url: https://news.ycombinator.com/item?id=49550375
image_url: https://www.babyloniantwins.com/img/og.jpg
is_ask_or_show_hn: false
llm_input_tokens: 17863
llm_latency_ms: 17060
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1332
our_published_at: '2026-09-04T14:36:37Z'
rewritten_title: Porter un jeu Amiga de 1993 en Godot avec une IA lisant l'assembleur
  68000
source_published_at: '2026-09-03T14:28:18Z'
status: summarized
summarized_at: '2026-09-04T14:39:58.412149Z'
title: Porting my 1993 Amiga game to Godot, with an LLM reading the 68000 assembly
url: https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/
---

## Résumé de l'article

L'auteur a porté Babylonian Twins, un jeu commercial créé en 1993 sur Amiga 500 en assembleur 68000 pur, vers Godot 4 en utilisant Claude Fable 5 pour interpréter et convertir le code. Le jeu original, écrit en Irak sous embargo sans ressources externes, n'avait jamais été largement distribué jusqu'à sa récente publication gratuite sur itch.io et son édition révisée sur iOS, Android et Steam.

- L'IA a d'abord porté 34 000 lignes de code C++ d'un moteur 2010 en une soirée, puis a reconstruit les 72 758 lignes d'assembleur 68000 original en le compilant byte-identiquement à l'original avant de le traduire en GDScript à 50 Hz
- Les formats de données complexes (cartes de tuiles, tables d'objets, feuilles de sprites planaires, gradients copper) ont été inversés à partir du code assembleur sans documentation, l'IA détectant les ambiguïtés et validant les résultats pixel par pixel
- Le processus a découvert plusieurs bugs subtils introduits lors du portage (garde frappant à travers les murs, boutons de saut mal interprétés, porte de niveau 1 sans instructions) et a généré automatiquement captures d'écran multilingues, métadonnées d'app store et téléchargements
- Le jeu 1993 s'exécute désormais en tant qu'invité dans la version moderne 2026, basculant entre 50 Hz et 60 Hz selon les besoins, sans contenir du code Amiga réel—uniquement des données décodées et du comportement réécrit

## Discussion sur Hacker News (114 commentaires)

**Avis positifs** :
- L'utilisation d'IA pour porter du code assembly 68000 en Godot ouvre des possibilités concrètes : plusieurs commentateurs rapportent avoir réussi des ports similaires de jeux rétro (MSX, ROM files, ZX81, etc.) en moins d'une heure, avec Claude extrayant graphiques, sons et logique de jeu
- C'est un exploit technique remarquable : le jeu original tournait en 512 Ko de RAM sur Amiga, et voir Claude reconstruire un titre complet en assembly d'une machine des années 90 démontre que l'IA peut traiter les 'bricolages obscurs' et techniques oubliées des anciennes architectures
- La démarche représente un acte de conservation numérique précieux : des jeux oubliés, jamais documentés, peuvent être ressuscités et rendus accessibles sur des plateformes modernes (Steam, web) sans nécessiter une réimplémentation manuelle fastidieuse
- Le port fonctionne très bien dans la pratique : le gameplay se sent juste, avec seulement un tweak mineur nécessaire pour les trampolines, et le choix de Claude de ne pas utiliser la physique Godot mais de porter le code tel quel a préservé le comportement original
- C'est un cas d'usage légitime de l'IA : l'auteur a conservé 33 ans de fichiers et de mémoire, a relu et édité chaque ligne sur une semaine, transformant notes personnelles et archive en article, ce qui n'aurait probablement pas eu lieu sans l'assistance de l'IA

**Avis négatifs** :
- La qualité de la rédaction est visiblement assistée par IA et moins authentique qu'un compte personnel : plusieurs lecteurs détectent des 'tics' d'écriture IA malgré les retouches, avec un ton pédant ('The test was deliberate. Step one, the safe ask...') qui diminue la crédibilité du récit
- Le doute persiste sur la profondeur réelle de la compréhension : un commentateur souligne que Claude comprend maintenant mieux le port que l'auteur lui-même, et poser des questions au humain qui a lancé l'IA plutôt qu'à l'IA directement est frustrant et limite l'utilité
- L'absence de validation rigoureuse est problématique : pas de comparaison côte à côte avec la version originale en UAE, un mystérieux delta de 108 bytes entre les binaires, et pas de test comportemental exhaustif pour confirmer que le port est vraiment fidèle
- Le port n'est pas techniquement une 'réécriture' authentique mais une récréation : pour certains puristes, jouer le port Godot plutôt que l'original en émulateur UAE ou sur hardware réel manque du contexte d'authenticité du titre
- La scalabilité et les limites ne sont pas claires : commentateurs notent que des jeux plus complexes (Ultima 6 en 3D, Flight Simulator 4, Wing Commander) restent partiellement bloqués ou en cours, suggérant que la technique a des plafonds non documentés pour les projets ambitieux

**Top commentaires** :

- [gmerc](https://news.ycombinator.com/item?id=49561433) : It's a completely new world. Random retro games I ported to modern webgl/webgpu in the last few months: - The Adventures of Robin Hood - Opus 4.7/Sonnet https://robin.tooclever.org - Syndicate - Sol/Luna 5.6/Opus \( https://this.os.isfine.org/blog/posts/modern-game-port-syndi... \) - Kaiser 2 - Popul…
- [pkilgore](https://news.ycombinator.com/item?id=49565190) : This was an interesting read, in that it was obvious both that Claude was used in part for the prose but that a human had definitely edited some of the worst claudish out of it \(but not enough for me to be able to tell\). Confirmed in that last paragraph. Just interesting to me I can detect gradatio…
- [mattjoyce](https://news.ycombinator.com/item?id=49557188) : A few weeks ago I downloaded a memory dump of a zx81 game, and ask Claude to build it in Go. It nailed it. Converted the binary back to basic and then to go. My idea was that the game would be unknown to llm training and perhaps a nice bench. What a crazy thing it is to be first at the advent of pe…

---

[Article original](https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/) · [Discussion HN](https://news.ycombinator.com/item?id=49550375)
