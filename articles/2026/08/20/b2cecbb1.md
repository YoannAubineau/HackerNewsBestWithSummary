---
article_fetched_at: '2026-08-20T19:24:22.387765Z'
attempts: 0
content_source: extracted
discussion_comment_count: 249
discussion_fetched_at: '2026-08-20T19:24:18.866165Z'
error: null
guid: https://news.ycombinator.com/item?id=49374269
hn_item_id: 49374269
hn_url: https://news.ycombinator.com/item?id=49374269
image_url: https://safedep.io/images/arrayref-blog-blanner.png
is_ask_or_show_hn: false
llm_input_tokens: 26545
llm_latency_ms: 12413
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1019
our_published_at: '2026-08-20T19:16:43Z'
rewritten_title: Une crate Rust malveillante télécharge et exécute un binaire lors
  de la compilation
source_published_at: '2026-08-20T13:23:12Z'
status: summarized
summarized_at: '2026-08-20T19:25:02.034993Z'
title: Malicious Rust crate Arrayref runs a build-time payload
url: https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/
---

## Résumé de l'article

En août 2026, une version compromise de la crate populaire arrayref a été publiée sur crates.io. La version 0.3.10 ajoutait une dépendance vers une crate typosquattée appelée proc-macro1, dont le script de compilation télécharge et exécute un binaire distant pendant la compilation du projet. Le code s'exécute au moment de la compilation, ce qui rend l'infection effective dès qu'un projet compilant la mauvaise version.

- Le compte du mainteneur droundy a été compromis ; les versions malveillantes 0.3.5 à 0.3.9 ont été "yankées" pour forcer les développeurs vers la version malveillante 0.3.10
- La crate proc-macro1 est un clone renommé de la vraie crate proc-macro2 avec un script de compilation qui télécharge un binaire depuis 23.254.165.112:9089 et l'exécute détaché du processus de compilation
- Sur Unix, le payload est écrit dans /tmp/rust-setup et exécuté ; sur Windows, il est déployé via un script PowerShell lancé par WScript pour échapper à la gestion des processus de Cargo
- arrayref est largement utilisé en tant que dépendance transitive (245 millions de téléchargements cumulés), notamment dans les interfaces graphiques utilisant egui, eframe ou iced
- Les équipes de crates.io ont supprimé les versions malveillantes et les SHA256 des artefacts ont été documentés

## Discussion sur Hacker News (249 commentaires)

**Avis positifs** :
- Les attaques sur la chaîne d'approvisionnement Node.js se reproduisent maintenant dans d'autres écosystèmes, confirmant que c'est un problème systémique lié à la conception des gestionnaires de paquets modernes
- Cargo et les dépendances Rust présentent les mêmes failles de sécurité fondamentales que npm, rendant urgente une refonte des approches de gestion des dépendances
- Les machines de développement sont des cibles attrayantes car elles contiennent des credentials et peu de protections ; les attaques au moment du build capturent ces secrets avant que le code ne soit exécuté
- La sandbox et les capacités de sécurité au niveau du système d'exploitation sont essentielles mais largement ignorées pendant le développement, contrairement aux efforts massifs de sécurité à l'exécution
- Un délai minimum de publication et l'adoption de pratiques éprouvées (comme celles de pnpm) pourraient réduire significativement l'impact des attaques de chaîne d'approvisionnement

**Avis négatifs** :
- Restreindre les build scripts par défaut ne résout pas fondamentalement le problème : un attaquant peut tout aussi facilement modifier le code runtime, qui s'exécutera lors des tests ou de la production
- Sandboxer les build scripts est techniquement complexe (pas de standard cross-platform) et pourrait casser les cas d'usage légitimes comme la compilation de dépendances C
- Une stdlib plus grande ou plus de blessed crates ne changerait rien : arrayref était un petit crate dont la fonctionnalité existe maintenant en stdlib, mais l'écosystème est lent à adopter
- Blâmer la culture des micro-dépendances ignore que même les projets Go et Python avec des stdlibs solides finissent par avoir d'énormes arbres de dépendances transitives
- Les audits de sécurité centralisées ne sont pas viables à grande échelle sans financement massif ; cargo-vet et cargo-crev existent déjà mais souffrent de faible adoption et d'UX défaillante

**Top commentaires** :

- [cube00](https://news.ycombinator.com/item?id=49375609) : GitHub really needs something finer-grain then just pretending the repo never existed during these incidents. \[1\] The bad package version has also just disappeared from crates.io \[2\] with no indication its been yanked. There's no security advisory there either \[3\] "No advisories found for this crat…
- [cosmic\_cheese](https://news.ycombinator.com/item?id=49375369) : I think we should be taking a more “batteries included” approach to language and library design. The entire reason we’re in this mess is because we’ve decided it’s ok or maybe even preferable if stdlibs are rail thin, rendering base languages near-unusable. I can very easily build a highly function…
- [jakubadamw](https://news.ycombinator.com/item?id=49375101) : Cargo desperately needs sandboxing for build.rs scripts. It’s been attempted before, but didn’t go very far¹. ¹ https://rust-lang.github.io/goals/2024h2/sandboxed-build-scr...

---

[Article original](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/) · [Discussion HN](https://news.ycombinator.com/item?id=49374269)
