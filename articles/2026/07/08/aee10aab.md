---
article_fetched_at: '2026-07-08T20:57:50.107380Z'
attempts: 0
content_source: extracted
discussion_comment_count: 233
discussion_fetched_at: '2026-07-08T20:57:46.339706Z'
error: null
guid: https://news.ycombinator.com/item?id=48835111
hn_item_id: 48835111
hn_url: https://news.ycombinator.com/item?id=48835111
image_url: https://x.ai/images/news/grok-4-5-og.png
is_ask_or_show_hn: false
llm_input_tokens: 17458
llm_latency_ms: 12050
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1040
our_published_at: '2026-07-08T20:34:21Z'
rewritten_title: SpaceXAI lance Grok 4.5, son modèle d'IA le plus puissant pour la
  programmation et le travail technique
source_published_at: '2026-07-08T18:00:32Z'
status: summarized
summarized_at: '2026-07-08T20:58:27.765232Z'
title: Grok 4.5
url: https://x.ai/news/grok-4-5
---

## Résumé de l'article

Grok 4.5 est le nouveau modèle d'intelligence artificielle de SpaceXAI, conçu pour exceller dans le codage, les tâches autonomes et le travail de connaissance. Entraîné sur des millions de GPU NVIDIA avec un accent particulier sur l'optimisation des données et l'apprentissage par renforcement, il se positionne comme le modèle le plus performant de l'entreprise.

- Performances en codage : excelle sur des tâches complexes (Rust, C/C++, applications complètes) et atteint le score #1 sur le Harvey's Legal Agent Benchmark pour le travail juridique
- Efficacité : fonctionne à 80 tokens par seconde avec une efficacité tokenique 2x supérieure aux modèles concurrents comparables, réduisant les coûts
- Tarification : $2 par million de tokens d'entrée et $6 par million de tokens de sortie, offrant le meilleur rapport intelligence/coût
- Applications : intégré par défaut dans Grok Build avec capacités avancées pour Excel, PowerPoint et Word ; disponible dans Cursor et via l'API SpaceXAI
- Disponibilité : lancement immédiat sauf en UE (arrivée prévue mi-juillet)

## Discussion sur Hacker News (233 commentaires)

**Avis positifs** :
- Grok 4.5 offre un excellent rapport performance/prix (2$/6$ pour les contextes <200K), avec une efficacité de tokens supérieure à Opus et des tarifs nettement inférieurs à GPT et Claude
- Première fois qu'un modèle utilise des benchmarks difficiles non-gamifiés (DeepSWE, TerminalBench) plutôt que des benchmarks aux réponses publiques, suggérant une performance réelle au niveau Opus 4.7-4.8
- Grok Build offre une interface CLI/TUI très réactive et compétitive, améliorant considérablement l'expérience utilisateur par rapport aux alternatives web, notamment pour les développeurs systèmes
- L'acquisition de Cursor et ses données d'interaction réelles, combinée à l'entraînement par renforcement sur des problèmes difficiles, crée un vrai avantage compétitif et une boucle d'apprentissage vertueuse
- Plusieurs utilisateurs rapportent une excellente performance pour des tâches réelles (apps iOS natives, code complexe, tâches légales), parfois surpassant Claude ou GPT selon le contexte et style de prompt

**Avis négatifs** :
- Grok reste peu populaire et utilisé comparé à Claude/GPT (10x moins de throughput sur OpenRouter), avec une mauvaise réputation due aux associations politiques et à la gestion controversée des plateformes par Musk
- Risque de chaîne d'approvisionnement réel : Musk a historiquement utilisé ses plateformes pour cibler des individus/entreprises qu'il n'aime pas, créant une vulnérabilité commerciale inacceptable pour les clients institutionnels
- Documentation immature et manquante (pas de system card contrairement à Opus 4.8 avec 246 pages), contexte limité à 500K tokens avec prix doublé au-delà de 200K tokens, et capacités d'agentic tool calling apparemment faibles
- Grok n'est pas disponible en Europe (régulation/enquête criminelle en cours), représentant une fragmentation du marché et suggérant des problèmes de conformité non résolus
- Plusieurs témoignages anecdotiques suggèrent que les benchmarks peuvent surrepréenter les performances réelles, avec des utilisateurs rapportant des déceptions systématiques entre les résultats annoncés et l'utilisation quotidienne

**Top commentaires** :

- [Tiberium](https://news.ycombinator.com/item?id=48835179) : It seems to be extremely economical - 4x better reasoning efficiency compared to Opus while being priced at $2/$6. For comparison, GPT 5.4 is $2.5/$15, GPT 5.5/5.6 are $5/$30, Opus 4.8 is $5/$25, Fable is $10/$50. And by benchmarks \(unless they gamed them\), seems to be at around Opus 4.7 level, whi…
- [codemog](https://news.ycombinator.com/item?id=48836079) : Can someone breakdown to me how this makes any sort of economical sense? Spending billions and billions to have the 3rd best model while even the number 1 and 2 players already seem to struggle making a profit. What am I missing here? Not trying to go full Ed Zitron but this doesn’t make sense to m…
- [NitpickLawyer](https://news.ycombinator.com/item?id=48835861) : \(from Cursor's blog\) \> Training included trillions of tokens of Cursor data which capture a wide-range of user interactions with codebases and software tools. This dataset lets the model learn both from existing software as well as developer-agent interactions, capturing how developers work and how…

---

[Article original](https://x.ai/news/grok-4-5) · [Discussion HN](https://news.ycombinator.com/item?id=48835111)
