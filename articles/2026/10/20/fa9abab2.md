---
article_fetched_at: '2026-10-21T00:15:56.681924Z'
attempts: 0
content_source: extracted
discussion_comment_count: 155
discussion_fetched_at: '2026-10-21T00:15:19.240581Z'
error: null
guid: https://news.ycombinator.com/item?id=50165953
hn_item_id: 50165953
hn_url: https://news.ycombinator.com/item?id=50165953
image_url: https://blog.cloudflare.com/_emdash/api/media/file/01M5C82XAYSWX571T82A8AZRKS.png
is_ask_or_show_hn: false
llm_input_tokens: 11982
llm_latency_ms: 15130
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1089
our_published_at: '2026-10-20T23:30:03Z'
rewritten_title: Tsrs, un port Rust du compilateur TypeScript, lancé par Cloudflare
  et collaborateurs
source_published_at: '2026-10-20T13:18:07Z'
status: summarized
summarized_at: '2026-10-21T00:17:25.260816Z'
title: 'Tsrs: A Port of TypeScript to Rust'
url: https://blog.cloudflare.com/typescript-rust-port/
---

## Résumé de l'article

Tsrs est un port du compilateur TypeScript écrit en Rust, développé en collaboration entre Cloudflare, VoidZero, Max Schwenk et l'équipe TypeScript officielle. Ce projet vise à accélérer les vérifications de type et à réduire l'utilisation mémoire tout en restant fidèle à l'implémentation d'origine de TypeScript.

- Les benchmarks précoces montrent que tsrs est jusqu'à 8 fois plus rapide et consomme environ 70 % moins de mémoire que TypeScript 7.0 avec le même nombre de workers de vérification de type
- Rust a été choisi notamment pour sa capacité à générer du WebAssembly efficace en mémoire, ce qui permet de faire fonctionner TypeScript dans les navigateurs, les Workers Cloudflare et les appareils embarqués
- Cloudflare appliquera le même processus de maintenance qu'avec Vinext (son fork de Next.js), avec des agents automatisés qui synchronisent quotidiennement les changements et exécutent les tests de compatibilité
- Le projet ne constitue pas un fork de TypeScript ; l'équipe TypeScript conserve le contrôle total de la conception et de la direction du langage, tandis que tsrs doit respecter strictement ses décisions
- Cloudflare envisage d'intégrer plus profondément tsrs dans son écosystème d'outils open source Rust (Vite, Rolldown, Oxlint, Oxfmt) et d'explorer des cas d'usage avancés avec les agents IA

## Discussion sur Hacker News (155 commentaires)

**Avis positifs** :
- Gains de performance significatifs (3-4x sur VSCode, jusqu'à 8x sur certains benchmarks) et réduction mémoire (~70%), particulièrement utiles à grande échelle pour les agents IA et les infrastructures cloud.
- Le port Rust offre des avantages techniques réels pour WASM : pas de garbage collector intégré, meilleure intégration avec l'écosystème edge computing de Cloudflare, et réduction de la taille des binaires WASM.
- La suite de tests existante de TypeScript a permis une vérification rigoureuse du port et garantit la compatibilité fonctionnelle, indépendamment du processus de portage.
- Les optimisations découvertes dans tsrs (lazy evaluation, allocation patterns) bénéficient aussi à TypeScript 7.1, montrant que le travail IA/manuel génère des insights exploitables au-delà du simple changement de langage.
- Absorption du projet concurrent tsgo-rs prévue, consolidant les efforts et évitant une fragmentation de l'écosystème.

**Avis négatifs** :
- L'entièreté du port est générée par IA sans implication humaine, soulevant des préoccupations sur les décisions architecturales, la maintenabilité à long terme et la capacité à innover au-delà du portage direct.
- Le modèle mémoire utilise des arènes jamais désallouées avec gestion manuelle des preuves de recyclage, contournant les garanties de sécurité de Rust par de l'unsafe caché, plus proche d'une approche C que d'un vrai Rust.
- Pour 99% des projets TypeScript, les gains de 10ms à 1ms sont imperceptibles (monitors à 60Hz), et la latence réseau domine en CI—l'utilité est limitée aux très gros usages (Cloudflare, OpenAI).
- Risque de fragmentation : accumulation de ports multiples (tsrs, tsgo, bun check, tsc-rs) plutôt qu'une amélioration du compilateur officiel, et questions sur la motivation de l'équipe TypeScript face à une version IA plus rapide.
- L'accent sur la génération IA remet en question la valeur du travail d'ingénierie humain et la durabilité des projets complexes si le coût cognitif du maintien décroît face à des remplacements rapides.

**Top commentaires** :

- [DanRosenwasser](https://news.ycombinator.com/item?id=50167925) : Hey there, TypeScript team member here. The tsrs project has been extremely interesting to see come together. We've been working with the maintainers to better understand how tsrs is fast and what sorts of optimizations it uses are safe. We even did our own Rust vibe port and what we currently susp…
- [afdbcreid](https://news.ycombinator.com/item?id=50167990) : It appears they're using a unique memory model \(https://github.com/oxc-project/tsrs/blob/main/docs/PORTING.m...\) to overcome the challenge that prevented the TypeScript team from choosing Rust to begin with: Rust has no GC and porting from a GC language to it often requires restructure of data. Ess…
- [sheepscreek](https://news.ycombinator.com/item?id=50167635) : Ah took me a while to understand the reason behind this. It wasn’t “let’s build a faster Rust based Typescript compiler” at all. That was a nice side-effect. They needed a Typescript compiler that can run on their WASM only sandbox. So the only existing option was to export tsc Go to WASM, but that…

---

[Article original](https://blog.cloudflare.com/typescript-rust-port/) · [Discussion HN](https://news.ycombinator.com/item?id=50165953)
