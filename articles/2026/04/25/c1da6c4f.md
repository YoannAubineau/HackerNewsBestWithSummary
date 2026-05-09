---
article_fetched_at: '2026-04-25T08:17:18.659597Z'
attempts: 0
content_source: extracted
discussion_comment_count: 33
discussion_fetched_at: '2026-04-25T08:17:19.407414Z'
error: null
feed_summary: '<p>Article URL: <a href="https://hhh.hn/rodecaster-duo-fw/">https://hhh.hn/rodecaster-duo-fw/</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=47894747">https://news.ycombinator.com/item?id=47894747</a></p>

  <p>Points: 229</p>

  <p># Comments: 76</p>'
guid: https://news.ycombinator.com/item?id=47894747
hn_item_id: 47894747
hn_url: https://news.ycombinator.com/item?id=47894747
is_ask_or_show_hn: false
llm_input_tokens: 5973
llm_latency_ms: 10000
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 806
our_published_at: '2026-04-25T08:13:30Z'
rewritten_title: 'Interface audio Rodecaster Duo : SSH activé par défaut et firmware
  modifiable'
source_published_at: '2026-04-24T19:30:46Z'
status: summarized
summarized_at: '2026-04-25T08:17:35.582118Z'
title: My audio interface has SSH enabled by default
url: https://hhh.hn/rodecaster-duo-fw/
---

## Résumé de l'article

Un utilisateur a découvert que son interface audio Rodecaster Duo possède SSH activé par défaut avec des clés publiques prédéfinies, et que le firmware peut être modifié sans vérification de signature. L'auteur a pu extraire le firmware, analyser le processus de mise à jour et créer un firmware personnalisé pour accéder à l'appareil en SSH.

- SSH est activé par défaut sur le Rodecaster Duo avec authentification par clé publique uniquement, utilisant deux clés RSA et Ed25519 intégrées au système
- Le processus de mise à jour du firmware est relativement simple : envoi d'une commande HID pour passer en mode mise à jour, puis copie d'une archive gzippée et de sa somme de contrôle MD5 sur le disque exposé
- Le firmware n'a pas de vérification de signature, permettant aux utilisateurs de créer et flasher des versions personnalisées du logiciel
- L'auteur a rapporté le problème de sécurité à RODE mais n'a pas reçu de réponse, et ignore pourquoi SSH était activé par défaut
- Le dual boot du Rodecaster Duo offre une protection contre les briques logicielles en disposant de deux partitions de démarrage alternatives

## Discussion sur Hacker News (33 commentaires analysés)

**Avis positifs** :
- L'approche ouverte de Rode (firmware en tarball simple, pas de signature) est louée comme exemplaire et incite à l'achat, contrairement aux pratiques restrictives habituelles des fabricants.
- La découverte démontre que les appareils audio modernes sont des ordinateurs Linux complets, ce qui ouvre des possibilités légitimes de modification et personnalisation (résolution d'echo en gaming, mixage avancé, etc.).
- Le firmware de Rode est relativement propre et bien conçu comparé à d'autres appareils grand public, facilitant les corrections et modifications par l'utilisateur.
- L'utilisation d'IA (Claude) pour accélérer l'analyse de firmware est présentée comme un progrès positif qui démocratise l'accès à ce type de modification technique.

**Avis négatifs** :
- SSH activé par défaut sur le LAN (pas seulement l'USB) pose un réel risque de sécurité, même si le problème est facilement corrigeable.
- La Cyber Resilience Act (CRA) européenne risque de forcer les fabricants comme Rode à verrouiller complètement leurs appareils, fermant définitivement ces portes d'accès et de réparation.
- La découverte n'est pas techniquement impressionnante (nmap -p 22 aurait suffi) et ne mérite pas vraiment d'être qualifiée de "hacking" complexe.
- L'enthousiasme autour de cette ouverture doit être tempéré par des préoccupations réglementaires : les fabricants internationaux pourraient préférer fermer l'accès plutôt que de naviguer les obligations de conformité.

**Top commentaires** :

- [rikafurude21](https://news.ycombinator.com/item?id=47895644) : Its still crazy to me that everyone has a pocket AI-hacker ready to inspect firmware and modify their devices now. You just put the agent on it and it gives you access in minutes. You would have to be a Hotz tier hacker if you wanted to do anything close to this only last year, or at the very least…
- [yonatan8070](https://news.ycombinator.com/item?id=47895199) : Having the firmware image just be a boring old tarball + hash sounds super nice. I wish more devices were this open, and I hope Rode won't see this and decide to lock the firmware upgrades down.
- [ZihangZ](https://news.ycombinator.com/item?id=47898729) : Yeah, this is pretty common once a device has any real DSP in it. There's usually some stripped-down Linux on an ARM SoC underneath, and the vendor BSP just happens to ship with sshd on. Not necessarily malice, more like nobody on the audio side really owns the rootfs. The big question is whether i…

---

[Article original](https://hhh.hn/rodecaster-duo-fw/) · [Discussion HN](https://news.ycombinator.com/item?id=47894747)
