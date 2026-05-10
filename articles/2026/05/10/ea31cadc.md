---
article_fetched_at: '2026-05-10T14:24:42.801750Z'
attempts: 0
content_source: extracted
discussion_comment_count: 59
discussion_fetched_at: '2026-05-10T14:24:41.730315Z'
error: null
guid: https://news.ycombinator.com/item?id=48076815
hn_item_id: 48076815
hn_url: https://news.ycombinator.com/item?id=48076815
image_url: https://repository-images.githubusercontent.com/340518175/b16d0200-7540-11eb-9ca9-1b74271ac6f7
is_ask_or_show_hn: false
llm_input_tokens: 7032
llm_latency_ms: 11540
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 818
our_published_at: '2026-05-10T14:20:41Z'
rewritten_title: let-go, un dialecte Clojure écrit en Go avec démarrage en 7ms
source_published_at: '2026-05-09T17:52:13Z'
status: summarized
summarized_at: '2026-05-10T14:25:18.738724Z'
title: 'Show HN: I made a Clojure-like language in Go, boots in 7ms'
url: https://github.com/nooga/let-go
---

## Résumé de l'article

let-go est un dialecte Clojure avec compilateur bytecode et machine virtuelle à pile, écrit en Go. Il s'exécute en tant que binaire unique d'environ 10 Mo avec un démarrage froid de 7 ms, sans dépendre de la JVM, et affiche une compatibilité de 95% avec la suite de tests Clojure.

- Compilable en binaires autonomes, pages WASM auto-contenues ou bytecode ; supporte les scripts CLI, serveurs web et s'exécute même sur Plan 9
- Implémente la plupart des fonctionnalités Clojure (structures de données persistantes, lazy sequences, transducteurs, protocoles, records, multimethods, core.async, BigInts)
- Démarre 50 fois plus vite que Clojure JVM et 3 fois plus vite que Babashka sur les cas d'usage courts ; consomme moins de mémoire mais perd sur les calculs numériques intensifs
- Interopérabilité bidirectionnelle avec Go (fonctions, structs, channels) et support des pods Babashka (SQLite, AWS, Docker, etc.)
- Inclut un serveur nREPL compatible avec CIDER, Calva et Conjure pour l'intégration IDE ; peut être embarqué comme couche de scripting dans des programmes Go

## Discussion sur Hacker News (59 commentaires)

**Avis positifs** :
- Le démarrage en 7ms (temps avant exécution du code utilisateur, y compris compilation et chargement stdlib) répond à un vrai besoin que la JVM/Clojure n'avaient pas satisfait, notamment pour serverless et CLI
- L'approche Go offre une excellente base : runtime/stdlib solides, binaire unique, faible consommation mémoire et expressivité syntaxique supérieure à Go natif
- Le projet a une base fonctionnelle solide (macros, destructuring, core.async-like channels, REPL, nombreuses fonctions clojure.core) et une taille compact (~10MB)
- C'est une contribution utile dans un écosystème en expansion des langages compilés vers Go (Joe, Lisette, Glojure, Janet), signalant une demande réelle

**Avis négatifs** :
- Plusieurs variantes Clojure-like en Go existent déjà (Joker très apprécié, Glojure, Janet) avec des niveaux de maturité différents, questionnant la fragmentation de l'écosystème
- Incompatibilité avec les libs Clojure non modifiées (comme hiccup) limite l'effet réseau par rapport à Clojure/JVM
- L'interface README originale était meilleure; les améliorations AI-générées ont dégradé la clarté, signalant un manque d'implication personnelle
- La performance de la VM reste en retrait par rapport à d'autres approches (wazero), et les perf n'est pas la priorité affichée du projet

**Top commentaires** :

- [ingy](https://news.ycombinator.com/item?id=48079017) : Try out this Wasm browser REPL https://gloathub.org/repl/ Gloat is a Glojure AOT automation tool. I worked with James Hamlin to get Glojure AOT going last summer and have been moving it forward since. I've also been working with marcingas \(nooga\) to get Gloat/Glojure/let-go all cooperating.
- [boguscoder](https://news.ycombinator.com/item?id=48080767) : Micro nit: it says 7ms cold start and then 6ms just few lines lower.. maybe it gets faster as you read README
- [veqq](https://news.ycombinator.com/item?id=48080630) : Nice! I recently played around with a Lisp syntax for Go semantics: https://codeberg.org/veqq/Joe As far as JVM-free Clojure-like, Janet is really nice. I've been using it in production for a while: https://janet-lang.org/ There's also Fennel if you want the Lua vm and libraries.

---

[Article original](https://github.com/nooga/let-go) · [Discussion HN](https://news.ycombinator.com/item?id=48076815)
