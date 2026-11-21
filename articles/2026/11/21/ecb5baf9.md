---
article_fetched_at: '2026-11-21T21:22:35.565388Z'
attempts: 0
content_source: extracted
discussion_comment_count: 36
discussion_fetched_at: '2026-11-21T21:22:22.124905Z'
error: null
guid: https://news.ycombinator.com/item?id=50569998
hn_item_id: 50569998
hn_url: https://news.ycombinator.com/item?id=50569998
is_ask_or_show_hn: false
llm_input_tokens: 5245
llm_latency_ms: 6890
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 835
our_published_at: '2026-11-21T21:13:39Z'
rewritten_title: FFmpeg 9.1 'Gauss' et versions stables disponibles avec signatures
  cryptographiques
source_published_at: '2026-11-20T04:02:39Z'
status: summarized
summarized_at: '2026-11-21T21:24:20.614677Z'
title: FFmpeg 9.1 'Gauss'
url: https://ffmpeg.org/download.html#release_9.1
---

## Résumé de l'article

FFmpeg est un outil logiciel libre de traitement multimédia qui existe en plusieurs versions stables. La version 9.1 'Gauss' est la dernière version stable, sortie en novembre 2026, avec un cycle de libération majeur tous les six mois.

- FFmpeg 9.1 'Gauss' inclut les dernières versions des bibliothèques (libavutil 61.19.100, libavcodec 63.24.100, etc.) et a été créée à partir de la branche principale en octobre 2026
- Les versions stables précédentes sont disponibles : 9.0.2 'Lei', 8.1.3 'Hoare', 8.0.3 'Huffman', 7.1.5 'Péter', 6.1.6 'Heaviside', 5.1.10 'Riemann', et 4.4.8 'Rao'
- Toutes les versions sont signées cryptographiquement avec la clé PGP du projet FFmpeg et peuvent être vérifiées pour l'authenticité via gpg
- Les signatures post-quantiques (RFC 9980) sont disponibles pour certaines versions et doivent être vérifiées avec l'outil sq 1.4 ou ultérieur
- Le code source peut être téléchargé en tant que tarball compilé ou via Git ; les utilisateurs sont encouragés à utiliser la branche de développement pour les corrections de bogues plus rapides

## Discussion sur Hacker News (36 commentaires)

**Avis positifs** :
- FFmpeg 9.1 ajoute d'excellentes fonctionnalités : support ASTC, améliorations AAC, encodeurs Vulkan, support LCEVC, protocole libcurl et bien d'autres codecs/formats (DSD, DVD-Audio, etc.)
- Le projet FFmpeg est essentiel à l'écosystème open-source et au-delà, soutenant les services de streaming majeurs et de nombreux projets critiques
- L'amélioration du support HTTP via libcurl offre un accès aux fonctionnalités avancées du protocole HTTP, complétant l'implémentation HTTP interne sous-développée
- Les améliorations du support LCEVC et les nouveaux décodeurs/encodeurs élargissent considérablement les capacités de traitement multimédia du projet

**Avis négatifs** :
- Les notes de version actuelles sont minimalistes et peu accessibles ; la documentation complète du changelog n'est pas facilement découvrable et les versions récentes (comme 9.0) ne sont pas listées sur la page de news officielle
- Les builds binaires par défaut disponibles publiquement sont souvent dépouillés de certaines fonctionnalités (comme vidstabtransform), forçant les utilisateurs à chercher des versions complètes alternatives, ce qui crée confusion et frustration
- Certaines limitations subsistent : le support des cas d'usage avancés comme HLS X-DISCONT avec synchronisation de flux vidéo/audio/sous-titres n'est pas encore résolu

**Top commentaires** :

- [gyan](https://news.ycombinator.com/item?id=50569999) : Changelog: - ASTC image encoding and decoding via libastcenc, with .astc and KTX 1.0 muxers and demuxers - extensively improved AAC encoder - APV Vulkan encoder - iTerm2 inline image protocol muxer - LCEVC payload merging bitstream filter - Graph based bitstream filtering API - ffmpeg CLI dual trac…
- [minimaxa](https://news.ycombinator.com/item?id=50573223) : FFmpeg: holding the world's open-source video code on its shoulders.
- [adzm](https://news.ycombinator.com/item?id=50570667) : Thanks btw for the ffmpeg builds gyan!

---

[Article original](https://ffmpeg.org/download.html#release_9.1) · [Discussion HN](https://news.ycombinator.com/item?id=50569998)
