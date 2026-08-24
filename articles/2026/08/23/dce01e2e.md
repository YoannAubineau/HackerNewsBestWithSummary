---
article_fetched_at: '2026-08-24T20:19:43.322193Z'
attempts: 0
content_source: extracted
discussion_comment_count: 14
discussion_fetched_at: '2026-08-24T20:19:24.935942Z'
error: null
guid: https://news.ycombinator.com/item?id=49409092
hn_item_id: 49409092
hn_url: https://news.ycombinator.com/item?id=49409092
image_url: https://earendil.com/static/og/posts/what-is-a-harness.png
is_ask_or_show_hn: false
llm_input_tokens: 4667
llm_latency_ms: 10429
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 952
our_published_at: '2026-08-23T19:24:24Z'
rewritten_title: Qu'est-ce qu'un agent harness et comment fonctionne-t-il
source_published_at: '2026-08-23T14:24:21Z'
status: summarized
summarized_at: '2026-08-24T20:20:07.402805Z'
title: What Is a Harness?
url: https://earendil.com/posts/what-is-a-harness/
---

## Résumé de l'article

Un agent harness est un logiciel qui fournit un environnement d'exécution pour les modèles d'IA, permettant aux utilisateurs d'interagir avec ces modèles via différentes interfaces (terminal, email, chat, etc.). Contrairement aux modèles d'IA eux-mêmes, les harnesses peuvent être possédés et adaptés par les utilisateurs finaux, offrant une plus grande autonomie et flexibilité.

- Un harness comprend quatre composants clés : un système de prompts pour guider le comportement du modèle, un ensemble d'outils accessibles à l'IA (recherche web, exécution de code, composition d'email), une boucle agentique qui permet au modèle de décider lui-même quand utiliser ces outils et de les réappliquer si nécessaire, et une couche de traduction qui rend le harness compatible avec différents modèles d'IA.

- La boucle agentique fonctionne en permettant au modèle d'évaluer ses propres résultats et de décider de réappliquer les outils si nécessaire, créant ainsi une boucle de rétroaction jusqu'à ce que le modèle estime la tâche terminée.

- Les harnesses open source et neutres comme Pi, OpenClaw et OpenCode distribuent le contrôle aux utilisateurs finaux en leur permettant de choisir les modèles d'IA qu'ils souhaitent utiliser et de modifier les harnesses selon leurs besoins.

- La couche de traduction est cruciale car elle transfère le pouvoir des laboratoires d'IA vers les utilisateurs finaux, permettant à chacun de posséder, exécuter localement et adapter ses propres outils d'IA.

## Discussion sur Hacker News (14 commentaires)

**Avis positifs** :
- Les harnesses représentent une frontière technologique majeure, l'équivalent des « électroniques » pour les LLMs, avec un potentiel énorme pour créer des outils spécialisés (trading, factories logicielles, etc.)
- Les modèles frontière excellents peuvent raisonner efficacement sans instructions prescriptives détaillées ; il suffit de fournir des outils et des garde-fous plutôt que des workflows rigides
- Une interface CLI interne bien conçue est hautement précieuse pour les agents, offrant flexibilité et utilité tout en rendant la construction agréable
- L'approche des harnesses ouvre un domaine d'ingénierie intéressant et stimulant après une décennie de développement CRUD standard
- L'article est clair, pertinent et accessible, utile pour expliquer le concept aux non-experts

**Avis négatifs** :
- « Harness » est simplement un terme marketing hype 2026 pour rebaptiser des applications alimentées par LLM ; certaines choses commercialisées comme des agents sont juste du bon vieux code déterministe
- Il est difficile de construire des harnesses générales si les modèles ont été entraînés sur une architecture harness spécifique, ce qui crée une rigidité architecturale
- Les modèles plus récents rendent certains systèmes de prompts complexes obsolètes, suggérant que l'approche harness pourrait elle aussi devenir rapidement surannée
- Les harnesses existantes présentent des lacunes significatives en matière de « handoff » (passage entre CLI/web, équipes, modalités de communication, modèles/fournisseurs)

**Top commentaires** :

- [Syntaf](https://news.ycombinator.com/item?id=49410048) : I’ve been working on a harness for accounting agents at my job recently and it’s been a pretty interesting experience. We originally started with building a CLI tool so our LLMs could more easily interact with our platform. I cannot recommend enough the value of having an internal CLI. It’s both fu…
- [xrd](https://news.ycombinator.com/item?id=49410304) : Does anyone have a suggestion for a harness that is good at handoff? When I say handoff, I mean: \* handoff from a terminal CLI to webui \(on a phone\)? \* handoff from one team member, to another? \* handoff from one communication modality, like writing a prompt in a TUI, to email? \* handoff from one m…
- [theturtletalks](https://news.ycombinator.com/item?id=49409371) : Harnesses are the next frontier. If LLMs are electricity, harnesses are the “electronics.” Right now, it’s like an AC vs DC between Claude and ChatGPT, but once that settles, the harnesses will be the actual value providers. And Pi is the best harness because of the amazing extension system. You ca…

---

[Article original](https://earendil.com/posts/what-is-a-harness/) · [Discussion HN](https://news.ycombinator.com/item?id=49409092)
