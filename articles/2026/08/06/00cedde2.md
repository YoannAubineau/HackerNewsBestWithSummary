---
article_fetched_at: '2026-08-06T23:51:03.779826Z'
attempts: 0
content_source: extracted
discussion_comment_count: 59
discussion_fetched_at: '2026-08-06T23:50:55.041809Z'
error: null
guid: https://news.ycombinator.com/item?id=49189075
hn_item_id: 49189075
hn_url: https://news.ycombinator.com/item?id=49189075
image_url: https://primeintellect.ai/blog/prime-agent/cover.png?v=prime-agent
is_ask_or_show_hn: false
llm_input_tokens: 9965
llm_latency_ms: 10342
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 914
our_published_at: '2026-08-06T23:27:42Z'
rewritten_title: 'Prime Agent : un harness d''agent auto-améliorant basé sur les modèles
  de langage récursifs'
source_published_at: '2026-08-05T21:11:57Z'
status: summarized
summarized_at: '2026-08-06T23:51:24.331663Z'
title: 'Prime Agent: A self-improving RLM agent'
url: https://www.primeintellect.ai/blog/prime-agent
---

## Résumé de l'article

Prime Agent est un harness de codage open-source conçu autour de deux abstractions : le modèle de langage récursif (RLM) et le Continual Harness. Contrairement aux harness traditionnels avec des schémas fixes, Prime Agent traite le contexte comme une variable et permet à l'agent de créer, modifier et supprimer ses propres prompts, compétences, mémoire et sous-agents en temps réel.

- Le cœur technique repose sur un noyau IPython persistant (REPL) permettant à l'agent d'accéder programmatiquement à son historique, ses sous-agents et ses outils, sans limite de longueur de contexte
- Les sous-agents persistants communiquent par message asynchrone et peuvent être orchestrés en parallèle, avec support du branchement, du clonage et de la récupération de session
- Le mécanisme d'auto-amélioration (/refine) modifie incrementalement le harness en fonction de la trajectoire de l'agent, enregistrant chaque amélioration avec ses résultats
- Prime Agent est évalué sur ARC-AGI 3 (95,5% avec Opus 5, surpassant la baseline humaine), EmulatorBench (reconstruction d'émulateurs), et des tâches long-contexte comme le jeu Factorio
- L'outil est conçu pour fonctionner avec des modèles frontière actuels et futurs, bien qu'aucun modèle n'ait encore été entraîné spécifiquement autour de ce harness

## Discussion sur Hacker News (59 commentaires)

**Avis positifs** :
- Le concept de système auto-améliorant avec boucles de rétroaction est intéressant et représente une évolution naturelle des agents IA existants
- Les résultats sur ARC-AGI-3 (95%) sont impressionnants et montrent le potentiel de l'approche RLM pour les tâches complexes
- L'idée de compartimenter le contexte via des requêtes explicites plutôt que de remplir directement la fenêtre de contexte est intelligente et améliore l'efficacité
- Certains utilisateurs ont eu du succès avec des approches similaires (harnais RLM, gestion des compétences, synchronisation d'équipe)

**Avis négatifs** :
- Le code généré est excessivement volumineux et mal structuré (fichiers de 10K lignes, switch statements de 1000+ lignes) : une preuve que l'approche produit du code blobé et inefficace
- À mesure que les modèles s'améliorent, les harnais complexes deviennent moins nécessaires ; les utilisateurs trouvent qu'un simple stockage de contexte en markdown suffit
- Le concept n'est pas vraiment révolutionnaire mais plutôt une réitération de ce que les systèmes d'agents font déjà, combiné avec des techniques académiques connues
- Le système consomme énormément de tokens pour l'auto-amélioration : à l'économie actuelle des tokens, ce n'est pas viable
- Les résultats présentés peuvent ne pas être rigoureusement validés : absence du classement officiel ARC-AGI-3, risque de surapprentissage sur l'ensemble public

**Top commentaires** :

- [\_joel](https://news.ycombinator.com/item?id=49194368) : Installer might look pretty but it installs to the homebrew dir, despite not being a homebrew package. Very dirty. No uninstall method.
- [andai](https://news.ycombinator.com/item?id=49190852) : A write up on RLM \(Recursive Language Models\) by one of the authors of the RLM paper: https://alexzhang13.github.io/blog/2025/rlm/
- [embedding-shape](https://news.ycombinator.com/item?id=49190153) : LLM-generated code that seemingly went without much review or design is always such an interesting dive into just how bloated you can make code. In this repository, multiple files are close to 10K LOC, one file contains a switch statement that has so many case statements it spans more than 1000 lin…

---

[Article original](https://www.primeintellect.ai/blog/prime-agent) · [Discussion HN](https://news.ycombinator.com/item?id=49189075)
