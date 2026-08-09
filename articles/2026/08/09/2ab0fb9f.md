---
article_fetched_at: '2026-08-09T21:22:43.146281Z'
attempts: 0
content_source: extracted
discussion_comment_count: 108
discussion_fetched_at: '2026-08-09T21:22:41.365303Z'
error: null
guid: https://news.ycombinator.com/item?id=49223475
hn_item_id: 49223475
hn_url: https://news.ycombinator.com/item?id=49223475
image_url: https://opengraph.githubassets.com/db99d570a2f08cb94b0e1f0b92677ff310712fd980fc6217880e472af4b7dbde/andrewpollack/linkedin-feed-blocker
is_ask_or_show_hn: false
llm_input_tokens: 7690
llm_latency_ms: 9435
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 784
our_published_at: '2026-08-09T20:41:55Z'
rewritten_title: LinkedIn Feed Blocker, une extension Chrome qui désactive le fil
  d'actualité
source_published_at: '2026-08-08T16:49:07Z'
status: summarized
summarized_at: '2026-08-09T21:22:59.466171Z'
title: LinkedIn Feed Blocker
url: https://github.com/andrewpollack/linkedin-feed-blocker
---

## Résumé de l'article

LinkedIn Feed Blocker est une extension Chrome minimaliste qui désactive le fil d'actualité principal de LinkedIn tout en gardant les autres fonctionnalités de la plateforme opérationnelles. L'extension cible spécifiquement le fil principal et sa pagination infinie, sans affecter les profils, les offres d'emploi, la recherche, la messagerie ou les notifications.

- Masque entièrement le fil principal sur la page /feed et bloque la pagination infinite-scroll
- Laisse intactes les fonctionnalités comme les profils utilisateur, la recherche d'emploi, la messagerie, les notifications et autres outils LinkedIn
- S'installe manuellement via le mode développeur de Chrome (chargement de répertoire local) en attente de publication officielle sur le Web Store
- Cible uniquement le pagineur mainFeed de LinkedIn pour éviter d'interférer avec d'autres parties de la plateforme
- Idéale pour les utilisateurs qui exploitent LinkedIn pour la recherche d'emploi et le réseautage, mais qui veulent éviter le fil d'actualité social non modéré

## Discussion sur Hacker News (108 commentaires)

**Avis positifs** :
- Les outils de blocage du fil LinkedIn rendent le site enfin utilisable en supprimant les contenus de distraction majeure et la 'slop' générée par IA qui domine actuellement le flux
- Le blocage du fil s'avère particulièrement utile pour les chercheurs d'emploi qui trouvent des opportunités par d'autres canaux (messages, recherche), sans perdre de temps à scroller du contenu sans valeur
- Les extensions de personnalisation du web montrent que les utilisateurs peuvent reprendre le contrôle de leur expérience en ligne face à l'enshittification progressive des plateformes
- LinkedIn lui-même confirme l'inutilité de son flux : bloquer 90%+ du contenu ou le rendre vide révèle que la majorité des posts sont du spam ou du contenu promu sans intérêt

**Avis négatifs** :
- LinkedIn applique activement une détection des manipulations DOM et pourrait shadowbanner les utilisateurs d'extensions, réduisant leur visibilité dans les recherches de recruteurs ou supprimant leur engagement
- Un simple filtre uBlock Origin suffit techniquement, rendant une extension spécialisée redondante ; cependant, LinkedIn change régulièrement sa structure pour contrecarrer ces méthodes
- Bloquer le fil entièrement fait perdre les rares opportunités légitimes (offres d'emploi, informations d'anciens collègues) noyées dans le contenu promotionnel
- Pour les chercheurs d'emploi, LinkedIn reste un actif professionnel incontournable malgré sa qualité déclinante, car beaucoup d'employeurs l'exigent et le considèrent comme le standard

**Top commentaires** :

- [apparent](https://news.ycombinator.com/item?id=49224047) : I'd love to be able to filter the feed so it only shows me actual posts by my connections. I do not care about comments my connections made on strangers' posts, and I surely do not care about posts by strangers that my connections 'liked'. Anyone know if such a tool exists?
- [dwedge](https://news.ycombinator.com/item?id=49226188) : If you browse the mobile website instead of the app, after 6 or 7 posts it says "LinkedIn is better with the app" and then hits back on your browser either taking you back to the top or to another website. This is a very effective way to get me to close linkedin
- [c\_e](https://news.ycombinator.com/item?id=49225558) : linkedin cares a lot about preventing people from changing how people view their website, and they have very effective DOM detection code which watches for manipulation like this. So if you use this extension it's very likely that your account will be shadowbanned, meaning you won't show up in sear…

---

[Article original](https://github.com/andrewpollack/linkedin-feed-blocker) · [Discussion HN](https://news.ycombinator.com/item?id=49223475)
