---
article_fetched_at: '2026-09-13T12:58:40.252602Z'
attempts: 0
content_source: extracted
discussion_comment_count: 88
discussion_fetched_at: '2026-09-13T12:58:38.682415Z'
error: null
guid: https://news.ycombinator.com/item?id=49681152
hn_item_id: 49681152
hn_url: https://news.ycombinator.com/item?id=49681152
image_url: https://jetkvm.com/blog/jetkvm-mini/og-v2.jpg
is_ask_or_show_hn: false
llm_input_tokens: 7482
llm_latency_ms: 11154
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 948
our_published_at: '2026-09-13T12:23:48Z'
rewritten_title: JetKVM Mini, contrôleur KVM compact à partir de 33 dollars avec versions
  filaire et sans fil
source_published_at: '2026-09-13T07:49:46Z'
status: summarized
summarized_at: '2026-09-13T12:59:19.479629Z'
title: JetKVM Mini
url: https://jetkvm.com/blog/introducing-jetkvm-mini
---

## Résumé de l'article

JetKVM Mini est une version plus petite et abordable du contrôleur KVM JetKVM, disponible en modèle filaire (39 $) et sans fil (42 $), réduisant à 33 $ et 36 $ en packs de trois. Réenginérisé autour d'un microcontrôleur ESP32-P4X avec encodeur H.264 matériel, il offre la capture vidéo 1080p native (jusqu'à 4K avec JetKVM OS Services), le contrôle clavier/souris et l'interface web standard, dans un boîtier aluminium de la taille d'une boîte d'allumettes.

- Le modèle filaire propose un port Ethernet RJ45 pour connexion directe ; le modèle W ajoute le Wi-Fi 2.4/5 GHz avec Bluetooth pour configuration et IEEE 802.15.4 pour Zigbee/Thread
- Deux ports USB : le premier vers l'ordinateur cible (USB 2.0 High Speed, alimentation incluse, avec support des médias virtuels via carte TF) ; le second à usage général (USB 2.0 Full Speed, extensible en hôte USB avec alimentation externe)
- Firmware réécrit et open source dès le départ, compatible avec l'interface web, le cloud, les extensions et les mises à jour OTA existantes de JetKVM
- Supporte les mêmes fonctionnalités : montage de médias virtuels, accès JetKVM Cloud, Wake-on-LAN, MQTT, Home Assistant, OIDC, et prise d'empreinte de clé publique pour verrouillage de démarrage sécurisé (secure boot)
- Disponibilité prévue le 26 octobre 2026 chez les revendeurs autorisés

## Discussion sur Hacker News (88 commentaires)

**Avis positifs** :
- L'ESP32-P4 avec 32 MB de RAM est impressionnant pour gérer la capture et compression vidéo, ce qui était auparavant le principal défi des solutions KVM
- Le nouveau design mini améliore l'ergonomie et la praticité pour les installations en rack ou empilées, contrairement à la forme originale
- Les utilisateurs rapportent une grande utilité pratique : accès FDE sans janky workarounds, reboot serveur sécurisé, économies de temps significatives malgré un usage mensuel
- Le matériel est apprécié pour sa fiabilité (certains en service depuis la campagne Kickstarter sans problème), son open-source et son absence de dépendance aux services cloud propriétaires

**Avis négatifs** :
- Prix considéré comme élevé pour le marché ; des alternatives chinoises coûtent moins de $20, soulevant des questions sur la justification du coût
- Problèmes de fiabilité récurrents rapportés : pannes matérielles, problèmes de connexion réseau, défaillances de clavier après quelques mois d'utilisation sur plusieurs unités
- Limitations technologiques : pas de support 4K haute fréquence contrairement aux KVM haut de gamme type ATEN, charge vidéo limitée par rapport aux besoins gaming ou haute résolution
- Problèmes pratiques : connecteurs USB-C finicky et câbles manquants dans la boîte, confusion marketing autour de l'acronyme KVM non expliqué sur le site, délais Kickstarter historiques

**Top commentaires** :

- [mszcz](https://news.ycombinator.com/item?id=49682959) : I have 4 of the old ones in service and they're great. Whenever I need to remotely reboot a server those come in handy just great, no more fear of what I'm going to do if the server doesn't come back online. It also solved the issue I had with entering a password on FDE \(full disk encryption\) syste…
- [Shank](https://news.ycombinator.com/item?id=49681339) : I own 3 JetKVMs, of which two of them stopped working, one of which doesn't boot at all and the other that never connects to network. The third I took out of service because the keyboard wouldn't send input when it was connected for more than a couple months. I'm sure the newer hardware is better,…
- [theanonymousone](https://news.ycombinator.com/item?id=49681355) : It may be worth noting that this is not \_that\_ KVM, but this one: https://en.wikipedia.org/wiki/KVM\_switch I learnt this first myself from HN, a few months ago.

---

[Article original](https://jetkvm.com/blog/introducing-jetkvm-mini) · [Discussion HN](https://news.ycombinator.com/item?id=49681152)
