---
article_fetched_at: '2026-06-05T23:26:21.375480Z'
attempts: 0
content_source: extracted
discussion_comment_count: 243
discussion_fetched_at: '2026-06-05T23:26:20.515739Z'
error: null
guid: https://news.ycombinator.com/item?id=48411635
hn_item_id: 48411635
hn_url: https://news.ycombinator.com/item?id=48411635
is_ask_or_show_hn: false
llm_input_tokens: 31874
llm_latency_ms: 15949
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1241
our_published_at: '2026-06-05T22:32:27Z'
rewritten_title: Analyse empirique des bugs rsync avant et après commits assistés
  par Claude
source_published_at: '2026-06-05T12:43:33Z'
status: summarized
summarized_at: '2026-06-05T23:26:43.914382Z'
title: Did Claude increase bugs in rsync?
url: https://alexispurslane.github.io/rsync-analysis/
---

## Résumé de l'article

Un développeur a conduit une analyse statistique pour évaluer si l'utilisation de Claude pour générer du code a augmenté les bugs dans rsync, suite à une controverse en ligne basée sur des accusations sans preuves. rsync est un utilitaire Unix de synchronisation de fichiers très utilisé et stable.

- Deux releases contenant des commits assistés par Claude (v3.4.2 et v3.4.3) ont montré un taux de bugs pondérés par sévérité (0,29 et 2,59 bugs par 10 commits) qui se situent dans la plage historique normale, sans être des anomalies statistiques.
- Les tests statistiques (test de permutation exact et test exact de Fisher) indiquent que le taux de bugs des releases Claude n'est pas significativement différent du reste de l'historique rsync, avec une p-value d'environ 0,5 (comparable à un tirage au sort).
- Les releases Claude ont modifié beaucoup plus de lignes de code que la moyenne historique, mais sans augmentation proportionnelle du nombre de bugs, ce qui contredit l'hypothèse d'une dégradation liée à Claude.
- L'augmentation observée des changements et régressions était principalement due à une vague de rapports de CVE générés par des outils IA, forçant des corrections de sécurité rapides et extensives, plutôt qu'à une baisse de qualité du code assisté par Claude.
- La controverse a été alimentée par une corrélation spurieuse et une conviction a priori contre les LLM, plutôt que par des données empiriques, comme l'illustrent les débats sur les forums techniques (Hacker News, Lobsters).

## Discussion sur Hacker News (243 commentaires)

**Avis positifs** :
- L'analyse statistique montre que les releases avec Claude ne sont pas des anomalies : les bugs par commit se situent dans la distribution normale des versions précédentes, et une release antérieure à Claude avait bien plus de bugs sans susciter de réaction.
- Le contexte explique l'augmentation des commits : une vague de rapports de sécurité générés par l'IA a forcé des travaux défensifs massifs (tests, couverture de code, hardening), ce qui justifie l'accélération du développement indépendamment de la qualité du code.
- Les données brutes sont reproductibles et publiques (scripts Python, base de données) ; le code parle plus fort que le style de prose, et quiconque conteste les résultats peut les vérifier lui-même.
- Les reproches initiaux reposaient sur des anecdotes sélectionnées et aucune analyse sérieuse de sévérité comparée : l'absence de preuve d'une dégradation justifie le doute sur l'indignation généralisée.
- Le mainteneur d'rsync (Tridge) a lui-même confirmé les arbitrages délibérés (notamment les changements de sécurité au détriment de la compatibilité) et réfuté l'idée d'un 'vibe coding', reconnaissant une revue et une intention claires.

**Avis négatifs** :
- Avec seulement 2 releases marquées Claude, l'analyse manque cruellement de puissance statistique ; conclure l'absence de problème à partir de si peu de données viole les principes statistiques de base et confond absence de preuve avec preuve d'absence.
- La métrique 'bugs par commit' dissimule des dimensions critiques : elle ignore la sévérité (un crash systématique pèse autant qu'une typo), la complexité des changements, et masque l'augmentation extraordinaire de l'activité de commit qui pourrait indiquer un processus moins rigoureux.
- Plusieurs régressions sérieuses et confirmées (backups incrementaux cassées, incompatibilités de compatibilité ascendante non documentées) ne sont pas analysées en profondeur ; l'article escamote les vrais problèmes d'expérience utilisateur sous une argumentation statistique.
- L'analyse elle-même a d'abord été écrite avec un style LLM typique et reformulée après critique, ce qui mine la crédibilité sur la neutralité méthodologique ; l'auteur a un fort parti pris pro-IA et utilise le cadre statistique pour défendre une position antérieure.
- Tendre à blâmer uniquement les reporters et la mécanique des sécurité (plutôt que la qualité du code généré) évite la question centrale : si les LLM causent des rapports de sécurité massifs nécessitant une défense croissante, c'est un problème en soi, peu importe le taux de bugs final.

**Top commentaires** :

- [jarym](https://news.ycombinator.com/item?id=48419606) : I've been coding for over 2 decades. I love it, I've always loved it and I likely always will. I was an AI skeptic some months ago but truly Claude and Codex have changed my development style and velocity in a way I never imagined would ever be possible. With that, yes, I produce more code and am f…
- [GodelNumbering](https://news.ycombinator.com/item?id=48419197) : Was just looking at commits and came across a commit and its revert original commit: https://github.com/RsyncProject/rsync/commit/d046525de39315d... \`\`\` - if \(!ptr\) - ptr = malloc\(num \* size\); - else if \(ptr == do\_calloc\) + if \(!ptr || ptr == do\_calloc\) ptr = calloc\(num, size\); \`\`\` Written with cla…
- [RustyRussell](https://news.ycombinator.com/item?id=48419628) : For those commenting, I suggest you read the post linked by the rsync author: https://medium.com/@tridge60/rsync-and-outrage-d9849599e5a0 \(Disclosure: while I haven't talked with him in years, Tridge was my colleague and mentor for many years. I feel it is worth considering his view before joining…

---

[Article original](https://alexispurslane.github.io/rsync-analysis/) · [Discussion HN](https://news.ycombinator.com/item?id=48411635)
