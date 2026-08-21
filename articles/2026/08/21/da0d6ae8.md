---
article_fetched_at: '2026-08-21T20:15:33.216918Z'
attempts: 0
content_source: extracted
discussion_comment_count: 153
discussion_fetched_at: '2026-08-21T20:15:31.491389Z'
error: null
guid: https://news.ycombinator.com/item?id=49381896
hn_item_id: 49381896
hn_url: https://news.ycombinator.com/item?id=49381896
image_url: https://openrouter.ai/stealth/ox-alpha/opengraph-image-1oizug?abd1ffaa6102aa5f
is_ask_or_show_hn: false
llm_input_tokens: 11527
llm_latency_ms: 11788
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 861
our_published_at: '2026-08-21T19:20:19Z'
rewritten_title: Ox Alpha, modèle de raisonnement gratuit pour l'ingénierie logicielle
  et les tâches multi-modales
source_published_at: '2026-08-20T23:56:35Z'
status: summarized
summarized_at: '2026-08-21T20:15:52.555300Z'
title: Ox Alpha
url: https://openrouter.ai/stealth/ox-alpha
---

## Résumé de l'article

Ox Alpha est un modèle de raisonnement conçu pour le codage, les workflows multi-agents et les tâches de production logicielle complexe. Développé et exploité par un fournisseur tiers anonyme, il est accessible gratuitement via OpenRouter.

- Contexte de 1 million de tokens et support multimodal (texte, images, vidéo)
- Conçu spécifiquement pour l'ingénierie logicielle longue durée, le raisonnement complexe et les workflows combinant texte et contexte visuel
- Gratuit : aucun coût pour les tokens de prompt ou de complération
- Performances : débit de 22 tokens/s, latence de 5,50s (P50), disponibilité de 99,19%
- Supporte l'appel de fonctions, les outils et la sortie JSON ; prompts et réponses conservés par le fournisseur mais non utilisés pour l'entraînement

## Discussion sur Hacker News (153 commentaires)

**Avis positifs** :
- Le modèle semble performant sur des tâches créatives et de raisonnement, surpassant des modèles concurrents reconnus sur plusieurs benchmarks selon les utilisateurs
- Offre une alternative gratuite à des modèles payants tout en permettant de réaliser du vrai travail sur des projets personnels, sans nécessiter d'investissement en infrastructure GPU coûteuse
- Contraste avec la censure observable sur d'autres modèles chinois : certains utilisateurs rapportent que ce modèle répond correctement à des questions sensibles (Tiananmen Square, Tibet) avec des réponses équilibrées plutôt que propagandistes
- L'anonymat du fournisseur offre une opportunité de tester une nouvelle architecture sans le poids de la réputation marketing, tout en bénéficiant des analyses communautaires pour l'identifier

**Avis négatifs** :
- Promesses de non-conservation des données potentiellement non vérifiables : les fournisseurs pourraient contourner légalement cette limitation via des transformations, RLHF ou analyse de métadonnées sans que ce soit détectable
- L'absence de transparence sur l'identité du fournisseur, le modèle exact et ses limites de sécurité pose des risques de sécurité des données, particulièrement pour les données propriétaires ou sensibles
- Performances médiocres à mauvaises sur des tâches frontales (CSS, génération de code frontend), indiquant des capacités inégales selon les domaines
- Bien que certains rapportent une bonne réactivité sur Tiananmen Square, d'autres utilisateurs signalent des réponses manifestement censurées ou des comportements variables suggérant possiblement un routage vers plusieurs modèles, rendant l'évaluation de la censure incohérente
- La tendance croissante des modèles « stealth » préoccupe quant à la transparence des modèles d'IA en général : absence de carte modèle, de considérations de sécurité documentées et d'audit externe possible

**Top commentaires** :

- [fedpost](https://news.ycombinator.com/item?id=49382737) : It's Chinese. Won't answer anything about Tiananmen Square but will gleefully give you instructions to perform various electronic warfare attacks that opus and fable instantly refuse. Side tangent, why is fable so weird about questions involving "Welch's method"? Even really trivial ones it'll shut…
- [walrus01](https://news.ycombinator.com/item?id=49382602) : I highly recommend feeding all your proprietary data and confidential personal information into this model as quickly as possible. What could possibly go wrong?! In terms of equivalence of suspicion, this is the external inference provider equivalent of getting free steak that was smuggled out of a…
- [Palmik](https://news.ycombinator.com/item?id=49385661) : OpenCode offers this with ZDR agreement in place. Seems better than OpenRouter if you want to test it out: https://x.com/opencode/status/2090544355824038300

---

[Article original](https://openrouter.ai/stealth/ox-alpha) · [Discussion HN](https://news.ycombinator.com/item?id=49381896)
