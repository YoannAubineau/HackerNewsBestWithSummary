---
article_fetched_at: '2026-09-17T23:17:25.068102Z'
attempts: 0
content_failure_reason: content not usable
content_source: feed_fallback
discussion_comment_count: 87
discussion_fetched_at: '2026-09-17T23:17:18.903965Z'
error: null
guid: https://news.ycombinator.com/item?id=49733726
hn_item_id: 49733726
hn_url: https://news.ycombinator.com/item?id=49733726
is_ask_or_show_hn: false
llm_input_tokens: 7724
llm_latency_ms: 10080
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 606
our_published_at: '2026-09-17T22:55:00Z'
rewritten_title: 'HarnessTax : l''importance du cadre de test pour les agents de codage'
source_published_at: '2026-09-16T22:10:13Z'
status: summarized
summarized_at: '2026-09-17T23:18:21.802313Z'
title: 'HarnessTax: How Much Does the Harness Matter for Coding Agents?'
url: https://harnesstax.github.io/
---

## Résumé de l'article

(unable to load content: content not usable)

## Discussion sur Hacker News (87 commentaires)

**Avis positifs** :
- Le harnais importe, mais les différences entre eux sont largement surestimées ; la plupart des harnesses font le travail requis
- Un harnais minimaliste et simple (comme Pi) peut être aussi efficace en termes de coûts qu'un harness fermé complexe, remettant en question la nécessité de systèmes prompts massifs
- L'optimisation du harnais pour les outils natifs spécifiques au modèle (ex: différents formats d'édition pour Claude vs GPT) améliore significativement les performances
- La gestion du contexte et la boucle d'exécution du harnais jouent un rôle crucial, parfois plus important que le nombre d'appels au modèle
- Les harnesses open-source comme Pi offrent une transparence et une adaptabilité supérieures, permettant une personnalisation selon les besoins spécifiques

**Avis négatifs** :
- Le coûts apparemment élevés des harnesses fermés (Claude Code, Codex) incluent des mesures de sécurité et d'alignement légitimes, pas juste du gaspillage ; les ignorer crée des externalités négatives
- Pi manque de sandboxing intégré, d'auto-mode avec classification intelligente et de deny-hard/soft tunables critiques pour les tâches en production sensibles
- Les benchmarks manquent de rigueur : pas de comparaison fiable de tous les harnesses avec tous les modèles ouverts, ni de métriques au-delà du coût en tokens
- Claude Code impose des coûts d'abonnement supplémentaires sur les harnesses tiers (contre les conditions d'Anthropic), créant un verrouillage client injuste
- L'expérience utilisateur des harnesses fermés (Claude Code) présente des bugs d'IHM graves et des keybindings cassés, impactant la praticité bien au-delà du simple harnais

**Top commentaires** :

- [nojs](https://news.ycombinator.com/item?id=49736287) : We really need better harness benchmarks. It seems there's no reliable source that benchmarks the main harnesses against all open source models. I also wish the discussion around Pi did not always use cost/token count as the metric. It's amazingly token efficient, but how does it stack up again ope…
- [lukax](https://news.ycombinator.com/item?id=49736748) : What matters more is that you use the tools that the target model was fine-tuned on. E.g. for editing files with Claude models you should use Edit\(file\_path, old\_string, new\_string, replace\_all\) but with GPT models you should use apply\_patch\_call\(patch\) \(where patch is a custom patch string with cu…
- [corv](https://news.ycombinator.com/item?id=49735592) : My own findings are in line with this research: Having a coding harness is critical but the differences between them are overstated. Personally, I’ve replaced OpenCode with a thin wrapper around Pydantic-AI as the pythonic analogue to Pi-Agent for headless use via Hermes They’d all do the job - I j…

---

[Article original](https://harnesstax.github.io/) · [Discussion HN](https://news.ycombinator.com/item?id=49733726)
