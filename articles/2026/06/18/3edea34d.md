---
article_fetched_at: '2026-06-18T17:01:37.420757Z'
attempts: 0
content_source: extracted
discussion_comment_count: 171
discussion_fetched_at: '2026-06-18T17:01:36.647405Z'
error: null
guid: https://news.ycombinator.com/item?id=48582320
hn_item_id: 48582320
hn_url: https://news.ycombinator.com/item?id=48582320
image_url: https://cdn.mos.cms.futurecdn.net/UdLqeSxzsPucb6GRFDjLm6-1600-80.jpg
is_ask_or_show_hn: false
llm_input_tokens: 15623
llm_latency_ms: 12248
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1026
our_published_at: '2026-06-18T16:32:06Z'
rewritten_title: AMD désactive silencieusement le chiffrement mémoire sur les processeurs
  Ryzen grand public
source_published_at: '2026-06-18T08:08:00Z'
status: summarized
summarized_at: '2026-06-18T17:02:15.202547Z'
title: AMD silently removes memory encryption from consumer Ryzen CPUs
url: https://www.tomshardware.com/pc-components/cpus/amd-silently-removes-memory-encryption-from-consumer-ryzen-cpus-leaving-users-unaware-that-they-may-be-vulnerable-security-feature-vanishes-after-newer-agesa-firmware-amd-engineers-go-radio-silent-when-pressed-about-the-change
---

## Résumé de l'article

AMD a retiré la fonctionnalité Transparent Secure Memory Encryption (TSME) des processeurs Ryzen grand public, la limitant désormais aux puces Pro. TSME est une protection matérielle qui chiffre les données en RAM pour défendre contre les attaques physiques ; elle fonctionnait auparavant sur les processeurs consumer mais a disparu après la mise à jour firmware AGESA 1.2.7.0, sans annonce publique d'AMD.

- Un utilisateur Linux a découvert que TSME était soudainement « non supporté » sur son Ryzen 7 9700X après une mise à jour firmware, bien que le matériel reste techniquement capable d'exécuter la fonction
- Une enquête menée avec des ingénieurs d'AMD, du fabricant de carte mère MSI et d'autres révèle que le drapeau interne contrôlant TSME passe à FALSE sur les puces consumer mais reste TRUE sur les Pro
- AMD n'a fourni aucune explication officielle et a coupé court aux discussions GitHub, laissant incertain si c'est une décision délibérée de segmentation des produits ou une régression accidentelle
- La disparition est indétectable sur Windows et requiert des efforts techniques importants sur Linux, les utilisateurs restant donc ignorants du changement
- AMD avait antérieurement confirmé par ses propres ingénieurs que TSME fonctionnait sur les CPU Ryzen consumer, ce qui rend le retrait silencieux particulièrement problématique

## Discussion sur Hacker News (171 commentaires)

**Avis positifs** :
- Le chiffrement de la mémoire n'a jamais été commercialisé ou documenté par AMD comme une fonctionnalité consommateur, c'est donc une correction logique d'une fonctionnalité accidentellement présente
- Cette fonctionnalité était instable sur plusieurs plates-formes (gels lors de l'initialisation des pilotes GPU, problèmes VFIO) et n'a probablement jamais bien fonctionné
- Le nombre réel d'utilisateurs consommateurs dépendant de cette fonctionnalité est extrêmement faible, et les menaces physiques comme les attaques par refroidissement cryogénique sont très sophistiquées
- Les CPUs PRO d'AMD conservent la fonctionnalité pour les entreprises qui en ont réellement besoin, ce qui est une segmentation de marché légitime
- AMD a historiquement adopté une approche de ne pas éteindre les fonctionnalités d'entreprise sur les SKUs consommateur, il est donc plausible que cette suppression indique un problème systémique plus grave

**Avis négatifs** :
- AMD a supprimé silencieusement une fonctionnalité existante sans communication, ce qui est inacceptable quel que soit le statut de commercialisation - c'est de l'enshittification post-vente
- Retirer des fonctionnalités via mise à jour micrologicielle ouvre la porte à des dégradations futures des produits; les clients ne devraient pas perdre des capacités physiques après achat
- Le silence total d'AMD sur les raisons de la suppression nourit la spéculation inquiétante (intervention gouvernementale, problèmes de sécurité cachés) et aurait pu être stoppé par une transparence simple
- Cette décision affecte les petites entreprises utilisant des CPUs consommateur en serveurs et les utilisateurs qui dépendaient du chiffrement pour la défense en profondeur contre les attaques par rowhammer et extraction de clés
- AMD trahit sa réputation historique d'éviter la segmentation de marché abusive et manque de transparence ; Intel propose même cette fonctionnalité sur ses modèles équivalents

**Top commentaires** :

- [thg](https://news.ycombinator.com/item?id=48582778) : This was never marketed as a feature of the consumer CPUs and if some malignant actor does get physical access to my \(consumer\) hardware, then them being able to read out bytes through cryo-freezing the RAM really isn't high up on the list of things I'm going to worry about.
- [Integer](https://news.ycombinator.com/item?id=48583091) : I had this enabled as it protects against RAMbleed/ECC errors, so it's not limited to physical attacks.
- [nickjj](https://news.ycombinator.com/item?id=48583701) : I don't know how this works but does this mean if someone gained physical access to your locked running computer, they could gain access to your full encrypted drive and anything saved on disk? My reasoning there is if you used an encrypted drive, the decryption key you type when booting up would b…

---

[Article original](https://www.tomshardware.com/pc-components/cpus/amd-silently-removes-memory-encryption-from-consumer-ryzen-cpus-leaving-users-unaware-that-they-may-be-vulnerable-security-feature-vanishes-after-newer-agesa-firmware-amd-engineers-go-radio-silent-when-pressed-about-the-change) · [Discussion HN](https://news.ycombinator.com/item?id=48582320)
