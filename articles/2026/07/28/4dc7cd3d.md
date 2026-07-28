---
article_fetched_at: '2026-07-28T21:00:13.756063Z'
attempts: 0
content_source: extracted
discussion_comment_count: 111
discussion_fetched_at: '2026-07-28T21:00:07.271121Z'
error: null
guid: https://news.ycombinator.com/item?id=49085909
hn_item_id: 49085909
hn_url: https://news.ycombinator.com/item?id=49085909
is_ask_or_show_hn: false
llm_input_tokens: 12589
llm_latency_ms: 12742
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1007
our_published_at: '2026-07-28T20:18:43Z'
rewritten_title: DeltaNet et ses variantes de attention linéaire expliquées étape
  par étape
source_published_at: '2026-07-28T16:02:07Z'
status: summarized
summarized_at: '2026-07-28T21:00:37.033078Z'
title: A walk through of the DeltaNet family of linear attention variants
url: https://blog.doubleword.ai/you-could-have-come-up-with-kimi-delta-attention
---

## Résumé de l'article

Cet article présente une dérivation progressive de la famille DeltaNet de variantes d'attention linéaire, culminant avec Kimi Delta Attention (KDA). Ces mécanismes remplacent la softmax attention standard par des opérations linéaires utilisant une règle de correction delta pour mettre à jour un état compact, permettant une inférence efficace avec mémoire bornée au lieu de croissance quadratique.

- La progression pédagogique va de l'attention softmax classique à l'attention linéaire, puis aux variantes DeltaNet, Gated DeltaNet et KDA en montrant comment chaque étape résout un problème spécifique (éliminer softmax, corriger les écritures interférentes, oublier les états obsolètes, adapter par canal)
- DeltaNet introduit une règle delta qui remplace la valeur précédente stockée pour une clé donnée plutôt que de l'ajouter, éliminant les interférences entre paires clé-valeur passées et utilisant une formulation mathématique équivalente à un pas d'apprentissage en ligne
- Gated DeltaNet ajoute une porte de rétention scalaire pour oublier globalement l'état avant de le lire, tandis que KDA élève cette porte scalaire au rang de vecteur diagonal permettant un oubli par canal de clé
- KDA peut être exécuté de deux façons : en mode récurrent par jeton (efficace pour l'inférence) ou par chunks (réorganisant le travail en produits matriciels pour exploiter les tensor cores lors de l'entraînement et du prefill)
- La transition d'état dans KDA adopte une structure diagonal-plus-low-rank (DPLR) en espace de clé, et le traitement par chunks repose sur des résolutions triangulaires causales et des représentations WY pour gérer les dépendances entre erreurs delta au sein d'un bloc de tokens

## Discussion sur Hacker News (111 commentaires)

**Avis positifs** :
- L'article décompose bien l'évolution incrémentale de l'algorithme, rendant la progression logique et compréhensible à ceux ayant le background requis.
- Le toggle entre notation bra-ket et notation mathématique classique est une excellente pédagogie qui facilite l'accès selon le background du lecteur.
- La notation bra-ket clarife réellement les opérations (produit scalaire vs produit externe) et les dimensions, particulièrement pour ceux ayant une formation en physique.
- L'article explique clairement son choix de notation dès le départ et fournit les définitions des variables, ce qui aide à la compréhension.

**Avis négatifs** :
- Le titre 'You Could Have Come Up With...' est trompeur : il vise un public très spécialisé (experts en attention mechanisms) plutôt qu'un lecteur moyen, ce qui crée une fausse promesse pédagogique.
- L'innovation elle-même dépend largement de l'accès à du hardware powerful; c'est moins un bond conceptuel qu'une optimisation rendue possible par les ressources computationnelles modernes.
- La notation bra-ket, bien qu'utile pour certains, reste une barrière d'accès supplémentaire et ne représente pas réellement un avantage sur la notation standard d'algèbre linéaire pour ce domaine.
- L'article suppose une expertise préalable substantielle en transformers et attention mechanisms; sans ce bagage, même les explications restent opaques.
- Aucune approximation linéaire ne capture vraiment la richesse du scaling quadratique de l'attention originale, donc ces innovations hit diminishing returns face aux modèles full-attention.

**Top commentaires** :

- [TrackerFF](https://news.ycombinator.com/item?id=49086862) : Machine learning could need, and probably has needed, some unified math notation for the past 15 years IMO. With that said, it was worse back in the day - when ML papers were the products of researchers from all over, you'd see some wild notation. Many will likely disagree with me, but inconsistent…
- [benjiro29](https://news.ycombinator.com/item?id=49088502) : « You Could Have Come Up with ... » Creating or combining to have something new, that does not already exist is actually freaking hard! The moment its presented and people go "o, that is not that difficult", "i was able to also do that", or some nonsense like that. Everything looks simply the momen…
- [dr\_kretyn](https://news.ycombinator.com/item?id=49088673) : The bra-ket notation makes this all very simple/intuitive for me. With "vectors" I always get confused which is horizontal/vertical, and then I just follow blobs, and get distracted, and leave. With bra-kets the whole thing was very intuitive! I'm now going to covert other articles to the notation…

---

[Article original](https://blog.doubleword.ai/you-could-have-come-up-with-kimi-delta-attention) · [Discussion HN](https://news.ycombinator.com/item?id=49085909)
