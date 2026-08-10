---
article_fetched_at: '2026-08-10T03:44:26.761003Z'
attempts: 0
content_source: extracted
discussion_comment_count: 48
discussion_fetched_at: '2026-08-10T03:44:25.580520Z'
error: null
guid: https://news.ycombinator.com/item?id=49231809
hn_item_id: 49231809
hn_url: https://news.ycombinator.com/item?id=49231809
is_ask_or_show_hn: false
llm_input_tokens: 8142
llm_latency_ms: 11454
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 868
our_published_at: '2026-08-10T03:09:45Z'
rewritten_title: Les principes de conception des URI stables et durables sur le web
source_published_at: '2026-08-09T14:32:53Z'
status: summarized
summarized_at: '2026-08-10T03:45:04.766008Z'
title: Cool URIs Don't Change (1998)
url: https://www.w3.org/Provider/Style/URI
---

## Résumé de l'article

Cet article de Tim Berners-Lee (1998) expose les principes fondamentaux pour concevoir des URI (adresses web) qui restent valides et accessibles à long terme. Les URI changent rarement par nécessité technique, mais plutôt parce que les organisations les modifient, souvent par manque de prévoyance ou en exposant des détails techniques volatiles dans l'adresse.

- Éviter d'inclure dans l'URI des éléments qui changeront : répertoires techniques (« cgi-bin »), noms de responsables, extensions de fichiers, classifications organisationnelles ou domaines multiples qui pourraient être fusionnés ou renommés.
- Inclure plutôt la date de création du document au début de l'URI, car elle ne change jamais et permet de différencier les anciennes et nouvelles versions des systèmes.
- Traiter l'espace des URI comme un espace abstrait indépendant du système de fichiers réel, en utilisant le serveur web (par exemple Apache) pour mapper les URI permanentes vers les fichiers actuels, quelle que soit leur localisation physique.
- Comprendre que les liens cassés endommagent la confiance des utilisateurs et la réputation du propriétaire du serveur ; c'est un devoir du webmaster de concevoir des URI stables pour 2, 20, 200 ans ou plus.
- Résister à la tentation de créer une hiérarchie de sujets ou de domaines multiples pour simplifier l'administration court terme, car ces structures organisationnelles évoluent et risquent de casser les liens.

## Discussion sur Hacker News (48 commentaires)

**Avis positifs** :
- L'article gagne en crédibilité avec l'âge : avoir persisté 28 ans à la même URI valide son principe fondamental
- Les redirections 301/302 et les CMS modernes (WordPress) ont largement mis en œuvre cette philosophie, en faisant une priorité commerciale et technique plutôt qu'une simple bonne pratique
- La stabilité des URLs est un enjeu de préservation documentaire à long terme, similaire à l'objectif des DOI, et crée une charge de maintenance réelle lors de migrations ou réorganisations
- Des solutions techniques existent pour la préserver : génération statique append-only, vérification des URLs canoniques, et outils de préservation comme Archive.org, ARK, Perma.cc

**Avis négatifs** :
- Les entreprises majeures (Microsoft, NSF, agences gouvernementales) ignorent régulièrement ce principe ; même des produits tout neufs ont des QR codes/URLs invalides après quelques mois
- Le coût réel de maintenir la compatibilité rétroactive augmente exponentiellement après 2-3 migrations de CMS, contrairement à l'incitation financière des entreprises
- Les URLs encodent intrinsèquement les détails d'implémentation et l'organisation interne, rendant leur stabilité fondamentalement contraire à la flexibilité nécessaire aux systèmes modernes
- La philologie moderne de permanence des URLs crée un paradoxe : les accepter comme permanentes est contre-nature, alors que les moteurs de recherche actuels rendent la notion de bookmarking d'URLs dépassée

**Top commentaires** :

- [torh](https://news.ycombinator.com/item?id=49234288) : Not that long ago I clicked on a link that Microsoft provided somewhere in Windows -- could have been the event log, I don't remember. I do remember it was for a specific support article, but it ended up at a generic landing page for something. I am not talking about a link from Windows 95, it must…
- [mikepurvis](https://news.ycombinator.com/item?id=49233757) : Sadly, though: $ curl -I https://www.nsf.gov/pubs/1998/nsf9814/nsf9814.htm HTTP/2 404 content-type: text/html; charset=UTF-8 content-length: 54737 date: Sun, 09 Aug 2026 17:58:44 GMT strict-transport-security: max-age=31536000; includeSubdomains; preload server: Apache
- [firasd](https://news.ycombinator.com/item?id=49233572) : What this page doesn't mention is 301 or 302 redirects. SEO has made "old URLs staying live" more of a widespread concern than it was at the time. And WordPress etc ship with inbuilt redirects upon slug rename So to a large extent this has been mitigated and not using the suggestion here, which is…

---

[Article original](https://www.w3.org/Provider/Style/URI) · [Discussion HN](https://news.ycombinator.com/item?id=49231809)
