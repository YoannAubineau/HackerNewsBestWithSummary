---
article_fetched_at: '2026-05-04T19:31:48.394955Z'
attempts: 0
content_source: extracted
discussion_comment_count: 116
discussion_fetched_at: '2026-05-04T19:31:47.928251Z'
error: null
feed_summary: '<p>Article URL: <a href="https://www.dayswithoutgithubincident.com/">https://www.dayswithoutgithubincident.com/</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=48012022">https://news.ycombinator.com/item?id=48012022</a></p>

  <p>Points: 255</p>

  <p># Comments: 96</p>'
guid: https://news.ycombinator.com/item?id=48012022
hn_item_id: 48012022
hn_url: https://news.ycombinator.com/item?id=48012022
is_ask_or_show_hn: false
llm_input_tokens: 8033
llm_latency_ms: 9389
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 778
our_published_at: '2026-05-04T18:59:53Z'
rewritten_title: GitHub affiche un compteur de jours sans incidents
source_published_at: '2026-05-04T17:36:32Z'
status: summarized
summarized_at: '2026-05-04T19:32:04.020550Z'
title: Days Without GitHub Incidents
url: https://www.dayswithoutgithubincident.com/
---

## Résumé de l'article

GitHub, la plateforme de gestion de code et de collaboration pour développeurs, affiche un compteur public du nombre de jours écoulés sans incident de service majeur. Le record actuel affiché est de 2026 jours.

- GitHub maintient publiquement un compteur visible du temps écoulé sans interruption de service
- Le score actuel affiché est de 2026 jours sans incident
- Ce type de compteur est souvent utilisé dans les industries critiques pour communiquer sur la fiabilité et la stabilité des services

## Discussion sur Hacker News (116 commentaires)

**Avis positifs** :
- GitHub fait face à des défis réels de scaling avec une augmentation de 14x du trafic, en partie due aux outils de codage IA générant massivement de PRs, ce qui représente une charge de travail exponentielle sur les CI/CD
- Les employés de GitHub méritent de l'empathie car ils gèrent une infrastructure critique pour le développement logiciel mondial et doivent refactoriser des systèmes distribués complexes construits avec des hypothèses anciennes
- GitHub a apporté une valeur énorme à l'open source et à la communauté des développeurs, créant du goodwill justifié malgré les problèmes actuels
- Le tracker d'incidents segmenté par service offre une utilité réelle : les utilisateurs qui ne dépendent que de certaines parties peuvent savoir que le reste du service reste opérationnel
- Les problèmes d'infrastructure affectant GitHub ne sont pas simples à résoudre rapidement, même avec du talent et de l'argent; les systèmes distribués à grande échelle demandent du temps

**Avis négatifs** :
- Microsoft/GitHub n'a pas pris les mesures basiques comme throttler les plans gratuits ou mettre en pause les inscriptions pour protéger les utilisateurs payants, alors que des solutions temporaires auraient pu être déployées rapidement
- Une augmentation de 14x de charge ne devrait pas causer ces niveaux de défaillance pour une entreprise de cette taille avec ce budget; d'autres plateformes (Netflix, YouTube, services de paiement) gèrent des volumes bien supérieurs
- GitHub facture le service en prétendant le fournir, tout en cachant l'ampleur réelle des pannes par une segmentation artificielle du statut page, ce qui frise la malhonnêteté commerciale
- Les problèmes existaient avant l'arrivée de l'IA; GitHub a des problèmes d'architecture baseline qu'aucun volume d'excuses technologiques ne peut justifier après une décennie de domination de marché
- Utiliser l'empathie envers les employés pour défendre une entreprise en manquement est une tactique détournée; les utilisateurs payants ont droit à une service fiable, et la responsabilité incombe au management et à l'organisation, pas à celui qui critique

**Top commentaires** :

- [dpe82](https://news.ycombinator.com/item?id=48013220) : I recently moved all my projects to a self-hosted forgejo instance and have found it quite satisfactory so far. And it's fast! If you're in the market for a github alternative, take a look - there are options.
- [gyoridavid](https://news.ycombinator.com/item?id=48013721) : I'm pretty sure we all took down a production enterprise system once or twice. At InVision we had an incident every week, despite all the SOPs and safety nets. And that way waaay before vibe coding..
- [reilly3000](https://news.ycombinator.com/item?id=48012495) : This is a real business continuity issue for us. We’re kinda stuck with GitHub Enterprise but we may need to move from cloud to on-premises if this keeps up.

---

[Article original](https://www.dayswithoutgithubincident.com/) · [Discussion HN](https://news.ycombinator.com/item?id=48012022)
