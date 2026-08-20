---
article_fetched_at: '2026-08-20T16:23:36.836424Z'
attempts: 0
content_source: extracted
discussion_comment_count: 165
discussion_fetched_at: '2026-08-20T16:23:35.457141Z'
error: null
guid: https://news.ycombinator.com/item?id=49369408
hn_item_id: 49369408
hn_url: https://news.ycombinator.com/item?id=49369408
image_url: https://substackcdn.com/image/fetch/$s_!mvXW!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F20e598bd-cac0-4b10-8222-b432167c9159_5616x3744.jpeg
is_ask_or_show_hn: false
llm_input_tokens: 19669
llm_latency_ms: 12722
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 948
our_published_at: '2026-08-20T15:34:23Z'
rewritten_title: Utiliser les tours plutôt que les radians pour simplifier le code
  trigonométrique
source_published_at: '2026-08-20T01:29:12Z'
status: summarized
summarized_at: '2026-08-20T16:23:56.502460Z'
title: Turns are Better than Radians (2022)
url: https://www.computerenhance.com/p/turns-are-better-than-radians
---

## Résumé de l'article

L'article défend l'utilisation des tours (turns) — une paramétrisation des angles de 0 à 1 pour un cercle complet — à la place des radians dans le code, notamment pour les fonctions trigonométriques. Les tours correspondent à un concept mathématique légitime et offrent des avantages pratiques significatifs.

- Le code appelant multiplie souvent par π ou τ pour convertir en radians, alors que les implémentations de sin/cos divisent immédiatement par π (constante 4/π), créant une multiplication-division inutile
- Les valeurs communes en tours (0,25 pour 90°, 0,5 pour 180°, 0,75 pour 270°) se représentent exactement en virgule flottante, contrairement aux radians
- L'adoption des tours élimine les constantes π et τ du code applicatif et bibliothèque, simplifie la lisibilité et réduit les calculs
- Certaines bibliothèques proposent déjà des variantes comme sincospi (paramétrisée en demi-tours), disponibles par exemple en CUDA
- La transition est simple : modifier les fonctions sin/cos pour accepter des tours au lieu de radians ne requiert qu'un ajustement de constante

## Discussion sur Hacker News (165 commentaires)

**Avis positifs** :
- Les turns simplifient les angles courants (quarts, demi-tours) en évitant les nombres irrationnels, contrairement aux radians où π/2 reste irrationnel
- L'utilisation de turns peut améliorer les performances et réduire les erreurs d'arrondi dans les bibliothèques mathématiques, puisque les implémentations internes font déjà des conversions vers les turns
- Les turns s'adaptent naturellement à la représentation en virgule fixe ou entiers (ex: 256 valeurs pour un octet), permettant l'arithmétique modulaire sans conversion
- C'est un simple changement d'API local : rien n'empêche de définir des fonctions sin_turns() sans récrire toute l'analyse mathématique ou les bibliothèques existantes
- Euler's formula devient plus simple avec les turns (ex: -1^(2x) = cost(x) + i*sint(x)), éliminant π et e de la formulation

**Avis négatifs** :
- En calcul différentiel, la dérivée devient sin'_turns(x) = 2π*cos_turns(x), réintroduisant π partout et rendant les formules plus complexes que avec les radians
- Les radians sont le choix naturel pour les mathématiques pures : e^(ix) = cos(x) + i*sin(x) fonctionne élégamment uniquement avec les radians, et la dérivée de sin(x) est cos(x) sans facteur supplémentaire
- En physique et en calcul différentiel, les radians émergent naturellement de relations fondamentales comme l'arc de cercle et les équations différentielles, éliminant les facteurs de conversion ailleurs
- Les turns compliquent la représentation des petits angles (ex: arcseconde = 1/1,296,000 de tour) et les applications comme la formule de Vincenty en géodésie
- π est une constante fondamentale présente dans les surfaces et volumes des sphères, les transformations de Fourier et l'analyse dimensionnelle : on ne peut pas l'éliminer, seulement le déplacer

**Top commentaires** :

- [kazinator](https://news.ycombinator.com/item?id=49371469) : The math is definitely not fine with turns, because your Euler formula e^ix = cos x + i sin x no longer holds. We can use a base other than e, namely B = e^2pi which around 535.4916. This doesn't have the nice e properties like d/dx e^x = e^x. The elegant fact that the base of the natural logarithm…
- [srean](https://news.ycombinator.com/item?id=49374474) : Let's do a full circle. It all began with replacing frequent occurrence of 2π in calls of sin and cos functions with τ. This post suggests an optimisation by getting rid of τ by getting rid of radians. That way one can get rid of frequent and adjacent radians to degrees conversions and back. I say,…
- [WCSTombs](https://news.ycombinator.com/item?id=49370076) : I think I cautiously agree with this notion to some extent, but IMHO the real answer is that it's application-dependent, and if you're writing a low-level trig library and you have to pick one or the other, it really isn't clear to me that turns should win over radians. I expect many systems that u…

---

[Article original](https://www.computerenhance.com/p/turns-are-better-than-radians) · [Discussion HN](https://news.ycombinator.com/item?id=49369408)
