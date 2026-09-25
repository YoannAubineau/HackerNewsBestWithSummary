---
article_fetched_at: '2026-09-25T17:38:58.745078Z'
attempts: 0
content_source: extracted
discussion_comment_count: 118
discussion_fetched_at: '2026-09-25T17:38:54.435397Z'
error: null
guid: https://news.ycombinator.com/item?id=49828969
hn_item_id: 49828969
hn_url: https://news.ycombinator.com/item?id=49828969
image_url: https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/05/run-adblocker-on-esp32-s3.JPG?w=1600&h=900&fit=crop
is_ask_or_show_hn: false
llm_input_tokens: 13095
llm_latency_ms: 15212
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1161
our_published_at: '2026-09-25T16:55:36Z'
rewritten_title: Le nouvel ESP32-S31 peut exécuter Linux avec des capacités proches
  d'un Raspberry Pi
source_published_at: '2026-09-24T11:08:39Z'
status: summarized
summarized_at: '2026-09-25T17:40:52.909380Z'
title: The newest ESP32 can run Linux and it's getting close to a Raspberry Pi
url: https://www.xda-developers.com/newest-esp32-run-linux-close-to-raspberry-pi/
---

## Résumé de l'article

L'ESP32-S31 est un microcontrôleur d'Espressif doté de caractéristiques inhabituelles pour sa catégorie : Ethernet gigabit, USB 2.0 haut débit, interfaces pour caméra, écran LCD et carte SD. Il dispose de deux cœurs RISC-V à 320 MHz avec une véritable MMU supportant les schémas de pagination RISC-V Sv32, ce qui lui permet d'exécuter un vrai noyau Linux en mode superviseur, plutôt que les hacky ports précédents sur d'autres ESP32.

- L'ESP32-S31 embarque un Ethernet MAC 1000 Mbps, un contrôleur USB 2.0 OTG, deux slots SD, une interface caméra, et des interfaces pour panneaux LCD parallèles, un bien supérieur à l'ESP32-P4 limité à 100 Mbps
- Espressif a publié une BSP Linux basée sur Buildroot et U-Boot en août ; la communauté a déjà porté Linux 6.18 et 7.1 avec pilotes fonctionnels pour presque tout le matériel
- La mémoire reste la limitation majeure : 512 KB de SRAM interne et 16 à 32 MB de PSRAM embarquée (maximum 64 MB), bien moins que les SBC concurrents comme le Milk-V Duo S (512 MB), forçant le noyau à s'exécuter depuis le flash
- Le processeur à 320 MHz offre environ 3 900 cycles par trame Ethernet maximum, mettant en doute la capacité à saturer pleinement le lien gigabit avec des paquets petits
- L'ESP32-S31 conserve Wi-Fi 6 2.4 GHz, Bluetooth 5.4 (LE et Classic), 802.15.4 pour Thread/Zigbee, et affiche une consommation électrique typique d'un microcontrôleur (110-147 mA) malgré ses capacités SBC-like

## Discussion sur Hacker News (118 commentaires)

**Avis positifs** :
- L'ajout d'une véritable MMU (Sv32) ouvre des possibilités majeures, notamment pour exécuter Linux sur un matériel intégré traditionnellement dédié au bare metal
- Plateforme excellente et bon marché pour l'émulation logicielle de périphériques rétro (consoles, ordinateurs 80186/386, terminaux VT-340) grâce à la puissance accrue et aux GPIO disponibles
- Intégration complète (WiFi, Bluetooth, stockage, RAM) dans un form factor compact et ultra-économique (~$6 en volume) rend le chip très compétitif face aux SBC ARM plus chers
- Meilleure expérience de développement : portabilité de logiciels Linux existants, support multilingue (Python, Rust, C++), débogage standard, sans portage nécessaire

**Avis négatifs** :
- Confusion marketing persistent : l'ESP32 reste conceptuellement une microcontrôleur, pas vraiment un SBC, impossible de connecter moniteur/clavier/souris comme sur Raspberry Pi
- Support Linux limité en 32-bit RISC-V : suppression du XIP (Execute-In-Place) depuis kernel 7.1 rend difficile l'exécution depuis flash sans copie en RAM, problématique pour 64 MB de RAM max
- À 64 MB max de RAM et cores lents, Linux introduit une surcharge importante sans bénéfice réel pour la majorité des cas d'usage IoT comparé à un firmware bare metal ou FreeRTOS
- Manque de CSI MIPI sur S31 pour caméra vidéo malgré assez de puissance brute, et seul WiFi 2.4 GHz (pas 5 GHz sauf C5), limitant les applications multimédia et environnements RF chargés
- Fragmentation extrême de la gamme ESP32 (Xtensa vs RISC-V, avec/sans WiFi, RAM/flash variables) crée confusion : impossible de savoir quel niveau de matériel est requis pour exécuter un projet annoncé comme 'compatible ESP32'

**Top commentaires** :

- [jameshart](https://news.ycombinator.com/item?id=49830118) : The range of difference in capabilities of different boards branded ESP32 is getting larger. Makes it tricky to figure out when someone says ‘you can run this on an ESP32’ what level of hardware investment is required.
- [dsign](https://news.ycombinator.com/item?id=49832602) : I’ve been developing a guitar pedal firmware in an ESP32-P4, and the flash image size is still under 1 MB and the PSRAM sits unused. It has not only a bunch of sound filters, control code for ADC, DAC a couple of USB devices, SDIO and LittleFS, but also a full-blown serial terminal TUI to control a…
- [mstaoru](https://news.ycombinator.com/item?id=49829396) : Ah, the Lord Giveth and the Lord Taketh Away. P4 didn't have enough raw speed for camera applications but had MIPI CSI, S31 has enough raw speed but no CSI.

---

[Article original](https://www.xda-developers.com/newest-esp32-run-linux-close-to-raspberry-pi/) · [Discussion HN](https://news.ycombinator.com/item?id=49828969)
