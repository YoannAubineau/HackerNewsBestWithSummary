---
article_fetched_at: '2026-09-01T19:02:19.646069Z'
attempts: 0
content_source: extracted
discussion_comment_count: 166
discussion_fetched_at: '2026-09-01T19:02:17.379545Z'
error: null
guid: https://news.ycombinator.com/item?id=49505217
hn_item_id: 49505217
hn_url: https://news.ycombinator.com/item?id=49505217
is_ask_or_show_hn: false
llm_input_tokens: 14606
llm_latency_ms: 11846
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 897
our_published_at: '2026-09-01T18:05:07Z'
rewritten_title: Configurer deux ordinateurs en Ethernet direct pour transférer des
  fichiers rapidement
source_published_at: '2026-08-31T03:19:42Z'
status: summarized
summarized_at: '2026-09-01T19:03:13.061844Z'
title: Transfer files over an Ethernet patch cable
url: https://maurycyz.com/misc/etherfiles/
---

## Résumé de l'article

Connecter directement deux ordinateurs via un câble Ethernet permet de transférer des fichiers à des vitesses proches de 900 Mbit/s (environ 6,7 Go par minute) sans infrastructure réseau complexe. Cette méthode consiste à configurer manuellement les adresses IP IPv6 sur chaque machine, puis à utiliser des outils comme socat pour établir une connexion TCP.

- Configuration simple : assigner une adresse IPv6 à chaque interface Ethernet (ex : fd42:dead:beef::1/48 et ::2/48) et les activer
- Vitesse supérieure aux alternatives : atteint ~900 Mbit/s avec un câble standard, bien plus rapide que le stockage amovible, le Wi-Fi ou le cloud
- Avantages techniques : l'Ethernet différentiel résiste aux interférences radio et aux différences de potentiel, fonctionne même sans pile TCP/IP complète et ne nécessite pas de commutateur réseau
- Comparaison avec autres méthodes : le cloud storage double les transferts (upload puis download), USB-C nécessite du matériel récent, le stockage amovible pâtit des connecteurs défaillants
- Cas d'usage : idéal pour fichiers >10 GB entre deux machines proches, y compris les microcontrôleurs via trames brutes

## Discussion sur Hacker News (166 commentaires)

**Avis positifs** :
- Cette technique est utile pour les cas d'urgence et les sauvegardes dédiées entre deux machines isolées sans infrastructure réseau
- Les modernes cartes Ethernet supportent l'auto-détection (Auto MDI-X) depuis le Gigabit, éliminant le besoin de câbles spécialisés contrairement à l'époque des câbles croisés
- IPv6 link-local et APIPA (169.254.x.x) permettent une configuration automatique sans intervention manuelle, rendant la connexion point-à-point très simple
- La compression on-the-fly avec zstd peut multiplier le débit effectif par 1,5 à 3x pour les données compressibles, atteignant 165-330 MB/s sur un lien gigabit
- Thunderbolt/USB4 offrent une alternative encore plus rapide et moins consommatrice d'énergie que l'Ethernet pour le transfert direct sur certains appareils modernes

**Avis négatifs** :
- Pour la plupart des utilisateurs, une clé USB ou un SSD portable est plus simple et plus rapide qu'une configuration manuelle d'adresses IP
- Cette approche n'est pas nouvelle : elle remonte aux années 1990 avec les câbles croisés et devrait être une pratique bien établie depuis 25+ ans
- Les risques électriques réels existent pour les câbles entre bâtiments (potentiels électriques différents, parafoudre, câbles blindés) ; la fibre optique est préférable pour ces usages
- La configuration manuelle des adresses ajoute une complexité inutile quand les adresses link-local se configurent automatiquement en quelques secondes
- Sur macOS et Linux, des méthodes encore plus simples existent (mDNS, Python HTTP server) qui ne nécessitent même pas de connaître les adresses IP

**Top commentaires** :

- [rmunn](https://news.ycombinator.com/item?id=49506392) : That used to require a crossover cable; I've done precisely that \(with a crossover cable\) back before https://en.wikipedia.org/wiki/Medium-dependent\_interface\#Aut... became widespread. With a straight-through cable, you'd be connecting the Transmit \(TX\) pin of one adapter to the TX pin of the other…
- [yjftsjthsd-h](https://news.ycombinator.com/item?id=49506376) : I am 95% confident you don't actually need to assign IPs. Do this: \# ping all link-local devices on an interface: ping ff02::1%eth0 And then do your socat/rsync/whatever to the only IP that responds.
- [SillyUsername](https://news.ycombinator.com/item?id=49507247) : You can also pipe it through zstd on the fly, for data that compresses well you'll often see 1.5 to 3× the raw throughput, so a gigabit link can effectively move 165–330MB/s. Receiver: socat -u TCP6-LISTEN:1234,reuseaddr STDOUT | zstd -d -c | tar -xpf - -C /destination Sender: tar -C /source -cf -…

---

[Article original](https://maurycyz.com/misc/etherfiles/) · [Discussion HN](https://news.ycombinator.com/item?id=49505217)
