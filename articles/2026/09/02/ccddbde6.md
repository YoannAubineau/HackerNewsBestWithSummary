---
article_fetched_at: '2026-09-02T05:17:04.249226Z'
attempts: 0
content_source: extracted
discussion_comment_count: 146
discussion_fetched_at: '2026-09-02T05:16:59.951194Z'
error: null
guid: https://news.ycombinator.com/item?id=49525297
hn_item_id: 49525297
hn_url: https://news.ycombinator.com/item?id=49525297
is_ask_or_show_hn: false
llm_input_tokens: 13964
llm_latency_ms: 10711
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 929
our_published_at: '2026-09-02T05:13:57Z'
rewritten_title: Le créateur de Jujutsu devient directeur technique chez East River
  Source Control
source_published_at: '2026-09-01T17:46:21Z'
status: summarized
summarized_at: '2026-09-02T05:17:48.324207Z'
title: The creator of Jujutsu has joined ERSC
url: https://ersc.io/blog/martin-joins-ersc
---

## Résumé de l'article

Martin von Zweigbergk, créateur du système de contrôle de version Jujutsu, a été nommé directeur technique (CTO) d'East River Source Control, une entreprise fondée en 2025 qui développe des outils de gestion de code source nouvelle génération adaptés aux besoins de l'industrie du logiciel à l'ère de l'IA.

- von Zweigbergk a lancé Jujutsu en tant que projet personnel en 2019 avant d'en faire son travail à temps plein chez Google ; le projet compte plus de 30 000 étoiles sur GitHub et est sous licence Apache 2.0
- Il a précédemment travaillé sur Fig, un client Mercurial pour Google, et a contribué à Git, utilisé professionnellement par 96 % des développeurs selon le sondage Stack Overflow 2022
- East River Source Control crée des outils pour aider les organisations à gérer les besoins croissants en gestion et collaboration du code source, avec un lancement en bêta privée de son stockage prévu plus tard dans le mois
- von Zweigbergk restera un mainteneur principal de Jujutsu en tant que projet open source, mais l'entreprise prévoit de développer une couche de stockage nouvelle génération pour dépasser les limites de Git à grande échelle

## Discussion sur Hacker News (146 commentaires)

**Avis positifs** :
- jj offre des améliorations UX significatives par rapport à git (undo universel, gestion des conflits différée et non destructive, rebasing/squashing/splitting plus intuitif)
- jj fonctionne de manière transparente avec les repos git existants sans migration de données, permettant une adoption progressive sans friction pour les équipes
- ERSC cible un vrai problème d'entreprise : la limitation de git pour les monorepos à grande échelle et les workflows avec agents IA, domaine où Google et Meta ont dû développer des solutions propriétaires
- Le modèle transactionnel interne de jj (op log, change-id) crée une base architecturale solide pour implémenter facilement l'undo et d'autres fonctionnalités avancées
- jj maintient un équilibre sain entre développement commercial et open source : Martin continue comme mainteneur core, la gouvernance du projet inclut des contre-poids contre la sur-représentation des employés ERSC

**Avis négatifs** :
- jj reste confronté à des limitations techniques (pas de support des submodules git, certaines features de git comme le bisect pas encore implémentées)
- Le site web d'ERSC a des problèmes de performance importants (animation GPU-intensive, comportement choppy sur plusieurs navigateurs/OS), contredisant le positionnement infrastructure-focused
- Les détails techniques du problème que ERSC résout restent vagues et tenus secrets ('we'll talk about it later'), rendant difficile d'évaluer si c'est un vrai problème ou du marketing
- La syntaxe de revset de jj (@--+:: etc) et l'apprentissage conceptuel nécessaire créent une barrière d'adoption, notamment pour les développeurs qui ne vivent pas dans les commits
- Le modèle est limité aux besoins d'entreprise au lancement : accès enterprise-only, pas d'onboarding self-service, risque de lock-in et questions sur la viabilité commerciale d'une nouvelle infrastructure VCS propriétaire

**Top commentaires** :

- [umvi](https://news.ycombinator.com/item?id=49529872) : I like the idea of jujutsu, but I must not operate at a scale where its "killer features" would truly shine. Git hardly ever gets in my way, I have never had to do complex octopus merges or anything like that. It's usually: feature branch, implement, merge, and occasionally fix a merge conflict. JJ…
- [steveklabnik](https://news.ycombinator.com/item?id=49525736) : Working with Martin has been a real pleasure, and we'll have some more stuff to talk about very soon!
- [fallat](https://news.ycombinator.com/item?id=49525911) : Someone will have to explain the value proposition to me... We have git. jujutsu works with git. git can do everything jujutsu can do \(otherwise, jujutsu couldn't work with git\). Thus, jujutsu is a UX / new steering wheel. ERSC is trying to be a GitHub competitor with what surplus value? Don't get…

---

[Article original](https://ersc.io/blog/martin-joins-ersc) · [Discussion HN](https://news.ycombinator.com/item?id=49525297)
