---
article_fetched_at: '2026-04-21T13:18:44.357467Z'
attempts: 0
content_source: extracted
discussion_fetched_at: '2026-04-21T13:18:45.866594Z'
error: null
feed_summary: '<p>Article URL: <a href="https://www.politico.eu/article/eu-brussels-launched-age-checking-app-hackers-say-took-them-2-minutes-break-it/">https://www.politico.eu/article/eu-brussels-launched-age-checking-app-hackers-say-took-them-2-minutes-break-it/</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=47831742">https://news.ycombinator.com/item?id=47831742</a></p>

  <p>Points: 255</p>

  <p># Comments: 159</p>'
guid: https://news.ycombinator.com/item?id=47831742
hn_item_id: 47831742
hn_url: https://news.ycombinator.com/item?id=47831742
is_ask_or_show_hn: false
model: anthropic/claude-haiku-4.5
our_published_at: '2026-04-21T13:18:44.233250Z'
rewritten_title: Une application de vérification d'âge de l'Union européenne contournée
  en deux minutes par des chercheurs en cybersécurité
source_published_at: '2026-04-20T08:49:22Z'
status: summarized
summarized_at: '2026-04-21T13:19:03.733264Z'
title: Brussels launched an age checking app. Hackers took 2 minutes to break it
url: https://www.politico.eu/article/eu-brussels-launched-age-checking-app-hackers-say-took-them-2-minutes-break-it/
---

## Résumé de l'article

La Commission européenne a présenté mercredi une application mobile de vérification d'âge destinée à empêcher les enfants d'accéder aux réseaux sociaux, mais des experts en cybersécurité ont rapidement identifié des failles graves dans le code concernant la confidentialité et la sécurité.

- L'application, présentée comme « techniquement prête » par la présidente Ursula von der Leyen, a été contournée en seulement deux minutes
- La Commission a mis le code en open source pour permettre à chacun de vérifier sa sécurité
- L'outil est destiné à aider les pays européens à mettre en œuvre des interdictions d'accès aux réseaux sociaux pour les mineurs

## Discussion sur Hacker News

**Confirmations** :

- Le système présente des failles de sécurité concrètes : les selfies ne sont pas supprimés après vérification (stockage permanent sur l'appareil), ce qui reproduit les erreurs passées de Discord et brise la confiance des utilisateurs dans les systèmes de vérification d'âge.
- La vérification d'âge par application est fondamentalement contournable par partage de téléphone : un adulte peut donner son téléphone déverrouillé à un mineur, rendant le contrôle technique illusoire sans supervision parentale réelle.
- Le projet reflète une surveillance accrue déguisée en protection de l'enfance : il s'agit d'une expansion du contrôle d'identité en ligne plutôt qu'une simple vérification d'âge, avec des implications politiques et libertaires importantes ignorées dans le débat technique.
- Les critiques soulignent une fausse dichotomie : le projet ne peut satisfaire simultanément l'anonymat (ZKP) et la prévention d'abus (rate-limiting), car empêcher la réutilisation de credentials exige une traçabilité gouvernementale.

**Réfutations** :

- Le code publié est un prototype de démonstration, pas une version finale, et l'UE a volontairement ouvert la source pour invitation à l'examen externe avant déploiement—ce n'est pas une arnaque camouflée mais une démarche délibérément transparente.
- La "faille majeure" décrite (édition de fichiers JSON) ne fonctionne que sur téléphones rootés/déverrouillés, pas sur appareils standards ; comparer cela à un hack réel survalue la vulnérabilité initiale.
- Les preuves zéro-connaissance fonctionnent réellement : l'infrastructure eIDAS existante permet à l'app de prouver l'âge sans révéler l'identité au site relying party, distinct de l'authentification gouvernementale initiale qui reste séparée.
- L'alternative au contrôle parental technologique n'existe pas : supprimer tout contrôle équivaut à accepter l'accès mineur sans frein, comme laisser l'alcool à portée des enfants parce que "la responsabilité parentale suffit".

---

[Article original](https://www.politico.eu/article/eu-brussels-launched-age-checking-app-hackers-say-took-them-2-minutes-break-it/) · [Discussion HN](https://news.ycombinator.com/item?id=47831742)
