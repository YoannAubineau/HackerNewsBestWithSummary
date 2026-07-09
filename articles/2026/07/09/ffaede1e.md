---
article_fetched_at: '2026-07-09T08:24:48.693930Z'
attempts: 0
content_source: extracted
discussion_comment_count: 229
discussion_fetched_at: '2026-07-09T08:24:48.158812Z'
error: null
guid: https://news.ycombinator.com/item?id=48839984
hn_item_id: 48839984
hn_url: https://news.ycombinator.com/item?id=48839984
is_ask_or_show_hn: false
llm_input_tokens: 22670
llm_latency_ms: 11674
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1003
our_published_at: '2026-07-09T07:40:25Z'
rewritten_title: Un développeur expose son épuisement face à l'utilisation quotidienne
  intensive des modèles de langage
source_published_at: '2026-07-09T01:56:28Z'
status: summarized
summarized_at: '2026-07-09T08:25:07.047498Z'
title: I think I have LLM burnout
url: https://www.alecscollon.com/blog/llm-burnout/
---

## Résumé de l'article

Un développeur qui utilise intensément les LLM au quotidien pour coder et chercher des informations décrit une forme de fatigue accumulée suite à des mois d'exposition constante à du contenu généré par intelligence artificielle. Bien qu'il reconnaît les bénéfices productifs de ces outils, il constate une dégradation de son bien-être due aux patterns répétitifs et aux défauts systématiques des textes générés par IA.

- Le développeur consacre plusieurs heures par jour à interagir avec des LLM (Claude Code, Codex, Qwen) pour concevoir, générer et réviser du code, ce qui représente un changement radical par rapport à sa pratique antérieure
- Les LLM produisent régulièrement les mêmes types d'erreurs et d'affectations stylistiques : hallucinations, fausses hypothèses, fragments hachés, emojis excessifs, ce qui génère une usure cumulée
- L'auteur consulte aussi les LLM pour des recherches quotidiennes (ChatGPT, Gemini) en lieu et place de la navigation web traditionnel
- Bien qu'il ne critique pas les LLM en soi, il soulève que la répétition du même style et des mêmes erreurs l'épuise davantage que les défauts ponctuels
- Les mécanismes de personnalisation des interfaces offrent une aide limitée, et l'auteur ne contrôle pas le style du contenu généré par d'autres utilisateurs ou systèmes

## Discussion sur Hacker News (229 commentaires)

**Avis positifs** :
- Les techniques simples de style (guides CLAUDE.md, interdiction d'emojis, ton académique) réduisent significativement la fatigue de lire du code LLM généré
- Les LLMs libèrent du temps sur les tâches répétitives et le boilerplate, permettant de se concentrer sur l'architecture et les problèmes de haut niveau
- Pour les projets personnels et prototypes, les LLMs offrent une barrière à l'entrée drastiquement réduite et permettent de réaliser des idées auparavant impossibles
- Une stratégie claire de test exhaustif (TDD, tests end-to-end) et de typage fort crée des garde-fous efficaces pour contrôler la qualité du code généré
- Les LLMs excellents (comme Opus 4.5+) pour l'ingénierie logicielle représentent un vrai changement de paradigme comparable à la révolution industrielle

**Avis négatifs** :
- Les attentes de productivité augmentent exponentiellement, forçant les développeurs à des sessions de 15h+ sans pause, causant un épuisement physique et mental distinct de l'épuisement normal
- Le coût asymétrique : générer du code LLM prend 5 minutes, le reviewer doit passer des heures à vérifier les hallucinations, fausses hypothèses et à corriger les erreurs sémantiques
- Les développeurs incompétents ou incurieux produisent 10x plus de 'slop' à traiter, transformant le travail en validation sans fin de code mal pensé au lieu de résoudre des problèmes intéressants
- Le plaisir du métier disparaît : passer de la création et du craftsmanship à du 'rubber-stamping' QA et du babysitting d'agents sans compréhension réelle du code produit
- Les mandats corporatifs forçant l'utilisation d'LLMs (leaderboards de tokens, impact sur les évaluations) créent une pression systémique impossible à échapper individuellement

**Top commentaires** :

- [dpc\_01234](https://news.ycombinator.com/item?id=48840162) : I don't think I have a "burnout", but LLMs are really exhausting due to amount of pressure they generate. No one is really pushing me to increase my workload, but at every moment there is always something ready, done by my clankers or clankers of other people that I could be unblocking. In the past…
- [treefry](https://news.ycombinator.com/item?id=48840499) : From my experience, there are mainly 3 burnout reasons. 1. Multi-tasking is the top one. I usually have to frequently switch between 3 to 5 agent windows which are on different things. It's extremely exhausting when each round takes a few minutes. Before coding agent era, I believe most developers…
- [block\_dagger](https://news.ycombinator.com/item?id=48840215) : I've started feeling slightly physically ill when I read Opus output for hours straight. This article rings very true for me. I've started complaining about it with my team; at least have a personal style guide in your agent rules that eliminates emdashes, the "it's not X, it's Y"s, the long lists…

---

[Article original](https://www.alecscollon.com/blog/llm-burnout/) · [Discussion HN](https://news.ycombinator.com/item?id=48839984)
