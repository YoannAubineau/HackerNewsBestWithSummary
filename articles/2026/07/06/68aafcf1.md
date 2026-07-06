---
article_fetched_at: '2026-07-06T16:16:55.956920Z'
attempts: 0
content_source: extracted
discussion_comment_count: 100
discussion_fetched_at: '2026-07-06T16:16:31.912412Z'
error: null
guid: https://news.ycombinator.com/item?id=48802535
hn_item_id: 48802535
hn_url: https://news.ycombinator.com/item?id=48802535
is_ask_or_show_hn: false
llm_input_tokens: 8779
llm_latency_ms: 8520
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 759
our_published_at: '2026-07-06T15:51:10Z'
rewritten_title: Signalbox, une carte en temps réel du réseau ferroviaire britannique
source_published_at: '2026-07-06T09:38:36Z'
status: summarized
summarized_at: '2026-07-06T16:17:48.860697Z'
title: Real-time map of Great Britain's rail network
url: https://www.map.signalbox.io
---

## Résumé de l'article

Signalbox est une application web offrant une visualisation cartographique en direct des trains circulant sur le réseau ferroviaire de Grande-Bretagne. L'outil est accessible à l'adresse map.signalbox.io.

- Utilise Mapbox et OpenStreetMap pour afficher la géolocalisation des trains en temps réel
- Fonctionnalité de contribution pour améliorer la carte via le système de feedback de Mapbox
- Fourni par Trainline, plateforme majeure de réservation de billets de train au Royaume-Uni

## Discussion sur Hacker News (100 commentaires)

**Avis positifs** :
- La carte fonctionne bien en pratique et offre un suivi utile des trains, même si imparfait, particulièrement pour les enfants et les voyageurs
- C'est l'outil de suivi ferroviaire en temps réel le plus utile jamais vu, incluant les réseaux de métro comme le Tyne and Wear Metro et d'autres systèmes régionaux
- La technologie d'identification des trains par correspondance de données de smartphones avec les trajectoires est innovante et similaire aux approches d'autres applications de transport
- La transparence sur la source de données (signalisation ferroviaire publique de Network Rail) et la reconnaissance qu'il s'agit d'interpolation plutôt que de positionnement GPS exact est appréciée
- Des équivalents existent dans de nombreux pays (Suisse, Pays-Bas, Suède, Danemark, Italie, Inde, etc.) montrant l'intérêt global pour ces outils de visualisation ferroviaire

**Avis négatifs** :
- Les positions affichées sont souvent inexactes : trains traversant des autoroutes, l'eau, ou des champs; trains disparaissant/apparaissant sans raison; confusion entre les lignes; icônes décalées par rapport aux voies
- L'interpolation en temps réel est basée sur des données très grossières (signalisation par sections pouvant être très longues) et crée une illusion de précision plutôt qu'un vrai suivi en temps réel
- Les données de station sont obsolètes et incomplètes : stations récemment ouvertes (Cambridge South) absentes, stations anciennes majeures (Sheffield, Cambridge North) manquantes, autocomplétions limitées
- Le rafraîchissement à 2 Hz n'est pas du vrai temps réel, et l'outil est peu fiable pour des usages importants, notamment comparé aux réseaux d'autres pays civilisés mieux investis
- Préoccupations sur la collecte de données de localisation via applications tierces intégrées à l'API, même si les données publiques existaient déjà

**Top commentaires** :

- [Bengalilol](https://news.ycombinator.com/item?id=48803357) : Switzerland's real-time map of trains and public transport \(zoom in on a city to view its public transport in real time\). You can find boats too. And if you check on/off the other options, you get way more informations. https://maps.trafimage.ch/ch.sbb.netzkarte?lang=en&baselayer...
- [dan\_sbl](https://news.ycombinator.com/item?id=48805100) : Meanwhile, the sad state of intercity trains in the United States, outside of the Northeast Corridor. https://asm.transitdocs.com/ https://amtraker.com/map
- [AJRF](https://news.ycombinator.com/item?id=48802688) : « Signalbox's technology identifies the train a device is on by matching a snapshot of smartphone data to a train’s trajectory data. The technology uses advanced algorithms works even with severely degraded data. We are able to pinpoint a smartphone to any type of train without background locatio »…

---

[Article original](https://www.map.signalbox.io) · [Discussion HN](https://news.ycombinator.com/item?id=48802535)
