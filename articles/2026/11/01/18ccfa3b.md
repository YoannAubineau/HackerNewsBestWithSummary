---
article_fetched_at: '2026-11-01T15:37:21.441318Z'
attempts: 0
content_source: extracted
discussion_comment_count: 165
discussion_fetched_at: '2026-11-01T15:37:17.249627Z'
error: null
guid: https://news.ycombinator.com/item?id=50320995
hn_item_id: 50320995
hn_url: https://news.ycombinator.com/item?id=50320995
image_url: https://opengraph.githubassets.com/dbf780aa2e313bdb3a00c279240962d399cbbf3352d4ba756de0adb03672ae0e/guregodevo/memdoor
is_ask_or_show_hn: false
llm_input_tokens: 16315
llm_latency_ms: 11111
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1135
our_published_at: '2026-11-01T15:34:46Z'
rewritten_title: Une équipe de cinq modèles Qwen3.8-27B égale la performance de Fable
  5 sur LiveCodeBench Hard
source_published_at: '2026-10-31T22:46:12Z'
status: summarized
summarized_at: '2026-11-01T15:37:51.836085Z'
title: 'Memdoor: A team of 5 Qwen3.8-27B models beats Fable 5 on LiveCodeBench Hard'
url: https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve
---

## Résumé de l'article

Memdoor est un framework de workflows qui coordonne plusieurs modèles de langue pour résoudre des problèmes de programmation de manière collaborative. Cinq instances du modèle Qwen3.8-27B (un planificateur, deux générateurs d'idées, un solveur, un gestionnaire et un réparateur) communiquent uniquement via des fichiers et interagissent avec un script externe qui valide les solutions.

- La méthode implémente le système GVS5H décrit dans un article de 2026, configurée entièrement en YAML sans code personnalisé ni référence directe au modèle utilisé.
- Sur les dix premiers problèmes de la liste LiveCodeBench Hard, cinq passages chacun, l'équipe atteint la parité avec les résultats rapportés par les auteurs (9,8 et 9,6 problèmes résolus), sans surpassement démontré sur ce petit échantillon.
- Chaque exécution prend en médiane 40 minutes et coûte 0,39 dollar ; les 50 exécutions totalisent 35,79 dollars via OpenRouter.
- Les workflows peuvent fonctionner avec différents fournisseurs (OpenRouter, Anthropic, OpenAI, Gemini) ou localement via Ollama, llama.cpp, vLLM ou LM Studio.
- La solution originale de Fable 5 n'a pas été re-exécutée dans ce framework ; la possibilité de contamination des données d'entraînement (problèmes du printemps 2025) ne peut être exclue.

## Discussion sur Hacker News (165 commentaires)

**Avis positifs** :
- La stratégie multi-agents avec rôles spécialisés (planificateur, créatifs, solveur, gestionnaire) améliore significativement les performances en distribuant le contexte et en éliminant le bruit des tokens de réflexion intermédiaires.
- Les modèles open-weight comme Qwen 3.8-27B sont déjà suffisamment performants pour de nombreuses tâches réelles de programmation, particulièrement en itération rapide et développement local.
- L'approche par harnais (harness engineering) représente une vraie moat technique largement sous-estimée, capable d'extraire beaucoup plus de capacités des modèles existants que ce qu'on croit généralement.
- Les tests en conditions réelles montrent que les utilisateurs ne distinguent pas les résultats entre les swarms de modèles ouverts et les modèles propriétaires (Claude/Fable) sur du travail de production.
- L'infrastructure locale devient viable : possibilité de faire tourner Qwen 27B localement sur hardware grand public avec quantization, éliminant les risques de fuite de données avec les services propriétaires.

**Avis négatifs** :
- Le benchmark LiveCodeBench Hard utilise seulement 10 problèmes (version ancienne) et est fortement saturé ; les gains de 9.8 vs 9.6 vs 8.0 ne sont statistiquement pas différenciables sur cet échantillon minuscule.
- Les quantizations agressives (2-bit Bonsai) dégradent significativement la qualité réelle des modèles malgré les revendications ; les taux d'erreur s'accumulent exponentiellement à travers les tours d'agent.
- Le coût computationnel caché est énorme : ces benchmarks requièrent souvent plus d'une heure sur les problèmes les plus durs et ne généralisant pas bien au-delà de cas d'usage spécifiquement optimisés.
- Les harness optimisées pour un benchmark sont très difficiles à généraliser ; il est 'remarquablement facile' de construire une harness qui améliore une seule évaluation mais extrêmement difficile d'en créer une vraiment généralisable.
- Les modèles ouverts ont des problèmes d'obsolescence : connaissances figées au moment du training et risques de restrictions futures (HuggingFace pourrait supprimer les modèles 'uncensored', les poids sont publics mais le contrôle politique s'accélère).

**Top commentaires** :

- [fedpost](https://news.ycombinator.com/item?id=50321623) : We desperately need to keep local models competitive with the hyper scalers. I won't want to be beholden to them and their whims forever. With anthropic now restricting game reverse engineering I think we're about to cross a Rubicon of censorship.
- [robertkluin](https://news.ycombinator.com/item?id=50326567) : I use a similar approach for some types of work. I use a planner \(read only\), researcher \(read only\), implementer, and reviewer \(read only\). I allow the implementer to spawn researchers and reviewers to help it with its work. I interact with a controller to manage the subagent trees. The agents use…
- [jbellis](https://news.ycombinator.com/item?id=50326126) : I spent several weeks working on trying to get swarms of cheap models to match the coding ability of a single expensive one. My take: it's remarkably easy to build a harness that improves a single eval, and remarkably difficult to build one that generalizes.

---

[Article original](https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve) · [Discussion HN](https://news.ycombinator.com/item?id=50320995)
