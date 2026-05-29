---
article_fetched_at: '2026-05-29T15:03:06.006561Z'
attempts: 0
content_source: extracted
discussion_comment_count: 136
discussion_fetched_at: '2026-05-29T15:03:01.209296Z'
error: null
guid: https://news.ycombinator.com/item?id=48319509
hn_item_id: 48319509
hn_url: https://news.ycombinator.com/item?id=48319509
is_ask_or_show_hn: false
llm_input_tokens: 12336
llm_latency_ms: 11245
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 807
our_published_at: '2026-05-29T14:59:37Z'
rewritten_title: Volkswagen bloque l'intégration Home Assistant en exigeant une assertion
  client
source_published_at: '2026-05-29T05:45:36Z'
status: summarized
summarized_at: '2026-05-29T15:04:02.785882Z'
title: Volkswagen blocks Home Assistant by requiring client assertion
url: https://github.com/robinostlund/homeassistant-volkswagencarnet/issues/967
---

## Résumé de l'article

Home Assistant Volkswagen Carnet est une intégration permettant de contrôler et monitorer les véhicules Volkswagen connectés via Home Assistant. Volkswagen a modifié son authentification en exigeant une assertion client, ce qui empêche désormais Home Assistant de se connecter aux services VW Connect, tandis que l'application mobile Android et les connexions par navigateur restent fonctionnelles.

- L'authentification échoue avec un message d'erreur lors de la tentative de connexion via Home Assistant, bien que les identifiants soient corrects
- L'application mobile Volkswagen Connect et la connexion web à vwid.vwgroup.io continuent de fonctionner normalement
- Le problème affecte spécifiquement l'intégration HomeAssistant-VolkswagenCarnet, indiquant un changement d'API côté Volkswagen
- Les utilisateurs peuvent toujours accéder à VW Connect par d'autres moyens, mais l'automatisation domestique via Home Assistant est bloquée

## Discussion sur Hacker News (136 commentaires)

**Avis positifs** :
- Volkswagen bloque effectivement les intégrations non officielles pour monétiser l'accès aux données et forcer les utilisateurs vers leurs services propriétaires payants (WeConnect), plutôt que par altruisme sécuritaire
- Cette pratique reflète une culture managériale rigide chez les constructeurs allemands : contrôle des données privilégié sur la profitabilité réelle, priorité au pouvoir administratif plutôt qu'à l'innovation
- Le blocage illustre un problème systémique : tous les fabricants automobiles adoptent la même stratégie, créant un oligopole où les utilisateurs n'ont aucune véritable alternative
- L'attestation distante via Google/Apple consolide un écosystème où les Big Tech aident les fabricants à verrouiller les appareils, ce qui risque de violer les lois de la concurrence européennes

**Avis négatifs** :
- La majorité des consommateurs n'achètent pas des voitures pour l'intégration Home Assistant ; ce segment est trop marginal pour justifier une telle mesure ou constituer un vrai conflit
- Contrairement aux suppositions, l'API n'est pas une source de revenus significative : peu de clients paieraient pour un accès API comparé à ce que Tesla réussit à facturer ou à ce que Volvo propose officiellement
- L'UE Data Act (articles 4-5) et la guidance sur les données automobiles devraient légalement contraindre VW à fournir accès aux données ; cette interdiction pourrait être contestée légalement plutôt que de justifier un boycott
- Des alternatives existent (OpenVehicles, sniffer CAN, authentification par navigateur) ; le blocage n'est pas insurmontable et d'autres fabricants (Volvo, Tesla historiquement) ont choisi une approche API ouverte sans effondrement commercial

**Top commentaires** :

- [kuizu](https://news.ycombinator.com/item?id=48321408) : Wasn't the EU Data Act \(https://digital-strategy.ec.europa.eu/en/policies/data-act\) put in place to exactly prevent these kind of scenarios \(Article 4 and 5\)? "where the user cannot directly access the data from the connected product or related service, the data holder must make the readily availab…
- [NiekvdMaas](https://news.ycombinator.com/item?id=48321565) : BYD DMCAd my whole repo to connect to their cars... https://github.com/github/dmca/blob/master/2026/05/2026-05-2... It's a shame these car makers are locking down their cars \(which are brought for a premium!\) and going on a crusade against open source.
- [venzaspa](https://news.ycombinator.com/item?id=48320481) : Quite a few other manufacturers have done the same thing. I use a reverse engineered Polestar library to get charging status but I'm in the middle of building a CANBUS sniffer to do the same job because I don't trust they won't do the same thing as this. I don't really understand it, it doesn't see…

---

[Article original](https://github.com/robinostlund/homeassistant-volkswagencarnet/issues/967) · [Discussion HN](https://news.ycombinator.com/item?id=48319509)
