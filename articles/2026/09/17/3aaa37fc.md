---
article_fetched_at: '2026-09-17T17:57:06.665311Z'
attempts: 0
content_source: extracted
discussion_comment_count: 78
discussion_fetched_at: '2026-09-17T17:56:48.962999Z'
error: null
guid: https://news.ycombinator.com/item?id=49718773
hn_item_id: 49718773
hn_url: https://news.ycombinator.com/item?id=49718773
image_url: https://jakeasmith.com/blog/http-build-url/og.png
is_ask_or_show_hn: false
llm_input_tokens: 7633
llm_latency_ms: 10817
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 823
our_published_at: '2026-09-17T17:16:31Z'
rewritten_title: Un développeur déprécie son polyfill PHP de 2014 devenu omniprésent
  avec 20 millions d'installations
source_published_at: '2026-09-15T20:53:36Z'
status: summarized
summarized_at: '2026-09-17T17:58:16.139307Z'
title: My temporary PHP fix from 2014 has nearly 20M installs. Today I'm deprecating
  it
url: https://jakeasmith.com/blog/http-build-url/
---

## Résumé de l'article

Un polyfill PHP écrit en 2014 comme solution temporaire pour reproduire la fonction http_build_url() lors d'une migration a accumulé près de 20 millions d'installations via Packagist et s'est intégré dans des projets majeurs comme WPML et des distributions Linux. Son auteur a décidé de le déprécier plutôt que de le maintenir ou de le confier à un nouveau responsable, recommandant aux utilisateurs de migrer vers des solutions modernes.

- Le code initial de 174 lignes reproduisait une fonction d'extension PHP supprimée lors d'une migration de la version 5.2 à 5.3 chez AOL
- Le package reçoit encore plus de 400 000 installations mensuelles et est embarqué dans WPML (1,5 million de sites), les distributions Debian/Ubuntu et d'autres projets
- Des bugs non corrigés existent, notamment un qui supprime les lettres « a » du chemin quand celui-ci se termine par une barre oblique
- L'auteur refuse de maintenir le code ou de le transférer pour éviter les risques de sécurité liés à un changement de responsable sur un package critique non vérifié
- PHP 8.5 offre désormais une API URI native conforme aux standards, et la librairie URI du PHP League constituent de meilleures alternatives

## Discussion sur Hacker News (78 commentaires)

**Avis positifs** :
- La dépublication d'un package après 12 ans est pragmatique : maintenir du code obsolète dans une langue abandonnée pendant des années supplémentaires ne serait pas un bon usage du temps du mainteneur
- Le marquage comme abandonné sur Packagist suffit à alerter les utilisateurs via des avertissements lors de l'installation, ce qui incite les développeurs à migrer sans forcer une rupture totale
- L'open source n'impose pas une maintenance perpétuelle : les utilisateurs peuvent forker le projet s'ils en ont besoin, ce qui est la beauté du modèle open source
- Même l'IA ne résout pas le problème : les correctifs nécessitent une relecture rigoureuse, et fixer le bug pourrait créer une fausse attente de maintenance future

**Avis négatifs** :
- Avec 20 millions d'installations, abandonner le projet sans suggérer un remplaçant dans Packagist laisse les utilisateurs dans le vague sur les alternatives disponibles
- Un dernier release avec des notifications de migration intégrées aurait aidé les développeurs découvrant le package via d'anciennes réponses Stack Overflow des années plus tard
- Qualifier la dépendance passée au package de 'mauvaise idée' est condescendant envers les utilisateurs qui ont résolu des problèmes réels avec lui à l'époque
- L'absence de fix pour le bug connu (suppression des 'a' avec slash trailing) laisse potentiellement des applications défectueuses en production

**Top commentaires** :

- [Sander\_Marechal](https://news.ycombinator.com/item?id=49737297) : There is nothing as permanent as a temporary fix that works.
- [jakeasmith](https://news.ycombinator.com/item?id=49718838) : Author here, happy to answer any questions. I never imagined a polyfill for http\_build\_url would gain so much traction. After 12 years, deprecating it feels like the right move, especially given the new options from the community and PHP itself.
- [zackmorris](https://news.ycombinator.com/item?id=49742911) : PHP did extensions and PECL modules wrong, due to its roots as a web server language. With managed hosting, often PHP doesn't offer what we might think of as basic functionality, since the admin didn't install/enable it. So it makes sense that these little one-off packages exist to route around sna…

---

[Article original](https://jakeasmith.com/blog/http-build-url/) · [Discussion HN](https://news.ycombinator.com/item?id=49718773)
