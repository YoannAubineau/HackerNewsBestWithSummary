---
article_fetched_at: '2026-09-07T05:28:57.646645Z'
attempts: 0
content_failure_reason: content not usable
content_source: feed_fallback
discussion_comment_count: 99
discussion_fetched_at: '2026-09-07T05:28:55.749986Z'
error: null
guid: https://news.ycombinator.com/item?id=49590611
hn_item_id: 49590611
hn_url: https://news.ycombinator.com/item?id=49590611
image_url: https://anubis.techaro.lol/chrystarium.webp
is_ask_or_show_hn: false
llm_input_tokens: 8568
llm_latency_ms: 8558
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 653
our_published_at: '2026-09-07T04:37:19Z'
rewritten_title: Le déploiement de WebAssembly dans Anubis a pris un an
source_published_at: '2026-09-06T20:32:38Z'
status: summarized
summarized_at: '2026-09-07T05:29:12.914927Z'
title: It took a year to ship WebAssembly in Anubis
url: https://anubis.techaro.lol/blog/2026/anubis-wasm/
---

## Résumé de l'article

(unable to load content: content not usable)

## Discussion sur Hacker News (99 commentaires)

**Avis positifs** :
- Anubis avec Argon2id (memory-hard PoW) rend les accélérateurs GPU beaucoup moins efficaces, fermant la route aux solveurs CUDA simplifiés
- L'approche est justifiée économiquement : il ne faut pas rendre le scraping impossible, juste assez coûteux pour que les attaquants non-sophistiqués abandonnent
- L'effort de rétrocompatibilité est remarquable, notamment la transpilation wasm2js pour les vieux navigateurs et les appareils sans WebAssembly
- En pratique, Anubis démontre une réduction du trafic de bots abusifs, et représente une alternative décentralisée aux services de Cloudflare/Google/Amazon
- Le problème est bien compris comme économique : les coûts en CPU et bande passante sont réels même pour les pages statiques, particulièrement avec des millions de requêtes de bots

**Avis négatifs** :
- L'hypothèse fondamentale est fausse : les bots sophistiqués avec funding (AI companies) ne seront pas ralentis par Argon2id, ils disposent de ressources RAM/CPU illimitées
- Le PoW pénalise les utilisateurs légitimes à chaque première visite (notamment sans cookies persistants), ce qui les décourage bien plus qu'un simple défi JavaScript
- Une difficulté de 1 à 10ms sur VPS bon marché contre plusieurs minutes sur téléphone montre que le coût n'est pas uniforme : les scrapers évitent la partie coûteuse en temps
- Le système réinvente progressivement les problèmes de la cryptomonnaie (tokens, échanges entre sites, microtransactions) sans en reconnaître les implications
- Les scrapers sophistiqués contourneront le système facilement via LLM, rotation d'IP et stratégies adaptatives ; c'est une course sans fin où les défenses s'accumulent indéfiniment

**Top commentaires** :

- [vintagedave](https://news.ycombinator.com/item?id=49591304) : « In my experience the kinds of people who run this exact combination of circumstances also tend to be the kind of people that have a wide variance in the level of kindness they display to the authors of open source programs that happen to be in their way. » Love this. There’s been past discussion…
- [doctor\_radium](https://news.ycombinator.com/item?id=49593106) : I have every copy of Firefox here configured with webassembly disabled...because I don't tend to do what Webassembly was designed for, i.e. online games, video/audio editing, emulation, etc. \[1\] and because I dislike things running in the background without my knowledge. So this is going to be inte…
- [kccqzy](https://news.ycombinator.com/item?id=49591573) : Hats off to Xe for spending so much time on backwards compatibility, especially the tidbit about targeting Chrome 66. I have a Mac from 2014 running Yosemite that I occasionally use to test for backwards compatibility in my own frontend code \(for fun!\). But IMO the best way to ensure compatibility…

---

[Article original](https://anubis.techaro.lol/blog/2026/anubis-wasm/) · [Discussion HN](https://news.ycombinator.com/item?id=49590611)
