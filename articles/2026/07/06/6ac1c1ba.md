---
article_fetched_at: '2026-07-06T08:11:36.615454Z'
attempts: 0
content_source: extracted
discussion_comment_count: 61
discussion_fetched_at: '2026-07-06T08:11:34.248812Z'
error: null
guid: https://news.ycombinator.com/item?id=48799155
hn_item_id: 48799155
hn_url: https://news.ycombinator.com/item?id=48799155
is_ask_or_show_hn: false
llm_input_tokens: 4432
llm_latency_ms: 9267
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 851
our_published_at: '2026-07-06T07:29:51Z'
rewritten_title: L'API du Art Institute of Chicago marque les œuvres visionnées moins
  de 200 fois
source_published_at: '2026-07-05T23:49:00Z'
status: summarized
summarized_at: '2026-07-06T08:12:07.081800Z'
title: Has_not_been_viewed_much
url: https://iamwillwang.com/notes/has-not-been-viewed-much/
---

## Résumé de l'article

L'API du Art Institute of Chicago, interface de programmation du musée américain permettant d'accéder aux données de ses collections, inclut un champ booléen nommé has_not_been_viewed_much. Ce champ indique si une œuvre d'art a été visionnée moins de 200 fois sur le site web du musée depuis janvier 2010.

- Le musée expose ainsi quelles œuvres de ses collections reçoivent peu d'attention du public en ligne
- Le seuil défini est fixé à moins de 200 consultations cumulées sur plus de 14 ans
- L'auteur soulève la question des raisons pour lesquelles certaines œuvres sont peu visitées numériquement

## Discussion sur Hacker News (61 commentaires)

**Avis positifs** :
- Le projet est créatif et innovant : il redonne vie à des œuvres oubliées du musée en mettant en lumière celles peu consultées, ce qui correspond probablement à l'intention des développeurs.
- L'expérience utilisateur est addictive et agréable : les utilisateurs trouvent des pépites artistiques surprenantes et apprécient la découverte progressive d'œuvres rares (sketches préparatoires, photographies, estampes japonaises, etc.).
- Le concept rappelle d'autres initiatives réussies de mise en avant du contenu négligé (articles Wikipedia peu lus, chansons Spotify sans écoutes, vidéos YouTube zéro-vues), montrant une tendance saine à valoriser ce qui passe inaperçu.
- L'API du musée permet une utilisation créative et directe, invitant les développeurs à innover autour des collections publiques.
- Les utilisateurs signalent une certaine magie émotionnelle à découvrir des œuvres oubliées, notamment en redécouvrant des photographies anciennes ou des détails artistiques rarement contemplés.

**Avis négatifs** :
- Le projet court le risque de détruire sa propre métrique : à mesure qu'il devient populaire via Hacker News, les images peu vues accumulent des visites et franchissent le seuil de 200 vues, disparaissant du pool de selection permanemment.
- L'interface présente des défauts techniques : naviguer loin du site et revenir ne permet jamais de retrouver l'œuvre consultée; certains utilisateurs signalent des erreurs de chargement dues à Cloudflare Turnstile.
- La conception pose un dilemme éthique : cliquer sur les œuvres qu'on aime les retire du pool pour les autres, inversant les incitations habituelles de découverte artistique.
- Les problèmes de comptabilité de vues persistent : les crawlers d'IA contemporains risquent de gonfler les chiffres artificiellement, rendant le critère des 200 vues depuis 2010 peu fiable.
- Certains utilisateurs expriment une ambivalence morale face au projet : « violer » la sacralité de ces œuvres oubliées, même pour les valoriser, soulève des questions éthiques.

**Top commentaires** :

- [ggm](https://news.ycombinator.com/item?id=48799768) : I used to borrow the books which had "to be disposed if not lent in the next 3 months" slip in them. Never regretted reading them. The best one included a very odd short story by Flann OBrien about a carpenter who walls himself inside the oak panelling of a build he is working on, and a woman convi…
- [noduerme](https://news.ycombinator.com/item?id=48801864) : Just professionally, I'm curious whether they derive has\_not\_been\_viewed\_much by some nightly cron process, by an insert trigger on a \`user\_image\_viewed\` table, or by some monstrous full table join that HN is currently obliterating.
- [anilakar](https://news.ycombinator.com/item?id=48801240) : This feels like I am violating something that is sacred. The last time I felt the same was when I accidentally found a Japanese Youtube channel that had tons of clips of konbini storefronts, a few seconds long each, most of them with zero views.

---

[Article original](https://iamwillwang.com/notes/has-not-been-viewed-much/) · [Discussion HN](https://news.ycombinator.com/item?id=48799155)
