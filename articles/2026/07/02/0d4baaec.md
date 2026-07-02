---
article_fetched_at: '2026-07-02T00:34:39.049551Z'
attempts: 0
content_source: extracted
discussion_comment_count: 89
discussion_fetched_at: '2026-07-02T00:34:01.651156Z'
error: null
guid: https://news.ycombinator.com/item?id=48747116
hn_item_id: 48747116
hn_url: https://news.ycombinator.com/item?id=48747116
is_ask_or_show_hn: false
llm_input_tokens: 9012
llm_latency_ms: 11717
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 885
our_published_at: '2026-07-02T00:03:22Z'
rewritten_title: FFmpeg 9.1 intègre un nouvel encodeur AAC entièrement réécrit avec
  optimisations perceptuelles
source_published_at: '2026-07-01T14:10:28Z'
status: summarized
summarized_at: '2026-07-02T00:34:57.247315Z'
title: FFmpeg 9.1's new AAC encoder
url: https://hydrogenaudio.org/index.php/topic,129691.0.html
---

## Résumé de l'article

FFmpeg 9.1 introduit un encodeur AAC complètement réengineré qui améliore significativement la qualité audio par rapport aux encodeurs existants comme qaac et fdk-aac selon les métriques d'évaluation audio (Zimtohrli, ViSQOL). L'encodeur réimplémente tous les outils de codage (PNS, TNS, I/S, M/S) et utilise une boucle RDO (optimisation débit-distorsion) pour décider automatiquement quels outils appliquer.

- L'encodeur fonctionne en mode CBR strict avec très peu de variation de débit ; l'utilisation du mode VBR (-q:a) n'est pas recommandée
- Les outils de codage (PNS, TNS, I/S, M/S) font partie intégrale de la boucle RDO sans heuristiques arbitraires ni seuils de débit fixes
- Le codage perceptuel utilise l'énergie de bande masquée pour l'optimisation, allant au-delà de la simple courbe d'allocation de bande utilisée par qaac
- L'encodeur corrige un bug découvert dans le décodeur AAC de FFmpeg concernant le PNS stéréo qui affectait probablement d'autres décodeurs
- L'encodeur a été optimisé pour l'audio 48 kHz ; les utilisateurs peuvent désactiver I/S et PNS (-aac_is 0 -aac_pns 0) si le fichier sera downmixé pour préserver la phase du signal

## Discussion sur Hacker News (89 commentaires)

**Avis positifs** :
- Le nouvel encodeur AAC de FFmpeg surpasse les encodeurs AAC existants en qualité et résout des bugs audio longstanding (PNS en stéréo), permettant de se passer d'encodeurs propriétaires comme Core Audio
- L'investissement dans un meilleur encodeur AAC est justifié car AAC reste le standard de facto pour le streaming vidéo en direct (RTMP, H.264/AAC sur YouTube/Twitch) et bénéficie d'une ubiquité matérielle et logicielle établie depuis deux décennies
- Cette avancée technique est valuable même face à la supériorité générale d'Opus, car elle montre l'intérêt continu d'optimiser les anciens codecs et améliore l'expérience utilisateurs des outils de streaming et capture d'écran (OBS)

**Avis négatifs** :
- L'encodeur est principalement optimisé pour 48 kHz et manque de mode VBR (bitrate variable), ce qui le rend moins flexible que Core Audio d'Apple pour certains cas d'usage professionnels
- Opus surpasse AAC à tous les débits testés et offre bien meilleures performances, rendant l'optimisation d'AAC moins prioritaire qu'investir dans adoption/support d'Opus
- Le problème fondamental reste la fragmentation des codecs et la dépendance historique aux normes propriétaires (AAC, H.264) imposées par les plateformes, plutôt que d'adopter des standards ouverts et royalty-free

**Top commentaires** :

- [cogman10](https://news.ycombinator.com/item?id=48750342) : Man what a showcase for Opus this is. Don't get me wrong, this sort of thing is a valuable exercise and we are better off with better encoders for these older codecs. But look at the numbers for Opus on this benchmark. It simply blows all the AAC encoders out of the water even at 64 kbps.
- [ndiddy](https://news.ycombinator.com/item?id=48750369) : Nice, I'm looking forward to seeing how this performs in practice. FFmpeg's previous AAC encoder produced poor quality output and often had irritating chirping artifacts, so I've always had to install Apple's Core Audio encoder on any computer I do video recording on to get decent sound. I've done…
- [HugoTea](https://news.ycombinator.com/item?id=48750131) : « FFmpeg's AAC DEcoder is busted with regards to stereo PNS, and the bug may be in other AAC decoders too, so we work around it in the encoder. Since no other encoder used PNS, the bug was not found until now. » I don't know what PNS is, but I bet this has been bothering someone's niche use-case fo…

---

[Article original](https://hydrogenaudio.org/index.php/topic,129691.0.html) · [Discussion HN](https://news.ycombinator.com/item?id=48747116)
