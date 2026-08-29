---
article_fetched_at: '2026-08-29T23:44:44.446006Z'
attempts: 0
content_source: extracted
discussion_comment_count: 103
discussion_fetched_at: '2026-08-29T23:44:41.046622Z'
error: null
guid: https://news.ycombinator.com/item?id=49490702
hn_item_id: 49490702
hn_url: https://news.ycombinator.com/item?id=49490702
image_url: https://cdn.bsky.app/img/avatar_thumbnail/plain/did:plc:kym5w7pcv4v7xbz7lvbj24na/bafkreickcnmrwdtb3mwqzz7v7s2xgmczwzrdwp3ucvadpeuorzbsgvunjm
is_ask_or_show_hn: false
llm_input_tokens: 10019
llm_latency_ms: 9613
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 853
our_published_at: '2026-08-29T23:24:35Z'
rewritten_title: GrapheneOS annonce l'absence de support ARM MTE sur Pixel 11 après
  une semaine de portage
source_published_at: '2026-08-29T15:26:28Z'
status: summarized
summarized_at: '2026-08-29T23:45:01.358051Z'
title: 'GrapheneOS project: pixel 11 no longer supports hardware memory tagging (MTE)'
url: https://bsky.app/profile/grapheneos.org/post/3mua32q4ds22e
---

## Résumé de l'article

GrapheneOS, un système d'exploitation Android orienté sécurité, a commencé le portage sur la série Pixel 11 mais n'a pu le finaliser. Le projet GrapheneOS affirme que Google a supprimé le support matériel du Memory Tagging Extension (MTE) ARM, une fonctionnalité de sécurité, possiblement pour des raisons économiques.

- GrapheneOS a réalisé un portage partiel en une semaine mais ne peut le compléter faute de support MTE dans le logiciel, le firmware et vraisemblablement le matériel
- Le Memory Tagging Extension est une fonctionnalité de sécurité ARM importante pour la protection de la mémoire
- L'équipe impute l'absence de cette fonctionnalité à une décision de Google de réduire les coûts de production
- Le problème affecte l'ensemble de la série Pixel 11

## Discussion sur Hacker News (103 commentaires)

**Avis positifs** :
- MTE est une technologie de sécurité prometteuse et validée en production par Apple, qui rend sa suppression particulièrement regrettable alors que le besoin de sécurité augmente
- GrapheneOS a démontré un usage productif de MTE pour le noyau et la majorité des processus utilisateur, corrigeant de nombreux bugs découverts, contrairement à l'utilisation limitée de Google
- La décision de Google est incompréhensible car MTE a un impact de performance négligeable en mode asymétrique et aucun coût significatif en mode asynchrone pour la majorité du système
- L'approche de GrapheneOS force l'activation de MTE par défaut pour les allocateurs standards et génère des notifications utilisateur pour les accès mémoire invalides, permettant un retour aux développeurs
- Les partenariats Motorola offrent une alternative prometteuse avec une meilleure architecture matérielle (CPU/GPU) tout en préservant MTE et les exigences de sécurité

**Avis négatifs** :
- Google a probablement supprimé MTE pour réduire les coûts de fabrication (espace die du processeur) sur une fonctionnalité qu'ils n'ont jamais déployée par défaut, ce qui relève de décisions commerciales légitimes
- Même Apple, malgré une bonne intégration de MTE, a échoué à obtenir l'adoption dans l'écosystème applicatif iOS, ce qui limite l'impact réel de la fonctionnalité
- Le partenariat Motorola reste incertain quant aux délais de lancement, à la disponibilité mondiale et à la capacité à servir le marché abordable des séries A actuellement accessibles
- GrapheneOS ne peut pas forcer un OEM à inclure une fonctionnalité matérielle contre ses intérêts économiques, et les appareils Pixel 8-10 restent supportés avec MTE pour plusieurs années
- Les préoccupations géopolitiques concernant Motorola (entreprise chinoise) pourraient limiter les options futures si des restrictions gouvernementales surviennent

**Top commentaires** :

- [Pfhortune](https://news.ycombinator.com/item?id=49491920) : Feeling like my Pixel 9 Pro was the best timed hardware buy I've made in recent years. The 10 dropped the physical SIM slot and Google started with their device tree shenanigans that year, with little to no improvements in exchange. I've got 16GB of RAM and 512GB in an ecosystem that shows every si…
- [newsomix9xl](https://news.ycombinator.com/item?id=49491265) : "Pixel 11 series is a lot more expensive for an incremental improvement to the CPU, the same underpowered GPU and reduced RAM for the Pro base models. They finally caught up to the last generation of Qualcomm cellular radio. It's overpriced, the upgrades aren't impressive and losing MTE is appallin…
- [perarneng](https://news.ycombinator.com/item?id=49490829) : What, MTE is such a promising tech and for security and now that we need all security we can get. WTF this is terrible development. You cant go backwards when the world needs getting even more secure.

---

[Article original](https://bsky.app/profile/grapheneos.org/post/3mua32q4ds22e) · [Discussion HN](https://news.ycombinator.com/item?id=49490702)
