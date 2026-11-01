---
article_fetched_at: '2026-11-01T08:27:57.987793Z'
attempts: 0
content_source: tweet
discussion_comment_count: 186
discussion_fetched_at: '2026-11-01T08:27:55.713523Z'
error: null
guid: https://news.ycombinator.com/item?id=50319358
hn_item_id: 50319358
hn_url: https://news.ycombinator.com/item?id=50319358
is_ask_or_show_hn: false
llm_input_tokens: 14946
llm_latency_ms: 6640
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 676
our_published_at: '2026-11-01T08:12:47Z'
rewritten_title: Anthropic bloque les utilisateurs pour tout ce qui touche à l'entraînement
  de modèles plus grands
source_published_at: '2026-10-31T19:39:19Z'
status: summarized
summarized_at: '2026-11-01T08:28:44.015872Z'
title: Anthropic blocks users for anything touching training larger models
url: https://twitter.com/jiahaoshao1/status/2116475922190922088
---

## Résumé de l'article

Tweet de @jiahaoshao1 :

> Shame on @DarioAmodei / Anthropic. I never distilled Claude—rollouts came from a strong open-source model; Claude just helped submit jobs and run analysis. Still got tagged for "training a competitor," and now anything touching RFT, SFT, or training larger models gets me blocked, Opus 5.5 downgraded to Opus 5, or the session killed outright. You built your models on the world's data, then treat paying users doing research automation as the enemy. Pathetic.

## Discussion sur Hacker News (186 commentaires)

**Avis positifs** :
- Les refus de Claude sur le fine-tuning et l'entraînement de modèles sont justifiés : bloquer plutôt que de fournir des informations erronées ou des secrets de conception évite les abus potentiels
- Les restrictions géographiques et les classifieurs de sécurité sont compréhensibles dans un contexte de sensibilité nationale sur l'IA, particulièrement pour les chercheurs basés en zones géo-bloquées
- Les modèles de petite taille (BERT, tâches locales) fonctionnent bien sans déclencher les garde-fous, offrant une alternative pragmatique pour la plupart des usages
- L'accès à des modèles open-source et alternatifs (Qwen, DeepSeek, Kimi) se développe rapidement et offre des solutions comparables à Opus pour de nombreux cas d'usage
- La nécessité d'avoir plusieurs harnesses et modèles de secours est une saine pratique d'ingénierie, indépendamment des restrictions d'Anthropic

**Avis négatifs** :
- Anthropic applique des restrictions opaques et incohérentes : les classifieurs déclenchent sur du code personnel et des tâches légitimes, même pour des utilisateurs approuvés ou basés aux États-Unis
- L'hypocrisie fondamentale : Anthropic restreint l'accès à la formation de modèles concurrents alors qu'elle a elle-même construit Claude en utilisant massivement des données web sans consentement, y compris des livres piratés (règlement de 1,5 milliard de dollars)
- Les restrictions anti-concurrence visent à maintenir une position de marché plutôt que de servir la sécurité : bloquer la recherche académique légitime et le fine-tuning pour des tâches inoffensives n'a aucun fondement de sécurité
- La nature arbitraire et fluctuante des refus (basée sur des scores de confiance non transparents) rend Claude peu fiable pour les workflows critiques, forçant les utilisateurs vers OpenAI ou les modèles locaux
- L'accumulation de restrictions et de comportements dogmatiques (refus de tâches de sécurité défensive, blocages sur du code personnel, injections de morale dans les artefacts) crée une mauvaise expérience utilisateur généralisée et pousse les utilisateurs à abandonner la plateforme

**Top commentaires** :

- [zmmmmm](https://news.ycombinator.com/item?id=50321207) : It's very clear to me that however much you like Claude and Anthropic models, every professional user shoudl be actively cultivating a set of alternatives and fallbacks to use and seeking to ensure the overall ecosystem is as open, standardised and portable as possible. Anthropic is highly opiniona…
- [bob1029](https://news.ycombinator.com/item?id=50323361) : The guardrails on Anthropic have become an albatross. I've got OAI models doing testing of banking workflows that Claude would have a full scale panic attack over. Even OAI needs some alignment and reassurance regarding the fact that it's not about to pull credit for a real person. GPT6.1 will happ…
- [bushido](https://news.ycombinator.com/item?id=50321403) : Something I've seen it do recently is refusing to extract services out of my own monolith code base because it finds copying code morally wrong. But its refusal to work pattern is getting pretty obnoxious. Another one I ran into last week was it refused to start a developer session to do browser te…

---

[Article original](https://twitter.com/jiahaoshao1/status/2116475922190922088) · [Discussion HN](https://news.ycombinator.com/item?id=50319358)
