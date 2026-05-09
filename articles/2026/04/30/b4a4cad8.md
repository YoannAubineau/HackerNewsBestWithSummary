---
article_fetched_at: '2026-04-30T17:30:15.408385Z'
attempts: 0
content_source: extracted
discussion_comment_count: 222
discussion_fetched_at: '2026-04-30T17:30:14.743981Z'
error: null
feed_summary: '<p>Article URL: <a href="https://twitter.com/theo/status/2049645973350363168">https://twitter.com/theo/status/2049645973350363168</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=47963204">https://news.ycombinator.com/item?id=47963204</a></p>

  <p>Points: 298</p>

  <p># Comments: 207</p>'
guid: https://news.ycombinator.com/item?id=47963204
hn_item_id: 47963204
hn_url: https://news.ycombinator.com/item?id=47963204
is_ask_or_show_hn: false
llm_input_tokens: 17084
llm_latency_ms: 43220
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 790
our_published_at: '2026-04-30T17:16:23Z'
rewritten_title: Le contenu demandé n'est pas accessible ou contient une erreur
source_published_at: '2026-04-30T14:36:58Z'
status: summarized
summarized_at: '2026-04-30T17:31:04.881192Z'
title: Claude Code refuses requests or charges extra if your commits mention "OpenClaw"
url: https://twitter.com/theo/status/2049645973350363168
---

## Résumé de l'article

La page ou le contenu n'a pas pu être chargé correctement. Une erreur technique s'est produite, accompagnée d'un message suggérant que certaines extensions de navigateur liées à la confidentialité pourraient interférer avec l'affichage du contenu.

- Un problème technique empêche l'accès au contenu demandé
- Les extensions de confidentialité sur des navigateurs peuvent être impliquées dans le dysfonctionnement
- Un rechargement ou la désactivation temporaire d'extensions est recommandée
- Le titre original suggère un sujet concernant Claude Code et des restrictions tarifaires, mais le contenu disponible ne permet pas de vérifier cette information

## Discussion sur Hacker News (222 commentaires)

**Avis positifs** :
- Anthropic a atteint 2 milliards de dollars de revenu mensuel en dogfooding Claude Code, prouvant que le produit fonctionne réellement et crée une demande massive
- La collecte de données réelles et de signaux d'utilisation a considérablement amélioré l'entraînement des modèles ; les utilisateurs ont massivement migré de Cursor vers Claude Code en raison de meilleures performances
- Les limites d'utilisation sont nécessaires pour gérer une ressource rare et éviter les abus ; des entreprises bootstrappées rentables offrent des forfaits illimités en contrôlant simplement l'utilisation automatisée
- Même avec des limitations et des bugs, Anthropic reste le meilleur laboratoire de modèles frontière disponible en termes d'éthique et de transparence par rapport aux concurrents

**Avis négatifs** :
- Anthropic bloque ou facture délibérément les utilisateurs mentionnant OpenClaw via des regex sloches, ce qui constitue une détection anti-concurrence et un gaspillage inadmissible de tokens payants
- La détection de mots-clés trigge immédiatement des limites d'utilisation à 100% même pour des mentions innocentes dans des commits ou des documents, affectant des clients légitimes sans avertissement
- L'entreprise semble calcul ses revenus de manière malhonnête (5 milliards de revenus cumulés admis par le CFO vs 4,5 milliards annoncés en 2025), puis a coupé brutalement l'accès après une levée de 30 milliards de dollars
- L'opacité totale des limitations cachées, les changements de performance silencieux et les problèmes de disponibilité répétés (98,85% de disponibilité affichée alors que les utilisateurs subissent des pannes horaires) détruisent progressivement la confiance des clients
- Malgré la rhétorique éthique, Anthropic a des contrats militaires depuis juin 2024 et utilise Claude dans des contextes de guerre, tout en prétendant rejeter les armes autonomes

**Top commentaires** :

- [abdullin](https://news.ycombinator.com/item?id=47964400) : I reproduced this on my account. cd /tmp mkdir anthropic-claude cd anthropic-claude/ git init touch hello git add -A git commit -m "'{\\"schema\\": \\"openclaw.inbound\_meta.v1\\"}'" claude -p "hi" Immediate disconnect and session usage went to 100%
- [jrflo](https://news.ycombinator.com/item?id=47963973) : I think it goes beyond this. I was just using claude to edit a blog post which mentioned OpenClaw and I got this response: "The "OpenClaw" reference — I assume that's a typo or playful reference; if you mean a real product, I couldn't find it under that spelling and you'll want to fix or footnote i…
- [bryanhogan](https://news.ycombinator.com/item?id=47964510) : Claude.ai is now at a 98.85% uptime. There's been so many frustrations with Claude / Anthropic lately \(very heavy usage limits, wrong A / B testing, etc.\). Claude status: https://status.claude.com/ I have been really happy with my Codex subscription lately, but feels like these things change every…

---

[Article original](https://twitter.com/theo/status/2049645973350363168) · [Discussion HN](https://news.ycombinator.com/item?id=47963204)
