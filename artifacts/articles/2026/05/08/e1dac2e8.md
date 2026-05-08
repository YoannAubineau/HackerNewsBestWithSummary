---
article_fetched_at: '2026-05-08T17:30:32.052564Z'
attempts: 0
content_source: extracted
discussion_comment_count: 56
discussion_fetched_at: '2026-05-08T17:30:31.710226Z'
error: null
feed_summary: '<p>Article URL: <a href="https://clojurescript.org/news/2026-05-07-release">https://clojurescript.org/news/2026-05-07-release</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=48059662">https://news.ycombinator.com/item?id=48059662</a></p>

  <p>Points: 233</p>

  <p># Comments: 55</p>'
guid: https://news.ycombinator.com/item?id=48059662
hn_item_id: 48059662
hn_url: https://news.ycombinator.com/item?id=48059662
is_ask_or_show_hn: false
llm_input_tokens: 6583
llm_latency_ms: 7845
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 698
our_published_at: '2026-05-08T17:04:58Z'
rewritten_title: ClojureScript ajoute le support des fonctions async et await
source_published_at: '2026-05-08T07:04:24Z'
status: summarized
summarized_at: '2026-05-08T17:30:46.148647Z'
title: ClojureScript Gets Async/Await
url: https://clojurescript.org/news/2026-05-07-release
---

## Résumé de l'article

ClojureScript, un dialecte de Clojure compilé en JavaScript, a ajouté le support natif des fonctions asynchrones avec la syntaxe async/await. Cette amélioration permet au compilateur d'émettre des fonctions JavaScript async lorsqu'une fonction est annotée avec ^:async.

- L'annotation ^:async sur une fonction ClojureScript génère automatiquement une fonction JavaScript async équivalente
- L'opérateur await peut être utilisé pour attendre les Promises au sein de ces fonctions asynchrones
- Cette fonctionnalité fonctionne également pour les tests unitaires annotés avec ^:async
- Cette amélioration a été très demandée dans les sondages communautaires comme priorité pour l'interopérabilité JavaScript
- Elle élimine le besoin de dépendances externes pour interagir avec les APIs modernes du navigateur et les bibliothèques JavaScript populaires

## Discussion sur Hacker News (56 commentaires)

**Avis positifs** :
- ClojureScript avait déjà des capacités asynchrones sophistiquées via core.async bien avant que JavaScript n'adopte async/await, montrant la puissance des macros Lisp pour étendre le langage.
- Cette nouvelle fonctionnalité améliore l'interopérabilité JavaScript native sans dépendre de bibliothèques supplémentaires, facilitant l'adoption et la maintenance.
- Reagent et les composants ClojureScript offrent une meilleure expérience développeur que React en JavaScript, avec une séparation plus claire entre éléments statiques et dynamiques.
- L'écosystème Clojure favorise les bonnes pratiques (tests extensifs, immuabilité par défaut, REPL interactif) qui facilitent le travail avec les agents IA et rendent le code plus robuste.

**Avis négatifs** :
- core.async a des limitations significatives : il gonfle les artefacts JavaScript, manque d'un modèle d'erreur inhérent, et génère du code d'automate d'état difficile à déboguer.
- ClojureScript reste une technologie obscure comparée à JavaScript ou TypeScript, ce qui limite l'adoption professionnelle et rend les LLM moins efficaces pour générer du code.
- La dépendance au Google Closure Compiler impose toujours une surcharge significative en 2026 alors que des minificateurs et optimiseurs JS modernes existent.
- Adopter ClojureScript en production reste difficile et délicat en dehors de boutiques Clojure existantes, et nombreux sont ceux qui ont quitté l'écosystème.

**Top commentaires** :

- [koito17](https://news.ycombinator.com/item?id=48065996) : I noticed borkdude posted this thread \*and\* he is listed as a contributor for this release. For the longest time, I recall the opposition to async/await support being twofold: 1. adding support would require deep changes across the CLJS compiler \(theller, creator of shadow-cljs, once tried and conc…
- [osener](https://news.ycombinator.com/item?id=48061748) : Surprised to see Clojure/ClojureScript come up on socials more often all of a sudden. I used it professionally for a few years around ~2012 and like many others moved off JVM and moved into typed \[functional\] languages. Is the sudden buzz due to agentic coding? Does it rip through code faster with…
- [midnight\_eclair](https://news.ycombinator.com/item?id=48060138) : fun fact: clojurescript had support for asynchronous paradigm through core.async library \(CSP style\) long before async/await landed in javascript itself. edit: i'm in no way trying to diminish the value of this release, just pointing out how cool it is that you can get new language features before…

---

[Article original](https://clojurescript.org/news/2026-05-07-release) · [Discussion HN](https://news.ycombinator.com/item?id=48059662)
