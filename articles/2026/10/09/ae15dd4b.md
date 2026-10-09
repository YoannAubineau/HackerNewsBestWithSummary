---
article_fetched_at: '2026-10-09T14:48:46.449465Z'
attempts: 0
content_source: extracted
discussion_comment_count: 158
discussion_fetched_at: '2026-10-09T14:48:31.334581Z'
error: null
guid: https://news.ycombinator.com/item?id=50019911
hn_item_id: 50019911
hn_url: https://news.ycombinator.com/item?id=50019911
image_url: https://deno.com/blog/cloudflare/deno-cf-balanced-og.webp
is_ask_or_show_hn: false
llm_input_tokens: 10369
llm_latency_ms: 14614
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 811
our_published_at: '2026-10-09T14:09:17Z'
rewritten_title: L'équipe Deno rejoint Cloudflare pour développer sa plateforme de
  calcul distribué
source_published_at: '2026-10-09T13:03:48Z'
status: summarized
summarized_at: '2026-10-09T14:49:21.132789Z'
title: Deno Is Joining Cloudflare
url: https://deno.com/blog/cloudflare
---

## Résumé de l'article

Deno, un runtime JavaScript open source créé pour simplifier le développement serveur avec des garanties de sécurité et une meilleure distribution de modules, intègre Cloudflare pour fusionner ses efforts avec les équipes Workers et Durable Objects.

- Le runtime Deno sera maintenu pendant un an avec des correctifs de sécurité, puis son développement cessera ; le code reste open source et disponible pour d'autres contributeurs
- Deno Deploy ferme dans six mois ; les clients payants recevront une aide à la migration vers Cloudflare Workers
- L'équipe se concentre désormais sur celld, un modèle de programmation d'applications distribuées basé sur Durable Objects, conçu pour simplifier l'infrastructure de calcul
- JSR (le registre JavaScript) continue d'opérer sous la gestion de Cloudflare, et les outils rusty_v8 seront intégrés dans workerd
- Cloudflare vise à faire de ce modèle de programmation l'approche par défaut pour construire des serveurs, y compris pour les agents d'IA à grande échelle

## Discussion sur Hacker News (158 commentaires)

**Avis positifs** :
- Le code Deno reste open source sous licence MIT et peut être continué par la communauté ou des forks; la base technique et l'expérience développeur sont solides
- L'acquisition permet une fusion de celld avec workerd pour créer un runtime open source auto-hébergeable et de première classe, améliorant l'écosystème serverless
- Les compétences de l'équipe Deno sont bien utilisées chez Cloudflare pour améliorer sa plateforme workers/durables objects, plutôt que gaspillées
- Node.js a depuis adopté des fonctionnalités clés de Deno (--run, stripping TS, .env loading, watch mode, sqlite), réduisant les lacunes technologiques

**Avis négatifs** :
- Le runtime Deno sera abandonné après 1 an de maintenance minimale, ce qui est particulièrement cruel pour les entreprises ayant migré de Node vers Deno
- L'information critique sur la fin du support Deno est enterrée au bas du post Deno alors qu'absente du post Cloudflare, manquant de transparence vis-à-vis des utilisateurs
- Il s'agit d'une acquihire pure déguisée en acquisition positive: Deno meurt et son développement cesse, représentant un échec pour le projet et un risque pour l'écosystème open source
- Après l'acquisition de Bun par Anthropic, les deux alternatives majeures à Node.js sont maintenant absorbées par des monolithes propriétaires, étouffant l'innovation open source indépendante
- Les VCs qui ont financé Deno font un profitable exit tandis que les utilisateurs et développeurs qui ont cru au projet se retrouvent abandonnés en 13 mois

**Top commentaires** :

- [theodorejb](https://news.ycombinator.com/item?id=50020072) : « We will support the Deno runtime for another year with monthly releases containing bug fixes and security updates. After that year we will end our development of the Deno runtime. Deno will remain open source, and we welcome others who want to continue its development. » So unless someone else pi…
- [coldtea](https://news.ycombinator.com/item?id=50020818) : "Deno development effectively shut down via a Cloudflare acquihire" would be a better headline.
- [bennett\_dev](https://news.ycombinator.com/item?id=50020269) : I feel it leaves a bitter flavor how Ryan Dahl pushed so hard for Deno and Deno Deploy for years, just to let them die within 1 year and 6 months respectively. Thankfully I don't have any codebases that heavily use Deno features, otherwise this would be a steep curve now.

---

[Article original](https://deno.com/blog/cloudflare) · [Discussion HN](https://news.ycombinator.com/item?id=50019911)
