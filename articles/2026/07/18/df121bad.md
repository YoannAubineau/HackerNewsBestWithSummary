---
article_fetched_at: '2026-07-18T17:48:54.257579Z'
attempts: 0
content_source: extracted
discussion_comment_count: 69
discussion_fetched_at: '2026-07-18T17:48:52.632655Z'
error: null
guid: https://news.ycombinator.com/item?id=48952565
hn_item_id: 48952565
hn_url: https://news.ycombinator.com/item?id=48952565
image_url: https://opengraph.githubassets.com/e6fd667eae739e33f1e127dc6c434cff8e9af2275c49200aeae6e6142572c621/BadChemical/IoT-Vulnerability-Research-Public
is_ask_or_show_hn: false
llm_input_tokens: 12153
llm_latency_ms: 15553
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1408
our_published_at: '2026-07-18T17:13:24Z'
rewritten_title: Caméras TP-Link Kasa ont exposé les coordonnées GPS domestiques via
  UDP non authentifié pendant six ans
source_published_at: '2026-07-17T21:42:43Z'
status: summarized
summarized_at: '2026-07-18T17:49:31.849159Z'
title: TP-Link Kasa cameras leaked home GPS via unauthenticated UDP for 6 years
url: https://github.com/BadChemical/IoT-Vulnerability-Research-Public/blob/main/TP-Link_Kasa_EC71/Kasa_EC71.md
---

## Résumé de l'article

Les caméras TP-Link Kasa Spot EC71 contenaient trois vulnérabilités critiques permettant l'exposition de données sensibles : une clé RSA partagée par tous les appareils, le stockage non chiffré des identifiants utilisateur en MD5, et l'exposition des coordonnées GPS précises via une requête UDP non authentifiée. Ces vulnérabilités, documentées publiquement depuis 2016 et 2020 pour le protocole sous-jacent, ont affecté des millions d'appareils pendant au moins six ans avant correction en firmware 2.4.1.

- **Exposition GPS publiquement connue depuis 2020** : une simple requête UDP non authentifiée sur le port 9999 révèle les coordonnées GPS précises du domicile, l'identifiant matériel unique, l'alias de l'appareil et la version du firmware, protégés seulement par un chiffre XOR trivial.

- **Clé cryptographique partagée par tous les appareils** : le firmware contient une clé RSA 2048-bit identique sur tous les appareils EC71 fonctionnant avec le firmware 2.3.26, extraïble physiquement via accès au flash SPI en quelques minutes.

- **Stockage des identifiants en clair et non salé** : les informations de compte TP-Link sont stockées avec l'adresse email en clair et le mot de passe sous forme de hash MD5 sans salt, permettant une compromission multidomain complète via tables arc-en-ciel ou accélération GPU.

- **Vecteur d'attaque du marché secondaire** : un acheteur d'appareil d'occasion peut récupérer les coordonnées GPS précises et les identifiants du propriétaire précédent sans accès réseau, localiser le domicile et prendre le contrôle de toute l'infrastructure domotique incluant les serrures intelligentes.

- **Remédiation lente et incohérente** : TP-Link a corrigé une vulnérabilité identique sur les prises intelligentes en 2020 mais n'a pas étendu le correctif à la gamme caméra, le problème ne réapparaissant publiquement que six ans après la divulgation initiale.

## Discussion sur Hacker News (69 commentaires)

**Avis positifs** :
- La vulnérabilité GPS est réelle et sérieuse : des coordonnées précises au mètre sans authentification via UDP, exposées depuis 6 ans, mériterait au minimum une notation CVSS haute (7.1) plutôt que 5.3
- Les défauts de divulgation coordonnée sont graves : patches qui briquent les appareils, réinitialisation d'usine inefficace (les données du propriétaire précédent persistent), et mauvaise compréhension des vulnérabilités par TP-Link
- Le problème s'étend au-delà de Kasa : TP-Link, fabricant majeur de routeurs réseau, produit régulièrement du matériel critiqué pour ses failles de sécurité intentionnelles ou non, et certains produits sont interdits d'importation aux USA
- L'architecture cloud-first est problématique : beaucoup de ces appareils ne fonctionnent pas en local et nécessitent des comptes obligatoires, empêchant les utilisateurs de maintenir un contrôle réseau simple et sécurisé
- Les données non chiffrées transitant par des serveurs tiers créent des risques masqués : les adresses IP des serveurs ne sont pas toujours contrôlées par l'éditeur, et les données personnelles en clair peuvent être facilement stockées et partagées via des courtiers de données

**Avis négatifs** :
- La menace est conditionnelle à une mauvaise configuration réseau : l'appareil n'est exposé que si l'utilisateur configure maladroitement son routeur (DMZ ou port-forwarding), ce qui ne devrait pas survenir avec une utilisation réseau intranet standard
- Le contexte local rend la fuite moins grave que présenté : si l'appareil reste sur le réseau local, les voisins connaissent déjà la localisation approximative, et un attaquant LAN aurait d'autres moyens pour obtenir cette information
- Critiquer les produits chinois sans perspective est partial : les vulnérabilités graves en IoT existent aussi chez les fabricants US (iRobot, Honeywell, Ecobee), et les appareils chinois bon marché sans abonnement obligatoire offrent plus de contrôle utilisateur que certaines alternatives
- Zigbee et les protocoles locaux ne sont pas adaptés aux caméras : bien que les réseaux mailles locaux comme Zigbee/Z-Wave fonctionnent bien pour les capteurs, ils ne supportent pas les flux vidéo, rendant le reproche théorique pour ce cas d'usage
- Les consommateurs acceptent ce trade-off volontairement : l'accès à distance sans configuration technique complexe (VPN, DNS dynamique) est un argument de vente majeur, et le coût des alternatives sécurisées (HomeKit, professionnels qualifiés) les rend inaccessibles pour la majorité

**Top commentaires** :

- [drnick1](https://news.ycombinator.com/item?id=48954568) : This underscores the principle that IoT devices should not be allowed to communicate over the public Internet. Pretty much all cheap, Chinese-made hardware of this kind has intentional or unintentional security holes waiting to be exploited.
- [gruez](https://news.ycombinator.com/item?id=48954331) : The report seems obviously AI generated, so I can't be bothered to read in its entirety, but based on my quick skim, "leaked home GPS" makes it sound worse than it is. Unless you're dumb enough to set DMZ on this device, this won't be exposed to the internet, and if it's LAN only, don't you already…
- [ericpauley](https://news.ycombinator.com/item?id=48957532) : A shocking number of devices are continuously reporting location data over random unencrypted protocols. What’s worse, they’re often sending the data to cloud IPs that aren’t even controlled by the company, so some random person is getting your real-time location.

---

[Article original](https://github.com/BadChemical/IoT-Vulnerability-Research-Public/blob/main/TP-Link_Kasa_EC71/Kasa_EC71.md) · [Discussion HN](https://news.ycombinator.com/item?id=48952565)
