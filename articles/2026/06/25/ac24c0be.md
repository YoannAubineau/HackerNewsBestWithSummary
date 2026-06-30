---
article_fetched_at: '2026-06-25T16:45:31.122496Z'
attempts: 0
content_source: extracted
discussion_comment_count: 76
discussion_fetched_at: '2026-06-25T16:45:26.247796Z'
error: null
guid: https://news.ycombinator.com/item?id=48673671
hn_item_id: 48673671
hn_url: https://news.ycombinator.com/item?id=48673671
image_url: https://hackernewstrends.com/opengraph-image?72011d0134607af3
is_ask_or_show_hn: false
llm_input_tokens: 6944
llm_latency_ms: 12696
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 985
our_published_at: '2026-06-25T16:35:12Z'
rewritten_title: Un créateur a indexé 18 années de commentaires pour créer Google
  Trends sur Hacker News
source_published_at: '2026-06-25T14:08:55Z'
status: summarized
summarized_at: '2026-06-25T16:46:08.201162Z'
title: 'Show HN: I made Google Trends for Hacker News by indexing 18 years of comments'
url: https://hackernewstrends.com
---

## Résumé de l'article

Hacker Trends est un outil qui visualise la fréquence d'apparition de sujets, outils et personnes dans les 45 millions de posts et commentaires de Hacker News sur 18 ans. Les utilisateurs peuvent superposer plusieurs termes pour observer comment leur popularité monte et descend au fil du temps, avec accès aux stories et commentaires originaux filtrable par terme ou auteur.

- L'outil révèle des cycles de domination technologique : Cloudflare/Vercel, OpenAI/Anthropic, AMD/Nvidia, chacun cédant progressivement le leadership à un concurrent
- Les frameworks et langages suivent des générations distinctes (Angular→Vue→Svelte en frontend, TensorFlow→PyTorch→JAX en ML, Docker→Kubernetes en containerization)
- Les éditeurs de texte connaissent des successions claires : Sublime Text→Atom→VS Code, avec Zed émergeant récemment
- Les plateformes et services montrent des basculements majeurs : Zoom surpasse Skype en 2020, Bluesky dépasse Mastodon en 2024, Vite remplace Webpack à partir de 2022
- Les tendances longues révèlent des inflexions technologiques : Flash cédant à HTML5, REST faisant place à gRPC/GraphQL, x86 perdant du terrain face à ARM depuis 2024

## Discussion sur Hacker News (76 commentaires)

**Avis positifs** :
- Outil innovant et visuellement attrayant qui offre une perspective unique sur l'évolution des tendances technologiques et des sujets sur HN sur 18 ans, permettant de découvrir des pics d'activité révélateurs
- Les données brutes du HN Archive (48GB) provenant de l'API Firebase officielle constituent une ressource précieuse et ouvrent des possibilités pour d'autres services similaires, y compris des bases de données publiques interrogeables
- Fonctionnalité utile pour identifier les tendances professionnelles réelles (langages de programmation dans les posts 'Who is Hiring?') et potentiellement comme indicateur prédictif de performances d'entreprises
- Excellente comparaison avec Google Trends mais adaptée aux discussions HN ; permet de voir des transitions intéressantes (p.ex. crypto vers IA) et des phénomènes comme la durabilité médiatique de Stuxnet
- L'idée de normaliser les données par rapport au volume total de commentaires et d'ajouter une analyse de sentiment sont des améliorations pertinentes déjà identifiées par la communauté

**Avis négatifs** :
- Affiche uniquement les comptes absolus sans normalisation, ce qui rend difficile la séparation des tendances réelles de la croissance générale du site HN au fil du temps
- Limitation sémantique : ne distingue pas les termes ambigus (ex. 'Atom' peut désigner l'éditeur ou d'autres concepts) contrairement à Google Trends, rendant certaines analyses peu fiables
- Incohérence visuelle identifiée : les couleurs des lignes diffèrent entre le graphique miniature et le graphique complet, rendant la lecture confuse
- Impossibilité actuelle de découvrir automatiquement nouvelles tendances sans saisir manuellement des mots-clés ; pas de support des opérateurs de recherche avancée (pipes, guillemets) pour préciser les requêtes
- Différence fondamentale avec Google Trends : mesure les occurrences textuelles plutôt que les recherches intentionnelles, ce qui produit des données non directement comparables

**Top commentaires** :

- [zX41ZdbW](https://news.ycombinator.com/item?id=48675889) : I host a publicly open database with Hacker News data at https://play.clickhouse.com/play?user=play\#U0VMRUNUICogRlJPT... So you can create any sort of similar services in a single SQL query and an HTML page. I also hosted it as a publicly accessible data lake, which you can query from everywhere: h…
- [Aachen](https://news.ycombinator.com/item?id=48675818) : Google Trends is about searches This is about text submissions. More like if Google Trends counted word occurrences on webpages. Or if Google Ngrams counted webpages instead of books People don't write much about non-newsworthy things whereas many people search "burger" anytime they want a burger d…
- [kaelyx](https://news.ycombinator.com/item?id=48675169) : Hello, /api/hn -\> 502 {"error":"Your database has been temporarily rate-limited, please contact support@upstash.com for further details."}

---

[Article original](https://hackernewstrends.com) · [Discussion HN](https://news.ycombinator.com/item?id=48673671)
