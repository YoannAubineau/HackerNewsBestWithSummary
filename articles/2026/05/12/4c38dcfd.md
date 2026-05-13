---
article_fetched_at: '2026-05-13T00:30:26.884532Z'
attempts: 0
content_source: extracted
discussion_comment_count: 93
discussion_fetched_at: '2026-05-13T00:30:26.149514Z'
error: null
guid: https://news.ycombinator.com/item?id=48111896
hn_item_id: 48111896
hn_url: https://news.ycombinator.com/item?id=48111896
image_url: https://opengraph.githubassets.com/ef127fabadb9bf8563f209fec3eb3f7195b6a60a43f61ead8b122bb2421f3f40/cactus-compute/needle
is_ask_or_show_hn: false
llm_input_tokens: 6668
llm_latency_ms: 11433
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1034
our_published_at: '2026-05-12T23:35:40Z'
rewritten_title: 'Needle: un modèle de 26 millions de paramètres pour l''appel d''outils
  distillé depuis Gemini'
source_published_at: '2026-05-12T18:03:11Z'
status: summarized
summarized_at: '2026-05-13T00:30:44.578350Z'
title: 'Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model'
url: https://github.com/cactus-compute/needle
---

## Résumé de l'article

Needle est un modèle de langage minimaliste basé sur une architecture « Simple Attention Network » créé par distillation de Gemini 3.1, capable d'exécuter des appels de fonction avec des performances compétitives malgré sa taille réduite. Le modèle a été pré-entraîné sur 200 milliards de tokens en 27 heures sur TPU v6e, puis post-entraîné en 45 minutes sur 2 milliards de tokens de données d'appels de fonction.

- Needle fonctionne en production à 6000 tokens/seconde en préfill et 1200 en décoding, avec un poids total de 26 millions de paramètres (configuration : 512 dimensions, 8 têtes d'attention, 4 têtes de valeur)
- L'architecture combine un encodeur (12 blocs) sans couche feed-forward et un décodeur (8 blocs) avec attention croisée, utilisant RoPE et normalisation ZCRMSNorm
- Le modèle surpasse FunctionGemma-270M, Qwen-0.6B et d'autres modèles légers sur les tâches d'appel de fonction unique, mais les modèles rivaux conservent une meilleure capacité conversationnelle
- Les poids sont entièrement publics sur GitHub (Cactus-Compute/needle), avec un générateur de données, un playground web pour tester et affiner le modèle localement
- L'outil fournit une interface CLI et Python pour l'inférence, l'affinage, l'évaluation et l'entraînement complet, conçu pour les appareils consommateurs (téléphones, montres, lunettes)

## Discussion sur Hacker News (93 commentaires)

**Avis positifs** :
- Le modèle de 26M paramètres ouvre des possibilités concrètes pour les appareils minuscules (montres, écouteurs, lunettes) et pourrait fonctionner localement sans dépendre du cloud
- L'architecture innovante sans FFN (feedforward network) est remarquable et la distillation de Gemini pour l'appel de fonctions représente un progrès technique intéressant
- Les cas d'usage pratiques sont prometteurs : assistant vocal pour Home Assistant, remplacement local de Siri, applications mobiles privacy-first, CLI en langage naturel
- Le projet est entièrement open-source avec code accessible et facile à exécuter, permettant à quiconque de l'expérimenter localement
- Des utilisateurs rapportent que le modèle surpasse Siri sur des tâches simples d'appel de fonctions, validant l'approche de distillation

**Avis négatifs** :
- La distillation de Gemini viole potentiellement les conditions d'utilisation de Google qui interdisent explicitement de développer des modèles concurrents ou de reproduire les composants des services
- Les cas d'usage restent peu convaincants : Siri fonctionne déjà sur les téléphones, et les montres intelligentes manquent de scénarios d'agent d'IA réellement utiles comparés à une interface tactile
- Le modèle ne dispose pas encore d'apprentissage en contexte (in-context learning) et ne peut pas enchaîner les appels d'outils, limitant son utilité pour des tâches complexes
- Capacités limitées pour gérer l'ambiguïté : les exemples montrent surtout des cas simples univoques, et il reste flou comment il discrimine entre des centaines de fonctions similaires
- Infrastructure de déploiement manquante : les développeurs reconnaissent ne pas être prêts pour la scalabilité, forçant les utilisateurs à exécuter localement ou sur des VPS personnels

**Top commentaires** :

- [efskap](https://news.ycombinator.com/item?id=48116373) : No FFN is blowing my mind. This is pretty much "Attention Is ACTUALLY All You Need". Reminds me of BERT Q&A which would return indices into the input context, but even that had a FFN. Really exciting work.
- [nl](https://news.ycombinator.com/item?id=48116333) : Do you have any examples or data on the discriminatory power of the model for tool use? The examples are things like "What is the weather in San Francisco", where you are only passed a tool like tools='\[{"name":"get\_weather","parameters":{"location":"string"}}\]', I had a thing\[1\] over 10 years ago…
- [ilaksh](https://news.ycombinator.com/item?id=48113166) : Hmm.. this might make it feasible to build something like a command line program where you can optionally just specify the arguments in natural language. Although I know people will object to including an extra 14 MB and the computation for "parsing" and it could be pretty bad if everyone started d…

---

[Article original](https://github.com/cactus-compute/needle) · [Discussion HN](https://news.ycombinator.com/item?id=48111896)
