---
article_fetched_at: '2026-10-06T01:09:07.598981Z'
attempts: 0
content_source: extracted
discussion_comment_count: 250
discussion_fetched_at: '2026-10-06T01:08:51.796467Z'
error: null
guid: https://news.ycombinator.com/item?id=49964303
hn_item_id: 49964303
hn_url: https://news.ycombinator.com/item?id=49964303
image_url: https://discuss.grapheneos.org/opengraph.png
is_ask_or_show_hn: false
llm_input_tokens: 23076
llm_latency_ms: 12562
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 985
our_published_at: '2026-10-06T01:04:46Z'
rewritten_title: GrapheneOS signale l'absence de support ARM MTE sur le Pixel 11 et
  envisage de ne pas le supporter
source_published_at: '2026-10-05T13:02:25Z'
status: summarized
summarized_at: '2026-10-06T01:14:31.337586Z'
title: Pixel 11 doesn't yet meet the GrapheneOS security standards and may be skipped
url: https://discuss.grapheneos.org/d/41564-pixel-11-doesnt-yet-meet-the-grapheneos-security-standards-and-may-be-skipped
---

## Résumé de l'article

GrapheneOS, système d'exploitation Android durcisé axé sur la sécurité, a achevé un portage partiel du Pixel 11 mais ne peut le finaliser faute de prise en charge du marquage de la mémoire matérielle ARM (MTE), une fonctionnalité de sécurité critique.

- Google aurait volontairement supprimé le support MTE sur le Pixel 11 pour réduire les coûts, contrairement aux appareils Pixel 8, 9 et 10 qui en disposent
- GrapheneOS utilise MTE dans l'ensemble du système d'exploitation pour améliorer considérablement la protection contre les exploits à distance et locaux, tandis qu'Apple intègre une fonctionnalité équivalente (Memory Integrity Enforcement) sur tous les iPhone 17
- Le Pixel 11 présente des améliorations de sécurité mineures comme le démarrage vérifié post-quantique et Titan M3, mais leur bénéfice est annulé par l'absence de MTE en fonctionnement normal
- GrapheneOS recommande fortement d'éviter l'achat de Pixel 11 et privilégie les modèles Pixel 8, 9, 10 ou les futurs appareils Motorola bénéficiant de MTE
- L'équipe considère de ne pas supporter la série Pixel 11 et de concentrer ses efforts sur le partenariat avec Motorola pour l'accès au firmware et aux pilotes en source ouverte

## Discussion sur Hacker News (250 commentaires)

**Avis positifs** :
- GrapheneOS a raison de maintenir des standards de sécurité stricts : MTE est une fonctionnalité importante de durcissement mémoire utilisée par Apple (MIE) et Samsung, et son absence affaiblit réellement la posture de sécurité.
- Le partenariat avec Motorola change la donne : GrapheneOS ne sera plus dépendant de Google et pourra enfin proposer une alternative viable aux Pixel, offrant aux utilisateurs un vrai choix.
- La communication de GrapheneOS est honnête et transparente : ils expliquent clairement les problèmes techniques au lieu de contourner les exigences de sécurité pour des raisons commerciales.
- Le comportement de Google ressemble à des pratiques anticoncurrentielles : empêcher les OEMs de vendre des appareils avec GrapheneOS préinstallé rappelle les tactiques de Microsoft des années 1990-2000.

**Avis négatifs** :
- Les rumeurs sur les raisons du retrait de MTE (économies, timeline) sont spéculatives : sans preuves, accuser Google de mauvaise foi dans sa communication professionnelle semble contre-productif.
- MTE n'a jamais été utilisé par Android au départ, donc son absence n'affecte pas l'expérience utilisateur Android pour le Pixel 11 ; la majorité des utilisateurs ne remarqueront rien.
- Les critiques sur l'anti-compétitivité de Google sont exagérées comparées à Apple : Apple ne permet même pas d'alternatives sur ses appareils, tandis que Google reste plus ouvert globalement à d'autres OS.
- GrapheneOS est un projet de niche avec des exigences matérielles strictes qui limitent intrinsèquement ses options d'appareils ; cela n'est pas uniquement la faute de Google.
- Le Pixel 11 a des compromis mais reste fonctionnel : pour la plupart des utilisateurs, attendre une mise à jour future (décembre 2026 rumeur) ou choisir un ancien modèle est une solution acceptable.

**Top commentaires** :

- [microtonal](https://news.ycombinator.com/item?id=49964791) : As others have said, this is not the most recent status update \(it depends on future Google changes in QPR1 or QPR2\). The much more interesting recent news IMO is that Google is not allowing \(non-Samsung\) OEMs to sell devices with GrapheneOS: https://news.ycombinator.com/item?id=49946698 See the la…
- [aftbit](https://news.ycombinator.com/item?id=49964734) : The Pixel 11 is the first Pixel phone to be released after the RAMpocolypse. It has made a lot of compromises in the name of lowering cost. I am definitely going to skip that generation. I tend to upgrade every 3 years, but there really isn't a big driver to do so right now. My Pixel 8 is holding u…
- [rickdeckard](https://news.ycombinator.com/item?id=49964683) : Quite a bad signal-to-noise ratio in this link. It's an emotional discussion about Google not supporting MTE on Pixel 11 \(old news of August, GrapheneOS had to roll back that statement in September \[0\]\). Now the question is whether MTE will be enabled by Google as part of a future OS-upgrade, to wh…

---

[Article original](https://discuss.grapheneos.org/d/41564-pixel-11-doesnt-yet-meet-the-grapheneos-security-standards-and-may-be-skipped) · [Discussion HN](https://news.ycombinator.com/item?id=49964303)
