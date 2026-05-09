---
article_fetched_at: '2026-04-27T14:40:46.540130Z'
attempts: 0
content_source: extracted
discussion_comment_count: 107
discussion_fetched_at: '2026-04-27T14:40:46.261942Z'
error: null
feed_summary: '<p>Article URL: <a href="https://github.com/pgbackrest/pgbackrest">https://github.com/pgbackrest/pgbackrest</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=47919997">https://news.ycombinator.com/item?id=47919997</a></p>

  <p>Points: 240</p>

  <p># Comments: 108</p>'
guid: https://news.ycombinator.com/item?id=47919997
hn_item_id: 47919997
hn_url: https://news.ycombinator.com/item?id=47919997
image_url: https://opengraph.githubassets.com/10fc0c8e2c9e79ec35304941d5b6ea2a66c38abbc535825def1a475c6012ab32/pgbackrest/pgbackrest
is_ask_or_show_hn: false
llm_input_tokens: 10506
llm_latency_ms: 12133
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 962
our_published_at: '2026-04-27T14:38:55Z'
rewritten_title: pgBackRest, outil de sauvegarde PostgreSQL, n'est plus maintenu
source_published_at: '2026-04-27T10:56:34Z'
status: summarized
summarized_at: '2026-04-27T14:41:04.887969Z'
title: Pgbackrest is no longer being maintained
url: https://github.com/pgbackrest/pgbackrest
---

## Résumé de l'article

Le créateur et mainteneur de pgBackRest, un logiciel de sauvegarde et restauration pour PostgreSQL, a annoncé l'arrêt du développement après 13 ans de travail. Cette décision intervient suite à la vente de son employeur précédent (Crunchy Data) et à l'incapacité à trouver un financement ou une position professionnelle permettant de poursuivre le projet.

- Le développeur ne peut plus consacrer le temps nécessaire au projet (maintenance, corrections de bugs, revue de code, support communautaire) tout en gagnant sa vie
- pgBackRest v2.58.0 reste la dernière version stable et le code source reste disponible pour d'éventuels forks, qui devront adopter un nouveau nom et construire leur crédibilité
- Le projet a bénéficié du parrainage de Crunchy Data, Resonate et Supabase au cours de son existence
- pgBackRest offrait des fonctionnalités avancées : sauvegardes parallélisées, compression efficace, archivage WAL asynchrone, chiffrement, et support des stockages cloud (S3, Azure, GCS)

## Discussion sur Hacker News (107 commentaires)

**Avis positifs** :
- Le projet a livré une excellente solution de sauvegarde PostgreSQL pendant plus de 13 ans avec une forte réputation et ~3,8k stars, méritant des remerciements pour ce travail exemplaire.
- La décision de l'auteur est légitime : après l'acquisition de Crunchy Data, il n'a trouvé ni emploi soutenant le projet ni sponsoring suffisant, et refuser de maintenir mal un logiciel critique est responsable.
- L'archivage du dépôt plutôt qu'une passation risquée est prudent : il prévient les attaques de supply chain et les pièges de maintenance par des inconnus sur un logiciel gérant des données sensibles en production.
- Des alternatives existent (WAL-G, Barman, pg_probackup, databasus) même si certaines n'offrent pas l'ensemble complet des fonctionnalités de pgBackRest.
- Le vrai problème n'est pas l'archivage mais l'incapacité structurelle du modèle économique actuel à financer les logiciels critiques open source, reflétant des faiblesses des écosystèmes de donation et de sponsorship.

**Avis négatifs** :
- Bloquer le nom du projet est excessif : au lieu d'archiver et d'interdire l'usage du nom, l'auteur aurait pu permettre une passation organisée avec obligations de qualité, comme d'autres projets (paperless-ng/ngx).
- Le code source reste disponible et forçable, mais l'absence de bénédiction officielle décourage les continuateurs potentiels et complique la confiance des utilisateurs envers un fork orphelin.
- La responsabilité repose unilatéralement sur le mainteneur bénévole, pas sur les utilisateurs/entreprises qui en tirent profit : forcer une passation n'est pas déraisonnable quand des milliers de bases de données dépendent du projet.
- Des structures comme la Fondation Apache auraient pu absorber le projet et gérer la gouvernance de succession de manière sûre, mais cette option n'a apparemment pas été explorée.
- Le timing malheureux (annonce immédiate, utilisateurs découvrant l'arrêt en configurant le projet) suggère une communication insuffisante vers la communauté avant l'archivage définitif.

**Top commentaires** :

- [radimm](https://news.ycombinator.com/item?id=47921198) : This is the message the author posted on LinkedIn: After a lot of thought, I have decided to stop working on pgBackRest. I did not come to this decision lightly. pgBackRest has been my passion project for the last thirteen years, and I was fortunate to have corporate sponsorship for much of this ti…
- [freakynit](https://news.ycombinator.com/item?id=47920386) : So sad to see this happening.. I had just last year prepared a detailed guide for reliable postgre backups to local volume as well as cloud storage, using pgBackRest, for my own projects.. pgBackRest have worked so well for me https://github.com/freakynit/postgre-backup-and-restore-guid... Thanks t…
- [j1elo](https://news.ycombinator.com/item?id=47920621) : Open Source has worked fine here. The author doesn't find financial support for the work, so they just want to change winds and that's a perfectly fine path forward. If this is really much more than a personal project "for fun, on my leisure time", and it became an actually serious product-level pr…

---

[Article original](https://github.com/pgbackrest/pgbackrest) · [Discussion HN](https://news.ycombinator.com/item?id=47919997)
