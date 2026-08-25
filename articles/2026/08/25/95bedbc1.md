---
article_fetched_at: '2026-08-25T13:41:25.436886Z'
attempts: 0
content_source: extracted
discussion_comment_count: 148
discussion_fetched_at: '2026-08-25T13:41:23.834599Z'
error: null
guid: https://news.ycombinator.com/item?id=49421536
hn_item_id: 49421536
hn_url: https://news.ycombinator.com/item?id=49421536
is_ask_or_show_hn: false
llm_input_tokens: 15655
llm_latency_ms: 15342
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1219
our_published_at: '2026-08-25T12:59:56Z'
rewritten_title: XMPP, protocole ouvert de communication créé il y a 25 ans, offre
  une alternative d'infrastructure indépendante
source_published_at: '2026-08-24T15:51:31Z'
status: summarized
summarized_at: '2026-08-25T13:42:04.666372Z'
title: 'Jabber/XMPP: 25 Years of Digital Independence'
url: https://gultsch.de/posts/25-years-of-digital-independence/
---

## Résumé de l'article

XMPP (Extensible Messaging and Presence Protocol), anciennement appelé Jabber, est un protocole standardisé pour la communication instantanée développé depuis plus de 25 ans. Conçu autour d'un standard ouvert géré par la XMPP Standards Foundation, il permet l'interopérabilité entre différents clients et serveurs, contrairement aux plateformes propriétaires fermées.

- Contrairement à Signal, Wire ou Matrix, XMPP repose sur un standard ouvert développé collaborativement au sein d'une organisation de normalisation, plutôt que contrôlé par une unique entreprise, ce qui permet l'indépendance vis-à-vis des fournisseurs.
- Le protocole s'adapte aux évolutions technologiques grâce à ses extensions (XEP), incluant le chiffrement bout-à-bout (OMEMO), la gestion mobile (Stream Management) et des fonctionnalités modernes comme les réactions emoji et la synchronisation multi-appareils.
- Des clients modernes comme Dino (Linux) et Conversations (Android) offrent une parité fonctionnelle avec les messagers propriétaires, tout en permettant l'auto-hébergement et la fédération entre serveurs indépendants.
- XMPP représente une véritable infrastructure numérique collective selon les principes de propriété commune, où les utilisateurs ne sont pas verrouillés chez un unique opérateur et où plusieurs implémentations indépendantes du protocole coexistent.
- Le protocole a traversé plusieurs cycles technologiques et reste viable face aux alternatives plus récentes, offrant une résilience et une stabilité basées sur des décennies d'évolution collaborative.

## Discussion sur Hacker News (148 commentaires)

**Avis positifs** :
- XMPP bénéficie d'utilisations cachées mais significatives : armées (NATO), agences de renseignement et forces de police l'utilisent pour les communications critiques, notamment sur des liaisons dégradées en bande passante très limitée
- Le protocole reste solide techniquement avec un support complet des fonctionnalités modernes (chiffrement OMEMO, appels vidéo, partage d'écran, notifications push via UnifiedPush) et une vraie décentralisation contrairement à Matrix
- Les serveurs XMPP modernes comme Prosody et Snikket sont simples à déployer avec des configurations par défaut sensées, contrastant avec la complexité perçue d'Apache ; l'écosystème est fragmenté mais fonctionnel
- Réseau fédéré stable avec une base d'utilisateurs dispersée mais loyale : présent sur le fediverse, Disroot, jmp.chat ; utilisé efficacement pour des cas d'usage spécialisés (orchestration d'agents IoT, notification système, bridges téléphonie)
- 25 ans de pérennité et indépendance : à l'inverse des protocoles commerciaux qui disparaissent (Google Chat, Facebook Chat fermés), XMPP ne sera jamais repris par une big tech et laissé à l'abandon

**Avis négatifs** :
- Adoption publique pratiquement nulle depuis 10-15 ans : malgré les utilisations militaires/gouvernementales, aucune communauté visible grand public ; les serveurs publics sont désertés et les listes d'amis historiques sont vides
- Fragmentation critique des clients et serveurs sur les extensions (XEPs) : OMEMO incompatible entre versions, absence de support hétérogène des images et formatage, clients refusant de fonctionner ensemble (Conversations vs Fluux), nombreux crashes et dysfonctionnements imprévisibles
- Expérience utilisateur loin derrière Telegram/Signal/Matrix : interfaces datées des années 2000, notifications fragmentées, synchronisation multi-appareils défaillante, pas de récupération automatique d'erreur, chiffrement se désactivant ou se cassant aléatoirement sans MitM
- Spam massif non maîtrisé publiquement accessibles : contrairement à l'email, XMPP clients mal armés contre les demandes d'amitié malveillantes en masse, rendant impraticable l'utilisation comme canal public (bug reports, etc.)
- Manque chronique de ressources financières et de momentum développement : contrairement à Matrix bénéficiant de millions en financement européen, les implémentations XMPP restent fragmentées avec un seul client vraiment maintenable par plateforme, bloquant l'émergence d'alternatives au monopole Synapse

**Top commentaires** :

- [fishgoesblub](https://news.ycombinator.com/item?id=49423612) : I love XMPP and am hopeful for its future with what the teams behind Movim\[0\], and Fluux\[1\] are doing. It was a tremendous shame that Matrix didn't improve upon XMPP and instead did their own thing. I continuously wonder what would the XMPP ecosystem look like, if the millions of dollars of funding…
- [pavo-etc](https://news.ycombinator.com/item?id=49427130) : I have recently picked up XMPP as my agent communication layer, and its worked great. Each pi agent is given an account and wrapped in an XMPP client\[0\] that lets it speak to me and other agents when needed. This has worked well since I can spin up new accounts on demand and I can use existing serv…
- [delduca](https://news.ycombinator.com/item?id=49422866) : It was so cool when facebook, google and others used to use xmpp, at that time I used a single IM client https://adium.im

---

[Article original](https://gultsch.de/posts/25-years-of-digital-independence/) · [Discussion HN](https://news.ycombinator.com/item?id=49421536)
