---
article_fetched_at: '2026-07-20T17:25:24.128643Z'
attempts: 0
content_source: extracted
discussion_comment_count: 15
discussion_fetched_at: '2026-07-20T17:25:07.257360Z'
error: null
guid: https://news.ycombinator.com/item?id=48951898
hn_item_id: 48951898
hn_url: https://news.ycombinator.com/item?id=48951898
is_ask_or_show_hn: false
llm_input_tokens: 14409
llm_latency_ms: 12808
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 953
our_published_at: '2026-07-19T16:20:23Z'
rewritten_title: Optimiser les arbres de recherche statiques jusqu'à 40 fois plus
  rapide que la recherche binaire
source_published_at: '2026-07-17T20:24:55Z'
status: summarized
summarized_at: '2026-07-20T17:25:49.984030Z'
title: 'Static search trees: 40x faster than binary search (2024)'
url: https://curiouscoding.nl/posts/static-search-tree/
---

## Résumé de l'article

Cet article détaille l'optimisation d'une structure de données appelée S+ tree (arbre de recherche statique) pour interroger efficacement des listes triées de nombres entiers. Les S+ trees combinent les avantages des B-trees et de la disposition Eytzinger, en stockant les données dans des nœuds de 16 éléments alignés sur les lignes de cache.

- L'optimisation du nœud (fonction « find ») passe de 21 instructions en code branchant à 18 en vectorisation SIMD avec popcount, grâce à l'élimination des sauts précoces et de l'interleaving d'instructions.
- Le traitement par lots (batching) de 128 requêtes permet d'utiliser le parallélisme matériel : au lieu d'attendre 80 ns par lecture mémoire, 8 à 12 lectures en parallèle réduisent le temps amorti à environ 8 ns par requête.
- L'interleaving de plusieurs niveaux de recherche équilibre les parties liées au CPU (premiers niveaux, rapides) et à la mémoire (derniers niveaux, latents), atteignant un débit proche du maximum théorique de la bande passante disponible.
- Le partitionnement par les bits de poids fort accélère légèrement les petites données mais offre peu de gain sur les entrées volumineuses ; il augmente aussi la complexité du code sans justifier les bénéfices.
- L'article atteint un speedup global de 40× : de 1 150 ns/requête en recherche binaire classique à 27 ns/requête avec l'arbre optimisé et les requêtes interleavées sur une entrée de 4 GB.

## Discussion sur Hacker News (15 commentaires)

**Avis positifs** :
- La disposition Eytzinger en mémoire est effectivement optimale pour le cache : les premières couches de l'arbre tiennent dans une ligne de cache ou une page, réduisant drastiquement les défauts de cache lors de la recherche binaire
- Le concept n'est pas nouveau mais bien fondé : la même disposition est utilisée depuis longtemps dans les tas binaires (binary heaps), confirmant son efficacité pratique pour l'accès mémoire hiérarchique
- L'approche est valide pour des cas d'usage concrets comme l'indexation de données génomiques (tableaux de suffixes) où les données sont pré-triées et l'accès aux données est uniforme

**Avis négatifs** :
- Sur des données de taille normale, Eytzinger peut être moins performant qu'une simple recherche sur un tableau trié, remettant en question la pertinence pratique générale
- Les cas d'usage idéaux (données 32-bit triées uniformément) ne reflètent pas les vrais problèmes pour lesquels cette technique a été conçue, notamment la recherche dans des chaînes génomiques de milliards de caractères
- L'efficacité cache dépend à la fois de l'arrangement des données ET de l'algorithme d'accès utilisé : une mauvaise stratégie de lookup (comme une traversée en inorder ou une recherche B-tree sur cette structure) annule les bénéfices
- Les implémentations théoriquement supérieures (arbres Van Emde Boas) restent impraticables en raison de constantes trop élevées, suggérant que les gains réels peuvent être limités par des facteurs d'implémentation

**Top commentaires** :

- [kazinator](https://news.ycombinator.com/item?id=48954054) : « The main benefit of the Eytzinger layout is that all values needed for the first steps of the binary search are close together, so they can be cached efficiently: we put the root at index 1 and the two children of the node at index i are at 2i and 2i + 1. » This is exactly what is done in good ol…
- [TheRealPomax](https://news.ycombinator.com/item?id=48958969) : « Input. A sorted list of 32bit unsigned integers vals: Vec\<u32\>. » Okay, but that's not even remotely like the kind of input that this tree was created for. From the next paragraph, this work is in part \> \[...\] to make efficient datastructures to index DNA \[...\]. One such datastructure is the suff…
- [petters](https://news.ycombinator.com/item?id=48956944) : Why does figure 1 use the same color and style for two different graphs?

---

[Article original](https://curiouscoding.nl/posts/static-search-tree/) · [Discussion HN](https://news.ycombinator.com/item?id=48951898)
