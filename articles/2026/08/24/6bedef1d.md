---
article_fetched_at: '2026-08-24T22:16:56.851042Z'
attempts: 0
content_source: extracted
discussion_comment_count: 22
discussion_fetched_at: '2026-08-24T22:16:53.935012Z'
error: null
guid: https://news.ycombinator.com/item?id=49411468
hn_item_id: 49411468
hn_url: https://news.ycombinator.com/item?id=49411468
image_url: https://www.dbreunig.com/img/sf_beach_og.jpg
is_ask_or_show_hn: false
llm_input_tokens: 4051
llm_latency_ms: 12596
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1089
our_published_at: '2026-08-24T19:24:38Z'
rewritten_title: L'émergence de Fable marque la fin de l'optimisation gratuite en
  intelligence artificielle
source_published_at: '2026-08-23T19:06:09Z'
status: summarized
summarized_at: '2026-08-24T22:17:16.564815Z'
title: Fable and the end of the free lunch
url: https://www.dbreunig.com/2026/08/23/fable-the-end-of-moore-s-law.html
---

## Résumé de l'article

Fable est un modèle d'IA très performant mais coûteux d'Anthropic, dont l'arrivée marque un tournant : les développeurs doivent désormais réfléchir stratégiquement à quel modèle utiliser pour chaque tâche, plutôt que de compter sur des modèles plus performants et meilleur marché qui apparaîtront prochainement. Cette dynamique rappelle le moment où Moore's Law a ralenti et a forcé les programmeurs à optimiser leur code au lieu de laisser le matériel résoudre les problèmes.

- Avant Fable, l'amélioration des stratégies de codage semblait inutile car les nouveaux modèles arrivaient à prix égal ou inférieur et compensaient les inefficacités
- GLM 5.2, lancé simultanément à Fable, coûte environ 1/9ème du prix de Fable tout en étant suffisant pour la plupart des tâches de codage courant, notamment avec un bon contexte
- Les développeurs commencent à router les travaux intelligemment : interroger Fable pour affiner une conception, puis confier l'exécution à des modèles moins chers comme GLM
- Les réductions de coût futures bénéficieront à tous les modèles (K3, Qwen, etc.), et les meilleures harnesses rendront les modèles moins puissants compétitifs avec un contexte adapté
- Les mesures de contrôle d'accès et de conservation de données de Fable incitent aussi les entreprises à réfléchir à la répartition stratégique des appels aux modèles

## Discussion sur Hacker News (22 commentaires)

**Avis positifs** :
- Les modèles moins chers et plus rapides (DeepSeek v4, GLM 5.2, etc.) offrent un très bon rapport qualité-prix et suffisent largement pour les tâches courantes de codage répétitif, particulièrement avec un bon contexte fourni.
- Pour de nombreux utilisateurs, des modèles déjà « assez bons » qui ne s'améliorent plus mais deviennent plus rapides et moins chers seraient largement satisfaisants; l'amélioration perpétuelle n'est pas nécessaire.
- Une approche hybride fonctionne bien : utiliser les modèles haut de gamme pour la planification et concevoir l'architecture, puis déléguer l'implémentation aux modèles moins chers.
- L'utilisation d'LLMs pour simplifier l'accès à des outils complexes (cron, regex, SQL) et réduire les couches d'abstraction interface est justifiée, même si cela implique des inefficacités computationnelles.

**Avis négatifs** :
- Les modèles haut de gamme offrent bien plus que 10% de mieux : ils rivalisent avec des ingénieurs senior vs mid-level, trouvant des insights clés, des approches novatrices et des designs plus robustes que les modèles bon marché.
- Un codebase conçu et implémenté par les meilleurs modèles serait substantiellement meilleur que celui conçu par eux mais implémenté par des modèles inférieurs, bénéficiant à long terme à tous les modèles futurs.
- Les preuves empiriques suggèrent que les capacités plafonnent et que le progrès en vitesse/coût n'arrive pas vraiment comme prévu, contrairement à l'optimisme sur la courbe d'amélioration continue.
- Les LLMs restent fondamentalement peu fiables pour les faits établis (conseils culinaires contradictoires, températures incohérentes), problème intrinsèque à leur fonctionnement qui ne peut pas être résolu par grounding seul.
- L'inefficacité logicielle actuelle est extrême même comparée à il y a 10 ans, contredisant l'argument que les contraintes budgétaires favorisent l'optimisation des modèles.

**Top commentaires** :

- [nchmy](https://news.ycombinator.com/item?id=49412015) : The real revolution is Deepseek v4 flash and similar models \(GPT 5.6 Luna, muse spark 1.2, mimo, etc...\) - Genuinely good performance for a tiny fraction of the cost of Fable and even GLM etc... I think a lot of people would be very content if they never got smarter, and just kept getting even chea…
- [HighGoldstein](https://news.ycombinator.com/item?id=49420586) : I find it somewhat funny that the author starts by talking about how Moore's law enabled inefficient software and that we then had to make it more efficient, when almost all software today is horrendously inefficient compared to even 10 years ago, let alone 20-30. We've somehow even achieved a stat…
- [pigpop](https://news.ycombinator.com/item?id=49412540) : Reading this as someone who switched over to ChatGPT after \(and largely because of the changes made in\) the Fable release, it reads a bit naive. Not only do I find Sol to be as good, if not better than, Fable it is also faster, better behaved and has a much more coherent writing style. You also don…

---

[Article original](https://www.dbreunig.com/2026/08/23/fable-the-end-of-moore-s-law.html) · [Discussion HN](https://news.ycombinator.com/item?id=49411468)
