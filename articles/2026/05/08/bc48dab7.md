---
article_fetched_at: '2026-05-08T20:21:15.605244Z'
attempts: 0
content_source: extracted
discussion_comment_count: 102
discussion_fetched_at: '2026-05-08T20:21:14.795673Z'
error: null
feed_summary: '<p>Article URL: <a href="https://aniket.foo/posts/20260505-netboot/">https://aniket.foo/posts/20260505-netboot/</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=48045012">https://news.ycombinator.com/item?id=48045012</a></p>

  <p>Points: 203</p>

  <p># Comments: 102</p>'
guid: https://news.ycombinator.com/item?id=48045012
hn_item_id: 48045012
hn_url: https://news.ycombinator.com/item?id=48045012
is_ask_or_show_hn: false
llm_input_tokens: 13574
llm_latency_ms: 10790
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 819
our_published_at: '2026-05-08T19:51:01Z'
rewritten_title: Configuration complète du démarrage réseau sans disque avec ZFS,
  iSCSI et PXE
source_published_at: '2026-05-07T03:13:24Z'
status: summarized
summarized_at: '2026-05-08T20:21:49.943602Z'
title: Diskless Linux boot using ZFS, iSCSI and PXE
url: https://aniket.foo/posts/20260505-netboot/
---

## Résumé de l'article

Un guide pratique pour configurer un système Linux Debian qui démarre entièrement depuis le réseau via iSCSI, en utilisant un volume ZFS distant comme disque système. Cette approche permet de conserver intact un système Windows local tout en disposant d'un environnement Linux dédié aux modèles d'IA sans affecter les partitions existantes.

- Installation et compilation de Netboot.xyz sur un serveur Proxmox pour servir l'interface de démarrage PXE/iPXE, avec création de menus personnalisés pour les cibles iSCSI
- Configuration du TFTP et DNSMasq sur le routeur pour rediriger les clients PXE vers les binaires Netboot.xyz compilés (support BIOS, UEFI et iPXE)
- Création d'un volume ZFS (ZVOL) de 32 Go et exposition en tant que cible iSCSI avec authentification mutuelle via targetcli-fb
- Installation de Debian 13 via l'installateur netboot en détectant et configurant le disque iSCSI distant, avec saisie manuelle des identifiants iSCSI en TTY 2
- Démarrage complet du système depuis le disque SAN distant après installation, sans modification du GRUB ou des partitions locales Windows

## Discussion sur Hacker News (102 commentaires)

**Avis positifs** :
- ZFS en backend permet de gérer l'OS sans support ZFS dans l'OS lui-même, offrant flexibilité et contrôle accru
- iSCSI présente des avantages sur NFS pour les environnements multi-machines (bloc vs fichier, chiffrement disque natif, gestion de volumes)
- Cette approche a fait ses preuves en production (clusters robotiques, postes de travail sans disque en entreprise avec Ubuntu LTSP) avec gains majeurs de maintenance et déploiement
- PXE avec boot de kernel/initramfs en RAM fonctionne bien sans disque local, permettant des configurations discless robustes
- Performance viable avec réseau 10Gbps moderne, bien supérieure aux alternatives SD card ou anciennes connexions gigabit

**Avis négatifs** :
- iSCSI très sensible à la congestion réseau et aux pertes de paquets; NBD offre meilleure résilience aux interruptions réseau selon les utilisateurs
- Performance réseau reste 4-8x plus lente qu'un NVMe local, limitant l'attrait pour workloads exigeantes malgré 10GbE
- Configuration initiale complexe (ansible, targetcli, tftp, dhcp) par rapport à alternatives plus simples comme 9front; courbe apprentissage importante
- NFS diskless plus commun, plus facile à mettre en place; certains gestionnaires de paquets (Redhat, Arch) ont des problèmes avec root-on-NFS
- Nécessite infrastructure réseau dédiée et dimensionnement spécifique (switches avec buffering, VLANs prioritaires) pour performances acceptables en production

**Top commentaires** :

- [cwillu](https://news.ycombinator.com/item?id=48047183) : Friends don't let friends use grub. rEFInd is \_so\_ much simpler: one efi entry, one text config file in the efi partition, nothing that needs to change when the kernel updates, and no massive pile of templating and moving parts to mysteriously break dumping you at an impenetrable grub “rescue” shel…
- [deathanatos](https://news.ycombinator.com/item?id=48045924) : « UEFI fixes that to some extent, but it’s a pain to maintain the UEFI entries manually and change them every time the kernel updates. » … you don't have to update the UEFI entries every time the kernel updates. \(I guess you might if you do like a kernel w/ CONFIG\_EFI\_STUB, and you place the new ke…
- [stereo-highway](https://news.ycombinator.com/item?id=48050426) : This post generated more attention than I expected. I wanted to share something that i got working at home on consumer hardware and with software that I’m slightly more familiar with. This is by no means the only way to implement this, an I’m sure there are better ways. Thank you for the feedback,…

---

[Article original](https://aniket.foo/posts/20260505-netboot/) · [Discussion HN](https://news.ycombinator.com/item?id=48045012)
