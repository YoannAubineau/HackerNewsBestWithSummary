---
article_fetched_at: '2026-05-28T11:11:10.428205Z'
attempts: 0
content_source: extracted
discussion_comment_count: 297
discussion_fetched_at: '2026-05-28T11:11:09.757346Z'
error: null
guid: https://news.ycombinator.com/item?id=48299220
hn_item_id: 48299220
hn_url: https://news.ycombinator.com/item?id=48299220
image_url: http://www.jacquescorbytuech.com/themes/jacques_2026/icons/og-default.png
is_ask_or_show_hn: false
llm_input_tokens: 34260
llm_latency_ms: 15226
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1050
our_published_at: '2026-05-28T10:20:55Z'
rewritten_title: Comment Apple et Google transforment les notifications push en intermédiaires
  éditoriaux
source_published_at: '2026-05-27T19:24:10Z'
status: summarized
summarized_at: '2026-05-28T11:11:32.082556Z'
title: What Apple and Google are doing to push notifications
url: https://www.jacquescorbytuech.com/writing/what-apple-and-google-are-doing-your-push-notifications
---

## Résumé de l'article

Apple et Google contrôlent les deux canaux dominants de notification push mobile (APNs et FCM). Depuis 2009, ces plates-formes sont passées du simple relais de messages à des intermédiaires actifs qui résument, classent, déprioritisent et filtrent les notifications via des modèles d'apprentissage automatique embarqués sur l'appareil (Apple Intelligence et Gemini Nano), réduisant considérablement la visibilité des expéditeurs sur ce qui arrive aux utilisateurs.

- Les plates-formes utilisent des modèles de langage embarqués pour résumer automatiquement les notifications, les regrouper et les classer par importance perçue, avec des contrôles utilisateur (Focus, canaux, permissions) qui limitent progressivement le contrôle de l'expéditeur.
- Les métriques traditionnelles (ouvertures, clics) sont devenues peu fiables car elles ne révèlent pas si une notification a été résumée, déprioritisée, masquée par Focus ou jamais affichée—la couche intermédiaire reste opaque.
- Les notifications pertinentes et personnalisées (basées sur les activités ou demandes de l'utilisateur) traversent les filtres mieux que les envois promotionnels génériques, qui sont systématiquement relégués à des sections secondaires.
- Les expéditeurs devraient déplacer le poids vers les surfaces propriétaires (messages in-app, inboxes produit) que les modèles ne peuvent pas modifier, réserver push pour l'engagement dormant et les alertes transactionnelles, et structurer les messages autour de faits concrets plutôt que de voix de marque.
- À mesure que les assistants IA (Siri, Gemini) apprendront à agir sur les notifications au lieu de les afficher simplement, les expéditeurs devront exposer les actions de leurs apps via App Intents et App Actions pour permettre aux agents de traiter les notifications sans intervention humaine.

## Discussion sur Hacker News (297 commentaires)

**Avis positifs** :
- Apple et Google jouent un rôle utile en filtrant les notifications spam et marketing abusives, protégeant l'attention des utilisateurs face aux abus des développeurs
- Les restrictions des platforms sur les notifications correspondent aux intérêts des utilisateurs plutôt qu'à ceux des marketeurs, qui ont historiquement abusé de ce canal de communication
- Les mécanismes de contrôle des notifications (canaux Android, focus modes iOS) fonctionnent bien quand ils sont correctement configurés et permettent aux utilisateurs motivés de reprendre le contrôle
- La modération des notifications est justifiée par l'expérience réelle : les apps mélangent transactionnel et marketing, rendent les paramètres difficiles à trouver, et créent constamment de nouveaux canaux pour contourner les filtres utilisateurs

**Avis négatifs** :
- Apple et Google utilisent leur position de gatekeepers pour exercer un contrôle opaque et sans appel sur les notifications, créant une dépendance aux intermédiaires tech au lieu de résoudre le problème structurellement
- Les platforms appliquent inconsistamment leurs propres politiques : Uber, eBay et Doordash violent les règles anti-marketing avec impunité tandis que les petits développeurs sont sanctionnés
- La solution repose sur les utilisateurs pour configurer manuellement des dizaines de paramètres complexes et mal étiquetés, ce que la majorité ne fera jamais ; les défauts devraient être sains par défaut
- Les alternatives existent (UnifiedPush, Signal via WebSocket, connexions locales) mais les platforms découragent leur adoption pour maintenir le contrôle et la surveillance centralisée
- Le problème est instrumentalisé pour légitimer une surveillance accrue : les grandes tech font de la modération une excuse pour monitorer et monétiser davantage les données utilisateur plutôt que de simplement empêcher l'abus

**Top commentaires** :

- [lanerobertlane](https://news.ycombinator.com/item?id=48299932) : If my phone interrupts me, it should either mean someone genuinely needs my attention right now or it should not be disrupting me at all. That's my notification set up. Apps allowed to receive push notifications Phone, Messages, Whatsapp, Apple Health, \[brand\] bank. That concludes the list. There i…
- [nateguchi](https://news.ycombinator.com/item?id=48299526) : I feel like this article reads like the author is upset that Apple + Google prevent / control certain types of notifications \(read: spam\) \> Cross-sell, upsell, education and discovery can work on push Push notifications should only be for transactional notifications. I don't want another inbox for…
- [cadamsdotcom](https://news.ycombinator.com/item?id=48301620) : I’m constantly amazed how passive people are with things that steal their attention My phone is in do not disturb mode 24/7. If your app notifies me about something pointless, it gets deleted and I start using your website instead I have a mail rule that moves any email with the word “unsubscribe”…

---

[Article original](https://www.jacquescorbytuech.com/writing/what-apple-and-google-are-doing-your-push-notifications) · [Discussion HN](https://news.ycombinator.com/item?id=48299220)
