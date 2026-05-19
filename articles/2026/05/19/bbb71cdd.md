---
article_fetched_at: '2026-05-19T16:58:44.342494Z'
attempts: 0
content_source: extracted
discussion_comment_count: 158
discussion_fetched_at: '2026-05-19T16:58:42.579558Z'
error: null
guid: https://news.ycombinator.com/item?id=48192882
hn_item_id: 48192882
hn_url: https://news.ycombinator.com/item?id=48192882
is_ask_or_show_hn: false
llm_input_tokens: 15917
llm_latency_ms: 11350
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 970
our_published_at: '2026-05-19T16:56:13Z'
rewritten_title: OpenBSD 7.9 publie nouvelles fonctionnalités système et améliorations
  de sécurité
source_published_at: '2026-05-19T13:11:51Z'
status: summarized
summarized_at: '2026-05-19T17:00:12.809445Z'
title: OpenBSD 7.9
url: https://www.openbsd.org/79.html
---

## Résumé de l'article

OpenBSD 7.9 est une nouvelle version du système d'exploitation libre basé sur Unix. Elle introduit des améliorations de sécurité, des mises à jour cryptographiques, des raffinements d'outils système et des optimisations de performance.

- Sécurité renforcée : support de MLKEM768_X25519 pour la cryptographie post-quantique en TLS, corrections de vulnérabilités NULL dereference, et amélioration des mécanismes de limitation de déni de service (DDoS).
- Outils système : nouvelles options pour xargs, tmux, traceroute, pfctl et xterm ; meilleure gestion des limites disque et des systèmes de fichiers temporaires.
- LibreSSL et cryptographie : révisions d'ASN.1, amélioration des structures EC_POINT, dépréciation de comportements hérités incompatibles, et ajout de benchmarks ML-KEM.
- OpenSSH : nouvelles commandes de multiplexage pour afficher les informaux des canaux ouverts et pénalités configurables pour les tentatives de connexion avec noms d'utilisateur invalides.
- Installation multi-plateforme : versions d'installation pour 17 architectures matérielles différentes (amd64, i386, arm64, armv7, riscv64, sparc64, etc.) avec supports USB, CD, réseau et médias spécifiques.

## Discussion sur Hacker News (158 commentaires)

**Avis positifs** :
- OpenBSD maintient une excellente réputation de sécurité avec des années d'audit de code, exemplifiée par sa politique des zéro trous de sécurité dans l'installation par défaut
- Le projet est remarquablement cohérent : système de base bien intégré, excellente documentation (man pages), et code lisible et bien structuré qui reste compréhensible pour les utilisateurs
- Idéal pour des cas d'usage spécifiques : firewalls/passerelles réseau (PF supérieur à iptables), serveurs sécurisés, et matériel ancien ou obscur que Linux ne supporte pas bien
- Excellente expérience utilisateur pour les administrateurs : installations simples, mises à jour régulières sans complications, et interface de configuration intuitive comparée à Linux
- Nombreuses innovations logicielles maintenues par le projet : OpenSSH, LibreSSL, OpenNTPD, tmux, PF qui bénéficient à l'écosystème plus large

**Avis négatifs** :
- Limitations matérielles significatives : absence de support Bluetooth, support WiFi historiquement médiocre (bien qu'amélioré récemment), et problèmes de batterie/chaleur sur portables
- Partitionnement du disque rigide et inflexible : croissance des besoins en espace de stockage entre versions crée des problèmes récurrents nécessitant repartitionnage manuel du système
- Performance sacrifiée au nom de la sécurité (5-15% de ralentissement) et certaines décisions limitent les fonctionnalités (pas de système de fichiers journalisé, pas de ZFS natif)
- Écosystème logiciel moins complet que Linux/FreeBSD : moins de drivers, certains ports abandonnés par upstream, et dépendance à des packages supplémentaires pour des fonctionnalités attendues (DDNS)
- Courbe d'apprentissage et niche étroite : convient principalement aux serveurs/firewalls sécurisés mais moins approprié pour les usages desktop/portable généralistes

**Top commentaires** :

- [upofadown](https://news.ycombinator.com/item?id=48195932) : The big news for some of us is that Exim has been dropped from ports. Here is a good article about transitioning from Exim to OpenSMTPD: https://nxdomain.no/~peter/time\_for\_opensmtpd.html I tried using OpenSMTPD a long time ago, shortly after it came out, but things were not stable enough. I guess…
- [brynet](https://news.ycombinator.com/item?id=48194457) : OpenBSD 7.9 release artwork by Lyra Henderson https://www.openbsd.org/images/PinkPuffy.png https://www.openbsd.org/images/puffy79.gif Release song is "Diamond in the Rough" - Composed & produced by Bob Kitella. https://www.openbsd.org/lyrics.html\#79 Apparel \(t-shirts, so far\): https://openbsdstore.…
- [fmajid](https://news.ycombinator.com/item?id=48195890) : They've made major progress on the WiFi front in this release, finally getting experimental WiFi 6 support.

---

[Article original](https://www.openbsd.org/79.html) · [Discussion HN](https://news.ycombinator.com/item?id=48192882)
