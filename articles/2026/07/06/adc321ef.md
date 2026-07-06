---
article_fetched_at: '2026-07-06T22:07:08.299280Z'
attempts: 0
content_source: extracted
discussion_comment_count: 82
discussion_fetched_at: '2026-07-06T22:06:57.712845Z'
error: null
guid: https://news.ycombinator.com/item?id=48804014
hn_item_id: 48804014
hn_url: https://news.ycombinator.com/item?id=48804014
image_url: https://cf-assets.www.cloudflare.com/zkvhlag99gkb/6S1TZg4kL1049Rkw44RiIc/5adca4df8432fb3401517712f2b8d15f/Your_Worker_can_now_have_its_own_cache_in_front_of_it-OG.png
is_ask_or_show_hn: false
llm_input_tokens: 15038
llm_latency_ms: 11587
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 992
our_published_at: '2026-07-06T21:23:08Z'
rewritten_title: Cloudflare lance Workers Cache, un système de cache hiérarchisé en
  deux niveaux pour les Workers
source_published_at: '2026-07-06T13:02:51Z'
status: summarized
summarized_at: '2026-07-06T22:08:45.733923Z'
title: Workers Cache
url: https://blog.cloudflare.com/workers-cache/
---

## Résumé de l'article

Workers Cache est un système de mise en cache hiérarchisé que Cloudflare lance pour les Workers — son service de calcul edge. Il s'active par une simple ligne de configuration Wrangler et utilise les en-têtes Cache-Control standard HTTP. Le cache s'intercale désormais devant chaque Worker, permettant de servir les réponses en cache sans exécuter le code du Worker et sans facturer le temps CPU associé.

- Le cache fonctionne sur tous les plans tarifaires de Cloudflare et se configure en une ligne de code ("cache": { "enabled": true }), puis s'administre via les en-têtes Cache-Control HTTP ordinaires et les tags de cache
- Il résout le problème du rendu côté serveur sur Workers en offrant une troisième option entre le pré-rendu au build (temps de construction long) et le rendu à chaque requête (coût latence élevé) : rendus à la demande avec mise en cache et rafraîchissement en arrière-plan via stale-while-revalidate
- Le cache fonctionne en deux tiers hiérarchisés (par défaut) : un niveau local dans chaque datacenter Cloudflare et un niveau supérieur qui agrège les remplissages sur tout le réseau, réduisant les appels à l'Worker
- Chaque entrypoint de Worker peut avoir son cache indépendant avec sa propre clé, TTL et espace de tags pour invalidation ; les appels entre entrypoints via ctx.exports passent par le cache, permettant de composer plusieurs étapes de cache au sein d'une seule application
- Les réponses authentifiées peuvent être cachées en toute sécurité par utilisateur via ctx.props (partie de la clé de cache), transformant les APIs multi-locataires de "non cacheable" à "cacheable par utilisateur"

## Discussion sur Hacker News (82 commentaires)

**Avis positifs** :
- La fonctionnalité répond à un besoin critique manquant : les Workers n'exécutaient jamais le cache en front, ce qui gaspillait CPU et coûtait cher même pour les réponses en cache (3ms d'invocation par millions de requêtes)
- L'implémentation respecte les standards HTTP (Cache-Control, stale-while-revalidate) plutôt que de réinventer la roue, avec une API de cache tags pour l'invalidation granulaire
- Cloudflare a systématiquement livré depuis 2020 des features réduisant significativement les coûts (réduction de 15k£ à 0£ dans certains cas grâce aux Snippets gratuits)
- L'architecture technique révélée (ctx.exports, channel tokens, entrypoints) offre une flexibilité permettant de la logique personnalisée avant et après le cache

**Avis négatifs** :
- L'article est clairement généré ou fortement édité par IA, avec des tournures génériques ("here's the biggest unlock, and it's the hardest to see"), hyphenation excessive et structure artificielle qui manquent de voix humaine authentique
- Facturation paradoxale : les requêtes statiques et invocations worker-to-worker deviennent payantes avec le cache alors qu'elles étaient gratuites, créant une incitation perverse à fragmenter les workers plutôt qu'à centraliser le cache
- Le temps d'implémentation (9 ans) reste injustifié dans l'article malgré la tentative d'explication technique, et le feature était fondamental pour une plateforme de cache de premier plan
- L'architecture originale (workers devant le cache) semblait inadaptée depuis le départ pour un service de edge computing, soulevant des questions sur la vision initiale du produit

---

[Article original](https://blog.cloudflare.com/workers-cache/) · [Discussion HN](https://news.ycombinator.com/item?id=48804014)
