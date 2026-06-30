---
article_fetched_at: '2026-06-26T01:41:52.598730Z'
attempts: 0
content_source: extracted
discussion_comment_count: 117
discussion_fetched_at: '2026-06-26T01:41:51.651011Z'
error: null
guid: https://news.ycombinator.com/item?id=48657049
hn_item_id: 48657049
hn_url: https://news.ycombinator.com/item?id=48657049
is_ask_or_show_hn: false
llm_input_tokens: 14214
llm_latency_ms: 15106
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1174
our_published_at: '2026-06-26T00:53:06Z'
rewritten_title: Construire un pipeline de points d'intérêt avec données géospatiales,
  Wikipédia et modèles de langage
source_published_at: '2026-06-24T08:54:12Z'
status: summarized
summarized_at: '2026-06-26T01:42:30.117920Z'
title: You can't unit test for taste
url: https://dev.karltryggvason.com/you-cant-unit-test-for-taste/
---

## Résumé de l'article

In the Long Run est une application qui permet aux coureurs de suivre leur progression virtuelle le long de routes célèbres dans le monde en utilisant leurs données Strava. L'auteur a développé un pipeline pour enrichir ces routes avec des points d'intérêt pertinents en combinant des données GeoNames, des signaux de notoriété Wikipedia, et un modèle de langage pour évaluer leur importance.

- Le pipeline utilise GeoNames comme source de données initiale, filtrée sur 725 000 points d'intérêt pertinents (parcs, sites historiques, châteaux, monuments), stockée en Apache Parquet et interrogée via DuckDB et Python
- Les signaux de notoriété combinent les liens Wikipedia existants et le nombre de langues Wikipédia couvrant chaque site, corrigeant un biais initial favorisant les régions anglophones
- Un modèle LLM (Anthropic Haiku) a d'abord servi à générer des résumés textuels, mais a produit des hallucinations (sites mal identifiés, données inventées), forçant l'auteur à revenir aux résumés Wikipedia
- Le modèle LLM a été redéployé pour évaluer un score de subjectivité reflétant l'« intérêt » des sites, combiné à d'autres métriques pour classer les points
- La finalisation a nécessité des ajustements par-route (filtres de population, poids des paramètres, répartition géographique) car aucune approche unique ne fonctionne pour tous les territoires, et il n'existe pas de mesure objective pour évaluer la qualité des résultats

## Discussion sur Hacker News (117 commentaires)

**Avis positifs** :
- On peut partiellement externaliser le goût en le décomposant : documenter les conventions de code, les guidelines de design (comme celles d'Apple), les patterns reconnus, et les critères objectivables permet aux agents d'améliorer leurs résultats progressivement.
- Le goût peut être distillé à travers l'accumulation : en observant des centaines de décisions et de projets, les modèles commencent à capturer des préférences cohérentes ; c'est un processus qui s'améliore avec l'échelle et le contexte.
- Des outils de validation externe (tests visuels, linters, scripts de pré-commit) peuvent servir de garde-fous : même si le goût complet ne peut être testé, on peut bloquer les erreurs manifestes et guider progressivement l'agent vers de meilleures décisions.
- Le goût humain repose aussi sur l'intuition et l'expérience accumulée, qui ne sont pas fondamentalement différentes des patterns que les modèles peuvent apprendre à travers les données et le feedback itératif.
- Une approche collaborative itérative (plan → révision → évaluation utilisateur) permet aux agents d'acquérir du discernement sans avoir à formaliser chaque règle explicitement.

**Avis négatifs** :
- Même en externalisant précisément ce qu'on veut, les modèles ne généralisent pas au-delà des règles spécifiques énoncées et échouent à capturer l'ensemble quasi-infini des cas particuliers qui constituent le véritable goût.
- Le goût n'est pas simplement un ensemble de règles codifiables : c'est une expérience sensorielle et contextuelle qui disparaît une fois expérimentée et qu'on ne peut pas réduire à des métriques mesurables ou des critères formels.
- Les modèles entraînés sur des préférences agrégées convergent vers un style homogène et évident, perdant les nuances individuelles ou organisationnelles ; moyenner les goûts de plusieurs personnes ne produit rien d'intéressant.
- Contrairement aux humains, les LLM ne peuvent pas apprendre individuellement ou évoluer dans le temps : ils restent figés à un état généraliste sans capacité de long-terme memory, ce qui rend impossible une véritable personnalisation du goût.
- Le goût involve aussi des jugements implicites et l'intuition basée sur l'expérience : on ne peut pas toujours articuler pourquoi quelque chose « sent bon » ou « sent mauvais », et externaliser cela force à perdre les subtilités essentielles.

**Top commentaires** :

- [trjordan](https://news.ycombinator.com/item?id=48672897) : You can't unit test for taste if you haven't written down what you mean by taste. If you can externalize it, then you can. Follow this line of thinking, and the AI-friendly answer is easy: we just have to externalize everything we know, so Claude can implement what I want. Except that I can't fully…
- [zamalek](https://news.ycombinator.com/item?id=48675088) : Unrelated to code, but along the same lines. I've been keeping track of the Reckless Ben case to fuel my unhealthy indignation, and we just had a like-for-like comparison between a human and an LLM. Human: well-scoped argument that does just enough to get the job done with minimal risk. AI: Extreme…
- [cadamsdotcom](https://news.ycombinator.com/item?id=48680939) : You can’t unit test for all the aspects that make up taste, it’s true. But if you break off parts of that - eg. by looking at what is codified out there as “good” design, what’s considered best practice etc - you can create tools the agent can call on that let it get critiques of its own work. What…

---

[Article original](https://dev.karltryggvason.com/you-cant-unit-test-for-taste/) · [Discussion HN](https://news.ycombinator.com/item?id=48657049)
