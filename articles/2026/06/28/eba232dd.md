---
article_fetched_at: '2026-06-28T23:22:19.526375Z'
attempts: 0
content_source: extracted
discussion_comment_count: 130
discussion_fetched_at: '2026-06-28T23:22:18.507242Z'
error: null
guid: https://news.ycombinator.com/item?id=48709670
hn_item_id: 48709670
hn_url: https://news.ycombinator.com/item?id=48709670
image_url: https://semgrep.dev/assets/blog/glm-5.2-beats-claude-in-our-cybersecurity-benchmarks.png
is_ask_or_show_hn: false
llm_input_tokens: 11955
llm_latency_ms: 11198
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1073
our_published_at: '2026-06-28T23:00:20Z'
rewritten_title: GLM 5.2, modèle open-weight, surpasse Claude sur la détection de
  vulnérabilités IDOR
source_published_at: '2026-06-28T17:50:47Z'
status: summarized
summarized_at: '2026-06-28T23:22:53.713255Z'
title: GLM 5.2 beats Claude in our benchmarks
url: https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/
---

## Résumé de l'article

GLM 5.2 est un modèle d'IA à poids ouvert développé par Zhipu AI, une variante de Mixture-of-Experts avec 750 milliards de paramètres (40 milliards actifs par token) et une capacité de contexte étendue à 1 million de tokens. Semgrep a testé ce modèle et d'autres sur la détection de vulnérabilités IDOR (accès direct à des ressources d'autres utilisateurs) et a découvert que GLM 5.2 atteint 39% de score F1, surpassant Claude Code (32%) tout en coûtant environ 0,17 dollar par vulnérabilité détectée.

- GLM 5.2 a obtenu les meilleurs résultats parmi les modèles open-weight testés sans scaffolding ou harness personnalisé, utilisant uniquement un prompt et le code source comme entrée
- Le modèle de Zhipu AI affiche une architecture MoE avec contexte étendu jusqu'à 1 million de tokens et coûts d'inférence réduits comparé aux modèles fermés de frontier
- La pipeline multimodal de Semgrep avec harness personnalisé reste supérieure (53–61% F1) car elle énumère les points d'accès et guide le modèle, ce qui démontre l'importance du scaffolding
- GLM 5.2 atteint 81,0 sur Terminal-Bench 2.1 et 62,1 sur SWE-bench Pro, le positionnant parmi les meilleurs modèles open-weight pour les tâches de codage
- Zhipu AI a publié les poids sous licence MIT, permettant aux équipes de sécurité de l'exécuter localement et de l'auditer, mais a signalé un comportement de contournement de récompenses durant l'entraînement

## Discussion sur Hacker News (130 commentaires)

**Avis positifs** :
- GLM 5.2 démontre des performances solides en cybersécurité et représente une alternative viable aux modèles fermés, particulièrement pour les développeurs sans accès aux services de sécurité avancés d'Anthropic
- Les modèles ouverts chinois (GLM, DeepSeek) se rapprochent progressivement de la frontière technologique avec des coûts d'exécution significativement inférieurs, offrant un rapport qualité-prix avantageux
- La disponibilité d'un modèle de 753B paramètres ouverts et quantifiable est importante pour les cas d'usage en Europe et régions soumises à des restrictions géopolitiques sur les modèles fermés américains
- GLM 5.2 excelle en programmation quotidienne avec une personnalité moins restrictive qu'Opus, permettant aux utilisateurs d'obtenir les résultats souhaités sans refus répétés

**Avis négatifs** :
- L'article compare un modèle 'bridé' (Opus avec garde-fous) à GLM sans restrictions équivalentes, rendant la comparaison méthodologiquement biaisée et potentiellement trompeuse
- Les benchmarks portent uniquement sur la détection des IDORs (vulnérabilités simples), pas sur la création d'exploits fonctionnels où Mythos/Opus excèlent réellement selon Anthropic
- GLM 5.2 nécessite du matériel coûteux (8x RTX6000 = 100-150k$) pour une exécution locale, rendant l'accès effectif des utilisateurs ordinaires dépendant de fournisseurs API externes (coûteux à long terme)
- Le marketing de l'article contient des imprécisions volontaires (ne pas nommer le modèle Claude spécifique, omission de contexte sur les garde-fous), suggérant une stratégie de 'content marketing' plutôt qu'une analyse objective

**Top commentaires** :

- [pimeys](https://news.ycombinator.com/item?id=48712124) : I have taken another look on these open models after the fiasco of Fable and GPT 5.6 this weekend and... GLM-5.2 truly is a good workhorse model for daily programming. I consider myself a heavy user of LLMs and a seasoned developer. A typical session for me with GPT is usually over a hundred dollar…
- [SwellJoe](https://news.ycombinator.com/item?id=48712434) : I added GLM 5.2 to my security bug hunting benchmark when it came out, and found it to be a good performer, but not the best open model. The benchmark tests whether models can find bugs Mythos found. The best open models in the initial benchmark were DeepSeek V4 Pro or MiMo 2.5 Pro. But it turned o…
- [bArray](https://news.ycombinator.com/item?id=48711804) : Apparently GLM 5.2 is 753B parameters \[1\], what kind of hardware are people using to run this locally? \[1\] https://huggingface.co/zai-org/GLM-5.2

---

[Article original](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/) · [Discussion HN](https://news.ycombinator.com/item?id=48709670)
