---
article_fetched_at: '2026-08-23T17:13:30.814471Z'
attempts: 0
content_source: extracted
discussion_comment_count: 32
discussion_fetched_at: '2026-08-23T17:13:29.467440Z'
error: null
guid: https://news.ycombinator.com/item?id=49402781
hn_item_id: 49402781
hn_url: https://news.ycombinator.com/item?id=49402781
is_ask_or_show_hn: false
llm_input_tokens: 5482
llm_latency_ms: 12273
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 960
our_published_at: '2026-08-23T16:38:51Z'
rewritten_title: Un administrateur réseau britannique raconte comment NetBSD a transformé
  sa vie professionnelle et personnelle
source_published_at: '2026-08-22T19:07:46Z'
status: summarized
summarized_at: '2026-08-23T17:14:08.854682Z'
title: NetBSD and my life (2005)
url: https://mail-index.netbsd.org/netbsd-advocacy/2005/09/10/0000.html
---

## Résumé de l'article

En 2005, Gary Rolland, administrateur réseau dans une grande entreprise britannique, décrit son expérience de migration de 29 serveurs Windows vers NetBSD pour gérer 4 800 utilisateurs. Cette transition a considérablement amélioré la stabilité de l'infrastructure informatique et lui a permis de retrouver un meilleur équilibre vie professionnelle-vie personnelle.

- Le réseau NetBSD gère des charges extrêmes : plus de 870 Go de données par jour, 1 200 e-mails quotidiens et 35 requêtes HTTP par minute en heures de pointe, via MySQL, Apache, Postfix et Samba.
- Sous Windows, les serveurs tombaient régulièrement en panne, forçant Rolland à intervenir d'urgence et le privant de temps avec sa famille (exemple : interruption d'une sortie à Alton Towers avec sa fille).
- Après avoir testé deux serveurs NetBSD avec succès (contrairement aux serveurs Windows qui ont planté ce même jour), Rolland a progressivement migré tout le réseau vers NetBSD.
- La stabilité accrue a libéré du temps pour l'équipe d'administration, permettant aux trois autres administrateurs d'apprendre NetBSD et d'améliorer leurs compétences.
- L'amélioration de la fiabilité a supprimé les astreintes de week-end pour l'équipe, qui peut désormais administrer à distance par SSH, améliorant ainsi l'équilibre vie-travail et les relations familiales de Rolland.

## Discussion sur Hacker News (32 commentaires)

**Avis positifs** :
- NetBSD se distingue par sa portabilité exceptionnelle sur de nombreuses architectures (SPARC, SH3, Raspberry Pi, etc.) et reste un choix idéal pour les anciens matériels et les systèmes embarqués.
- La communauté NetBSD maintient une excellente documentation et un système de base utile et minimaliste, permettant de comprendre le fonctionnement complet du système sans dépendances excessives.
- NetBSD conserve une philosophie artisanale et une approche 'hacking' pure, sans préoccupations commerciales, offrant une expérience cyberpunk comparée aux premiers jours de Linux.
- Les BSD en général (dont NetBSD) se sont matérialisés en excellents systèmes serveurs avec des performances fiables et une stabilité éprouvée au fil des années.
- Les projets open-source comme NetBSD, Linux et Gentoo ont transformé les vies de nombreux utilisateurs en les aidant à acquérir des compétences informatiques et à démarrer des carrières en informatique.

**Avis négatifs** :
- Même en 2005, les performances de NetBSD (35 requêtes/minute) étaient faibles comparées à d'autres systèmes, bien que cela reflète probablement l'application plutôt que le système lui-même.
- FreeBSD offrait une meilleure compatibilité des pilotes matériels dans les années 1990-2000, ce qui en faisait un choix plus pratique pour de nombreux utilisateurs.
- La faible adoption de navigateurs et de paquets logiciels rend les BSD progressivement moins viables pour un usage polyvalent à mesure que le logiciel moderne se raréfie.
- À l'époque moderne, NetBSD reste peu utilisé en comparaison avec Linux, et son utilisation s'est historiquement concentrée sur des cas d'usage niche plutôt que grand public.

**Top commentaires** :

- [avhception](https://news.ycombinator.com/item?id=49404970) : For me, it was Gentoo. I was a little bit lost after a bad time in the public school system, and not sure what to do with my life after that. I was fascinated by Linux, but never really got the hang of it. Used SuSE, which was fine, but I never really knew what I was doing. And then I get into Gent…
- [cavem0nkey](https://news.ycombinator.com/item?id=49403991) : NetBSD was my favourite playing around OS from the late 1990s to about 2010. Worked on any old crap I had lying around which was mostly thoroughly obsolete SPARC and x86 kit. Did the job. Never went wrong. Good documentation built in. Netbooted on anything. No idea where it is now but this post has…
- [tolerance](https://news.ycombinator.com/item?id=49403461) : I'm considering initiating a campaign to influence a community space that I'm a part of into running NetBSD on some low-risk infrastructure that we may adopt.

---

[Article original](https://mail-index.netbsd.org/netbsd-advocacy/2005/09/10/0000.html) · [Discussion HN](https://news.ycombinator.com/item?id=49402781)
