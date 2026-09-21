---
article_fetched_at: '2026-09-21T21:27:46.468129Z'
attempts: 0
content_source: extracted
discussion_comment_count: 277
discussion_fetched_at: '2026-09-21T21:27:44.768195Z'
error: null
guid: https://news.ycombinator.com/item?id=49788838
hn_item_id: 49788838
hn_url: https://news.ycombinator.com/item?id=49788838
image_url: https://x.ai/images/news/grok-4-7-og.webp
is_ask_or_show_hn: false
llm_input_tokens: 19707
llm_latency_ms: 11436
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 950
our_published_at: '2026-09-21T21:22:58Z'
rewritten_title: Grok 4.7, le modèle le plus capable pour le codage et le travail
  analytique, lancé aujourd'hui
source_published_at: '2026-09-21T15:50:15Z'
status: summarized
summarized_at: '2026-09-21T21:28:37.233126Z'
title: Grok 4.7
url: https://x.ai/news/grok-4-7
---

## Résumé de l'article

Grok 4.7 est le dernier modèle d'IA de xAI, conçu pour les tâches de codage, d'analyse et de travail professionnel. Il propose le même prix et la même vitesse que la version précédente (Grok 4.6) tout en offrant des performances améliorées, notamment sur les tâches longues et complexes.

- Entraîné sur un base plus large avec renforcement intensif sur des tâches difficiles, le modèle gère mieux les contextes longs et vérifie son propre travail
- Excelle en création de documents et présentations, comparable aux modèles de pointe sur les benchmarks professionnels (droit, santé, finance)
- Utilise une nouvelle architecture de garde-fous, affichant la meilleure résistance aux jailbreaks testée et score de 62,4% sur le benchmark biosécurité de LatchBio
- Équilibre capacités de cybersécurité et faible taux de refus pour usages légitimes, bloquant seulement 3,3% des requêtes à risque sur HackerBench v0.3
- Disponible via Cursor, Grok Build, API, et plateformes cloud au tarif de 2 $ par million de tokens d'entrée et 6 $ par million de tokens de sortie

## Discussion sur Hacker News (277 commentaires)

**Avis positifs** :
- Grok 4.7 offre un bon rapport qualité-prix pour les tâches de codage, notamment pour l'agentic coding et les workflows terminaux, avec une tarification compétitive par rapport à OpenAI et Anthropic.
- Le modèle parle en anglais clair et direct, contrairement au style 'Claudish' verbeux d'Anthropic, ce qui le rend plus lisible pour beaucoup d'utilisateurs.
- Intégration avantageuse avec Cursor ($200/mois) offrant une allocation de tokens très généreuse pour une utilisation pratiquement illimitée.
- Progression rapide et cadence de release agressive montrant une amélioration continue en tant que concurrent frontier viable face à OpenAI et Anthropic.
- Performance particulière en recherche légale, reconnaissance d'images et génération d'images, domaines où les concurrents sont plus limités.

**Avis négatifs** :
- Efficacité en tokens drastiquement dégradée : Grok 4.7 utilise 2,5x plus de tokens (240M vs 97M) pour un gain de performance marginal (46 vs 44), éliminant son avantage historique de concision.
- La comparaison benchmark trompeuse (4.7 xHigh vs 4.6 High) masque probablement une régression réelle, et les tests indépendants (Vals AI, AA) montrent un classement en baisse.
- Prix du cache particulièrement désavantageux ($0.50/M contre $0.25/M pour Fable) rendant les workflows d'IA agent longs plus coûteux que la concurrence.
- Problèmes de fiabilité rapportés : boucles infinies en mode réflexion, instructions ignorées, et tendance à produire du code verbeux et inélégant avec mauvaises pratiques.
- Associations politiques négatives avec Musk dissuadent certains utilisateurs indépendamment de la performance technique, particulièrement concernant les problèmes d'alignement et de modération.

**Top commentaires** :

- [moojacob](https://news.ycombinator.com/item?id=49789234) : Apparently Grok 4.7 has 40% more weights than Grok 4.6, but the price \($6 output token, $2 input\) is the same. Given that the decrease in their margin and the fact they delayed the release of Grok 4.7 almost two weeks past the original date, XAI must not have been happy with the results for 4.7. An…
- [vessenes](https://news.ycombinator.com/item?id=49789739) : Nice to see this release cadence increasing and some continued improvement in quality. I am guessing these models are basically still outcomes of the cursor team integrating with the massive amount of compute they now own: I’d imagine we will see significant step up improvements with grok 5 later t…
- [simonw](https://news.ycombinator.com/item?id=49790209) : https://tools.simonwillison.net/markdown-svg-renderer?url=ht... - default reasoning level. Here's reasoning level high: https://tools.simonwillison.net/markdown-svg-renderer?url=ht... For some reason reasoning effort low and medium used similar numbers of tokens, and xhigh used less than high. I th…

---

[Article original](https://x.ai/news/grok-4-7) · [Discussion HN](https://news.ycombinator.com/item?id=49788838)
