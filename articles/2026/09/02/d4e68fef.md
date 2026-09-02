---
article_fetched_at: '2026-09-02T18:15:52.074570Z'
attempts: 0
content_source: extracted
discussion_comment_count: 281
discussion_fetched_at: '2026-09-02T18:15:50.112026Z'
error: null
guid: https://news.ycombinator.com/item?id=49537553
hn_item_id: 49537553
hn_url: https://news.ycombinator.com/item?id=49537553
image_url: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-3-8_flash__blog__header__16-9__light.width-1300.png
is_ask_or_show_hn: false
llm_input_tokens: 19136
llm_latency_ms: 14911
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1314
our_published_at: '2026-09-02T18:13:17Z'
rewritten_title: Google lance Gemini 3.8 Flash et 3.8 Flash Cyber pour le codage et
  la cybersécurité
source_published_at: '2026-09-02T15:12:40Z'
status: summarized
summarized_at: '2026-09-02T18:17:06.543973Z'
title: Gemini 3.8 Flash and 3.8 Flash Cyber
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/
---

## Résumé de l'article

Google présente Gemini 3.8 Flash et 3.8 Flash Cyber, deux variantes de son dernier modèle de raisonnement et codage. Gemini 3.8 Flash (à $0,75 par million de tokens en entrée) offre des améliorations majeures en ingénierie logicielle et tâches autonomes, tandis que Gemini 3.8 Flash Cyber est un modèle spécialisé en cybersécurité réservé aux défenseurs de confiance via le programme Fairwind.

- Gemini 3.8 Flash surpasse les modèles plus coûteux sur DeepSWE v1.1 (ingénierie logicielle longue durée) et atteint 54,9 % sur HLE-Verified, démontrant des capacités de raisonnement multi-étapes avancées dans les domaines STEM et professionnels
- Le modèle utilise délibérément plus de tokens sur les tâches complexes pour maximiser les performances, avec des niveaux d'effort configurables pour l'efficacité
- Gemini 3.8 Flash Cyber atteint une performance de frontier-level en découverte autonome de vulnérabilités (>70 % de taux de réussite sur 20 langages de programmation) et un pass@1 de 47,2 % sur CWE-Bench pour la correction de vulnérabilités
- Les équipes de Google (Chrome Security, Cloud Vulnerability Research) rapportent des gains réels : 2,6× plus de correctifs corrects en cybersécurité et découverte de vulnérabilités critiques en moins de 2 heures
- Les deux modèles intègrent des protections contre les injections de prompts et les usages malveillants en chimie, biologie, radiologie, nucléaire et cyberattaque offensive

## Discussion sur Hacker News (281 commentaires)

**Avis positifs** :
- Les modèles Flash de Gemini offrent un excellent rapport qualité-prix avec des performances proches des modèles phares (Opus, Sol) à une fraction du coût et avec une vitesse exceptionnelle, particulièrement adaptés aux tâches de codage et d'analyse multimodale.
- La stratégie d'amélioration continue et rapide de Google (versions 3.6, 3.7, 3.8 en quelques semaines) démontre une accélération de l'innovation en post-training, et les benchmarks montrent des gains substantiels notamment au niveau de raisonnement moyen.
- Gemini 3.8 Flash bénéficie d'avantages structurels uniques : accès aux TPU propriétaires de Google, intégration avec la Recherche Google, support audio/vidéo, et grounding avec Google Maps, offrant des capacités multimodales supérieures à la concurrence.
- L'expérience utilisateur avec Flash s'améliore constamment pour les cas d'usage réels (planification de voyages, extraction de données, recherche d'informations locales), où le modèle surpasse régulièrement ses concurrents malgré sa plus petite taille.
- Les utilisateurs rapportent une satisfaction croissante avec la rapidité de génération de tokens et la fiabilité pendant les heures de travail, rendant le modèle attractif pour une utilisation en production avec les bons outils (antigravity CLI).

**Avis négatifs** :
- Google maintient une stratégie de déploiement fragmentée et confuse (Gemini.google.com en retard, AI Studio, antigravity CLI) qui crée de la friction pour les utilisateurs et contraste nettement avec la disponibilité immédiate des modèles chez Anthropic et OpenAI.
- Gemini 3.8 Flash consomme près du double de tokens que 3.7 pour des gains de performance marginaux, ce qui remet en question l'efficacité réelle des améliorations et augmente les coûts opérationnels malgré l'annonce de prix réduits.
- Pour les tâches de codage complexe et les révisions de code, le modèle reste inférieur à Claude Opus et GPT Sol, nécessitant plus d'itérations et produisant du code de qualité inférieure, avec un comportement jugé « reckless » et peu fiable en production.
- Gemini 3.5 Pro a été abandonné sans explication publique claire, suggérant un pivot stratégique qui interroge sur la viabilité à long terme de la gamme Pro et créant de l'incertitude chez les utilisateurs investis.
- Les guardrails de sécurité bloquent excessivement l'utilisation légitime (génération d'images pour applications pédagogiques, optimisation de code avec JIT), et les capacités de recherche de connaissances du modèle restent souvent inexactes ou hallucinator, comme observé dans Google Search AI Mode.

**Top commentaires** :

- [simonw](https://news.ycombinator.com/item?id=49538953) : The speed combined with the fact that this thing is really good at HTML JavaScript is pretty exciting. Here's what I got for 1.8 cents and 13 seconds from the prompt "make me a cool thing in html": https://gisthost.github.io/?6a77bc41a81718c6aaa10d4ab243c59f Transcript here \(it was part of a chat\):…
- [jampa](https://news.ycombinator.com/item?id=49538512) : I've been using Gemini 3.7 for my personal trip planning app. Across multiple benchmarks, it ranks higher on everything I tried: - Real world knowledge \(when a thing opens and closes, the geographic region, historical facts\). It's also the best at taking a cluster of places and working out a visiti…
- [mattlondon](https://news.ycombinator.com/item?id=49537983) : Currently top at https://deepswe.datacurve.ai - beating Opus 5! https://artificialanalysis.ai/models/gemini-3-8-flash shows an intelligence score of 59, the same as Opus 5 medium! Wow - for a flash model this seems to benchmark powerfully. Remains to be seen what it is like to use.

---

[Article original](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) · [Discussion HN](https://news.ycombinator.com/item?id=49537553)
