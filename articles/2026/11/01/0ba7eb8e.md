---
article_fetched_at: '2026-11-01T01:42:10.087372Z'
attempts: 0
content_source: extracted
discussion_comment_count: 39
discussion_fetched_at: '2026-11-01T01:42:07.532204Z'
error: null
guid: https://news.ycombinator.com/item?id=50308697
hn_item_id: 50308697
hn_url: https://news.ycombinator.com/item?id=50308697
image_url: https://dka575ofm4ao0.cloudfront.net/assets/logos/favicon-2b86ed00cfa6258307d4a3d0c482fd733c7973f82de213143b24fc062c540367.png
is_ask_or_show_hn: false
llm_input_tokens: 4777
llm_latency_ms: 7206
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 903
our_published_at: '2026-11-01T00:47:42Z'
rewritten_title: Bunny CDN subit un incident de sécurité impliquant un serveur en
  Arménie
source_published_at: '2026-10-30T19:05:22Z'
status: summarized
summarized_at: '2026-11-01T01:42:40.026886Z'
title: Bunny CDN Security Incident
url: https://status.bunny.net/incidents/p6gf1by9kr7m
---

## Résumé de l'article

Bunny CDN, un service de distribution de contenu, a été victime d'un incident de sécurité touchant l'un de ses fournisseurs d'infrastructure. Un nœud CDN hébergé en Arménie a connu un accès non autorisé via un logiciel de gestion de serveur tiers, mais l'enquête n'a trouvé aucune preuve que le serveur Bunny lui-même ait été compromis.

- L'équipe d'ingénierie a isolé le serveur en 20 minutes après l'alerte, puis l'a effacé de manière sécurisée et supprimé de l'infrastructure
- Les données potentiellement exposées incluent le contenu CDN en cache temporaire, les configurations des Pull Zones et les certificats TLS du serveur
- Bunny a révoqué et réémis tous les certificats TLS pour ses domaines de plateforme (b-cdn.net et bunny.run) ; les certificats personnalisés gérés seront réémis dans les 24 heures
- Les données de compte client Bunny et les systèmes internes n'étaient pas stockés sur le serveur affecté
- Les clients gérant leurs propres certificats TLS sont invités à les révoquer et en émettre de nouveaux par précaution

## Discussion sur Hacker News (39 commentaires)

**Avis positifs** :
- Bunny a réagi rapidement et de manière compétente : arrêt du trafic en 20 minutes, révocation des certificats, et suppression permanente du serveur affecté
- La responsabilité incombe au fournisseur de services : Bunny doit répondre de ses choix d'infrastructure tiers, même si Gcore a été piratée en premier
- Les certificats gérés par Bunny sont automatiquement renouvelés ; seuls les certificats personnalisés des clients nécessitent une intervention manuelle, une mesure de précaution raisonnable
- L'incident était limité : un seul nœud CDN en Arménie affecté, pas d'accès aux données de compte client ni aux systèmes internes

**Avis négatifs** :
- Le protocole d'incident response est défaillant : Bunny a 'securely wiped' le serveur au lieu de préserver toutes les preuves pour investigation, détruisant potentiellement des éléments critiques
- Des milliers de clés privées TLS stockées sur un nœud CDN exposé indique une architecture de sécurité problématique, aggravée par un taux de limitation Let's Encrypt retardant la révocation
- Bunny refusait de divulguer des informations basiques de sécurité lors d'audits, ce qui soulève des doutes structurels sur leurs pratiques et leur confiance en leur infrastructure
- Préoccupations géopolitiques : Gcore serait contrôlée par des intérêts russes avec connexions à Moscou, et Bunny aurait confié les certificats TLS à une entreprise opérant depuis la Russie
- En tant que CDN bon marché sans serveurs propres, Bunny n'a qu'un contrôle limité sur la sécurité de ses fournisseurs tiers ; les risques sont inhérents au modèle économique

**Top commentaires** :

- [colonCapitalDee](https://news.ycombinator.com/item?id=50309403) : Prompt and competent response, as expected from bunny. "Last week, one of our infrastructure providers reported unauthorized access involving third-party server management software. One of our CDN nodes, located in Armenia, was hosted on a server supplied by this provider. After receiving the alert…
- [eraclide](https://news.ycombinator.com/item?id=50309394) : Bunny used Gcore in Armenia. Gcore themselves got hacked, not Bunny. Bunny was just an affected downstream, in only one of their POPs. https://lowendtalk.com/discussion/222315/gcore-compromised-v... The title is heavily misleading.
- [bobtheborg](https://news.ycombinator.com/item?id=50309446) : While neither investigation has found any indication of unauthorized access to our server, we cannot completely rule out the possibility. If unauthorized access to our CDN node did occur, the potentially exposed information would have been: temporarily cached CDN content, Pull Zone configurations,…

---

[Article original](https://status.bunny.net/incidents/p6gf1by9kr7m) · [Discussion HN](https://news.ycombinator.com/item?id=50308697)
