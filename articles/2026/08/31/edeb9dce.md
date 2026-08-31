---
article_fetched_at: '2026-08-31T20:31:17.314419Z'
attempts: 0
content_failure_reason: content not usable
content_source: feed_fallback
discussion_comment_count: 66
discussion_fetched_at: '2026-08-31T20:31:07.506164Z'
error: null
guid: https://news.ycombinator.com/item?id=49511856
hn_item_id: 49511856
hn_url: https://news.ycombinator.com/item?id=49511856
image_url: https://jasontucker.blog/content/images/size/w1200/2026/06/birdnet-2.jpeg
is_ask_or_show_hn: false
llm_input_tokens: 5158
llm_latency_ms: 9242
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 694
our_published_at: '2026-08-31T19:51:22Z'
rewritten_title: Migration de 51 000 photos et vidéos d'iCloud vers un serveur Immich
  auto-hébergé
source_published_at: '2026-08-31T16:47:11Z'
status: summarized
summarized_at: '2026-08-31T20:32:55.381333Z'
title: I turned my security cameras into an automatic bird identification system
url: https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/
---

## Résumé de l'article

(unable to load content: content not usable)

## Discussion sur Hacker News (66 commentaires)

**Avis positifs** :
- L'utilisation d'IA audio pour identifier les oiseaux fonctionne très bien en pratique, même avec des microphones de qualité moyenne, et offre une alternative efficace aux applications commerciales comme Merlin Bird ID
- L'approche DIY avec des caméras de sécurité existantes et des solutions open-source (BirdNET-Go, Frigate) permet d'éviter l'enfermement propriétaire, les frais d'abonnement et la dépendance à des services cloud
- Le projet inspire une communauté active : nombreux utilisateurs partagent des variations (e-ink displays, versions portables, intégrations Home Assistant) et améliorations du concept
- L'identification audio des oiseaux est un cas d'usage particulièrement adapté à l'IA, car les oiseaux eux-mêmes utilisent leur capacité à différencier les appels, validant l'approche technique
- Cette réutilisation des caméras de sécurité existantes pour le suivi faunistique représente un meilleur usage que la simple surveillance de propriété

**Avis négatifs** :
- Le modèle BirdNET-Go produit régulièrement des faux positifs (ex : les grenouilles sont identifiées comme des hérons night-crowned, les chauves-souris mal détectées) et nécessite un réglage strict de la confiance
- La qualité des microphones intégrés aux caméras de sécurité est généralement insuffisante ; les appels de chauves-souris nécessitent des fréquences d'échantillonnage plus élevées que ce que ces équipements offrent habituellement
- L'IA a tendance à créer des certitudes convaincantes au-delà de la vérité réelle ; les utilisateurs avertis recommandent de valider visuellement les identifications ou de vérifier par sources externes (iNaturalist)
- Le volume de détections est très variable selon les régions (110 en 7 jours dans l'article vs >110 par jour en Australie), suggérant que l'approche n'est pas universellement calibrée

**Top commentaires** :

- [ben1040](https://news.ycombinator.com/item?id=49512197) : I did exactly this with BirdNet-Go and my Unifi doorbell cam. Unifi exposes an RTSP feed for each camera so it was easy for the tool to just "listen" to the doorbell and start classifying. I have a spare e-ink display and my next weekend project to follow onto this is to wire it up so it shows some…
- [comboy](https://news.ycombinator.com/item?id=49512466) : Btw, Merlin Bird ID app by Cornell University is so good that I got some people interested that weren't into that topic at all.
- [simenf](https://news.ycombinator.com/item?id=49514272) : Cool project! Inspired by AvianVisitors \[1\] I made a similar project \[2\] with an android app for bird detection using Perch, and then displays the birds detected during the last 24 hours with nice art on a samsung frame tv in "art mode". If you dont want to repurpose an old android device, my app a…

---

[Article original](https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/) · [Discussion HN](https://news.ycombinator.com/item?id=49511856)
