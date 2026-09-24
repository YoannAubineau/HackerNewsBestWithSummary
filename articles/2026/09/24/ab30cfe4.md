---
article_fetched_at: '2026-09-24T05:40:40.471039Z'
attempts: 0
content_source: extracted
discussion_comment_count: 113
discussion_fetched_at: '2026-09-24T05:40:33.273105Z'
error: null
guid: https://news.ycombinator.com/item?id=49817615
hn_item_id: 49817615
hn_url: https://news.ycombinator.com/item?id=49817615
image_url: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__keyword__metacard__light.width-1300.png
is_ask_or_show_hn: false
llm_input_tokens: 9854
llm_latency_ms: 12903
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1044
our_published_at: '2026-09-24T04:53:06Z'
rewritten_title: Google annonce les modèles Gemini 3.8 de synthèse vocale avec personnalisation
  et contrôle créatif
source_published_at: '2026-09-23T15:29:23Z'
status: summarized
summarized_at: '2026-09-24T05:41:18.157810Z'
title: Gemini 3.8 text-to-speech
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/
---

## Résumé de l'article

Google présente deux nouveaux modèles de synthèse vocale (text-to-speech) intégrés à la famille Gemini : le 3.8 Flash TTS pour la création créative avancée et le 3.8 Flash-Lite TTS pour les applications à grande échelle. Ces modèles permettent de générer des voix personnalisées, expressives et multilingues avec un contrôle précis ligne par ligne sur la performance vocale.

- **Gemini 3.8 Flash TTS** offre la création de voix originales à partir de descriptions en langage naturel, avec contrôle détaillé sur l'intonation, le rythme, l'accent et les indices vocaux non verbaux (rires, soupirs).
- **Gemini 3.8 Flash-Lite TTS** optimise le coût et la vitesse pour les applications de doublage massif, création de contenu audio et agents vocaux expressifs.
- Les modèles supportent plus de 100 langues, 2 000+ voix pré-configurées, et la réplication vocale à partir d'échantillons de 30 secondes avec vérification de consentement vocal.
- Chaque contenu audio est marqué de SynthID, un filigrane imperceptible pour détecter le contenu généré par IA et prévenir la désinformation.
- Les modèles sont accessibles dès aujourd'hui via Google AI Studio, l'API Gemini et bientôt en version Entreprise ; des intégrations sont prévues avec Figma, HeyGen, Wondercraft et d'autres partenaires.

## Discussion sur Hacker News (113 commentaires)

**Avis positifs** :
- Le prix est très compétitif (0,27 à 0,81 $/heure selon la variante), particulièrement pour les audiobooks volumineux comparé à ElevenLabs (75$ vs 15$), ce qui rend l'outil accessible à de nombreux utilisateurs
- La qualité vocale est impressionnante et comparable à ElevenLabs v3, avec une expressivité remarquable qui fonctionne bien pour les cas d'usage pratiques
- La technologie fonctionne pour des applications concrètes (audiobooks, dramatiques radiophoniques) et offre plus de contrôle que les concurrents existants grâce à une large bibliothèque de voix
- L'écosystème des modèles TTS locaux (Kokoro, Qwen3, Fish Audio, Higgs) s'améliore rapidement et offre des alternatives viables sans coûts récurrents ni stockage de données
- Les safeguards de consentement et de watermarking (SynthID, C2PA) pour le clonage vocal montrent une approche responsable face aux risques de fraude vocale

**Avis négatifs** :
- Les résultats ignorent fréquemment des éléments clés du prompt (balises de stage directions, intonations spécifiques, indices vocaux) et ne correspondent pas toujours à ce qui est demandé
- Les voix féminines sonnent génériques et identiques, tandis que les voix masculines sont plus convaincantes, suggérant un biais dans les données d'entraînement
- L'expressivité exagérée des modèles SOTA devient fatigante à l'écoute prolongée (plus de 45 secondes), avec des émotions artificielles et distraya incessante
- Le déploiement fragmenté de Google entre plateformes (consumer, prosumer, cloud) crée une incohérence majeure : même modèle, capacités différentes selon la plateforme, ce qui complique l'intégration
- Les accents britanniques sonnent encore non convaincants (accent américain forcé), et la disponibilité régionale est limitée (voice replication indisponible dans certaines régions)

**Top commentaires** :

- [rcr-anti](https://news.ycombinator.com/item?id=49820339) : Pet peeve on Google's AI rollouts: there's no alignment across the three platforms they have, consumer, prosumer, cloud. Scroll to the end of every release, including this one, and you'll see different availabilities. The fun part is the models don't even have the same capabilities across platforms…
- [simonw](https://news.ycombinator.com/item?id=49818414) : « Voice replication: Recreate consistent vocal profiles from just a 30-second audio sample of your voice or a voice you have the rights to use, backed by built-in consent verification, SynthID watermarking, and C2PA credentials to protect both developers and their vocal talent. » I guess voice clon…
- [thangalin](https://news.ycombinator.com/item?id=49818395) : Here's a video of my Emotive Audiobook Creator, KeenLore, a locally hosted web app: https://www.youtube.com/watch?v=WAeHgE94rVo No cloud, no tokens to pay. Reads a book using a full cast of characters. Quotation attribution detection \(for my novel\) is at 97.2% accuracy \(485/499 quotes identified an…

---

[Article original](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/) · [Discussion HN](https://news.ycombinator.com/item?id=49817615)
