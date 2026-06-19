---
article_fetched_at: '2026-06-19T21:24:18.851508Z'
attempts: 0
content_source: extracted
discussion_comment_count: 145
discussion_fetched_at: '2026-06-19T21:24:18.049149Z'
error: null
guid: https://news.ycombinator.com/item?id=48599515
hn_item_id: 48599515
hn_url: https://news.ycombinator.com/item?id=48599515
image_url: https://overreacted.io/there-are-no-instances-in-atproto/opengraph-image?5b0b970dfd19bb8c
is_ask_or_show_hn: false
llm_input_tokens: 20671
llm_latency_ms: 11901
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1012
our_published_at: '2026-06-19T21:08:02Z'
rewritten_title: ATProto sépare l'hébergement de l'agrégation, contrairement aux instances
  Mastodon
source_published_at: '2026-06-19T15:10:02Z'
status: summarized
summarized_at: '2026-06-19T21:24:37.473441Z'
title: There are no instances in ATProto
url: https://overreacted.io/there-are-no-instances-in-atproto/
---

## Résumé de l'article

ATProto est un protocole décentralisé qui distingue fondamentalement l'hébergement des données de leur agrégation par les applications, contrairement à Mastodon où ces deux fonctions sont couplées dans des instances autonomes. Cette architecture s'inspire du modèle des blogs et des flux RSS, où le contenu existe indépendamment des applications qui le consultent.

- ATProto n'a pas d'instances au sens Mastodon : il n'y a pas de « boîtes » autonomes qui hébergent à la fois les données et les applications, mais plutôt un système où chacun peut héberger ses données et où plusieurs applications agrègent le contenu de tous les utilisateurs.
- Les utilisateurs d'ATProto peuvent changer d'hébergement (migrer vers un autre fournisseur ou auto-héberger) sans perdre leur identité, et les applications tierces peuvent accéder aux mêmes données sans dépendre de Bluesky.
- La décentralisation dans ATProto se mesure par la diversité des hébergeurs et des applications, pas par le nombre de boîtes isolées ; c'est comparable à la relation entre les blogs individuels et les agrégateurs comme Feedly ou Google Reader.
- Le couplage historique entre hébergement et application (modèle des réseaux sociaux traditionnels et de Mastodon) crée des problèmes d'incitations économiques et de contrôle centralisé ; ATProto résout cela en les séparant au niveau du protocole.

## Discussion sur Hacker News (145 commentaires)

**Avis positifs** :
- ATProto sépare efficacement l'hébergement des données, les applications et la modération, offrant une flexibilité impossible avec Mastodon où ces éléments sont couplés dans des instances monolithiques
- L'architecture permet aux utilisateurs de changer d'application ou de fournisseur d'hébergement sans perdre leur identité ou leurs données, contrairement à ActivityPub où migrer impose généralement de recréer un compte
- Le modèle de données partagées et réutilisables entre applications crée un écosystème de contenus ouvert similaire à RSS, où différentes applications peuvent indexer et présenter les mêmes données différemment
- Les relais et composants d'ATProto ne sont pas structurellement coûteux (environ 30$/mois) et le système n'impose pas de dépendre d'une unique entité centrale pour chaque fonction
- La clarification des rôles séparés (hébergement, app, modération) rend les problèmes de censure plus granulaires et évite le blocage en bloc d'une instance entière

**Avis négatifs** :
- En pratique, Bluesky PBC héberge 99%+ des données utilisateurs et fournit l'appview par défaut, créant une dépendance centralisée de facto malgré la théorie décentralisée
- Le modèle ne résout pas réellement les problèmes que les instances resolvent dans Mastodon : les appviews deviennent de facto des instances avec modération propre, mais sans la pluralité réelle de choix
- Les composants critiques comme le PLC directory et les relais performants reste limités, et lancer une alternative complète à Bluesky AppView reste pratiquement impossible pour la plupart
- L'économie du système décourage la multiplication d'alternatives viables : peu d'incitatifs financiers pour maintenir gratuitement des relais ou appviews concurrents quand Bluesky l'offre déjà
- Pour l'utilisateur moyen, l'expérience reste centralisée : il choisit bsky.app par défaut et doit être technique pour explorer des alternatives, ce qui ne diffère pas fondamentalement de Mastodon/mastodon.social

**Top commentaires** :

- [1dom](https://news.ycombinator.com/item?id=48601340) : « Every single time a post about atproto hits Hacker News, somebody asks in the comments: “But where are all the Bluesky instances?”. The problem is, there are no instances in atproto! The question is a category error. Instances are a Mastodon-brained concept, and I wanted something I can link to »…
- [p4bl0](https://news.ycombinator.com/item?id=48601880) : I think the analogy presented here is broken. RSS doesn't depend on Google Reader at all. Even at its prime, RSS depended less on Google Reader than email depends on Gmail now. In ATProto, AppViews heavily depends on Relays to be useful, and Relays are quite expensive to run. Also, the yellow circl…
- [muglug](https://news.ycombinator.com/item?id=48600835) : As far as I can tell, Relays\[1\] are the glue that makes ATProto work performantly. I think they're supposed to be content-agnostic — they just shuttle data through, reducing the number of services each AppView needs to be aware of. As the blog mentions, the big improvement vs Mastodon is that Relay…

---

[Article original](https://overreacted.io/there-are-no-instances-in-atproto/) · [Discussion HN](https://news.ycombinator.com/item?id=48599515)
