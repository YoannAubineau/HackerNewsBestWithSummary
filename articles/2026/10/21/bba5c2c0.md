---
article_fetched_at: '2026-10-21T10:53:19.227796Z'
attempts: 0
content_source: extracted
discussion_comment_count: 163
discussion_fetched_at: '2026-10-21T10:53:07.289231Z'
error: null
guid: https://news.ycombinator.com/item?id=50175070
hn_item_id: 50175070
hn_url: https://news.ycombinator.com/item?id=50175070
image_url: https://www.joshwcomeau.com/images/og-interop-2027.png
is_ask_or_show_hn: false
llm_input_tokens: 15703
llm_latency_ms: 14330
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1016
our_published_at: '2026-10-21T10:38:10Z'
rewritten_title: Dix fonctionnalités CSS futures susceptibles d'être adoptées via
  le programme Interop
source_published_at: '2026-10-21T01:47:28Z'
status: summarized
summarized_at: '2026-10-21T10:54:14.926344Z'
title: The Future of CSS
url: https://www.joshwcomeau.com/css/interop-2027/
---

## Résumé de l'article

Cet article explore les dix meilleures propositions de nouvelles fonctionnalités CSS votées pour potentiellement intégrer le programme Interop 2027, un effort collaboratif des principaux éditeurs de navigateurs visant à accélérer l'adoption de technologies web modernes entre navigateurs.

- Les fonctions CSS (@function) permettront de définir et réutiliser des calculs complexes comme les conversions de coordonnées polaires, déjà implémentées dans Chromium
- Les propriétés corner-shape et border-shape offriront de nouvelles façons de façonner les coins et les bordures des éléments, utiles pour les interfaces de jeux vidéo et les designs modernes
- Les « Anchored Container Queries » complètent l'API d'ancrage positionnement en permettant de détecter si un élément utilise une position de secours, résolvant les cas d'usage des infobulles
- Les animations déclenchées au défilement (scroll-triggered animations), les animations d'éléments de taille clé (interpolate-size), et les décorateurs d'écart de grille (gap decorations) résoudront des problèmes d'accessibilité, d'animation et de mise en page
- Les requêtes d'état de défilement permettront de modifier les styles selon que les éléments sticky sont ancrés au viewport ou s'il reste du défilement disponible

## Discussion sur Hacker News (163 commentaires)

**Avis positifs** :
- Les nouvelles fonctionnalités CSS (variables, fonctions, nesting, @layer, :has(), grid, flexbox) rendent le développement drastiquement plus facile et plus agréable qu'avant, permettant de remplacer du JavaScript par du CSS natif.
- Le support inter-navigateurs s'améliore grâce au programme Interop, avec des fonctionnalités comme l'Anchor Positioning maintenant disponibles partiellement dans tous les navigateurs.
- Les capacités modernes de CSS offrent enfin des solutions élégantes pour des problèmes historiquement complexes (layout responsif, centrage, espacements) sans hacks ou contournements.
- CSS Functions et autres ajouts, bien que syntaxiquement maladroits, n'ajoutent pas autant de complexité que JavaScript et permettent une évaluation plus rapide sans machine virtuelle.
- Les cas d'usage pratiques comme les rapports PDF générés en HTML/CSS, les systèmes de design avec variables et dark mode, et les interfaces interactives montrent l'utilité réelle de ces nouvelles fonctionnalités.

**Avis négatifs** :
- CSS accumule sans cesse de la complexité et des fonctionnalités qui s'ajoutent à la syntaxe maladroite conçue à l'origine pour les feuilles de style, créant un langage de programmation involontaire et confus.
- Les nouvelles fonctionnalités CSS (fonctions, variables, nesting) reproduisent des concepts de JavaScript ou de SASS de manière inélégante au lieu d'améliorer véritablement le langage déclaratif.
- L'article met en avant des fonctionnalités disponibles principalement dans Chrome, ce qui contredit le message initial sur la collaboration inter-navigateurs et montre que Chrome continue à dominer l'évolution des standards.
- L'absence de tree-shaking, de typage statique et d'outils de vérification au build-time signifie que les bases essentielles d'une bonne ingénierie restent absentes malgré l'ajout de nouvelles fonctionnalités cosmétiques.
- Les améliorations de CSS sont souvent surengineered et ignorent les problèmes réels des développeurs (date pickers, inputs tactiles, accessibilité) au profit de features visuelles gratuites comme les border-radius et gradients.

**Top commentaires** :

- [paczki](https://news.ycombinator.com/item?id=50175911) : As someone who actively goes out of my way to stick to writing vanilla HTML/CSS/JS as much as possible, it's honestly hard to explain to people who only write within frameworks how good it's gotten. Use the proper tool for the job, of course, but it sparks joy!
- [fodkodrasz](https://news.ycombinator.com/item?id=50176887) : Wow even more fancy border styles! Infinite complexity for useless eyecandy. Date pickers are still barely working, last time i needed to build a touch optimized interface \(gloves, industrial setting\) with date picker, time picker, and numeric up/down style input fields it needed custom components…
- [CharlesW](https://news.ycombinator.com/item?id=50175529) : Since I’m in before the negativity: I love CSS! For whatever reason, it’s always made sense to me. I have great respect for everyone with the tenacity to push on improvements that might take 5-10 years to be in common use, if at all.

---

[Article original](https://www.joshwcomeau.com/css/interop-2027/) · [Discussion HN](https://news.ycombinator.com/item?id=50175070)
