---
article_fetched_at: '2026-11-16T22:40:44.363132Z'
attempts: 0
content_source: extracted
discussion_comment_count: 65
discussion_fetched_at: '2026-11-16T22:40:37.057159Z'
error: null
guid: https://news.ycombinator.com/item?id=50512441
hn_item_id: 50512441
hn_url: https://news.ycombinator.com/item?id=50512441
image_url: https://forum.torproject.org/uploads/default/original/2X/d/d3424bed34f4ec18b2e99178c2801ba6dfb655d6.png
is_ask_or_show_hn: false
llm_input_tokens: 5950
llm_latency_ms: 6306
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 853
our_published_at: '2026-11-16T22:26:33Z'
rewritten_title: Le Tor Project publie un correctif d'urgence contre les attaques
  DDoS en cours
source_published_at: '2026-11-16T00:21:54Z'
status: summarized
summarized_at: '2026-11-16T22:42:29.179361Z'
title: Tor Project Issues Rapid-Response DoS-Defense Fix Amid Sustained DDoS Attack
url: https://forum.torproject.org/t/security-release-0-4-9-17/22454
---

## Résumé de l'article

Le Tor Project a publié la version 0.4.9.17 contenant des correctifs de sécurité, dont un important pour les défenses contre les attaques par déni de service (DoS) concernant la gestion IPv6. Cette version répond à une attaque DDoS massive et coordonnée qui affecte actuellement le réseau Tor en inondant les relais de circuits clients.

- Un correctif de sécurité prioritaire renforce les défenses des relais contre les attaques DoS, en particulier pour la gestion IPv6
- L'attaque DDoS en cours submerge la majorité des opérateurs de relais du réseau par un flux massif de circuits clients
- Le Tor Project prévoit de publier d'autres mises à jour défensives à court terme et invite tous les opérateurs de relais à mettre à jour immédiatement
- Aucune action supplémentaire n'est requise après la mise à jour
- L'équipe du Tor Project remercie les opérateurs de relais pour leur aide et leur engagement via la liste de diffusion tor-relays@

## Discussion sur Hacker News (65 commentaires)

**Avis positifs** :
- Les attaques DDoS sur Tor sont un phénomène persistant qui nécessite une défense constante et adaptée, notamment via des mécanismes comme les défis PoW
- Tor s'est considérablement amélioré en vitesse au fil du temps grâce à des optimisations d'algorithmes de contrôle de congestion, permettant désormais de regarder des vidéos en haute qualité
- Tor reste un service critique et gratuit pour la censure, les journalistes et les citoyens vivant sous oppression, offrant une liberté que les VPN payants ne peuvent égaler
- La réponse rapide du Tor Project pour corriger les vulnérabilités DDoS démontre une capacité d'adaptation face aux menaces émergentes
- Les nœuds de garde et relais légitimes exploités par des contributeurs sérieux renforcent la confiance du réseau malgré les risques

**Avis négatifs** :
- Les défis PoW ralentissent significativement la connexion initiale des nouveaux visiteurs, risquant de les décourager et d'affecter l'expérience utilisateur
- Malgré les améliorations, Tor reste fondamentalement limité par la latence inhérente au routage en oignon (100-800ms), rendant son usage pénible pour beaucoup
- L'infrastructure de Tor est concentrée en Europe et aux États-Unis, créant des biais de réseau pour les utilisateurs en dehors de ces régions
- De nombreux services bloquent les adresses IP Tor en raison du taux d'abus élevé (trolls, spammeurs, arnaqueurs), limitant son utilité pour la navigation ordinaire
- Les relais Tor issus d'ISP résidentiels attirent l'attention des attaquants et peuvent compromettre la réputation de l'adresse IP du propriétaire malgré une utilisation légitime

**Top commentaires** :

- [Actor](https://news.ycombinator.com/item?id=50513763) : I started running a non-exit node a few months ago and after a little while it became trusted and became a guard node. Guard nodes seems more important than amiddle node so I was happy to run one I know is legitimate. That makes at least one legitimate guard node for the network. I noticed the atta…
- [sikozu](https://news.ycombinator.com/item?id=50513939) : I tried Tor briefly maybe about 10 years ago, only to have a little look around as I was curious, and to be honest I remember the experience was pretty disappointing, websites were slow and lots of resources seemed to be unavailable. Has it changed much at all? I don't really know what most people…
- [noident](https://news.ycombinator.com/item?id=50513599) : Could this be an effort to direct traffic to adversarial relays?

---

[Article original](https://forum.torproject.org/t/security-release-0-4-9-17/22454) · [Discussion HN](https://news.ycombinator.com/item?id=50512441)
