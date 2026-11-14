---
article_fetched_at: '2026-11-14T23:33:17.323415Z'
attempts: 0
content_source: extracted
discussion_comment_count: 226
discussion_fetched_at: '2026-11-14T23:32:13.171511Z'
error: null
guid: https://news.ycombinator.com/item?id=50499017
hn_item_id: 50499017
hn_url: https://news.ycombinator.com/item?id=50499017
image_url: https://www.crissyfield.de/images/research-lovable-opengraph.jpg
is_ask_or_show_hn: false
llm_input_tokens: 21133
llm_latency_ms: 9729
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1101
our_published_at: '2026-11-14T23:03:30Z'
rewritten_title: Applications créées avec Lovable exposent des données sensibles incluant
  passeports et messages privés
source_published_at: '2026-11-14T17:43:10Z'
status: summarized
summarized_at: '2026-11-14T23:34:56.662605Z'
title: Lovable apps expose passport details and more than 200K private messages
url: https://www.crissyfield.de/research/lovable-en/
---

## Résumé de l'article

Lovable est une plateforme suédoise fondée en 2023 qui permet de créer des applications web via des descriptions en langage naturel, accessible aux utilisateurs sans expérience technique. Une analyse de 159 041 projets Lovable a révélé que beaucoup d'entre eux exposent des données sensibles sans protection d'authentification.

- Sur 34 545 projets utilisant la base de données Supabase, 24 664 ont envoyé des données sans nécessiter de connexion ; 7 403 (30 %) contenaient des adresses email dans des tables accessibles sans authentification
- Les données exposées incluent plus de 80 000 profils avec noms complets, dates de naissance et genres ; plus de 200 000 messages de chat privés ; des passeports avec numéros, dates d'expiration et nationalités ; des informations de paiement et codes de tickets
- Les risques incluent l'usurpation d'identité, l'hameçonnage et la fraude aux tickets ; ces erreurs de contrôle d'accès sont facilitées par les schémas récurrents des intégrations de base de données
- Lovable place la responsabilité de la sécurité sur ses clients, laissant un écart entre sa promesse de plateforme tout-en-un facile d'utilisation et les exigences de sécurité réelles
- Les recommandations incluent un examen expert des permissions d'accès avant de traiter des données confidentielles, et l'absence de vérification automatisée ne peut remplacer une évaluation de sécurité professionnelle

## Discussion sur Hacker News (226 commentaires)

**Avis positifs** :
- Les failles de sécurité identifiées (données publiques sans authentification) reflètent des problèmes systémiques bien antérieurs à l'IA, mais amplifiés par l'accélération du développement et la démocratisation de la création d'apps
- La recherche est justifiée pour évaluer l'ampleur réelle du problème, contrairement aux minimisations habituelles des entreprises : connaître la portée (7 403 sites affectés) permet une action proportionnée
- Lovable place toute la responsabilité sur les utilisateurs sans expertise technique, malgré un marketing promettant que 'quiconque peut créer une app sans connaissances techniques' — cette asymétrie est la vraie responsabilité
- Supabase porte une responsabilité majeure pour ses défauts de conception (clés publiques donnant accès à la base, mauvaises valeurs par défaut, fuite d'informations via les messages d'erreur)
- Le vrai problème est culturel et structural : l'absence de conséquences légales réelles, la course à la croissance et les profits court-termistes incitent les entreprises à ignorer la sécurité plutôt que de l'intégrer par défaut

**Avis négatifs** :
- Le chercheur a potentiellement franchi une ligne légale en téléchargeant et analysant du contenu pour évaluer l'ampleur du problème au lieu de s'arrêter après avoir prouvé l'existence de la vulnérabilité
- L'IA n'est qu'un symptôme : les failles de sécurité massives existaient bien avant les LLMs ; blâmer l'IA détourne l'attention des vrais problèmes systémiques de l'industrie tech
- Accuser les utilisateurs non-techniques de négligence est injuste : interdire l'accès à des outils n'est pas réaliste socialement, et le blâme doit porter sur les entreprises qui profitent en mettant des outils dangereux entre des mains inexpérimentées
- Exiger une licence ou expertise pour publier une app ralentirait drastiquement l'innovation et exclurait les petits créateurs et non-techniciens légitimes
- Les données étaient publiquement accessibles via Common Crawl avant même la recherche : télécharger depuis une archive publique ne constitue pas une 'exfiltration' comparable à du piratage traditionnel

**Top commentaires** :

- [igorandri](https://news.ycombinator.com/item?id=50502105) : Igor here, Head of Security at Lovable. Thanks to the Crissy Field team for their work. The root cause in these apps was insufficent Row-Level Security, which is exactly what our scanning is built to catch. We scan every app automatically before publish and offer a deeper SAST scan, both free for a…
- [neathack](https://news.ycombinator.com/item?id=50499563) : Hi, I’m the author of this blog post. I submitted it to HN two weeks ago, but it didn’t gain much traction, so I’m glad to see it resubmitted. Happy to answer any questions, though I think the situation is fairly self-explanatory.
- [SOLAR\_FIELDS](https://news.ycombinator.com/item?id=50499905) : The part people are ignoring is Supabase's culpability in this matter: https://github.com/orgs/supabase/discussions/4547 This was supposedly fixed on October 30, but there are reports floating around that for existing projects, the defaults still apply. Lovable deserves some heat for using this, bu…

---

[Article original](https://www.crissyfield.de/research/lovable-en/) · [Discussion HN](https://news.ycombinator.com/item?id=50499017)
