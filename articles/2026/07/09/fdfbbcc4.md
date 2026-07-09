---
article_fetched_at: '2026-07-09T23:03:32.598684Z'
attempts: 0
content_source: extracted
discussion_comment_count: 75
discussion_fetched_at: '2026-07-09T23:03:22.865290Z'
error: null
guid: https://news.ycombinator.com/item?id=48847552
hn_item_id: 48847552
hn_url: https://news.ycombinator.com/item?id=48847552
is_ask_or_show_hn: false
llm_input_tokens: 8355
llm_latency_ms: 13517
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 884
our_published_at: '2026-07-09T22:27:53Z'
rewritten_title: Tencent lance Hy3, un modèle de langage rivalisant avec les plus
  grands open-source
source_published_at: '2026-07-09T15:27:48Z'
status: summarized
summarized_at: '2026-07-09T23:04:28.490538Z'
title: Hy3
url: https://hy.tencent.com/research/hy3
---

## Résumé de l'article

Hy3 est un modèle de langage développé par Tencent qui améliore significativement ses performances après une phase de preview en avril 2026. Le modèle égale ou surpasse des modèles open-source beaucoup plus grands tout en consommant 2 à 5 fois moins de paramètres.

- Hy3 excelle dans les tâches d'agent autonome, de raisonnement et de long contexte, avec des résultats comparables aux grands modèles phares ; en évaluation à l'aveugle avec 270 experts, il obtient 2,67/4, surpassant GLM-5.1 à 2,51/4
- Le modèle offre des améliorations majeures en fiabilité : taux d'hallucination réduit de 12,5% à 5,4%, erreurs de bon sens passant de 25,4% à 12,7%, et taux d'erreur en multi-tour de 17,4% à 7,9%
- En conditions réelles avec WorkBuddy, le taux de succès des tâches est passé de 72% (preview) à 90%, avec un temps moyen de réalisation réduit de 34% et une efficacité tokens supérieure (47% moins de tokens pour le traitement de documents)
- Hy3 est publié en open-source sous licence Apache 2.0 sur GitHub, HuggingFace, ModelScope et AtomGit avec une tarification API réduite (1 RMB pour 1M tokens en entrée)

## Discussion sur Hacker News (75 commentaires)

**Avis positifs** :
- Hy3 offre un excellent rapport taille/capacité, avec des performances comparables à des modèles beaucoup plus grands (proche de DeepSeek V4 Pro selon certains) tout en étant moins coûteux
- Le modèle est très bon marché et performant pour les tâches de codage, rivalisant avec des variantes Pro tout en étant tarifé comme les versions Flash/moins chères
- Excellent suivi d'instructions, bonne connaissance du monde, bonne vitesse de traitement et license MIT ouverte rendent le modèle attrayant
- Pour son taille (295B), les benchmarks de codage et les performances générales démontrent une amélioration significative par rapport à la version preview

**Avis négatifs** :
- Le modèle semble benchmarké agressivement ; en usage réel, plusieurs utilisateurs le trouvent décevant comparé à des modèles beaucoup plus petits comme Gemma 31B ou Qwen 3.6 27B
- Hy3 manque de l'efficacité KV cache de DeepSeek V4 (cache limité à ~130K tokens avec quantization FP4 vs 3M pour DS4 Flash), réduisant ses performances sur contextes longs
- Des problèmes pratiques ont limité son adoption : ralentissements sur OpenRouter, erreurs HTTP fréquentes et rate-limiting excessif sur la plateforme
- L'interface de démonstration est peu fonctionnelle et le site principal est inaccessible ; mauvaise communication sur ce qu'est réellement le produit et ses use-cases

**Top commentaires** :

- [simonw](https://news.ycombinator.com/item?id=48848950) : Pelican from a few days ago: https://simonwillison.net/2026/Jul/6/hy3/ - I was using the free tier on OpenRouter, which expires on July 21st. I tried the preview model 41 days ago and got a pelican with a "change pelican color" button: https://static.simonwillison.net/static/2026/hy3-preview-pel...
- [minimaxir](https://news.ycombinator.com/item?id=48848715) : A month ago I wrote a blog post about how Hy3 was topping the OpenRouter rankings despite no one talking about it: https://news.ycombinator.com/item?id=48317294 As of today, it has fallen to 8/9th on the rankings. I don't see a reason where you would use this model over competitors. However, price…
- [Catloafdev](https://news.ycombinator.com/item?id=48848284) : Curious how people feel about this compared to DS4 Flash, given they are pretty close in size. Also curious how well it holds up to heavy quantization. DS4 Flash can currently run reasonably well on systems with ~96gb+ RAM, I wonder if Hy3 can compete there.

---

[Article original](https://hy.tencent.com/research/hy3) · [Discussion HN](https://news.ycombinator.com/item?id=48847552)
