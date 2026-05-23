---
article_fetched_at: '2026-05-23T20:16:40.758644Z'
attempts: 0
content_source: extracted
discussion_comment_count: 130
discussion_fetched_at: '2026-05-23T20:16:40.210869Z'
error: null
guid: https://news.ycombinator.com/item?id=48247876
hn_item_id: 48247876
hn_url: https://news.ycombinator.com/item?id=48247876
image_url: https://storage.ghost.io/c/ed/a2/eda2c6f7-faef-48b4-9ed4-86a4fa4dca68/content/images/size/w1200/2026/05/ring-oura-zw-hero.jpeg
is_ask_or_show_hn: false
llm_input_tokens: 10650
llm_latency_ms: 10680
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 971
our_published_at: '2026-05-23T19:37:16Z'
rewritten_title: Oura reconnaît recevoir des demandes gouvernementales d'accès aux
  données utilisateurs
source_published_at: '2026-05-23T14:09:57Z'
status: summarized
summarized_at: '2026-05-23T20:17:16.208717Z'
title: Oura says it gets government demands for user data
url: https://this.weekinsecurity.com/oura-says-it-gets-government-demands-for-user-data-will-it-share-how-many/
---

## Résumé de l'article

Oura est un fabricant de bagues intelligentes de suivi sanitaire qui enregistre des données sensibles comme le rythme cardiaque, les cycles de sommeil et la localisation. L'entreprise a confirmé recevoir des demandes gouvernementales d'accès aux données utilisateurs, mais refuse de publier un rapport de transparence malgré les promesses initiales d'évaluer cette possibilité.

- Oura stocke les données utilisateurs de manière à permettre l'accès par le personnel, ce qui expose aussi les données aux demandes gouvernementales munies de mandat, aux attaques informatiques et aux abus internes
- L'entreprise n'utilise pas le chiffrement de bout en bout, permettant le déchiffrage des données à plusieurs points du parcours ring-application-serveurs
- Oura a déclaré examiner chaque demande gouvernementale pour légalité et portée, mais ne divulgue pas le nombre de demandes reçues ni sa taux de refus
- Huit mois après avoir évoqué une évaluation interne, Oura n'a pas répondu aux demandes de publication d'un rapport de transparence public, contrairement à d'autres grandes entreprises technologiques
- Avec 5,5 millions de bagues vendues et une valorisation de 11 milliards de dollars, Oura dispose désormais des ressources financières pour renforcer le chiffrement et la confidentialité des utilisateurs

## Discussion sur Hacker News (130 commentaires)

**Avis positifs** :
- Les données de santé sensibles (cycles menstruels, intimité) sont particulièrement préoccupantes face à la criminalisation de certains actes médicaux et aux poursuites judiciaires potentielles
- Les données biométriques peuvent être combinées avec d'autres informations pour établir des profils intimes détaillés (localisation, état émotionnel, activités) bien au-delà de simples statistiques isolées
- Les alternatives existent : Garmin offline, Withings RGPD-compliant, Pebble open source avec GadgetBridge, ou Apple Watch avec Advanced Data Protection offrant du vrai chiffrement bout-en-bout
- Les gouvernements exigent ces données sans motif légal clair ; l'absence de justification visible augmente les craintes d'utilisation abusive future
- Oura ne réplique pas aux demandes de transparence et ne s'engage pas à publier les statistiques de requêtes gouvernementales, contrairement aux bonnes pratiques du secteur

**Avis négatifs** :
- HIPAA est largement hors de propos ici puisqu'il ne protège que contre les accès non autorisés et n'empêche pas l'accès gouvernemental légal
- Le terme « chiffrement bout-en-bout » est mal utilisé par l'auteur : il confond avec le chiffrement en transit ; Oura n'a jamais prétendu à du E2EE, donc le reproche est flou
- Le chiffrement au repos a peu d'impact pratique contre les gouvernements (ils obtiennent les clés) et les données exfiltrées sont un problème plus grave que l'accès physique aux disques
- Apple elle-même est sujette aux mêmes lois qu'Oura ; sa réputation de confidentialité repose sur du marketing (elle a cédé aux autorités UK, collecte massivement en Chine, etc.)
- Les données de fréquence cardiaque et d'oxygène seules ont peu d'utilité directe pour les gouvernements sans contexte supplémentaire déjà disponible via d'autres canaux

**Top commentaires** :

- [JumpCrisscross](https://news.ycombinator.com/item?id=48248696) : « the once-responsive Oura has not yet replied to any of my inquiries, or committed to releasing the numbers » Illinois has a tight biometric-privacy law \[1\]. I’d bet Oura isn’t particularly careful about prohibiting e.g. a Texas police department querying the protected information of Illinois resi…
- [sz4kerto](https://news.ycombinator.com/item?id=48248262) : "In my previous blog, I revealed that Oura data is not end-to-end encrypted. That means that an Oura user's health data can be unscrambled at certain points as it travels from a person's ring, through their phone app, over the internet, and as it lands on Oura's servers." Very strange -- it seems t…
- [neves](https://news.ycombinator.com/item?id=48249547) : Is it from the evil govs of China or Russia? Oh, no...

---

[Article original](https://this.weekinsecurity.com/oura-says-it-gets-government-demands-for-user-data-will-it-share-how-many/) · [Discussion HN](https://news.ycombinator.com/item?id=48247876)
