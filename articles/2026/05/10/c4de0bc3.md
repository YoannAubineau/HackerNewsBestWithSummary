---
article_fetched_at: '2026-05-10T14:24:42.074983Z'
attempts: 0
content_source: extracted
discussion_comment_count: 128
discussion_fetched_at: '2026-05-10T14:24:41.241407Z'
error: null
guid: https://news.ycombinator.com/item?id=48073201
hn_item_id: 48073201
hn_url: https://news.ycombinator.com/item?id=48073201
is_ask_or_show_hn: false
llm_input_tokens: 13815
llm_latency_ms: 12127
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 988
our_published_at: '2026-05-10T14:20:41Z'
rewritten_title: Un ancien partisan d'AWS explique pourquoi il a quitté et ne revient
  pas
source_published_at: '2026-05-09T08:37:41Z'
status: summarized
summarized_at: '2026-05-10T14:25:01.196131Z'
title: I returned to AWS, and was reminded why I left
url: http://fourlightyears.blogspot.com/2026/05/i-returned-to-aws-and-was-reminded-hard.html
---

## Résumé de l'article

Un pionnier historique d'AWS qui a défendu la plateforme pendant 15 ans revient sur les raisons de son départ et sur une mauvaise expérience récente. Il détaille comment une accumulation de griefs—complexité croissante, facturation déloyale, prédation sur les projets open source, et service client défaillant—l'ont éloigné du service cloud.

- AWS a commencé par refuser de développer ses propres bibliothèques clientes, forçant les développeurs à le faire gratuitement, et a maintenu Python 2 bien trop longtemps
- Les frais de sortie de données (9 cents par gigaoctet) et la facturation enchevêtrée avec double/triple facturation sur les mouvements de données internes créent des pièges coûteux
- AWS a copié et monétisé des projets open source populaires (Elasticsearch, Redis, MongoDB) malgré l'opposition explicite des créateurs, ce que l'auteur qualifie de comportement prédateur
- Services complexes comme IAM, DynamoDB et Lambda offrent peu d'avantage réel tout en créant une forte dépendance au fournisseur
- Lors d'un retour récent pour des tests, AWS a suspendu son compte pour raisons de sécurité supposée; après 4 jours, le service reste bloqué et le support n'a pas répondu, affectant son email professionnel

## Discussion sur Hacker News (128 commentaires)

**Avis positifs** :
- AWS dispose de services fondamentaux matures et bien conçus (EC2, S3, IAM, RDS, EKS) qui restent supérieurs à la concurrence, notamment en termes de design d'IAM par rapport aux autres clouds
- La capacité à déployer l'infrastructure en minutes via API et à automatiser les ressources via Infrastructure as Code représente toujours un avantage réel par rapport aux solutions héritées
- Des alternatives comme Cloudflare, Vercel, DigitalOcean ou Hetzner offrent une expérience plus simple et moins coûteuse pour les projets courants, réduisant les frais de 10x ou plus
- L'écosystème de cloud alternatifs s'est considérablement amélioré, permettant aux utilisateurs de migrer facilement sans lock-in majeur si on évite les services propriétaires AWS

**Avis négatifs** :
- AWS a adopté des pratiques anti-concurrence envers les projets open-source (OpenSearch, Valkey, DocumentDB), forçant les créateurs à changer de licence pour se protéger, transformant d'anciens projets en propriétaires
- L'interface utilisateur et la documentation AWS sont délibérément complexes pour masquer les coûts réels ; les prix ne s'affichent pas directement lors de la création de ressources, créant une relation « abusive »
- Les nouveaux services AWS (Lambda, DynamoDB, Cognito, API Gateway, WorkMail) sont surcoûteux, mal documentés et pièges faciles pour les développeurs, générant des coûts démesurés ($20k/mois est courant sans raison technique)
- Le support AWS a dégradé significativement : réponses lentes (24h+ annoncé, 3j+ en réalité), fermetures de comptes sans raison, absence de responsabilité client ; l'entreprise privilégie les clients enterprise au détriment des PME
- AWS innove moins et se replie sur l'upsell de services médiocres ; les talents techniques quittent l'entreprise, beaucoup de startups reviennent à l'on-premise ou au colocatif après avoir compris le surcoût réel

**Top commentaires** :

- [aljgz](https://news.ycombinator.com/item?id=48083750) : Years ago, I joined a company, took over a dev team and was asked to launch the product in 3 months. They were using AWS, so I logged in the account to add a few more machines. Right there, in front of my eyes, were the signs of an adversarial, abusive relationship. The UI to fire up a new machine…
- [tedivm](https://news.ycombinator.com/item?id=48083506) : « AWS stomped on open source projects - despite the clear desire of projects like Elasticsearch, Redis, and MongoDB not to be cloned and monetized, AWS pushed ahead with OpenSearch, Valkey, and DocumentDB anyway, capturing the hosted-service money after those communities and companies had built t »…
- [djyde](https://news.ycombinator.com/item?id=48083677) : I've transitioned between cloud services and self-hosting a few times: 1. Vercel Phase My first project used Vercel. Since my project was Next.js, the experience was decent. But as my project gained some users, I found that even for projects under 100 users, I needed to pay $20 per month. Since my…

---

[Article original](http://fourlightyears.blogspot.com/2026/05/i-returned-to-aws-and-was-reminded-hard.html) · [Discussion HN](https://news.ycombinator.com/item?id=48073201)
