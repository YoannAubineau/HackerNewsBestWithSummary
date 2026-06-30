---
article_fetched_at: '2026-06-27T22:21:36.412551Z'
attempts: 0
content_source: extracted
discussion_comment_count: 108
discussion_fetched_at: '2026-06-27T22:21:35.549110Z'
error: null
guid: https://news.ycombinator.com/item?id=48688700
hn_item_id: 48688700
hn_url: https://news.ycombinator.com/item?id=48688700
image_url: https://opengraph.githubassets.com/e28c610ba0111a0f99986ef4dabb13cad76bd356854986df16855dcde4c091cc/workweave/router
is_ask_or_show_hn: false
llm_input_tokens: 10598
llm_latency_ms: 14393
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1150
our_published_at: '2026-06-27T22:03:11Z'
rewritten_title: Routeur de modèles IA intelligent compatible Claude, Codex et Cursor
  via proxy local
source_published_at: '2026-06-26T16:40:11Z'
status: summarized
summarized_at: '2026-06-27T22:21:57.205347Z'
title: 'Show HN: Smart model routing directly in Claude, Codex and Cursor'
url: https://github.com/workweave/router
---

## Résumé de l'article

Weave Router est un proxy qui dirige automatiquement chaque requête vers le meilleur modèle d'IA disponible parmi Anthropic, OpenAI, Gemini et modèles open source, en utilisant un classificateur embarqué plutôt qu'une sélection aléatoire. Il s'installe comme service local (localhost:8080) ou se configure en quelques commandes auprès des éditeurs de code Claude Code, Codex et Cursor.

- Le routeur sélectionne le meilleur modèle à chaque requête via un scorer dérivé de recherches sur l'optimisation performance-coût (Avengers-Pro)
- Compatible avec les APIs d'Anthropic, OpenAI et Gemini, supporte le streaming, les outils et la vision ; accède aussi à DeepSeek, Qwen, Llama via OpenRouter
- Installation simple : `npx @workweave/router` pour les outils Claude, Codex ou opencode ; `make full-setup` pour un déploiement local autonome avec Postgres
- Les clés API restent locales et chiffrées ; traces OTLP intégrées, visualisables dans le tableau de bord Weave ou des outils tiers (Honeycomb, Datadog, Grafana)
- Activation/désactivation sans perte de configuration via commandes NPM ou slash commands intégrés aux éditeurs ; Cursor en version bêta précoce

## Discussion sur Hacker News (108 commentaires)

**Avis positifs** :
- L'approche est cache-aware : contrairement aux routeurs stateless existants, elle considère le coût des cache misses lors du changement de modèle, ce qui évite les pertes financières qu'induisent les routeurs naïfs.
- Les résultats concrets sont prometteurs : l'équipe reporte 40% d'économies sur ses propres usages et amélioration de la vélocité sans dégradation de qualité, mesurée via leurs métriques d'productivité.
- Pertinent pour les workflows agentic avec sous-agents : chaque sous-agent bénéficie d'une fenêtre de contexte fraîche, réduisant les interdépendances de cache et offrant plus de flexibilité de routage.
- Utilise les prix subsidisés des abonnements : le routeur exploite les tarifs réduits Claude/Copilot quand disponibles et bascule sur l'API seulement en cas de besoin, optimisant le coût réel.
- Entrainé sur des traces réelles d'agents : le modèle de routage a été forcé à utiliser différents modèles et intègre des garde-fous pour éviter que les petits modèles échouent, avec escalade vers des modèles plus puissants.

**Avis négatifs** :
- La décision de routage repose sur une détermination de complexité généralement indécidable : pour des problèmes ambigus (refactorisation, décisions contextuelles), le routeur ne peut pas anticiper correctement et doit gérer les erreurs de classification a posteriori.
- Les modèles agentic existants routent déjà intelligemment les tâches selon leur nature (planning aux modèles lourds, exploration aux flash) : ajouter une couche proxy casse cette boucle de contrôle et rétroaction interne, notamment pour les tentatives échouées qui doivent re-router.
- Risque de staleness du modèle d'IA : entrainé sur quelques milliers d'exemples internes, le routeur ne verra jamais la majorité des prompts réels et devra se réadapter chaque semaine avec les nouvelles versions de modèles sans accès aux données utilisateurs.
- Le gain diminue avec l'augmentation du nombre de modèles routés : au-delà de 2-3 modèles, les cache misses cumulées peuvent annuler les économies, réduisant l'utilité à un très petit nombre de choix (planner vs exécutant).
- Les petits modèles open-source restent moins fiables que les frontières pour le coding : bien que bon marché (DeepSeek), ils ont tendance à s'arrêter prématurément, générer des erreurs et boucles infinies, ce qui complique l'automatisation du routage sans risque.

---

[Article original](https://github.com/workweave/router) · [Discussion HN](https://news.ycombinator.com/item?id=48688700)
