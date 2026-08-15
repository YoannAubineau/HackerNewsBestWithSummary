---
article_fetched_at: '2026-08-15T17:13:23.474785Z'
attempts: 0
content_source: extracted
discussion_comment_count: 69
discussion_fetched_at: '2026-08-15T17:13:14.257832Z'
error: null
guid: https://news.ycombinator.com/item?id=49309549
hn_item_id: 49309549
hn_url: https://news.ycombinator.com/item?id=49309549
image_url: https://sankalp.bearblog.dev/static/og-image.png
is_ask_or_show_hn: false
llm_input_tokens: 13744
llm_latency_ms: 14179
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1147
our_published_at: '2026-08-15T16:20:58Z'
rewritten_title: Optimiser un kernel QR sur GPU grâce à auto-research et modèles d'IA
  pour atteindre 232x d'accélération
source_published_at: '2026-08-15T11:00:02Z'
status: summarized
summarized_at: '2026-08-15T17:14:13.912759Z'
title: 'Auto-research with codex: How I achieved a 232x Faster Kernel'
url: https://sankalp.bearblog.dev/autoresearch/
---

## Résumé de l'article

L'auteur a participé à un concours GPU Mode visant à optimiser une factorisation QR compacte Householder sur GPU, en utilisant des modèles d'IA (GPT-5.5/Codex et Claude) pour guider l'optimisation. Il a obtenu la 12ème place avec un speedup de 232x par rapport à la solution de base, passant de 419 ms à 1,8 ms de temps d'exécution moyen.

- Le problème demandait d'implémenter une factorisation QR par réflexions de Householder sur des matrices carrées FP32 en batch, avec accélération GPU. L'auteur a appliqué l'algorithme « blocked Householder » pour transformer le travail séquentiel en opérations GEMM exploitables par les tensor cores.
- L'approche reposait sur des **boucles d'auto-research** : plus de 1500 soumissions en 14 jours, avec logs détaillés des idées testées, accès à du profiling (Modal, NCU), et utilisation d'instructions `/goal` et `/advisor` pour guider les modèles d'IA sans interruption.
- Pour échapper aux optima locaux autour de 3000 µs, l'auteur a maintenu un **beam de 3-5 candidats** parallèles plutôt qu'une seule meilleure solution, encouragé le modèle à prendre des risques, et utilisé des sous-agents pour explorer des idées ambitieuses (réductions fusionnées, optimisations compilateur, précision mixte).
- Les principaux goulots d'étranglement résolvables étaient le **surcoût de lancement** (launch overhead) et le **surcoût du panel**, rarement des limitations mémoire ou calcul. L'optimisation a progressé en réduisant ces frais indirects et en rendant les mises à jour WY plus GEMM-compatibles.
- Parmi les regrets : ne pas avoir exploré les distributions d'entrée (dense, rank-déficient, etc.), gardé assez de travail en FP16, utilisé les instructions TCgen05 de Blackwell, ou maintenu le beam de candidats dès le départ.

## Discussion sur Hacker News (69 commentaires)

**Avis positifs** :
- Les LLM excellen dans les boucles benchmark-profile-verify-research-improve avec des contraintes bien définies et une vérification automatique possible, permettant une optimisation autonome rapide et peu coûteuse
- Les modèles sont particulièrement performants pour identifier et transférer des optimisations entre implémentations similaires (C++ vers C#, entre versions de codecs) et pour générer du code SIMD/CUDA complexe
- L'approche démontre des gains mesurables considérables (232x, 2x en single-core, réductions de 1.6s à 200ms) en quelques heures pour un coût minimal ($0.2 pour FlashAttention)
- Les kernels GPU et opérations SIMD sont particulièrement adaptés car ils bénéficient d'oracles observables (profilers, compteurs de performance) et de vérification automatique, contrairement à d'autres domaines

**Avis négatifs** :
- Les solutions optimisées par LLM suroptimisent souvent pour les cas d'entrée spécifiques (8/10 solutions top se cassaient hors de la distribution de test), manquent de généralité et de stabilité numérique comparées aux solutions d'experts
- Les LLM ne peuvent pas terminer des boucles sans oracle observables et déclarent faussement les tâches complètes quand aucun signal d'erreur n'existe; ils rapportent aussi le succès même quand échoués si on les interroge après
- L'approche nécessite une direction humaine significative pour éviter que le LLM ne prenne des raccourcis ou triche (crasher du code plutôt que de l'optimiser), contrairement à la promesse d'autopilotage
- Les modèles sont mauvais pour les tâches visuelles et UI, rapportent des travaux comme terminés alors qu'ils ne le sont pas, et devinent des couleurs plutôt que de les extraire correctement

**Top commentaires** :

- [Almondsetat](https://news.ycombinator.com/item?id=49309929) : In the last couple of days I wanted to try out the new definitive DeepSeek v4 releases. I gave it the repository of a semi-abandoned video compression codec and I told it to perform the usual benchmark -\> profile -\> verify -\> research -\> improve loop. I specifically chose this codec because the aut…
- [augment\_me](https://news.ycombinator.com/item?id=49311399) : One thing worth to note in the competition is that 8 out of the 10 top solutions, which all happened to be optimized this way completely broke at any other input than the competition ones. The only solutions that did not break when tested with OOD shapes were made by experts who know a lot about GP…
- [sqquima](https://news.ycombinator.com/item?id=49310605) : Meta commentary but it felt fresh to read a long wall of text that didn't seem to be AI generated. Thanks.

---

[Article original](https://sankalp.bearblog.dev/autoresearch/) · [Discussion HN](https://news.ycombinator.com/item?id=49309549)
