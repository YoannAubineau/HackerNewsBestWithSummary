---
article_fetched_at: '2026-08-02T01:56:42.478784Z'
attempts: 0
content_source: extracted
discussion_comment_count: 93
discussion_fetched_at: '2026-08-02T01:56:40.971131Z'
error: null
guid: https://news.ycombinator.com/item?id=49136736
hn_item_id: 49136736
hn_url: https://news.ycombinator.com/item?id=49136736
is_ask_or_show_hn: false
llm_input_tokens: 8652
llm_latency_ms: 10793
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 985
our_published_at: '2026-08-02T01:02:39Z'
rewritten_title: NetBSD 11.0 est disponible avec des problèmes de sécurité connus
source_published_at: '2026-08-01T17:56:41Z'
status: summarized
summarized_at: '2026-08-02T01:57:39.168926Z'
title: NetBSD 11.0
url: https://blog.netbsd.org/tnf/entry/netbsd_11_0_released
---

## Résumé de l'article

NetBSD 11.0 a été publié le 1er août 2026 après un délai significatif. Le système d'exploitation libre et gratuit pour divers processeurs (x86, ARM, SPARC, etc.) est maintenant disponible en téléchargement avec des instructions d'installation spécifiques par architecture.

- Les images d'installation sont disponibles en formats CD-ROM (< 700 Mo), DVD complet ou fichiers .img pour clés USB, à décompresser avant utilisation
- Le projet reconnaît publiquement la présence de problèmes de sécurité non corrigés à la publication, attribués à l'augmentation des découvertes de vulnérabilités liées aux outils d'IA
- Les correctifs de sécurité en attente seront intégrés dans la branche stable et inclus dans la version 11.1, prévue dans les deux mois
- Le délai de publication a été allongé pour synchroniser les mises à jour des composants tiers et permettre les tests via des candidats de version

## Discussion sur Hacker News (93 commentaires)

**Avis positifs** :
- NetBSD excelle dans la portabilité extrême : elle supporte une gamme impressionnante d'architectures (VAX, PDP-11, 486, RISC-V, etc.) que Linux abandonne progressivement, la positionnant comme le choix naturel pour le matériel vintage et les systèmes exotiques.
- L'écosystème pkgsrc offre une gestion de paquets de qualité avec support multiplateforme (macOS, Linux, BSD), rootless, et à jour comparé à Arch ou Gentoo, avec mécanismes intégrés de sécurité et audit de vulnérabilités.
- NetBSD offre une expérience système cohérente et compréhensible : configurations et emplacements prévisibles, documentation solide, base système intégrée plutôt que collection de projets disparates, ce qui la rend plus facile à maîtriser et customiser que Linux.
- La sortie 11.0 apporte des améliorations notables : micropoyau x86 avec démarrage en 10ms, améliorations du firewall npf, support RISC-V, et Bluetooth depuis 20 ans, montrant une évolution continue malgré la taille réduite de la communauté.

**Avis négatifs** :
- Le compilateur GCC reste figé à la version 12.5.0 (juillet 2025) alors que la version 16.1 existe, freinant les optimisations modernes ; justifié par les défis de portabilité multi-architecture et la charge de travail de stabilisation, mais représente une limite pratique.
- L'adoption comme système de bureau reste marginale comparée à Linux : support matériel plus limité, logiciels incompatibles exigeant des correctifs (udev, glibc-isms), et nécessité de compromis importants (montages FUSE, accès root accru) qui rendent l'expérience utilisateur moins fluide.
- Les systèmes de fichiers non-journalisés (UFS) posent des risques réels d'intégrité en cas d'arrêt inattendu, avec fsck longues et fastidieuses, bien que les utilisateurs rapportent rarement de pertes catastrophales en pratique.
- La base utilisateur très réduite soulève des doutes sur la découverte de vulnérabilités zero-day : les exploits BSD sont prestigieux mais rares précisément parce que personne ne les cherche vraiment, contrairement à Linux où l'attaque surface massive et la valeur commerciale garantissent un audit constant.

**Top commentaires** :

- [haberman](https://news.ycombinator.com/item?id=49138032) : I often wonder what the current status is of the BSDs \(FreeBSD, OpenBSD, NetBSD\). Who uses them, who works on them, what is their motivation for doing so? How do they compare to Linux these days, in terms of size, feature set, security hardening, etc? Is their usage/development happening at a relat…
- [Panino](https://news.ycombinator.com/item?id=49138365) : From the linked release announcement: \> Improvements to the npf\(7\) firewall, including layer 2 and user/group filtering That's a valuable, useful feature \> New MICROVM kernel for x86... it can boot in about 10 ms That could open some doors, nice There are some good hardware improvements too.
- [jbs789](https://news.ycombinator.com/item?id=49137199) : As someone reading this fresh, they are almost apologetic for a release with open issues. But presumably the release closes off many more than it creates. I could see any other author/org approaching the messaging very differently!

---

[Article original](https://blog.netbsd.org/tnf/entry/netbsd_11_0_released) · [Discussion HN](https://news.ycombinator.com/item?id=49136736)
