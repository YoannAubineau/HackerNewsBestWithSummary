---
article_fetched_at: '2026-07-27T18:18:25.478725Z'
attempts: 0
content_failure_reason: content not usable
content_source: feed_fallback
discussion_comment_count: 113
discussion_fetched_at: '2026-07-27T18:18:24.442711Z'
error: null
guid: https://news.ycombinator.com/item?id=49070985
hn_item_id: 49070985
hn_url: https://news.ycombinator.com/item?id=49070985
image_url: https://opengraph.githubassets.com/5dd2a19b925d39438adfeba80bd46c599f0afc47ac7084cbcf2eafd10b0bfab1/MoonshotAI/Kimi-K3
is_ask_or_show_hn: false
llm_input_tokens: 9227
llm_latency_ms: 9337
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 695
our_published_at: '2026-07-27T17:32:39Z'
rewritten_title: Rapport technique Kimi-K3
source_published_at: '2026-07-27T15:23:45Z'
status: summarized
summarized_at: '2026-07-27T18:18:41.734824Z'
title: Kimi-K3 Technical Report [pdf]
url: https://github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf
---

## Résumé de l'article

(unable to load content: content not usable)

## Discussion sur Hacker News (113 commentaires)

**Avis positifs** :
- Moonshot a ouvert les poids du modèle avec infrastructure associée, démontrant que les modèles open source ne ralentissent pas nécessairement la progression en IA et favorisent au contraire la concurrence et l'innovation distribuée
- Les labos chinois (DeepSeek, Moonshot) contribuent davantage aux avancées en ML que les grandes structures fermées américaines, selon les publications aux conférences majeures
- L'open source crée un financement diversifié et un portefeuille de risques parallèles plus efficace qu'une concentration centralisée, permettant à davantage d'acteurs de rester à la frontière
- Le coût d'inférence chute drastiquement pour les grandes organisations (inférieur à 0,60$ par million de tokens générés avec un rack dédié), rendant l'indépendance vis-à-vis des API commerciales viable
- L'architecture du modèle (MoE, tanh modificatif, distillation multi-professeur) présente des innovations techniques concrètes et des optimisations non-triviales

**Avis négatifs** :
- La licence n'est pas vraiment open source (restrictions commerciales au-delà de 20M$ de revenus ou 100M utilisateurs) et les données d'entraînement ne sont pas divulguées, contredisant le discours de transparence complète
- Les modèles open source ont structurellement une capacité inférieure aux modèles fermés de frontière en raison des limites de déploiement localisé versus centralisé, plaçant un plafond à leur puissance réelle
- L'évaluation repose sur des benchmarks isolés (decode) sans données réalistes sur tokens/sec end-to-end, cache hit rates ou distributions de charge d'agents multi-tours critiques pour usage réel
- Les données d'entraînement proviennent largement de matériel protégé par copyright sans permission (contenu d'artistes, écrivains, codeurs), un coût éthique et légal non résolu que tous les labos partagent mais qui n'est pas justifié
- La distillation et les gains d'efficacité n'expliquent pas pleinement la qualité atteinte ; les détails techniques sur les distillateurs multi-professeurs restent flous et pourraient impliquer des sources fermées

**Top commentaires** :

- [GodelNumbering](https://news.ycombinator.com/item?id=49072173) : Back of the envelope calculation \(could be off, correct me if I am\) If you are a large enough company that spends million+ on inference a month, it makes sense to buy a GB300 rack \($6M on top range from what I could find\) which has 20.7 TB. Since the model is mixed trained \(MXFP4\), you would need l…
- [m\_ke](https://news.ycombinator.com/item?id=49071249) : Also open sourced a bunch of infra to go with it. Anyone who claims open source and open weights models are "decel" needs to get their head checked https://github.com/MoonshotAI/MoonEP https://github.com/kvcache-ai/AgentEnv https://github.com/MoonshotAI/FlashKDA
- [fahrradflucht](https://news.ycombinator.com/item?id=49071313) : License: https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE \> If the Licensee or any of its affiliates operates a Model as a Service business, and the aggregate revenue of the Licensee and its affiliates exceeds 20 million US dollars \(or the equivalent in other currencies\) in total over an…

---

[Article original](https://github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf) · [Discussion HN](https://news.ycombinator.com/item?id=49070985)
