---
article_fetched_at: '2026-05-18T22:30:33.751956Z'
attempts: 0
content_source: extracted
discussion_comment_count: 774
discussion_fetched_at: '2026-05-18T22:30:27.669880Z'
error: null
guid: https://news.ycombinator.com/item?id=48132488
hn_item_id: 48132488
hn_url: https://news.ycombinator.com/item?id=48132488
is_ask_or_show_hn: false
llm_input_tokens: 58200
llm_latency_ms: 10138
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 744
our_published_at: '2026-05-14T18:00:12Z'
rewritten_title: La réécriture de Bun en Rust a été intégrée au code principal
source_published_at: '2026-05-14T08:15:31Z'
status: summarized
summarized_at: '2026-05-18T22:31:47.969655Z'
title: Rewrite Bun in Rust has been merged
url: https://github.com/oven-sh/bun/pull/30412
---

## Résumé de l'article

Bun, un runtime JavaScript/TypeScript, a été réécrit de C++ en Rust et intégré au projet principal. Cette migration maintient l'architecture et les structures de données existantes tout en apportant des améliorations significatives.

- Le binaire est réduit de 3 à 8 MB et les performances restent neutres à plus rapides
- La passe complète de la suite de tests existante sur toutes les plateformes, avec correction de fuites mémoire et tests instables
- Rust fournit une assistance du compilateur pour détecter et prévenir les bugs mémoire, problème qui a consumé beaucoup de ressources développement
- L'architecture générale, les structures de données et l'approche minimaliste en dépendances externes restent inchangées
- Les développeurs peuvent tester via `bun upgrade --canary` ; optimisations et nettoyage de code à venir avant publication stable

## Discussion sur Hacker News (774 commentaires)

**Avis positifs** :
- Le passage à Rust élimine une large classe de bugs mémoire (use-after-free, double-free) qui affligeaient Bun en Zig, grâce aux garanties du compilateur Rust même avec du code unsafe
- La suite de tests exhaustive et le grand nombre d'utilisateurs permettront de détecter rapidement les régressions en phase canary avant un passage en stable
- C'est une preuve impressionnante des capacités des LLMs pour les tâches de traduction mécanique de code avec spécifications claires et tests exhaustifs disponibles
- Le maintien du Zig en parallèle offre une voie de secours et permet des tests comparatifs A/B si nécessaire avant dépréciement complet

**Avis négatifs** :
- Fusionner 1M+ lignes non examinées par des humains en 9 jours viole les principes basiques d'ingénierie logicielle, aucune personne n'a pu relire le code ou comprendre l'architecture
- Les 10k+ blocs unsafe minimisent les avantages de Rust ; c'est essentiellement du code Zig habillé en syntaxe Rust sans bénéfices de sécurité réels à court terme
- Les messages contradictoires (« c'est juste une expérience, probablement jeté » une semaine plus tôt) suscitent des soupçons sur le manque de transparence et les motivations marketing d'Anthropic plutôt que techniques
- Les tests eux-mêmes ont été modifiés pour passer (ajout de délais, augmentation de profondeurs de récursion) sans distinction claire entre vrais correctifs et contournements

**Top commentaires** :

- [sesm](https://news.ycombinator.com/item?id=48140229) : When announcements say that rewrite took 1 week, I wonder how much time went into preparing this file with very detailed instructions on mapping Zig to Rust idioms: https://github.com/oven-sh/bun/commit/46d3bc29f270fa881dd573... On top of that, if you look at 'Pointers & ownership' and 'Collections…
- [Jarred](https://news.ycombinator.com/item?id=48133519) : Still writing the blog post about this. Will share more details. For where this is coming from, skim the bugfixes in the Bun v1.3.14 and earlier release notes. Rust won’t catch all of these - leaks from holding references too long and anything that re-enters across the JS boundary are still on us.…
- [gm678](https://news.ycombinator.com/item?id=48138915) : $ rg 'unsafe \[{\]' src/ | wc -l 10428 $ rg 'unsafe \[{\]' src/ -l | wc -l 736 Language Files Lines Code Comments Blanks ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Rust 1443 929213 732281 116293 80639 Zig 1298 711112 574563 59118 77431 TypeScript 2604 654684 510464 82254 61966 JavaSc…

---

[Article original](https://github.com/oven-sh/bun/pull/30412) · [Discussion HN](https://news.ycombinator.com/item?id=48132488)
