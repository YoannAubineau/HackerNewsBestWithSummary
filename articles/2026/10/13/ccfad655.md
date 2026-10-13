---
article_fetched_at: '2026-10-13T16:36:27.438131Z'
attempts: 0
content_source: extracted
discussion_comment_count: 64
discussion_fetched_at: '2026-10-13T16:36:20.309002Z'
error: null
guid: https://news.ycombinator.com/item?id=50069971
hn_item_id: 50069971
hn_url: https://news.ycombinator.com/item?id=50069971
image_url: https://eg2.haku.sh/speed-table.png
is_ask_or_show_hn: false
llm_input_tokens: 5474
llm_latency_ms: 12782
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 897
our_published_at: '2026-10-13T16:17:22Z'
rewritten_title: EmbeddingGemma 2 adapté en modèle de transcription vocale sur appareil
source_published_at: '2026-10-13T11:27:14Z'
status: summarized
summarized_at: '2026-10-13T16:38:04.123559Z'
title: We turned EmbeddingGemma 2 into a speech-to-text model
url: https://eg2.haku.sh/
---

## Résumé de l'article

Google a développé EmbeddingGemma 2, un modèle multimodal capable d'encoder texte, images, audio et vidéo dans un même espace. Des chercheurs ont transformé ce modèle en transcripteur vocal en entraînant uniquement un petit composant « lecteur » qui projette les fragments audio dans l'espace textuel du modèle et retrouve le mot écrit le plus proche, sans modifier le modèle de base.

- La transcription fonctionne entièrement sur appareil (MacBook Air M3) en temps quasi-réel : environ 13 secondes pour une heure d'audio
- Le taux d'erreur atteint actuellement 5%, contre 2–3% pour les modèles vocaux leader ; un meilleur entraînement du lecteur devrait réduire cet écart
- Seul le lecteur a été entraîné (moins de 2 heures sur 8×H100) sur des données vocales libres de droits en anglais
- L'application permet de charger des fichiers audio ou de dicter directement dans n'importe quelle application (touche Option + dictée)
- L'audio ne quitte jamais l'appareil et s'exécute sur le Neural Engine du Mac

## Discussion sur Hacker News (64 commentaires)

**Avis positifs** :
- Application créative et innovante d'un modèle d'embedding, montrant un cas d'usage inattendu et prometteur
- Vitesse remarquable : transcription de 33 minutes en ~6-7 secondes sur M4 Mac Mini, comparable ou supérieure à Parakeet v3 et bien plus rapide que Whisper large
- Potentiel d'amélioration significatif : le WER de 5-8% peut s'améliorer substantiellement avec plus de données d'entraînement variées, et c'est déjà un résultat satisfaisant pour un projet de quelques jours
- Accès local et confidentialité : fonctionne entièrement sur l'appareil sans requêtes externes, contrairement aux modèles cloud
- Représente un saut qualitatif majeur en accessibilité : la transcription automatique est passée d'inutilisable il y a 7 ans à instantanée aujourd'hui, ouvrant de nouveaux workflows auparavant infaisables

**Avis négatifs** :
- Qualité de transcription insuffisante pour un usage professionnel : un WER de 5-8% est trop élevé pour les besoins critiques, bien qu'acceptable en hobby
- Support linguistique limité : actuellement anglais uniquement, sans roadmap claire pour les langues autres que les principales langues européennes
- Code source non ouvert malgré promesses : le projet n'est pas encore opensourcé et la licence effective reste floue, créant une barrière à l'adoption et la contribution
- Peut produire des résultats particulièrement mauvais sur du contenu non-anglophone (ex. portugais transcrit en anglais avec basse qualité) ou sur de l'audio difficile
- Approche possiblement non optimale : un simple tête CTC sur l'encodeur audio produirait probablement de meilleurs résultats avec une inférence plus rapide qu'utiliser les embeddings de mots

**Top commentaires** :

- [Shershah1024](https://news.ycombinator.com/item?id=50071209) : Hi all. I am Shahir. This was my experiment. First of all - Thanks to whoever posted this on HN. It came as a surprise. Just to clarify - This started as just an experiment to see if we can use the fact that text and audio share a vector space in Embedding Gemma 2 to convert audio to text. Had to h…
- [whstl](https://news.ycombinator.com/item?id=50072357) : For people interested in super quick models: "One cool trick" I like for running those kinds of models very quickly on macOS is converting them to CoreML so they run in the Neural Engine. I had amazing success with Spleeter, Demucs, MVSEP-MDX23-music-separation, DeepFilterNet, Whisper, Hunyuan3D fo…
- [sbdaman](https://news.ycombinator.com/item?id=50071933) : Maybe it's just a COVID time blending together effect but it still blows my mind how quickly we went from "automatic audio transcriptions are not even worth having on" to "an hour of audio transcribed in 13s locally." Pre-pandemic it seemed like even the very best in class auto-transcription featur…

---

[Article original](https://eg2.haku.sh/) · [Discussion HN](https://news.ycombinator.com/item?id=50069971)
