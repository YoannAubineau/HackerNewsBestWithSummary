---
article_fetched_at: '2026-11-21T21:22:34.597801Z'
attempts: 0
content_source: extracted
discussion_comment_count: 504
discussion_fetched_at: '2026-11-21T21:22:21.566489Z'
error: null
guid: https://news.ycombinator.com/item?id=50589618
hn_item_id: 50589618
hn_url: https://news.ycombinator.com/item?id=50589618
image_url: https://leanprover-community.github.io/blog/meta-twitter.png
is_ask_or_show_hn: false
llm_input_tokens: 37045
llm_latency_ms: 10155
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1260
our_published_at: '2026-11-21T21:13:39Z'
rewritten_title: Une preuve de l'hypothèse de Riemann vérifiée en Lean par la communauté
  mathématique
source_published_at: '2026-11-21T14:36:45Z'
status: summarized
summarized_at: '2026-11-21T21:24:07.721719Z'
title: Lean verification of the Riemann Hypothesis
url: https://leanprover-community.github.io/blog/posts/riemann-hypothesis/
---

## Résumé de l'article

Le 20 novembre 2026, le mathématicien Levent Alpöge a publié une preuve de l'hypothèse de Riemann sous forme de bibliothèque Lean contenant 17 millions de lignes de code. La communauté Lean et Mathlib a validé cette preuve selon quatre critères formels : l'énoncé mathématique est correct, la bibliothèque compile sans erreur, le code prouve exactement l'hypothèse de Riemann selon la formulation Mathlib (vérifié par des outils indépendants), et la preuve Lean est valide (attestée par plusieurs vérificateurs de preuve incluant le noyau officiel de Lean et des vérificateurs formels tiers).

- L'énoncé de l'hypothèse de Riemann a été soigneusement examiné par des experts en Lean et en théorie des nombres et figure dans Mathlib sous le nom RiemannHypothesis.
- Des dizaines de personnes ont reproduit avec succès la compilation complète de la bibliothèque sans erreur ni défaut de construction.
- Deux outils de comparaison indépendants ont confirmé que le théorème prouvé par Alpöge correspond exactement à l'énoncé de l'hypothèse de Riemann dans Mathlib.
- La validité de la preuve a été vérifiée par plusieurs vérificateurs de preuve indépendants, dont certains disposent de preuves formelles garantissant qu'ils ne peuvent accepter une fausse preuve.

## Discussion sur Hacker News (504 commentaires)

**Avis positifs** :
- La vérification formelle en Lean établit un standard bien supérieur à la plupart des revues par pairs en mathématiques, éliminant pratiquement toute possibilité d'erreur grâce aux multiples vérificateurs indépendants et aux preuves de cohérence formelles.
- Le travail formalisé ouvre la voie à de nombreuses avancées futures : les techniques et lemmes découverts peuvent être exploités pour progresser sur d'autres problèmes ouverts, notamment via des connexions entre domaines mathématiques (géométrie algébrique, théorie analytique des nombres).
- Cette preuve constitue un triomphe de l'approche hybride humain-IA : Levent Alpöge, mathématicien expert, a guidé Claude de manière décisive, démontrant que le talent et l'expérience restent essentiels pour orienter les modèles vers des résultats significatifs.
- Le résultat confirme définitivement ce que les mathématiciens assumaient depuis longtemps, consolidant tous les théorèmes qui reposaient sur l'hypothèse de Riemann et épargnant aux chercheurs futurs de poursuivre la recherche de contre-exemples.
- L'écosystème mathématique formalisé en Lean bénéficiera à long terme : la preuve peut être progressivement simplifiée et refactorisée par la communauté pour extraire les insights centraux et les rendre réutilisables.

**Avis négatifs** :
- Les 17 millions de lignes de code Lean restent largement incompréhensibles et ne transmettent aucune intuition mathématique ; sans simplification majeure, cette preuve n'explique pas *pourquoi* l'hypothèse est vraie, limitant son apport à la compréhension mathématique.
- La fiabilité repose en dernier ressort sur la cohérence de ZFC et de la théorie des types sous-jacente, qui ne peuvent elles-mêmes être prouvées formellement (théorème d'incomplétude de Gödel), introduisant une couche d'hypothèses irréducibles souvent passée sous silence.
- Contrairement aux proofs d'Erdős ou Perelman, cet exploit requiert l'accès exclusif à des ressources computationnelles massives et à des modèles propriétaires d'Anthropic, ce qui démocratise peu la découverte mathématique et concentre le pouvoir chez les grandes corporations.
- La publication d'un bloc monolithique généralisé par IA tend à décourager les efforts de formalisation humaine et collaborative de Mathlib, potentiellement nuisant au projet à plus long terme de construire une base mathématique formalisée, compréhensible et réutilisable.
- Le fait que personne n'ait encore pu vérifier manuellement et expliquer la preuve soulève des questions épistémologiques : accepter une affirmation mathématique sur la base d'une vérification mécanique seule, sans compréhension conceptuelle, marque un changement fondamental dans la nature d'une preuve mathématique.

**Top commentaires** :

- [rcr-anti](https://news.ycombinator.com/item?id=50590943) : While still possible, the proof exploiting a bug is vanishingly small now. Following a few bugs and bad proofs this year, there are a number of different implementations, in different languages, and with different levels of proofs of their consistency. con-leche and con-ron are the heavy hitters, w…
- [henearkr](https://news.ycombinator.com/item?id=50593566) : So, will this hypothesis be renamed as a theorem? For example, will it become Riemann-Alpöge theorem? Or even Riemann-Alpöge-Masullo theorem, once Alessandro Maria Masullo's proof has been double-checked?
- [thejokeisonme](https://news.ycombinator.com/item?id=50590575) : A fake refutation of the Collatz conjecture already got through one of these independent checkers in the past. What's harder, proving GRH or finding a way to get through every checker \(which aren't as independent as they are sometimes touted to be\)? In this case there was a human expert in the loop…

---

[Article original](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) · [Discussion HN](https://news.ycombinator.com/item?id=50589618)
