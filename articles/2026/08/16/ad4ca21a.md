---
article_fetched_at: '2026-08-16T22:11:41.598850Z'
attempts: 0
content_source: ask_show_hn
discussion_comment_count: 53
discussion_fetched_at: '2026-08-16T22:11:40.369594Z'
error: null
guid: https://news.ycombinator.com/item?id=49322107
hn_item_id: 49322107
hn_url: https://news.ycombinator.com/item?id=49322107
is_ask_or_show_hn: true
llm_input_tokens: 4713
llm_latency_ms: 9159
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 738
our_published_at: '2026-08-16T21:52:43Z'
rewritten_title: Cloudflare injecte silencieusement ses analytics lors du changement
  de serveurs de noms
source_published_at: '2026-08-16T17:49:46Z'
status: summarized
summarized_at: '2026-08-16T22:11:57.605439Z'
title: 'Tell HN: Cloudflare silently injects its analytics when you switch nameservers'
url: https://news.ycombinator.com/item?id=49322107
---

## Résumé de l'article

Un utilisateur rapporte que Cloudflare a automatiquement injecté un script d'analyse (snippet JavaScript) dans son site web sans consentement préalable, suite au changement de ses serveurs de noms vers Cloudflare pour utiliser le service R2. L'injection s'est faite sur un site conçu pour fonctionner sans JavaScript.

- Le script d'analytics a été injecté automatiquement sans opt-in explicite de la part de l'utilisateur
- L'utilisateur a dû accéder au tableau de bord Analytics, ajouter manuellement son site, puis désactiver le snippet
- L'utilisateur qualifie cette approche d'invasive et appelle à un système d'opt-in plutôt que d'opt-out pour ces fonctionnalités
- Le site affecté (textlog.cc) était conçu comme un site HTML/texte sans JavaScript, ce qui rend l'injection particulièrement problématique

## Discussion sur Hacker News (53 commentaires)

**Avis positifs** :
- Cloudflare injecte effectivement du code analytics sans consentement explicite, ce qui représente un problème de transparence et de confiance bien documenté
- Le problème s'étend au-delà des paramètres techniques : même les utilisateurs ayant explicitement désactivé analytics retrouvent le script injecté, révélant des défauts de conception des paramètres par défaut
- Cette pratique s'inscrit dans un pattern d'enshittification : Cloudflare accumule du pouvoir de marché puis impose progressivement des modifications moins acceptables aux utilisateurs
- L'injection de code par un tiers interposé (man-in-the-middle) soulève des questions légales sur le dépassement d'accès autorisé et des préoccupations quant à la surveillance de trafic en clair

**Avis négatifs** :
- Le problème est souvent dû à l'activation accidentelle du proxy reverse par défaut, non à une injection DNS-only : Cloudflare n'injecte que lorsqu'il agit réellement comme proxy
- L'utilisation du proxy reverse est la raison pour laquelle 99% des utilisateurs choisissent Cloudflare ; le comportement par défaut est rationnel pour ce cas d'usage principal
- Des alternatives existent et fonctionnent bien (DNS-only sans proxy), mais peu d'utilisateurs les explorent ; les utilisateurs DNS-only ne sont généralement pas affectés
- Cloudflare a annoncé cette fonctionnalité publiquement (blog officiel sur RUM Analytics) ; ce n'est pas vraiment une pratique 'silencieuse' mais plutôt peu remarquée lors du lancement

**Top commentaires** :

- [okzgn](https://news.ycombinator.com/item?id=49323462) : An alternative: \<meta http-equiv="Content-Security-Policy" content="script-src 'self' https://only-scripts-allowed-from-here.com"\> This makes the client only load self-hosted scripts, or scripts only from the specified origins, among the other directives CSP allows \(e.g. restricting styles, images,…
- [purpleidea](https://news.ycombinator.com/item?id=49322782) : Yikes! I see this too: \<script type="module" src="https://static.cloudflareinsights.com/beacon.min.js/v4513226..." integrity="sha512-ZE9pZaUXND66v380QUtch/5sE9tPFh2zg45pR2PB0CVkCtOREv2AJKkSidISWkysEuQ0EH8faUU5du78bx87UQ==" data-cf-beacon='{"version":"2024.11.0","token":"c0859b51a7804ab5a9cc8e9e2b2c…
- [kazinator](https://news.ycombinator.com/item?id=49323755) : If you're only using Cloudfare for DNS, but HTTPS connections go directly to your server, how does it inject HTML? You must be allowing Cloudfare to terminate your HTTPS connections; i.e. using them for actual proxying.

---

[Article original](https://news.ycombinator.com/item?id=49322107) · [Discussion HN](https://news.ycombinator.com/item?id=49322107)
