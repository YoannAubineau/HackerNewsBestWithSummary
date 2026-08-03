---
article_fetched_at: '2026-08-03T09:25:35.147282Z'
attempts: 0
content_source: extracted
discussion_comment_count: 171
discussion_fetched_at: '2026-08-03T09:25:22.468378Z'
error: null
guid: https://news.ycombinator.com/item?id=49147263
hn_item_id: 49147263
hn_url: https://news.ycombinator.com/item?id=49147263
image_url: https://i.ytimg.com/vi/3XaHHFOZeJg/maxresdefault.jpg
is_ask_or_show_hn: false
llm_input_tokens: 25656
llm_latency_ms: 13884
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1100
our_published_at: '2026-08-03T08:32:20Z'
rewritten_title: SwiftUI après sept ans reste une version bêta instable avec des problèmes
  de performance et de compatibilité
source_published_at: '2026-08-02T18:59:05Z'
status: summarized
summarized_at: '2026-08-03T09:26:24.158042Z'
title: SwiftUI After 7 Years
url: https://ykvm.com/2026/07/swiftui-a-story-of-mediocrity/
---

## Résumé de l'article

SwiftUI est un framework d'interface utilisateur déclaratif lancé par Apple en 2019 pour remplacer UIKit et AppKit sur toutes les plateformes Apple. Sept ans après son annonce, SwiftUI reste un produit instable et fragmenté qui n'a pas atteint la maturité promise, souffrant de problèmes chroniques de performance, de prévisibilité des mises en page et d'une fragmentation API permanente nécessitant des contournements constants.

- **Flux de données imprévisible** : Le système de réactivité de SwiftUI passe par plusieurs itérations (@State, @Binding, @Observable) mais reste une boîte noire où le nombre de mises à jour et leurs causes sont impossibles à déterminer avec certitude
- **Moteur de mise en page fragile** : La négociation de taille produit des résultats imprévisibles qui s'effondrent inopinément, même dans les tutoriels officiels d'Apple, forçant les développeurs à utiliser GeometryReader et à calculer les coordonnées manuellement
- **Instabilité API et fragments de code** : Sept ans après son lancement, le code SwiftUI est rempli de vérifications #available et de contournements de compatibilité car les API manquent de parité avec UIKit/AppKit (AsyncImage, clavier sur scroll, caching d'images toujours en bêta)
- **Performance inférieure** : Les comparaisons directes UIKit vs SwiftUI montrent que SwiftUI défile moins régulièrement même sur du matériel récent, nécessitant des optimisations obscures qui annulent les bénéfices de simplicité promis
- **Mythe du multiplateforme** : Les concepts SwiftUI diffèrent significativement entre iOS et macOS, rendant l'apprentissage une fois inapplicable ; cela s'inscrit dans un déclin plus large de la qualité chez Apple vers une mentalité « suffisamment bon »

## Discussion sur Hacker News (171 commentaires)

**Avis positifs** :
- SwiftUI excelle pour les interfaces simples et les animations/effets visuels complexes (blur, Metal shaders, blend modes), tâches triviales en SwiftUI mais laborieuses en UIKit
- Le framework permet une meilleure adoption par les nouveaux développeurs comparé à UIKit/AppKit, avec un cycle de développement plus rapide pour les cas d'usage standards
- Les versions récentes (iOS 17+) ont considérablement amélioré la stabilité, les performances et l'API (NavigationStack, @Observable, onGeometryChange), rendant beaucoup de critiques obsolètes
- SwiftUI offre une vraie scalabilité cross-platform (iOS, iPad, macOS) sans traitement spécifique, contrairement aux anciens frameworks
- L'approche déclarative-réactive, une fois maîtrisée correctement, réduit les bugs liés aux oublis de mise à jour de l'interface et simplifie le raisonnement sur l'état

**Avis négatifs** :
- SwiftUI reste incomplet et non conforme en fonctionnalités par rapport à UIKit/AppKit après 7 ans, forçant les développeurs à alterner entre frameworks et créant de la friction
- Les sérieux problèmes de documentation, d'outils de débogage (pas d'équivalent View Debugger) et de magie noire rendent le diagnostic des problèmes de performance et de rendu extrêmement difficile
- L'ordre des modificateurs affecte le résultat de manière non intuitive, les cycles de vie sont mal documentés, et les re-rendus imprévisibles causent des ralentissements sans solutions claires
- Apple promouvoit SwiftUI comme remplaçant complet d'UIKit alors qu'il échoue pour les listes volumineuses, collections asynchrones, transitions complexes et de nombreux widgets standards
- Le framework a complexifié le langage Swift lui-même (surcharge de types, syntaxe hideuse) et les défis cross-platform restent importants malgré les promesses, avec ruptures entre versions iOS

**Top commentaires** :

- [rayiner](https://news.ycombinator.com/item?id=49147549) : The problem with complex systems is that you can be dead long before you realize you're dead. Things can continue to seem "pretty good" for a long time just from the inertia of past good decisions and built-up infrastructure. You see some fraying or cracks but everything looks fundamentally sound,…
- [sandoze](https://news.ycombinator.com/item?id=49148028) : This seems to be a popular ‘controversial’ topic. I’ve been using SwiftUI for production applications and games since 2021. I drop down UIKit, Metal, or core animation when needed. But that’s no different than when I was making games in UIKit and would drop down to core animation or glyph renderers…
- [mintflow](https://news.ycombinator.com/item?id=49151009) : As a solo app developper for two years mainly for apple platform\(previously do networking infra software using C/Go\) After two many trial and fail, now it's quite clear to me that for simple UI I will use swiftUI\(such as help sheet or simple toggles\), for complex and performance first, I will just…

---

[Article original](https://ykvm.com/2026/07/swiftui-a-story-of-mediocrity/) · [Discussion HN](https://news.ycombinator.com/item?id=49147263)
