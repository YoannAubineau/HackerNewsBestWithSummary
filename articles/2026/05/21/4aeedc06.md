---
article_fetched_at: '2026-05-21T11:03:26.981541Z'
attempts: 0
content_source: extracted
discussion_comment_count: 135
discussion_fetched_at: '2026-05-21T11:03:25.530137Z'
error: null
guid: https://news.ycombinator.com/item?id=48212046
hn_item_id: 48212046
hn_url: https://news.ycombinator.com/item?id=48212046
is_ask_or_show_hn: false
llm_input_tokens: 12473
llm_latency_ms: 14157
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1049
our_published_at: '2026-05-21T10:24:28Z'
rewritten_title: Spécifications techniques complètes du Flipper One
source_published_at: '2026-05-20T18:33:56Z'
status: summarized
summarized_at: '2026-05-21T11:03:50.498638Z'
title: Flipper One Tech Specs
url: https://docs.flipper.net/one/general/tech-specs
---

## Résumé de l'article

Le Flipper One est un appareil portable multi-fonctions actuellement en développement actif. Ses spécifications techniques couvrent les dimensions, matériaux, processeurs, connectivité et ports d'expansion.

- Dimensions : 155 mm × 67 mm × 40 mm de profondeur; écran LCD monochrome 256×144 pixels avec 64 niveaux de gris
- Processeurs : CPU Rockchip RK3576 (8 cœurs jusqu'à 2,2 GHz) + MCU Raspberry Pi RP2350 (dual Cortex-M33 + dual RISC-V); RAM 8 Go LPDDR5, stockage 64 Go UFS 2.2 + slot microSD
- Batterie et connectivité : 7000 mAh (24000 mWh); USB-C 3.1, USB-A 3.1, HDMI 2.1 (4K@120Hz), 2× Gigabit Ethernet, Wi-Fi 6, Bluetooth 5.2, prise jack 3,5 mm stéréo
- Expansion : port M.2 Key B à l'arrière supportant PCIe 2.1, USB 2.0/3.1, SATA3, avec accès GPIO et interfaces série (UART, I2C, SIM)
- Contrôles : pavé tactile avec retour haptique, 5 boutons + D-pad directionnels, bouton Power, bouton PTT (Push-to-Talk) configurable

## Discussion sur Hacker News (135 commentaires)

**Avis positifs** :
- Le matériel est significativement plus puissant qu'un Flipper Zero avec un processeur 8-core, 8 GB de RAM DDR5 et deux ports Ethernet, le rendant utile comme ordinateur portable ou routeur mobile.
- L'ajout d'un port M.2 modulaire permet d'étendre les capacités radio et SDR selon les besoins, offrant de la flexibilité sans surcharger le produit de base.
- Les deux ports Ethernet et la connectivité réseau (WiFi, Ethernet) ouvrent de nouveaux cas d'usage comme MITM, analyse réseau ou routeur de voyage que le Zero ne proposait pas.
- Le connecteur de microcontrôleur sur l'écran d'affichage est une conception intelligente permettant un affichage bas régime même en cas de crash Linux, ainsi qu'un mode basse consommation.
- C'est un véritable cyberdeck commercial et accessible, représentant une évolution bienvenue du hobby dans l'écosystème du hacking portable avec potentiel de personnalisation communautaire.

**Avis négatifs** :
- L'absence de capacités RF/RFID/NFC natives que possédait le Flipper Zero rend ce produit moins successeur que produit différent, forçant l'achat d'extensions M.2 coûteuses et optionnelles.
- Le prix prévu sera probablement entre 500-1000€ (bien au-delà de l'impulsion d'achat du Zero à 200€), rendant l'appareil moins accessible et plus niche, particulièrement avec les modules SDR à 300-500€.
- La taille et le poids sont significativement plus importants que le Zero, limitant la portabilité; l'autonomie batterie sera probablement médiocre comparée au Zero (des semaines vs quelques heures).
- L'écran monochrome 6-bit bas-résolution connecté au microcontrôleur est une régression frustrante pour une machine aussi puissante, et l'absence de clavier QWERTY limite l'interaction.
- Plusieurs détails techniques semblent générés par IA ou mal vérifiés (style d'écriture, incohérences, sections 'nécessite clarification'), soulevant des doutes sur la fiabilité des spécifications annoncées.

**Top commentaires** :

- [jgrahamc](https://news.ycombinator.com/item?id=48213073) : I have a Flipper Zero and I've used it... occasionally. Like that one time controlling the Taylor Swift Eras tour wristbands: https://blog.jgc.org/2024/05/controlling-taylor-swift-eras-t... but it's mostly sat around being an odd device. I duplicated a couple of RFID things, used the IR for some st…
- [throawayonthe](https://news.ycombinator.com/item?id=48220294) : i think this can be confidently called a cyberdeck. some may say a full massproduced commercial unit goes against the spirit of che hobby but... there are now hardware clones and evolutions\(!\) of the flipper zero, community alt firmwares, add-on thingymajigs etc; if they stay as open with this one,…
- [sterlind](https://news.ycombinator.com/item?id=48212963) : maybe I'm blind, but it looks like there's no radio! like there's wifi and bluetooth, sure, but I don't see NFC or RFID or sub-1ghz radio, at all. imo the flipper always needed to be a software-defined transciever, with a small FPGA to drive it, like the other SDRs on the market. I'm disappointed t…

---

[Article original](https://docs.flipper.net/one/general/tech-specs) · [Discussion HN](https://news.ycombinator.com/item?id=48212046)
