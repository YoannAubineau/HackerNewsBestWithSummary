---
article_fetched_at: '2026-06-22T18:22:05.243167Z'
attempts: 0
content_source: extracted
discussion_comment_count: 144
discussion_fetched_at: '2026-06-22T18:22:02.843346Z'
error: null
guid: https://news.ycombinator.com/item?id=48630535
hn_item_id: 48630535
hn_url: https://news.ycombinator.com/item?id=48630535
is_ask_or_show_hn: false
llm_input_tokens: 12908
llm_latency_ms: 10444
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 684
our_published_at: '2026-06-22T18:20:13Z'
rewritten_title: Claude Code stocke le raisonnement chiffré localement sans accès
  utilisateur
source_published_at: '2026-06-22T14:22:46Z'
status: summarized
summarized_at: '2026-06-22T18:22:22.456570Z'
title: The text in Claude Code’s “Extended Thinking” output
url: https://patrickmccanna.net/the-text-in-claude-codes-extended-thinking-output-is-not-authentic/
---

## Résumé de l'article

Claude Code, l'outil d'exécution de code d'Anthropic, enregistre les sessions incluant les « thinking blocks » (processus de raisonnement du modèle). Cependant, ce raisonnement est chiffré localement en une signature inaccessible à l'utilisateur : Anthropic conserve la clé de déchiffrement.

- Le modèle retourne uniquement un **résumé du raisonnement**, pas le raisonnement complet lui-même
- L'accès au texte intégral du thinking nécessite un **contrat d'entreprise** auprès d'Anthropic
- Les fichiers journaux locaux ne permettent pas de reconstituer une véritable **piste d'audit** du raisonnement qui a guidé les actions de l'agent
- La sortie "extended-thinking" via Ctrl+O est une **synthèse avec perte de données**, comparable à sauvegarder une image au format compressé puis l'éditer en format différent
- La documentation d'Anthropic présente ces limites de manière indirecte et peu transparente

## Discussion sur Hacker News (144 commentaires)

**Avis positifs** :
- Anthropic cache full reasoning to prevent competitors from distilling the model through training on reasoning tokens, which is a legitimate business protection strategy used by all major AI labs
- Summarized thinking is sufficient for most practical uses and provides better user experience by being concise and scannable compared to full token dumps
- Hidden reasoning prevents exposure of misaligned or harmful intermediate steps that could cause bad publicity or security issues if revealed to users
- Access to reasoning output (even summarized) helps with performance measurement and observability for deployment, enabling better evaluation of model drift over time

**Avis négatifs** :
- Hiding reasoning tokens undermines transparency and makes it harder to detect prompt injection attacks, data exfiltration attempts, or model behavior that contradicts the final output
- Full reasoning traces are essential for proper debugging and understanding why models make counterintuitive architectural choices, as demonstrated by real cases where hidden reasoning caused unnecessary complexity
- Claiming reasoning tokens represent actual model 'thinking' is misleading marketing; they're post-hoc generated text that can contradict actual internal computation, making the summarization both deceptive and a form of corporate opacity
- The encryption and hiding of reasoning creates an unhealthy dependency where users cannot verify what the model is actually doing, similar to hiring an engineer who refuses to explain their work
- Open-source and Chinese models that do show reasoning are becoming competitive advantages, suggesting Anthropic's opacity may eventually disadvantage rather than protect them as the market evolves

**Top commentaires** :

- [irthomasthomas](https://news.ycombinator.com/item?id=48631634) : I won't use or recommend models with hidden reasoning, \(thats all American models\). It's too much of a risk and makes prompt optimization harder. Risky because it makes it possible for an attacker to prompt inject the reasoning chain to carry out a secret objective, and to hide that from the summar…
- [furyofantares](https://news.ycombinator.com/item?id=48631089) : « It isn’t the actual thinking that drove the model’s actions in a session- but a summary of the thinking logic. This is like using saving a jpeg as a .bmp and then editing the .bmp and presenting it as a .jpeg. The conversion produces data loss. » You've got that backwards, .bmp is a lossless form…
- [StizzurpXDD](https://news.ycombinator.com/item?id=48631232) : This is not just Anthropic. Almost all big AI companies, including OpenAI and Google, hide their model's actual reasoning. This is because revealing the raw reasoning exposes exactly how the AI processes information. These companies spend in huge amounts on R&D to develop a thinking process that is…

---

[Article original](https://patrickmccanna.net/the-text-in-claude-codes-extended-thinking-output-is-not-authentic/) · [Discussion HN](https://news.ycombinator.com/item?id=48630535)
