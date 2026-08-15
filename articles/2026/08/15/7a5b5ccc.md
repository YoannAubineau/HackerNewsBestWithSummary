---
article_fetched_at: '2026-08-15T18:15:39.461451Z'
attempts: 0
content_source: extracted
discussion_comment_count: 61
discussion_fetched_at: '2026-08-15T18:15:38.439639Z'
error: null
guid: https://news.ycombinator.com/item?id=49299746
hn_item_id: 49299746
hn_url: https://news.ycombinator.com/item?id=49299746
image_url: https://www.mixedbread.com/images/blog/toast-1/intro-toast-1.jpg
is_ask_or_show_hn: false
llm_input_tokens: 6158
llm_latency_ms: 11157
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1002
our_published_at: '2026-08-15T18:11:16Z'
rewritten_title: Toast 1, un agent de recherche spécialisé avec performance frontière
  à coût réduit
source_published_at: '2026-08-14T15:07:57Z'
status: summarized
summarized_at: '2026-08-15T18:15:57.495889Z'
title: Introducing Toast 1
url: https://www.mixedbread.com/blog/toast-1
---

## Résumé de l'article

Toast 1 est un agent de recherche spécialisé lancé par Mixedbread qui fournit une qualité de recherche équivalente aux modèles frontier (Claude Opus 5, GPT-5.6 Sol) tout en étant jusqu'à 10 fois moins cher et 12 fois plus rapide. Il fonctionne comme agent autonome ou sous-agent intégré aux modèles frontier, automatisant la décomposition des requêtes, la collecte d'éléments de preuve et la sélection du contexte pertinent.

- Toast 1 établit un nouveau rapport qualité-coût : sur le benchmark OfficeQA Pro V2, GPT-5.6 Sol avec Toast 1 atteint 70 % de précision à 1,15 $ par tâche, contre 60 % à 4 $ pour Claude Fable 5
- Sur les tâches juridiques (benchmark Harvey LAB), Toast 1 réduit l'utilisation de tokens de 47 millions à 23 millions tout en conservant la même qualité de réponse, diminuant les coûts de plus de 60 %
- Tarification de lancement : 0,30 $ par million de tokens d'entrée, 0,72 $ par million de tokens de sortie, coût moyen d'environ 0,023 $ par requête avec 8 secondes de latence médiane
- Fonctionne de manière optimale avec Mixedbread Search mais reste compatible avec tout backend de recherche existant sans migration requise
- Disponible immédiatement via l'API Mixedbread avec 5 $ de crédits d'essai inclus

## Discussion sur Hacker News (61 commentaires)

**Avis positifs** :
- Les LLM spécialisés pour la recherche répondent à un vrai besoin : les requêtes complexes nécessitent généralement plusieurs tours d'itération et vérification, qu'un agent dédié pourrait accélérer significativement.
- L'approche de Toast (modèle spécialisé + indexation améliorée) surpasse les modèles génériques plus petits et obtient des performances comparables aux modèles frontière tout en étant plus rapide et moins coûteux.
- La réduction des tokens gaspillés en recherche permet au modèle principal de maintenir la qualité tout en réduisant les coûts globaux des tâches.
- L'intégration avec des stacks existants via client compatible OpenAI offre une flexibilité d'utilisation (on-prem ou cloud, données propres ou web).

**Avis négatifs** :
- Google a échoué à créer un bon produit de recherche par IA malgré ses avantages, ce qui remet en question la pertinence générale des LLM pour la recherche.
- Les benchmarks standard (officeqa, Harvey) ne reflètent pas nécessairement la qualité réelle en production ; de plus, les résultats LLM restent imprécis et nécessitent validation humaine.
- Le branding/naming de l'entreprise (Toast, Mixedbread) crée de la confusion auprès du marché cible et nuit à la perception professionnelle du produit, même si le produit lui-même est solide.
- L'absence d'un modèle open-weight limite l'accessibilité comparée à d'autres solutions existantes (SearXNG, Perplexity, Gemini) et réduit la transparence.
- La validité réelle des LLM pour la recherche reste douteuse : les utilisateurs rapportent que Google AI/Gemini se trompent souvent, obligeant à vérifier manuellement de toute façon.

**Top commentaires** :

- [trjordan](https://news.ycombinator.com/item?id=49300478) : I deeply love this idea of specialized LLMs for search. It's also extremely confusing to me how rough Google's entrance here is. When I, a human, need an answer to anything moderately complex, it's unlikely that I get it on the first \(pre-AI\) round of google searching. Simple stuff, sure, but more…
- [satvikpendem](https://news.ycombinator.com/item?id=49304482) : Looks good as I use something similar with the SearXNG MCP, but a shame this isn't an open weight model. There are some wrappers around SearXNG which seem to reduce the token counts returned thus making it easier for the calling model to understand, but a full dedicated model for search is nice. Ho…
- [blitzar](https://news.ycombinator.com/item?id=49304665) : I really wanted this to be a hardware startup - the Juicero of toast. Sadly its another software company.

---

[Article original](https://www.mixedbread.com/blog/toast-1) · [Discussion HN](https://news.ycombinator.com/item?id=49299746)
