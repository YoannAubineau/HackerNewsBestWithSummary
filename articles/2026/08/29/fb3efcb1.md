---
article_fetched_at: '2026-08-29T02:57:42.327065Z'
attempts: 0
content_source: extracted
discussion_comment_count: 65
discussion_fetched_at: '2026-08-29T02:57:30.085835Z'
error: null
guid: https://news.ycombinator.com/item?id=49476143
hn_item_id: 49476143
hn_url: https://news.ycombinator.com/item?id=49476143
is_ask_or_show_hn: false
llm_input_tokens: 6469
llm_latency_ms: 8152
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 769
our_published_at: '2026-08-29T02:11:21Z'
rewritten_title: Algorithme rapide pour calculer le volume d'un maillage 3D fermé
  via le théorème de divergence
source_published_at: '2026-08-28T09:00:46Z'
status: summarized
summarized_at: '2026-08-29T02:59:06.007865Z'
title: Hilariously fast volume computation with the divergence theorem (2018)
url: https://alyssarosenzweig.ca/blog/hilariously-fast-volume-computation-with-the-divergence-theorem.html
---

## Résumé de l'article

Cet article présente un algorithme efficace pour calculer le volume d'un maillage triangulé 3D fermé en utilisant le théorème de divergence. L'approche convertit l'intégrale de volume en intégrale de surface, puis en somme pondérée sur les triangles du maillage, éliminant tout besoin d'intégration numérique.

- L'algorithme est en O(n) où n est le nombre de triangles, sans boucles imbriquées ni opérations coûteuses de rendu
- Chaque triangle ne nécessite que sept additions et trois multiplications, rendant le calcul par-triangle très efficace
- Sur un Raspberry Pi à 60 fps, l'algorithme peut traiter environ 30 millions de triangles par image
- La dérivation repose sur le choix d'une fonction vectorielle dont la divergence vaut 1, appliquée via le théorème de divergence
- L'auteur découvre après publication qu'un article antérieur décrit le même algorithme avec une dérivation différente

## Discussion sur Hacker News (65 commentaires)

**Avis positifs** :
- La méthode est élégante, rapide et basée sur des principes mathématiques simples (théorème de la divergence, formule du shoelace généralisée en 3D)
- L'algorithme est pratique : il peut traiter ~30 millions de triangles par frame sur un Raspberry Pi, sans GPU
- Robust aux imprécisions du maillage (triangles mal jointés donnent des résultats raisonnables)
- Permet de généraliser à d'autres calculs : moments, matrices d'inertie, intégrales de champs scalaires via le théorème de Stokes généralisé
- Bonne approche pédagogique : dérivation claire étape par étape, reconnaît les travaux antérieurs (1970s, 1980s, shoelace 2D du 18e siècle)

**Avis négatifs** :
- La technique n'est pas nouvelle : connue depuis au moins 1970 (Messner et Taylor), réinvention du shoelace formula 3D, formule du surveyeur
- Nécessite des préconditions strictes : maillage simple et fermé, sinon les résultats peuvent être invalides
- Pour les applications pratiques, pré-calculer et stocker le volume est souvent plus efficace que de le recalculer à chaque frame
- Le calcul du volume via tetraèdres vers l'origine était déjà connu et offre essentiellement la même solution avec une présentation différente
- Pour les maillages denses, le rendu GPU avec sommation par pixels peut être plus efficace grâce au parallélisme matériel

**Top commentaires** :

- [physicsguy](https://news.ycombinator.com/item?id=49477090) : This is one of those when you go "Huh, this is amazing!" or "Huh, I thought this trick was really well known!" depending on your background ;\) Here's a similar impl from 1980 written in Fortran that also computes other properties like centroid: https://calgo.acm.org/550.zip Algorithm 550: Solid Pol…
- [eterevsky](https://news.ycombinator.com/item?id=49476604) : Isn't the same as just taking every triangle from the mesh, calculating the volume of a prism-like polytope between it and its projection on one the planes, and then taking it with a + sign if its projection is oriented in one direction, and with a - sign if it's oriented in another? This kind of f…
- [srean](https://news.ycombinator.com/item?id=49477382) : On the other hand, if you want to compute the area of a polygon that have vertices at lattice points, you can count the number of interior points I, the number of boundary points B. Then the area A is A = I + B/2 - 1 This is Pick's theorem https://en.wikipedia.org/wiki/Pick's\_theorem one of my favo…

---

[Article original](https://alyssarosenzweig.ca/blog/hilariously-fast-volume-computation-with-the-divergence-theorem.html) · [Discussion HN](https://news.ycombinator.com/item?id=49476143)
