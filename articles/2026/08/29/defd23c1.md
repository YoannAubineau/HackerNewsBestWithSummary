---
article_fetched_at: '2026-08-29T18:02:52.284109Z'
attempts: 0
content_source: extracted
discussion_comment_count: 68
discussion_fetched_at: '2026-08-29T18:02:49.268276Z'
error: null
guid: https://news.ycombinator.com/item?id=49485416
hn_item_id: 49485416
hn_url: https://news.ycombinator.com/item?id=49485416
image_url: https://pwning.systems/og.png
is_ask_or_show_hn: false
llm_input_tokens: 15022
llm_latency_ms: 13220
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1158
our_published_at: '2026-08-29T17:52:04Z'
rewritten_title: Un moteur Datalog pour maintenir l'état de la mémoire des agents
  LLM lors d'investigations
source_published_at: '2026-08-28T23:27:45Z'
status: summarized
summarized_at: '2026-08-29T18:04:38.621183Z'
title: I accidentally turned LLM memory into program analysis
url: https://pwning.systems/posts/llm-memory-program-analysis/
---

## Résumé de l'article

L'auteur décrit Lemmalog, un moteur Datalog conçu pour maintenir l'état d'une investigation de vulnérabilité assistée par LLM, plutôt que de confier au modèle la reconstruction répétée de ses conclusions. Lemmalog est un système de base de données logique qui stocke des faits et des règles, calcule les conclusions dérivées, et invalide automatiquement les résultats lorsqu'une hypothèse change — résolvant le problème des hallucinations et des contradictions dans les investigations longues.

- Lemmalog sépare le travail entre l'LLM (convertir le langage naturel, le code source et les sorties du débogueur en faits structurés) et le moteur Datalog (maintenir l'état cohérent et ses dépendances via des retraits et déductions incrémentales).
- Sur le benchmark LongMemEval, Lemmalog atteint 0,463 F1 avec ~2 700 tokens par question, contre ~104 000 tokens pour le contexte complet ; sur LoCoMo, il scores 0,533 F1, ce qui le place troisième parmi les systèmes de mémoire dédiés.
- Le système suit la provenance des faits dérivés, permettant d'expliquer pourquoi une conclusion est vraie et d'invalider automatiquement les résultats affectés lorsqu'une prémisse change.
- Les améliorations majeures provenaient de corrections en front-end : résolution d'entités, normalisation des dates, récupération sémantique hybride — pas de l'augmentation de la taille du modèle.
- Lemmalog excelle aux tâches de mises à jour de connaissance et de rejet de prémisses non supportées, mais reste faible sur l'inférence conditionnelle complexe, que l'architecture peut gérer par des règles plutôt que des tuples simples.

## Discussion sur Hacker News (68 commentaires)

**Avis positifs** :
- Combine l'IA symbolique classique (Datalog, logique programmation) avec les LLM pour pallier les limites de mémoire et de raisonnement des modèles, une approche neuro-symbolique prometteuse.
- Résout un problème réel : les LLM oublient les faits invalidés au cours de la conversation et ne propagent pas les corrections, ce que la structure logique déterministe peut corriger.
- L'approche sépare utilement les LLM (traitement du flou) des systèmes logiques (raisonnement déterministe), plutôt que demander aux LLM de tout faire.
- Cas d'usage validé : analyse de sécurité, chasse aux exploits, débogage matériel complexe et recherche en malware où la traçabilité et la cohérence logique sont essentielles.
- Connecte à des concepts établis (Graph RAG, CodeQL, Cyc) tout en les rendant pratiques avec les LLM modernes, et ouvre la voie à un système d'ontologie versionnée et à provenance.

**Avis négatifs** :
- Complexité pratique et coût computationnel élevé : exiger versioning, recalcul des relations et maintenance d'une unique source de vérité ajoute beaucoup de surcharge, ce qui explique l'absence d'adoption généralisée.
- Données LLM générées dérivent naturellement due aux imprécisions du modèle, ce qui corrompt les graphes logiques et nuit à la qualité du raisonnement mécanique en aval.
- Opacité des modèles commerciaux : impossible de vérifier si le modèle utilise réellement les structures logiques fournies ou s'il s'appuie sur son inférence interne, rendant l'impact réel incertain.
- Applicable surtout aux faits concrets et non-ambigus; les informations floues, ambiguës ou basées sur l'opinion restent du ressort des LLM, limitant le champ d'application.
- Confusion entre ce qui est une vraie amélioration et ce qui est juste un placebo structurant : beaucoup d'équipes construisent des systèmes complexes sans preuve que les mécanismes logiques y contribuent réellement à la performance.

**Top commentaires** :

- [sim04ful](https://news.ycombinator.com/item?id=49486931) : I reached a similar conclusion: LLMs should only really sit at the terminals of request fulfilment. 1. User request understanding: natural language -\> a more rigorous representation, in my case Datalog. 2. Result interpretation: facts and derived facts -\> natural language. Between those terminals,…
- [Animats](https://news.ycombinator.com/item?id=49487597) : So he's using an LLM to generate data stored in an "is\_a" representation. That's so classic AI. Soon, he'll discover that he needs quantifiers. Then that "for all" is too strong sometimes, and he needs "for most". That way lies Cyc. It's not a bad idea. But it does have a history.
- [jarboot](https://news.ycombinator.com/item?id=49489707) : I encountered this with trying to have LLMs populate facts about electoral campaigns. Like when a candidate drops out, when endorsements happen, but also if a candidate is un-endorsed or drops and rejoins. It also needed to handle if any of these facts were incorrect. I settled on a knowledge graph…

---

[Article original](https://pwning.systems/posts/llm-memory-program-analysis/) · [Discussion HN](https://news.ycombinator.com/item?id=49485416)
