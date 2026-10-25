---
article_fetched_at: '2026-10-25T19:23:45.811332Z'
attempts: 0
content_source: extracted
discussion_comment_count: 66
discussion_fetched_at: '2026-10-25T19:23:44.127629Z'
error: null
guid: https://news.ycombinator.com/item?id=50228167
hn_item_id: 50228167
hn_url: https://news.ycombinator.com/item?id=50228167
image_url: https://opengraph.githubassets.com/90e9cf263f4e475ebaa8b03d411d163a9871f7a3325fd80fb0e1d2e9621f1c2e/slee-persis/GVS5H
is_ask_or_show_hn: false
llm_input_tokens: 8399
llm_latency_ms: 10525
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 813
our_published_at: '2026-10-25T19:09:04Z'
rewritten_title: Orchestration multi-agents sans entraînement améliore les modèles
  ouverts jusqu'à la performance des frontières
source_published_at: '2026-10-25T03:56:01Z'
status: summarized
summarized_at: '2026-10-25T19:24:19.912050Z'
title: Five Qwen3.8-27B models match Fable 5 Using GVS5H Harness
url: https://github.com/slee-persis/GVS5H
---

## Résumé de l'article

Une méthode de coordination sans entraînement appelée orchestration basée ledger permet à plusieurs instances du même modèle de résoudre des problèmes de programmation en partageant un plan via système de fichiers. Testée sur les 100 derniers problèmes difficiles de LiveCodeBench, cette technique augmente les performances allant jusqu'à 25,6 points de pourcentage.

- Qwen3.8 Flash Next orchestré atteint 93,0% de pass@1, surpassant Fable 5 (90,4%) à 9% du coût
- Qwen3.8-27B auto-hébergé passe de 66,8% à 92,4% grâce à la décomposition de problèmes et la persistance du contexte
- L'approche ne bénéficie pas universellement à tous les modèles ; certains restent inchangés ou se dégradent
- La méthode est gratuite en entraînement et fonctionne en temps d'inférence via orchestration multi-agents
- Code disponible sous licence MIT, résultats reproductibles sur le benchmark LiveCodeBench

## Discussion sur Hacker News (66 commentaires)

**Avis positifs** :
- Excellente économie d'exploitation : exécution locale avec une acquisition matérielle unique et coûts électriques minimes comparé aux API cloud.
- Les modèles Qwen 3.8 27B offrent un bon rapport qualité-prix et sont accessibles pour les développeurs avec 24GB de VRAM, avec des alternatives viables (Flash Next) pour matériel limité.
- L'approche d'orchestration par état partagé (fichiers Markdown, JSON) est conceptuellement solide et reflète une tendance naturelle vers des harness plus simples et efficaces.
- Qwen 3.8 27B a démontré une capacité à gérer les interruptions et les corrections du contexte sans déstabilisation majeure dans les workflows agentic réels.

**Avis négatifs** :
- Résultats basés sur un benchmark unique et obsolète (dataset mai 2023-avril 2025) avec contamination probable des données, sans comparaison moderne avec Fable 5.1, Opus 5.5 ou Astra.
- La harness elle-même fait une différence majeure dans les résultats, invalidant les conclusions basées uniquement sur la comparaison de modèles ; le véritable progrès vient de l'orchestration, pas du modèle.
- Les modèles 27B-30B souffrent de confabulations et d'hallucinations notables, nécessitant des harness plus strictes pour compenser, contrairement aux modèles frontier qui en sont largement affranchis.
- Évaluation biaisée : utilisation d'une boucle agentive et de tools (délégation, Python) en écart aux règles du benchmark original, ce qui n'est pas une évaluation valide du modèle seul.

**Top commentaires** :

- [vikramkr](https://news.ycombinator.com/item?id=50228389) : So using this harness five qwen3.8-27b models roughly matched Fable 5 on a saturated coding benchmark from early 2025. No comparison to astra/6.1 sol/fable 5.1/opus 5.5. No comparison on a benchmark that reflects actual agentic work \(and agentic behavior is what modern models optimize for anyway -…
- [badsectoracula](https://news.ycombinator.com/item?id=50228427) : Interesting but \(from the PDF\): Every role but the verifier is the same underlying model, called in a fresh context and coordinating through a shared workspace on disk: \<ws\>/task.md - the problem statement \<ws\>/plan.md - the manager’s overarching plan \<ws\>/tasks.json - a debug mirror of the task li…
- [Olscore](https://news.ycombinator.com/item?id=50228925) : Everybody is converging on similar ideas, but the execution isn't super clean in a lot of "software factories" popping up. Coordinating through shared written state becomes obvious once you build something complex enough. Anyways, I have been building Pullboard \(open source\). The original concept c…

---

[Article original](https://github.com/slee-persis/GVS5H) · [Discussion HN](https://news.ycombinator.com/item?id=50228167)
