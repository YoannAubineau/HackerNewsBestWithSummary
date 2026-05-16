---
article_fetched_at: '2026-05-16T12:19:27.792153Z'
attempts: 0
content_source: extracted
discussion_comment_count: 94
discussion_fetched_at: '2026-05-16T12:19:27.315053Z'
error: null
guid: https://news.ycombinator.com/item?id=48155212
hn_item_id: 48155212
hn_url: https://news.ycombinator.com/item?id=48155212
is_ask_or_show_hn: false
llm_input_tokens: 11728
llm_latency_ms: 14209
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1210
our_published_at: '2026-05-16T11:33:14Z'
rewritten_title: Six requêtes SQL pour détecter la fraude aux transactions bancaires
source_published_at: '2026-05-15T23:22:30Z'
status: summarized
summarized_at: '2026-05-16T12:19:48.329465Z'
title: SQL patterns I use to catch transaction fraud
url: https://analytics.fixelsmith.com/posts/sql-fraud-patterns/
---

## Résumé de l'article

Un analyste spécialisé en intégrité des programmes décrit les requêtes SQL couramment utilisées pour identifier la fraude transactionnelle dans les données de paiements. Ces méthodes s'appliquent à tous les types de transactions loggées (cartes bancaires, allocations sociales, e-commerce, points de vente).

- **Vélocité** : détecter les rafales de transactions en peu de temps, particulièrement les petits montants fixes ($1, $5, $10) qui signalent souvent des tests de carte volée.
- **Voyage impossible** : identifier quand une carte est utilisée dans deux lieux distants en un laps de temps physiquement irréalisable (seuil typique : 600 mph).
- **Anomalies de montants** : flaguer les montants anormaux comme $99,99 ou $499,99 (juste en dessous des seuils de vérification d'identité ou de limite d'ATM).
- **Marchands suspects** : détecter une activité anormalement élevée à un point de vente en comparant chaque marchand à sa propre baseline historique plutôt que des seuils statiques.
- **Heures atypiques** : repérer les transactions en dehors des habitudes horaires du titulaire de carte, après vérification d'une vraie tendance (au moins 2 transactions antérieures dans cette heure sur 90 jours).
- **Fenêtres glissantes composables** : utiliser les window functions SQL pour créer des colonnes intermédiaires permettant aux analystes d'exprimer rapidement de nouvelles hypothèses de fraude par simples filtres, plutôt que des demandes d'ingénierie.

## Discussion sur Hacker News (94 commentaires)

**Avis positifs** :
- Les motifs SQL simples et déterministes restent une base valide en détection de fraude, complémentaires aux approches ML et utiles pour la révision manuelle par les analystes
- Ces heuristiques reflètent des pratiques éprouvées depuis des décennies dans la détection de fraude (détection d'impossible travel, acheteurs par habitude), applicables au-delà des seules transactions bancaires
- L'approche multi-signaux (scorer les transactions sur plusieurs indicateurs plutôt qu'un seul) est raisonnable : une transaction déclenchant 3-4 signaux indique probablement la fraude, tandis qu'un seul signal peut être un usage légitime inhabituel
- Les explainabilité et traçabilité des règles SQL sont avantageuses pour la conformité réglementaire et les appels de décisions, contrairement aux modèles ML opaques impossibles à justifier
- La distinction entre transactions « card present » et « card not present », ainsi que les différentes architectures de paiement (Apple Pay, Google Pay avec DPAN), valident que ces problèmes de détection restent complexes et nécessitent du contrôle granulaire

**Avis négatifs** :
- L'article repose sur des généralisations excessives basées sur le contexte américain (prix sans taxe, arrondis), qui ne s'appliquent pas globalement : les prix ronds sont courants en Europe, les stations-essence imposent des montants fixes, le café peut coûter un nombre entier
- Les heuristiques proposées généreraient des taux de faux positifs inacceptables (jusqu'à 50% de la population selon les critiques) et créent une friction client excessive : voyages d'affaires, urgences nocturnes, couples partageant un compte, ou simples écarts d'habitude seraient bloqués à tort
- L'article semble largement généré par IA : phrases incohérentes, contradictions internes (« aucun pattern n'est suffisant » vs « le pattern 1 suffit »), citations suspectes, et l'auteur « Fixel Smith » apparaît comme une persona synthétique (musicien, romancier, analyste, influenceur)
- Les systèmes de détection réels opèrent en temps réel et à grande échelle, nécessitant des bases de données en mémoire, des moteurs de stream-processing et du ML, pas des requêtes SQL batch ; les contraintes de latence (millisecondes) surpassent les capacités des SGBDR relationnels
- Les banques américaines appliquent ces règles de façon rigide et opaques : impossible d'obtenir une explication, incapable de paramétrer manuellement, forçant les clients légitimes à passer des appels répétés sans succès pour débloquer leurs cartes

**Top commentaires** :

- [jstanley](https://news.ycombinator.com/item?id=48156815) : « Real cardholders almost never buy something for exactly $1.00. Coffee is $4.73, gas is $52.81. The roundness is the signal. » Surely this depends on how the vendor sets their prices? If you're going to buy something from a website to test a stolen credit card you don't just get to make up your ow…
- [Kwpolska](https://news.ycombinator.com/item?id=48157809) : « Border crossings inside 10 minutes. International rings. » Or normal people living in Europe in border-adjacent areas. Also, I guess you don't include card-not-present transactions in this, but you incorrectly assume that every merchant has their location set correctly. And that every sale happen…
- [daneel\_w](https://news.ycombinator.com/item?id=48159229) : In reality, most banks perform a lot of these transaction checks in real time to block fraudulent txes up-front, instead of validating tx legitimacy retroactively at a point where the money is already gone. Some 15 years ago a security rep with Nordea \(a large Nordic bank\) called me late at night a…

---

[Article original](https://analytics.fixelsmith.com/posts/sql-fraud-patterns/) · [Discussion HN](https://news.ycombinator.com/item?id=48155212)
