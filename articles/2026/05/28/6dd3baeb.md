---
article_fetched_at: '2026-05-28T13:09:31.095359Z'
attempts: 0
content_source: extracted
discussion_comment_count: 222
discussion_fetched_at: '2026-05-28T13:09:16.859566Z'
error: null
guid: https://news.ycombinator.com/item?id=48291575
hn_item_id: 48291575
hn_url: https://news.ycombinator.com/item?id=48291575
is_ask_or_show_hn: false
llm_input_tokens: 22017
llm_latency_ms: 16788
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 916
our_published_at: '2026-05-28T13:07:12Z'
rewritten_title: Go propose l'ajout de méthodes génériques aux fonctions avec récepteur
source_published_at: '2026-05-27T09:02:59Z'
status: summarized
summarized_at: '2026-05-28T13:10:03.983383Z'
title: 'Go: Support for Generic Methods'
url: https://github.com/golang/go/issues/77273
---

## Résumé de l'article

Go envisage d'autoriser les paramètres de type sur les méthodes concrètes (non-interface), de la même manière qu'ils existent déjà pour les fonctions. Cette proposition change de perspective : les méthodes génériques seraient utiles en elles-mêmes pour organiser le code, indépendamment de leur implémentation d'interfaces.

- Les méthodes génériques auraient la même syntaxe que les fonctions génériques mais avec un récepteur : `func (r Receiver) methodP any { … }`
- Les appels de méthodes génériques fonctionneraient comme les appels de fonctions génériques, avec inférence ou fourniture explicite de types d'arguments
- Une méthode générique n'implémenterait pas une interface car l'interface ne peut pas avoir de paramètres de type ; c'est une limitation acceptée
- La modification est entièrement rétrocompatible et ne bloque pas les futures méthodes d'interface génériques
- L'implémentation nécessiterait des ajustements du parser (mineurs), du vérificateur de types et du format d'export/import des données, mais la traduction conceptuelle en appels de fonctions génériques est comprise

## Discussion sur Hacker News (222 commentaires)

**Avis positifs** :
- Les génériques pour les méthodes comblent un vrai manque et répondent à des besoins réels que les développeurs attendaient depuis des années, particulièrement pour les API de bibliothèques.
- Go a toujours reconnu que les génériques étaient difficiles à implémenter correctement ; cette addition pragmatique montre une évolution réfléchie plutôt qu'une simple capitulation.
- Comparé à Java qui a attendu aussi longtemps, Go bénéficie de leçons tirées de l'histoire des langages et d'une meilleure compréhension des pièges à éviter.
- Le sucre syntaxique pour les méthodes génériques améliore l'ergonomie du code, notamment pour les appels chaînés et les signatures de type paramétré.
- L'implémentation par le même Philip Wadler qui a travaillé sur les génériques Java et la théorie monadique apporte un haut niveau d'expertise au design.

**Avis négatifs** :
- Go a passé des années à affirmer que les génériques n'étaient pas nécessaires, ce qui ressemble à du gaslighting quand la langue change finalement de cap sans jamais reconnaître les critiques antérieures.
- Les méthodes génériques ne peuvent pas implémenter les interfaces, ce qui limite drastiquement leur utilité et crée une solution de compromis plutôt que complète.
- Le design des génériques Go reste maladroit comparé à d'autres langages modernes ; cette implémentation tardive et fragmentée contient les cicatrices des compromis de compatibilité rétroactive.
- Go devrait depuis longtemps avoir des énums appropriés, la sécurité null, et une meilleure gestion d'erreurs ; les génériques pour les méthodes restera du sucre syntaxique tant que ces fondamentaux restent incomplets.
- L'approche itérative et lente de Go signifie qu'après 16 ans, la langue redécouvre laborieusement ce que d'autres ont résolu ; cela reflète une manque de vision de conception initiale plutôt qu'une amélioration pragmatique.

**Top commentaires** :

- [thayne](https://news.ycombinator.com/item?id=48303030) : « Go doesn't support such generic interface methods because we don't know how to implement \(calls of\) them, or at least we don't know how to implement them efficiently. » I don't really understand this argument. I read the discussion linked to\[1\], and yeah, monomorphization approaches \(whether at c…
- [klik99](https://news.ycombinator.com/item?id=48306994) : I remember lack of generics being pitched as a feature of Go initially, not a lack. The original design goal was simplicity. I don’t use Go, so have no opinion on this, just interesting that it’s going in this direction.
- [pjmlp](https://news.ycombinator.com/item?id=48304834) : Go becoming a proper 21st century language, is like pulling teeth. It is Apple's school of design, think different, ah, actually, there are reasons why the fence is in the middle of nowhere. Then the design ends up half way there versus being done properly from the beginning.

---

[Article original](https://github.com/golang/go/issues/77273) · [Discussion HN](https://news.ycombinator.com/item?id=48291575)
