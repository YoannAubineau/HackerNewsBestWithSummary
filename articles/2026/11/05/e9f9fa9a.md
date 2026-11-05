---
article_fetched_at: '2026-11-05T16:58:28.932681Z'
attempts: 0
content_source: extracted
discussion_comment_count: 69
discussion_fetched_at: '2026-11-05T16:58:14.218858Z'
error: null
guid: https://news.ycombinator.com/item?id=50375354
hn_item_id: 50375354
hn_url: https://news.ycombinator.com/item?id=50375354
is_ask_or_show_hn: false
llm_input_tokens: 4530
llm_latency_ms: 6688
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 765
our_published_at: '2026-11-05T16:43:48Z'
rewritten_title: Animation CSS de Lemmings avec réflexe au redimensionnement de fenêtre
source_published_at: '2026-11-05T04:54:10Z'
status: summarized
summarized_at: '2026-11-05T16:59:39.485698Z'
title: Lemmings CSS Animation
url: https://markblah.github.io/lemmings/
---

## Résumé de l'article

Un projet d'animation CSS qui simule le jeu Lemmings en utilisant les colonnes de texte d'une page web comme terrains de jeu. Les personnages (walkers) peuvent se déplacer, chuter d'une ligne de texte à l'autre et interagir avec les éléments de la mise en page.

- Chaque ligne de texte fonctionne comme une plateforme ou un sol où les walkers peuvent marcher et chuter
- Les walkers peuvent tomber d'une ligne à l'autre et atterrir sur des éléments situés en dessous
- L'espacement entre les lignes est réduit pour éviter que les walkers ne restent bloqués entre les lignes d'un paragraphe
- Seuls certains éléments (bordures, boîtes, boutons, images, champs) bloquent le mouvement des walkers
- Un long sol au bas de la page rattrape tout élément qui tomberait complètement vers le bas

## Discussion sur Hacker News (69 commentaires)

**Avis positifs** :
- Nostalgie puissante : nombreux utilisateurs partagent leurs souvenirs d'enfance avec le jeu original sur Amiga/Commodore, trouvant l'animation touchante et émouvante
- Exploit technique impressionnant : démonstration réussie de ce qui est possible en CSS et JavaScript, avec gestion fluide de nombreux lemmings sans lag significatif
- Qualité de l'exécution : sprites extraits du jeu original, interaction intuitive (possibilité de les attraper et déplacer), détails amusants comme marcher sur les en-têtes de texte
- Créativité communautaire inspirante : génère des discussions sur d'autres projets similaires (xpenguins, DHTML Lemmings 2004) et encourage l'expérimentation web rétro

**Avis négatifs** :
- Perd l'essence du gameplay : sans mécanique de creusage, construction d'escaliers ou parachutes, ce n'est que du spectacle graphique plutôt que du vrai Lemmings
- Problèmes de design et d'accessibilité : lemmings tombent facilement hors de la zone de jeu sur les côtés (particulièrement sur mobile), ne fonctionne pas avec prefers-reduced-motion, bugs de zoom sur mobile et incompatibilité Edge
- CSS excessivement puissant : le projet démontre que CSS a dépassé son rôle initial de contrôle d'apparence, devenant quasi Turing-complet, ce qui est problématique architecturalement
- Différences de performance entre navigateurs : Chrome offre une animation fluide mais rend le scroll douloureux, tandis que Safari consomme plus de CPU et perd en fluidité avec plus de lemmings

**Top commentaires** :

- [bradley13](https://news.ycombinator.com/item?id=50381163) : Cute. However, the fact that this is possible shows how ridiculously out of control CSS is. It is supposed to control appearance, and that does not entail being Turing complete.
- [rfarley04](https://news.ycombinator.com/item?id=50376660) : I played this game for dozens of hours with my dad growing up and seeing and playing with these animations is one of those times when nostalgia is so overwhelming and unexpected that I feel physically dizzy. If the animation had the sounds of lemmings dying when they fell from too high\[1\] I might h…
- [Waterluvian](https://news.ycombinator.com/item?id=50375689) : That’s pretty sweet. I did something on my site recently like that where you can click a hexagon and it turns into a robot and starts SLAM mapping the page, navigating around text elements carefully. Were you initially surprised by how easy it was to get exact block size of individual characters an…

---

[Article original](https://markblah.github.io/lemmings/) · [Discussion HN](https://news.ycombinator.com/item?id=50375354)
