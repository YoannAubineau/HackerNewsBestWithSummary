---
article_fetched_at: '2026-08-28T20:32:04.923854Z'
attempts: 0
content_source: extracted
discussion_comment_count: 118
discussion_fetched_at: '2026-08-28T20:31:40.885949Z'
error: null
guid: https://news.ycombinator.com/item?id=49468818
hn_item_id: 49468818
hn_url: https://news.ycombinator.com/item?id=49468818
image_url: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_3-5_transcribe.width-1300.jpg
is_ask_or_show_hn: false
llm_input_tokens: 10967
llm_latency_ms: 11978
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 919
our_published_at: '2026-08-28T19:44:09Z'
rewritten_title: Google lance Gemini 3.5 Transcribe, un modèle de transcription vocale
  intelligent et précis
source_published_at: '2026-08-27T18:03:42Z'
status: summarized
summarized_at: '2026-08-28T20:35:11.166312Z'
title: Gemini-3.5-Transcribe
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/
---

## Résumé de l'article

Gemini 3.5 Transcribe est un nouveau modèle de reconnaissance vocale développé par Google, conçu pour convertir l'audio en texte formaté avec une précision supérieure aux systèmes conventionnels. Il gère le bruit de fond, le jargon complexe et nettoie les hésitations, et est accessible via l'API Gemini pour les développeurs ainsi que dans plusieurs applications Google.

- Disponible en deux modes : streaming en temps réel (API Live, latence sub-seconde) et traitement d'audio pré-enregistré (API Interactions) avec attribution de locuteurs et horodatage au niveau des mots
- Performances améliorées : taux d'erreur sur les mots (WER) de 4,0% en streaming et 2,6% en non-streaming ; temps de transcription final réduit de 70% par rapport à Chirp 3
- Fonctionnalités intelligentes : gère les auto-corrections, supprime les mots de remplissage, formate automatiquement le texte, prend en charge plus de 85 langues avec détection automatique, et identifie jusqu'à 3 locuteurs
- Vocabulaire personnalisé : reconnaît la terminologie spécialisée et les orthographes uniques en s'adaptant au vocabulaire fourni
- Déploiement : accessible aux développeurs via Google AI Studio et Gemini Enterprise Agent Platform en préversion publique ; intégré dans l'appli Gemini (macOS), Rambler (Android) et bientôt disponible dans Chrome

## Discussion sur Hacker News (118 commentaires)

**Avis positifs** :
- Excellente précision globale et gestion du formatage, superbe pour les cas d'usage en dictation personnelle et transcription générale
- Gère bien les conversations multilingues et détecte les langues mélangées mieux que beaucoup de concurrents (Whisper, Parakeet)
- Bon rapport coût/performance par rapport à ElevenLabs Scribe si la précision est similaire (~0,12$/heure contre 0,22$/heure)
- Intégration fluide dans l'écosystème Google (Gboard, Gemini app, Chrome) avec suppression des mots de remplissage et édition vocale
- Latence acceptable pour de nombreux cas d'usage, competitive avec Soniox sur certaines benchmarks

**Avis négatifs** :
- Latence insuffisante pour les applications de traduction en temps réel et commandes vocales comparé à Soniox STT v5
- Limitations critiques en diarisation multi-locuteurs (max 3 personnes) contrairement à Deepgram et Soniox, problématique pour les réunions professionnelles
- Problèmes de déiticitilité multilingue avérés : classifie le suédois comme du néerlandais, traite mal les jargons spécialisés multilingues et les acronymes
- Mode 'Smart' simplifie excessivement le texte et supprime des parties importantes du discours, nécessitant corrections manuelles plus difficiles qu'une saisie manuelle sur Android
- Disponibilité limitée (Pixel 11+ seulement, déploiement lent), processus d'accès API confus (délais de facturation indéterminés, interface Google Cloud compliquée)

**Top commentaires** :

- [Lucasoato](https://news.ycombinator.com/item?id=49471856) : I’ve tested at least 20 STT models in a benchmark I’ve set up with German, Italian and English voices from meetings in my company. The voices contained very industry specific words, the languages changed from one sentence to another, sometimes words in a language were mentioned while a discussion w…
- [etra0](https://news.ycombinator.com/item?id=49483685) : Just a few months ago I set-up a serverless gpu service just using whisper.cpp and it detects very well my very-local spanish modisms. I have an active program running on a vps that hits the serverless gpu with the audio when needed because I went with a telegram bot instead of building an app \(and…
- [Crystalin](https://news.ycombinator.com/item?id=49471838) : I've been testing it on Pixel 11 Pro and I mostly dislike it. It is convenient when you have something long to say without thinking about it first. But the main issue is when you want to say something precise with specific wording it might "simplify" it and break the meaning. Something like "I hesi…

---

[Article original](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) · [Discussion HN](https://news.ycombinator.com/item?id=49468818)
