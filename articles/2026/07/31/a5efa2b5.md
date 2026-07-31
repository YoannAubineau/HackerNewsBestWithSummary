---
article_fetched_at: '2026-07-31T05:37:34.631836Z'
attempts: 0
content_source: extracted
discussion_comment_count: 92
discussion_fetched_at: '2026-07-31T05:37:32.805906Z'
error: null
guid: https://news.ycombinator.com/item?id=49114639
hn_item_id: 49114639
hn_url: https://news.ycombinator.com/item?id=49114639
image_url: https://opengraph.githubassets.com/38c146a053d3f0b7d16ae66ccbea994f1961e426c08c3e9b9146438a46b83bc1/AminBlg/SimpleEnglish
is_ask_or_show_hn: false
llm_input_tokens: 8674
llm_latency_ms: 12323
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 946
our_published_at: '2026-07-31T05:32:33Z'
rewritten_title: Agent skill qui force la rédaction technique en anglais simplifié
  ASD-STE100
source_published_at: '2026-07-30T19:34:27Z'
status: summarized
summarized_at: '2026-07-31T05:37:53.862581Z'
title: Agent Skill to Force Docs in ASD-STE100 Simplified Technical English
url: https://github.com/AminBlg/SimpleEnglish
---

## Résumé de l'article

Un agent skill impose aux modèles de langage de rédiger la documentation technique en ASD-STE100, la langue contrôlée utilisée par l'aérospatiale depuis 1983 pour éviter les malentendus. Le skill fonctionne dans tous les environnements compatibles Agent Skills (Claude Code, Cursor, VS Code Copilot, OpenAI Codex, Gemini CLI, etc.) et s'installe sans dépendances.

- Les tests mesurent une réduction de 72,9 % des violations STE par 100 mots en moyenne sur 6 modèles Claude (96 exécutions).
- La longueur moyenne des phrases baisse de 11,2 à 9,7 mots et le nombre de tokens produits diminue sur tous les modèles testés.
- Le skill s'adapte à plusieurs formats : messages d'erreur, runbooks, rapports d'incidents, notes de version et instructions système.
- Installation simple via `npx skills add` pour les environnements supportés, ou collage du prompt système pour ChatGPT, Gemini et autres chatbots.
- Basé sur 53 règles numérotées de la norme ASD-STE100 (version 2025), conçu pour produire une documentation plate et sans ambiguïté plutôt que robotique.

## Discussion sur Hacker News (92 commentaires)

**Avis positifs** :
- ASD-STE100 produit effectivement une documentation plus lisible et moins verbale que les sorties LLM par défaut, améliorant l'expérience utilisateur.
- La méthode fonctionne bien en pratique : des utilisateurs rapportent des résultats visiblement moins « slop » et moins de jargon marketing lorsqu'elle est appliquée.
- Le standard réunit une communauté active explorant des solutions au problème croissant d'obscurité et de verbosité dans la génération LLM, avec plusieurs approches complémentaires (skills, prompts, linters).
- La clarté pour les non-anglophones et les lecteurs fatigués est bénéfique : une documentation précise limite les malentendus critiques et les erreurs d'interprétation.
- C'est un bon moyen de partager et packager des instructions réutilisables, même si une simple ligne de prompt suffit techniquement.

**Avis négatifs** :
- Le skill est du surremploi pour ce qui fonctionne mieux en une seule ligne de prompt ; les modèles oublient facilement les instructions et « dérivent » hors du style imposé.
- Le README du projet lui-même viole les règles ASD-STE100, ce qui sape la crédibilité et révèle probablement une génération LLM derrière le projet.
- Forcer ce style en phase d'instruction pourrait dégrader la capacité de raisonnement du modèle ou sa qualité de réflexion (chaîne de pensée), pas seulement la sortie.
- L'exemple « Test B is an alternative to test A » montre que le standard lui-même est ambigu pour les non-natifs censés en bénéficier ; les cas de mauvaise application (ajout de détails internes ou promesses non autorisées) sont troublants.
- Trend viral sans substance réelle : beaucoup de posts redondants et peu d'effort observable ; les méthodes existantes (style Orwell, prompts simples, linters dédiés comme Vale) accomplissent souvent mieux le même objectif.

**Top commentaires** :

- [Planktonne](https://news.ycombinator.com/item?id=49116735) : This is cruft \[1\]. No one who is capable of using this needs it--it's a line in the prompt at most. \[1\] https://knowyourmeme.com/memes/thinking-quickly-dave-constru...
- [dan\_sbl](https://news.ycombinator.com/item?id=49116416) : I took one of the examples \("Leveraging sqlpipe's robust..."\) and just prefixed it with this: \> Rewrite this using ASD-STE100 simplified technical English: And you get a good-enough result, it seems? Maybe add another sentence or two for guidance, but what's with needing these giant skills, when AS…
- [tajd](https://news.ycombinator.com/item?id=49116177) : On a related note I wrote a skill to apply the economist style guide to LLM generated writing https://github.com/TAJD/economist-style-guide-plugin Tends to produce relatively well structured prose that’s easy to edit.

---

[Article original](https://github.com/AminBlg/SimpleEnglish) · [Discussion HN](https://news.ycombinator.com/item?id=49114639)
