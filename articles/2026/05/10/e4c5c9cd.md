---
article_fetched_at: '2026-05-10T13:30:17.420752Z'
attempts: 0
content_source: extracted
discussion_comment_count: 84
discussion_fetched_at: '2026-05-10T13:30:16.442824Z'
error: null
guid: https://news.ycombinator.com/item?id=48081245
hn_item_id: 48081245
hn_url: https://news.ycombinator.com/item?id=48081245
is_ask_or_show_hn: false
llm_input_tokens: 7749
llm_latency_ms: 10119
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 921
our_published_at: '2026-05-10T13:25:27Z'
rewritten_title: Debian impose désormais les paquets reproductibles dans ses nouvelles
  versions
source_published_at: '2026-05-10T05:26:03Z'
status: summarized
summarized_at: '2026-05-10T13:31:07.771162Z'
title: Debian must ship reproducible packages
url: https://lists.debian.org/debian-devel-announce/2026/05/msg00001.html
---

## Résumé de l'article

L'équipe de publication de Debian a annoncé que tous les paquets doivent être reproductibles, c'est-à-dire que leur compilation doit produire des binaires identiques. Cette décision s'appuie sur le projet Reproducible Builds et est appliquée via un blocage automatique de la migration des paquets non reproductibles.

- Les outils de migration Debian bloquent désormais les nouveaux paquets et les régressions de reproductibilité dans les paquets existants de testing
- L'équipe teste automatiquement les autopkgtests pour les binNMUs, renforçant le contrôle qualité du processus de migration
- L'ajout de l'architecture loong64 au dépôt a généré une queue importante dans l'infrastructure CI
- Les responsables de paquets restent responsables de leur migration et doivent corriger les regressions détectées dans les dépendances

## Discussion sur Hacker News (84 commentaires)

**Avis positifs** :
- Reproducible builds permettent à n'importe qui de reconstruire les paquets Debian et de vérifier qu'ils correspondent bit-à-bit à ceux publiés, éliminant ainsi le besoin de faire confiance à une seule autorité de compilation
- C'est une mesure de défense en profondeur qui empêche un attaquant avec accès aux clés de signature de Debian d'injecter discrètement des backdoors binaires sans modification du code source
- Les builds reproducibles sont une pratique essentielle en informatique industrielle et pour les applications critiques de sécurité, offrant une meilleure longevité et auditabilité des systèmes
- C'est une étape de qualité supplémentaire et un tremplin pour d'autres mesures de sécurité de la chaîne d'approvisionnement, comme les listes de matériaux logiciels (SBOM) requises par la loi européenne sur la résilience
- Debian s'aligne sur les pratiques déjà adoptées par d'autres systèmes comme NetBSD, Yocto et les environnements critiques, tout en menant l'effort dans l'écosystème Linux open source

**Avis négatifs** :
- Les builds reproducibles ne résolvent pas la menace d'amont : si le code source uploadé contient déjà une vulnérabilité ou un malware (comme XZ-Utils), cela sera reproduit de manière fiable dans les binaires
- Aucun vrai problème de sécurité détecté dans Debian n'aurait été empêché par des builds reproducibles depuis 2007, et les prétentions sans preuve sur des attaques internes non détectées relèvent de la spéculation
- Ce projet augmente considérablement la barrière à l'entrée pour les contributeurs à Debian et n'offre peu de bénéfices concrets comparé à d'autres mesures de sécurité plus efficaces
- Le terme « reproducible » est mal défini et exploité différemment par les projets : beaucoup de distributions incluent des dépendances binaires tierces, contrairement à une approche de bootstrap complète de 0 comme stagex
- Le temps et les ressources énormes investis auraient pu être mieux utilisés pour sécuriser des parties plus critiques de Debian ou améliorer d'autres protections plutôt que de réduire de simples différences de timestamps

**Top commentaires** :

- [uecker](https://news.ycombinator.com/item?id=48082436) : This is a huge achievement for Debian and the free software world. It took a while though until this was understood. In 2007 when pointing out on debian-devel that this is needed, I was still told what huge waste of time this would be. And indeed it took a huge amount of work by many people to get…
- [perlgeek](https://news.ycombinator.com/item?id=48082262) : https://wiki.debian.org/ReproducibleBuilds has some more infos; some is outdated, but it also has a chart showing how many packages are built in the CI, and how many of those are reproducible builds. \(Orange = FTBR = "failed to build reproducibly"\) I'm not good at reading numbers from charts, but I…
- [Zopieux](https://news.ycombinator.com/item?id=48082001) : A great milestone, congrats Debian on taking a stance and holding high standards for yourself, especially in the current era.

---

[Article original](https://lists.debian.org/debian-devel-announce/2026/05/msg00001.html) · [Discussion HN](https://news.ycombinator.com/item?id=48081245)
