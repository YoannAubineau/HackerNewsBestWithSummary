---
article_fetched_at: '2026-09-13T19:08:21.393453Z'
attempts: 0
content_source: extracted
discussion_comment_count: 109
discussion_fetched_at: '2026-09-13T19:08:16.543803Z'
error: null
guid: https://news.ycombinator.com/item?id=49682087
hn_item_id: 49682087
hn_url: https://news.ycombinator.com/item?id=49682087
image_url: https://techcrunch.com/wp-content/uploads/2025/11/revolut.png?resize=1200,629
is_ask_or_show_hn: false
llm_input_tokens: 8082
llm_latency_ms: 11013
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1054
our_published_at: '2026-09-13T18:54:03Z'
rewritten_title: Revolut a divulgué des données clients suite à des demandes frauduleuses
  usurpant une agence gouvernementale
source_published_at: '2026-09-13T09:59:58Z'
status: summarized
summarized_at: '2026-09-13T19:09:09.436186Z'
title: Revolut confirms customer data breach through fake government requests
url: https://techcrunch.com/2026/09/12/revolut-confirms-customer-data-breach-through-fake-government-requests/
---

## Résumé de l'article

Revolut, fintech britannique de services bancaires et de paiement comptant plus de 80 millions de clients mondiaux, a confirmé avoir partagé les informations sensibles de certains clients avec un tiers non autorisé après avoir reçu des demandes falsifiées provenant d'une adresse email d'une agence gouvernementale légitime.

- Les données exposées incluaient identité, dates de naissance, adresses postales et électroniques, numéros de téléphone, copies de documents d'identité (passeports, permis de conduire), ainsi que potentiellement des selfies de vérification, relevés de compte et historiques de transactions
- Revolut n'a pas divulgué le nombre exact de clients affectés, qualifiant l'incident de « limité », ni précisé le pays ou l'agence gouvernementale impliqués
- L'entreprise a bloqué l'adresse email après découverte de l'usurpation et a alerté l'agence gouvernementale, les forces de l'ordre et les régulateurs ; les systèmes et fonds clients ne sont pas affectés
- Un chercheur réputé en sécurité crypto a indiqué que l'incident semblait cibler des utilisateurs fortunés
- Revolut poursuit son expansion mondiale avec des licences bancaires récentes en France et au Royaume-Uni, et une approbation conditionnelle pour lancer une banque nationale aux États-Unis en 2027

## Discussion sur Hacker News (109 commentaires)

**Avis positifs** :
- Le manque de canaux sécurisés officiels pour les demandes gouvernementales est systémique : la plupart des autorités utilisent simplement des emails ordinaires sans authentification appropriée (DKIM/DMARC), facilitant les usurpations d'identité
- Revolut n'est pas seul dans ce problème : les demandes des forces de l'ordre manquent structurellement de sécurité, et les institutions financières font face à un dilemme légal entre refuser des demandes légitimes ou accepter des fausses demandes
- L'absence de signature cryptographique sur les demandes gouvernementales et l'absence de numéro de référence vérifiable sont des failles systémiques bien documentées dans la gestion des données bancaires
- Les demandes d'urgence sans processus formel ou audience judiciaire contournent les protections légales qui devraient s'appliquer aux données sensibles
- Revolut a historiquement eu des problèmes graves de sécurité et de conformité (désactivation de vérification anti-blanchiment en 2018, défaut de gel de comptes en 2023, taux élevé de fraude signalée)

**Avis négatifs** :
- Si l'email provenait d'un domaine gouvernemental authentifié via DKIM, il est difficile de blâmer Revolut car l'authentification de domaine n'implique pas l'autorité du demandeur à faire la demande
- Le blocage de toutes les demandes sans DKIM aurait pour conséquence illégale d'ignorer de nombreuses demandes gouvernementales légitimes, mettant Revolut dans une situation sans issue
- Les fintech modernes héritent souvent de pratiques de sécurité moins développées que les banques traditionnelles, mais face à des infrastructures gouvernementales elles-mêmes peu sécurisées, l'amélioration unilatérale est impossible
- Stocker des selfies d'identification est légalement obligatoire dans de nombreuses juridictions pour la vérification KYC, et les systèmes automatisés sont plus efficaces qu'une vérification humaine pour prévenir la fraude
- Les alternatives comme faire vérifier les clients par des banques concurrentes locales seraient économiquement et pratiquement contre-productives, et les données sensibles sur la blockchain sont un risque plus pertinent à long terme

**Top commentaires** :

- [neither\_color](https://news.ycombinator.com/item?id=49685481) : I had an interesting experience with my Revolut card. I only top it up when traveling, and the rest of the time it sits nearly empty, with like $3-4. At some point I started getting occasional notifications about transactions declining. Stuff like video game points and random little online shops. C…
- [hndhyc0bdt](https://news.ycombinator.com/item?id=49682729) : Ran an LE request desk for a while and the whole thing was PDFs from .gov-ish email addresses. Only real control we had was calling the agency back on a number we looked up ourselves, not the one on the letterhead.
- [entropyneur](https://news.ycombinator.com/item?id=49686572) : Here in Latvia, anything the government ever sends you of any importance is cryptographicaly signed. Not bulletproof, but that should be a baseline we demand in this age.

---

[Article original](https://techcrunch.com/2026/09/12/revolut-confirms-customer-data-breach-through-fake-government-requests/) · [Discussion HN](https://news.ycombinator.com/item?id=49682087)
