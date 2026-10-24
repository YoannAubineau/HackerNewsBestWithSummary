---
article_fetched_at: '2026-10-24T15:06:30.641785Z'
attempts: 0
content_source: extracted
discussion_comment_count: 43
discussion_fetched_at: '2026-10-24T15:06:22.062024Z'
error: null
guid: https://news.ycombinator.com/item?id=50217500
hn_item_id: 50217500
hn_url: https://news.ycombinator.com/item?id=50217500
is_ask_or_show_hn: false
llm_input_tokens: 5249
llm_latency_ms: 11362
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 969
our_published_at: '2026-10-24T14:30:03Z'
rewritten_title: Douze ans d'histoire du SQLite distribué, de rqlite à la consolidation
  commerciale
source_published_at: '2026-10-24T01:16:58Z'
status: summarized
summarized_at: '2026-10-24T15:07:20.959897Z'
title: Twelve years of distributed SQLite
url: https://philipotoole.com/twelve-years-of-distributed-sqlite/
---

## Résumé de l'article

rqlite, lancé en 2014, a été le premier système open-source à combiner Raft et SQLite pour répliquer les données sur un cluster. Cet article retrace l'évolution du domaine du « SQLite distribué » depuis ses origines jusqu'aux plateformes commerciales actuelles.

- **2014-2017 : Les pionniers du consensus** — rqlite (2014) et dqlite de Canonical (2017) utilisent des protocoles de consensus pour garantir la cohérence forte, chacun répondant à des besoins d'infrastructure différents (serveur vs bibliothèque embarquée).
- **2021 : Un changement de paradigme** — Litestream (2021) abandonne le consensus et propose une récupération en S3 à faible coût pour une base de données mono-nœud, validant l'idée que la plupart des applications n'ont pas besoin d'un cluster.
- **2022 : Diversification des approches** — cr-sqlite ajoute les CRDTs pour les écritures multiples avec fusion (coin AP), tandis que libSQL (Turso) fourche SQLite lui-même pour offrir un service répliqué à l'edge, attirant des investissements.
- **Plateforme et monétisation** — Cloudflare D1 et Turso transforment le SQLite répliqué en service géré, marquant le passage de « chose que vous exécutez » à « chose que vous achetez ».
- **L'héritage open-source** — Pendant huit ans, les solutions de base (rqlite, dqlite, Litestream) sont restées gratuites et open-source avant que les entreprises ne commercialisent le concept; rqlite demeure le choix pour les utilisateurs cherchant une base de données auto-hébergée gratuite et maîtrisable.

## Discussion sur Hacker News (43 commentaires)

**Avis positifs** :
- rqlite est bien conçu et bien maintenu, avec un créateur exceptionnellement dédié et disponible pour aider les utilisateurs
- SQLite distribué simplifie drastiquement l'architecture des bases de données en cluster par rapport aux systèmes traditionnels complexes
- rqlite fonctionne bien pour les couches de contrôle et d'observabilité en production, offrant des garanties de réplication multi-nœuds
- SQLite en production (avec WAL ou multiwriter) est suffisamment performant pour la plupart des projets qui ne dépassent pas ses limites naturelles
- L'article fournit une perspective historique utile sur l'évolution de SQLite distribué et replace les contributions de différents acteurs dans leur contexte approprié

**Avis négatifs** :
- dqlite génère beaucoup d'erreurs 'database locked' en pratique, poussant les utilisateurs à migrer vers des solutions plus robustes
- rqlite est plus lent qu'une base de données mononode et nécessite de passer par le leader pour les requêtes, ce qui complique l'architecture
- D1 de Cloudflare s'est avéré peu fiable en production et n'est finalement qu'un wrapper autour de Durable Objects, ce qui rend les Durable Objects directes préférables
- PostgreSQL offre plus de fonctionnalités SQL et devient plus simple à gérer avec les agents modernes, rendant SQLite distribué moins attrayant
- L'article semble partiellement généré par IA (Claude), avec un style maladroit et des formulations typiques des LLM plutôt qu'une voix authentique

**Top commentaires** :

- [piterrro](https://news.ycombinator.com/item?id=50218626) : Having used D1 in production - it's not very reliable. There was a comment on HN from one of D1 devs \[1\] saying that D1 is a sql wrapper on top of durable objects that mimicks sqlite distributed like nature. \> I'll let you in on a sort of dirty secret: It's almost always better to use Durable Objec…
- [vikrantrathore](https://news.ycombinator.com/item?id=50219374) : Its funny, when I was reading part time parliament paper \(paxos\) and while learning zig and odin language created a pure paxos library and then the first application for that library was to build a multi-master sqlite. The two approaches I took are very different in case of zig I build zaxonlite \(h…
- [AgentME](https://news.ycombinator.com/item?id=50219960) : The comparisons between various projects, including between rqlite and Litestream, were interesting. \(rqlite uses a consensus algorithm between nodes to keep them synced and allow changing the primary node, while Litestream just syncs itself to S3 so another node could take over with the data from…

---

[Article original](https://philipotoole.com/twelve-years-of-distributed-sqlite/) · [Discussion HN](https://news.ycombinator.com/item?id=50217500)
