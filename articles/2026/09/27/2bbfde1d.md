---
article_fetched_at: '2026-09-27T18:47:37.303348Z'
attempts: 0
content_source: extracted
discussion_comment_count: 21
discussion_fetched_at: '2026-09-27T18:47:21.900444Z'
error: null
guid: https://news.ycombinator.com/item?id=49854219
hn_item_id: 49854219
hn_url: https://news.ycombinator.com/item?id=49854219
is_ask_or_show_hn: false
llm_input_tokens: 17581
llm_latency_ms: 12857
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 954
our_published_at: '2026-09-27T14:13:59Z'
rewritten_title: Construction d'un affichage à points basculants pilotés pour simuler
  un fluide en mouvement
source_published_at: '2026-09-26T07:50:24Z'
status: summarized
summarized_at: '2026-09-27T18:48:18.140817Z'
title: Flip Fluid on Flip Dots
url: https://mitxela.com/projects/flipflip
---

## Résumé de l'article

Un ingénieur a construit une installation artistique combinant des panneaux de points basculants (flipdots, des affichages électromécaniques rétro) avec une simulation fluide, créant ainsi du bruit audible et un effet visuel dynamique. Les flipdots sont des technologies obsolètes très coûteuses, que seul un fabricant produit encore commercialement.

- Les flipdots sont des panneaux non-volatiles fonctionnant via des noyaux polarisés et des aimants permanents, permettant d'afficher l'état sans alimentation continue.
- L'auteur a récupéré des panneaux anciens chez Sam (Look Mum No Computer) et a conçu des circuits de commande basés sur des puces H-bridge bon marché pour les piloter bien plus vite que l'électronique d'origine, en utilisant des capacités en série et une architecture en matrice optimisée.
- L'assemblage a nécessité 18 panneaux de 13×28 points chacun, soudés à la main avec des cartes filles personnalisées, des alimentations 1000µF pour gérer les pics de courant, et une architecture décentralisée avec contrôleurs CH32V003 communiquant en RS485.
- L'installation finale, montée sur un socle avec un joystick analogique permettant de contrôler la gravité simulée, a fonctionné sans défaut pendant les quatre jours de la conférence EMF 2024, avec un coût matériaux de moins de 500 £ (environ 0,17 £ par point).
- Le projet démontre qu'il est possible de créer des affichages flipdot rapides et sans artefacts en utilisant du matériel récupéré et des circuits modernes, ouvrant des perspectives pour des projets futurs comme des jeux arcade ou du stockage de données visible.

## Discussion sur Hacker News (21 commentaires)

**Avis positifs** :
- Le défluxage à l'air chaud est une technique efficace et couramment utilisée pour récupérer des composants délicats comme les flip-dots, bien qu'il faut rester prudent
- L'approche par condensateur offre une meilleure sécurité d'exploitation en comparaison à un contrôle direct, empêchant les défaillances dangereuses via une décharge progressive
- Le circuit de déflexion capacitive est comparable à des solutions éprouvées en industrie (vannes de chauffage, suspensions pneumatiques) où la sécurité de défaillance intrinsèque est critique
- Le travail de précision et l'innovation sur les panneaux flip-dots est remarquable et inspire l'intérêt du public pour l'électronique vintage

**Avis négatifs** :
- La déflexion thermique des flip-dots risque de faire fondre le plastique fin et bas point de fusion du mécanisme, causant plus de dégâts que sur des composants standards
- Regrouper les dots par lignes de 7 complique le défluxage en augmentant la zone chauffée et le risque de blocage, rendant la technique peu explorée en pratique
- Les techniques de traitement en masse pour récupérer les dots ne sont pas vraiment développées, faute d'intérêt commercial et du risque encouru par les propriétaires de panneaux
- Les panneaux flip-dots restent très coûteux et encombrants, limitant leur adoption domestique malgré leur attrait esthétique et leur fonctionnalité discrète

**Top commentaires** :

- [aiiotnoodle](https://news.ycombinator.com/item?id=49865515) : He mentions in the video and in the article Breakfast Studio and I happened to watch a video of one of their panels on an unrelated YouTube channel. I've skipped ahead to when the video has the panel. \(there is also a cool egg just before that point in the video\) it's only about 5 seconds. https://…
- [userbinator](https://news.ycombinator.com/item?id=49864059) : The dots are so delicate, with tiny magnet wires and soft plastic that can melt, that it has to be done very carefully. Even with the very best desoldering equipment it would take forever. Put a hot air gun on the back of the board, and they'll either just drop out or do so with a small poke of the…
- [steventhedev](https://news.ycombinator.com/item?id=49865891) : I'm always amazed by the precision work this guy does. My only nit with this article was he didn't link the Eurovision entry: https://youtu.be/I0tqgGVQkew

---

[Article original](https://mitxela.com/projects/flipflip) · [Discussion HN](https://news.ycombinator.com/item?id=49854219)
