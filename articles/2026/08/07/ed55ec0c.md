---
article_fetched_at: '2026-08-07T21:29:39.216778Z'
attempts: 0
content_source: extracted
discussion_comment_count: 91
discussion_fetched_at: '2026-08-07T21:29:37.755833Z'
error: null
guid: https://news.ycombinator.com/item?id=49208535
hn_item_id: 49208535
hn_url: https://news.ycombinator.com/item?id=49208535
image_url: https://malisper.me/wp-content/uploads/2026/08/image.png
is_ask_or_show_hn: false
llm_input_tokens: 11739
llm_latency_ms: 15238
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1294
our_published_at: '2026-08-07T20:39:58Z'
rewritten_title: pgrust optimise les requêtes analytiques avec batching, fusion d'opérateurs
  et SIMD
source_published_at: '2026-08-07T11:00:35Z'
status: summarized
summarized_at: '2026-08-07T21:30:01.541988Z'
title: 'Making Postgres 300x faster for analytics: batching, operator fusion, and
  SIMD'
url: https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/
---

## Résumé de l'article

pgrust est un moteur de base de données analytiques qui atteint une performance 300 fois supérieure à Postgres sur le benchmark Clickbench grâce à des optimisations du moteur de requêtes. Le projet, en version 0.2, redéfinit l'exécution des requêtes en remplaçant le modèle Volcano hérité de Postgres par des techniques modernes adaptées aux architectures CPU et mémoire contemporaines.

- Le moteur de requêtes de pgrust représente environ 10 fois des 300 fois d'amélioration totale en performance analytique, grâce à trois optimisations principales : le batching (traitement par lots de 1024 lignes au lieu d'une ligne à la fois), la fusion d'opérateurs (combinaison des nœuds de scan et d'agrégation), et les instructions SIMD (opérations parallèles sur les CPU modernes)
- Postgres, conçu dans les années 1980 quand le I/O disque était le goulot d'étranglement, reste non optimisé pour les charges analytiques modernes où les données tiennent en RAM et où le CPU et la bande passante mémoire sont les vrais limiteurs
- Le modèle Volcano de Postgres appelle la fonction `next()` une seule fois par ligne, générant un surcoût significatif ; le batching réduit ce surcoût en traitant 1024 lignes par appel, diminuant le temps d'exécution de 1,3 secondes à 480 ms pour une somme sur 500 millions de nombres
- L'application successive de ces trois optimisations ramène le temps d'exécution de 1,3 secondes à 135 ms, soit une amélioration de 10 fois, et approche la performance d'une simple boucle for en Rust optimisée (358 ms vs 135 ms avec SIMD)
- pgrust surpasse même Clickhouse sur le benchmark analytique Clickbench, tout en restant 30 % plus rapide que Postgres sur les charges OLTP transactionnelles

## Discussion sur Hacker News (91 commentaires)

**Avis positifs** :
- La découverte de bugs réels dans PostgreSQL (dont un problème de comparaison de nombres flottants dans l'implémentation quadtree) valide l'approche de vérification formelle et fuzzing exhaustif du projet
- Les optimisations techniques (fusion d'opérateurs, SIMD, planification adaptative des requêtes) adressent des problèmes bien établis que PostgreSQL ne résout pas depuis une décennie, et les résultats sur ClickBench sont reproductibles
- L'approche AGPL est justifiée pour protéger contre l'appropriation par les géants du cloud (AWS, Google) qui monétisent les projets permissifs sans contribuer en retour; la possibilité de double-licence commerciale offre flexibilité
- La capacité à tester 15% des fonctionnalités utilisateur avec preuve formelle d'équivalence avec PostgreSQL, plus les engagements avec Antithesis et Aretta pour tests de défaillance sérieux, montre une rigueur rare pour un tel projet
- Les améliorations en matière d'optimisation (test mode réduisant le clonage de DB de 100ms à <10ms, planification de requêtes adaptative) ouvrent des cas d'usage nouveaux comme l'embedded database type SQLite

**Avis négatifs** :
- Le projet n'a que 2 commits visibles dans la branche principale, tous générés par Claude, sans transparence sur le processus exact; le manque d'humilité et la présentation comme un 'nous' collectif alors qu'il s'agit d'une personne pose des questions de crédibilité
- Le choix de l'AGPL, même avec justification, bloque l'adoption dans les environnements d'entreprise (Google, la plupart des grandes corporations bannissent cette licence pour des raisons légales, créant un fossé avec la cible commerciale)
- Les résultats de performance (300x) ne sont pas équitables : le test désactive le parallélisme PostgreSQL, n'inclut pas l'I/O disque, et comparaît un exemple de jouet contre une sérialisation complète en tuples; sans contexte réel, les chiffres sont trompeurs
- Le facteur bus est extrêmement risqué (une seule personne de confiance douteuse) pour une base de données critique; aucune gouvernance ou équipe établie ne peut justifier sa production pour les données sensibles pendant des années
- Le problème de droit d'auteur du code généré par l'IA reste flou légalement : récrire via Claude pour changer de licence MIT vers AGPL contourne peut-être les droits d'auteur mais soulève des questions éthiques sur l'utilisation des corpus de formation sans attribution

**Top commentaires** :

- [malisper](https://news.ycombinator.com/item?id=49212080) : Author here. Let me know if you have any questions about the post or about pgrust. Let me take a shot at answering what I think will be the most common question: how can I trust pgrust? Our \#1 priority right now is correctness. Over the past two weeks, I've done a mix of formal verification and dif…
- [sgt](https://news.ycombinator.com/item?id=49213729) : Cool project but .. reality is that people will generally not choose pgrust over Postgres, even 5-10 years from now. The problem is not that it may be technically superior and faster by then, it's that it's not built by the trusted Postgres team. There's a lot more to trust than development velocit…
- [patkepa](https://news.ycombinator.com/item?id=49216210) : Question, does having it in pure rust, opens possibility of embedding pgrust directly into binary, making it an alternative to SQLite/turso?

---

[Article original](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/) · [Discussion HN](https://news.ycombinator.com/item?id=49208535)
