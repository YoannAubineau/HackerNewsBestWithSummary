---
article_fetched_at: '2026-04-26T19:18:25.142589Z'
attempts: 0
content_source: extracted
discussion_comment_count: 89
discussion_fetched_at: '2026-04-26T19:18:23.459045Z'
error: null
feed_summary: '<p>Article URL: <a href="https://github.com/orgs/community/discussions/192666">https://github.com/orgs/community/discussions/192666</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=47910546">https://news.ycombinator.com/item?id=47910546</a></p>

  <p>Points: 167</p>

  <p># Comments: 86</p>'
guid: https://news.ycombinator.com/item?id=47910546
hn_item_id: 47910546
hn_url: https://news.ycombinator.com/item?id=47910546
image_url: https://opengraph.githubassets.com/48caf01cfc1db531d3cfcb986194e584e8e4f83d129e3e13e65a7dc90ddf46a9/orgs/community/discussions/192666
is_ask_or_show_hn: false
llm_input_tokens: 7619
llm_latency_ms: 7690
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 643
our_published_at: '2026-04-26T19:14:18Z'
rewritten_title: 'GitHub modifie l''expérience utilisateur : les liens vers les issues
  s''ouvrent maintenant dans une fenêtre contextuelle'
source_published_at: '2026-04-26T14:18:38Z'
status: summarized
summarized_at: '2026-04-26T19:18:53.132434Z'
title: 'GitHub unwanted UX change: issue links now open in a popup'
url: https://github.com/orgs/community/discussions/192666
---

## Résumé de l'article

Le contenu fourni ne contient pas d'informations substantielles permettant de résumer le sujet. Il s'agit de fragments d'interface GitHub (menus de session, boutons de formatage, icônes de réaction) sans explication de la modification UX décrite dans le titre.

- Le titre indique un changement d'expérience utilisateur concernant l'ouverture des liens d'issues
- Le contenu ne fournit pas de détails sur cette modification, ses implications ou le contexte
- Impossible de produire un résumé factuel faute de contenu substantiel

## Discussion sur Hacker News (89 commentaires)

**Avis positifs** :
- Le changement peut améliorer les performances pour les utilisateurs naviguant entre dépôts en évitant le rechargement complet du header (selon un responsable GitHub, passage de 500-800ms à moins de 100ms)
- Un aperçu inline sans quitter la page d'origine est une pratique UX courante appréciée de certains utilisateurs qui désirent rester dans leur contexte
- Les navigateurs modernes offrent des alternatives comme les onglets scindés (Edge, Firefox, Chrome) qui peuvent partiellement résoudre le problème utilisateur

**Avis négatifs** :
- Ce changement viole les conventions de navigation web établies : les liens devraient rester des liens et naviguer vers la destination, pas s'ouvrir en popup/panneau latéral
- GitHub ignore depuis longtemps les retours de sa communauté (dépôt de feedback communautaire devenu un cimetière de plaintes) et ne dispose plus de leader responsable depuis le départ du CEO
- Le problème reflète une tendance plus large : des changements UI imposés sans raison fonctionnelle réelle, motivés par le besoin des designers/PMs de justifier leur existence plutôt que d'améliorer l'expérience utilisateur
- Microsoft transfère les mauvaises pratiques UX d'Azure DevOps vers GitHub (comme ce comportement problématique inspiré de Jira), dégradant ainsi l'avantage que GitHub avait sur GitLab
- Les métriques A/B testées mesurent l'interaction, pas la préférence réelle des utilisateurs ; cette justification manque de transparence et les données ne sont pas partagées avec la communauté

**Top commentaires** :

- [Matt138](https://news.ycombinator.com/item?id=47912521) : This was a performance driven change. We added this as loading a cross repo issue is a much slower experience than loading an issue in the same repo due to the way the header is loaded \(which is being worked on\). But we hear you on the feedback - we will roll this back while we keep pushing on the…
- [willio58](https://news.ycombinator.com/item?id=47911159) : It’s always been interesting to me that multi-million and even billion dollar tech companies don’t have perfect websites in terms of UX. Just last night I was helping my GF set up an ad for her job on LinkedIn. The UX was terrible. Like awful and basic things like save and exit were completely brok…
- [mwalser](https://news.ycombinator.com/item?id=47911519) : It's interesting to see that the UX issues that are annoying me when using Azure DevOps are finding their way into GitHub. In case they are truly chasing Azure DevOps level UX, I would recommend they implement an HTML editor for issues that, depending on whether the user has dark mode or light mode…

---

[Article original](https://github.com/orgs/community/discussions/192666) · [Discussion HN](https://news.ycombinator.com/item?id=47910546)
