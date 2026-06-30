---
article_fetched_at: '2026-06-29T13:24:38.446941Z'
attempts: 0
content_source: extracted
discussion_comment_count: 136
discussion_fetched_at: '2026-06-29T13:24:37.775621Z'
error: null
guid: https://news.ycombinator.com/item?id=48706714
hn_item_id: 48706714
hn_url: https://news.ycombinator.com/item?id=48706714
is_ask_or_show_hn: false
llm_input_tokens: 12711
llm_latency_ms: 8946
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 846
our_published_at: '2026-06-29T12:50:55Z'
rewritten_title: Demande de mécanisme pour exclure les fichiers sensibles dans OpenAI
  Codex
source_published_at: '2026-06-28T12:27:33Z'
status: summarized
summarized_at: '2026-06-29T13:25:12.545645Z'
title: A way to exclude sensitive files issue still open for OpenAI Codex
url: https://github.com/openai/codex/issues/2847
---

## Résumé de l'article

Un utilisateur demande l'ajout d'une fonctionnalité permettant d'exclure explicitement les fichiers sensibles de l'accès par l'agent OpenAI Codex. OpenAI Codex est un modèle de code d'IA capable de générer ou analyser du code à partir de fichiers du projet.

- Proposition d'un système de fichier d'exclusion (.codexignore) au niveau du dépôt et global, similaire à .gitignore, permettant de bloquer l'accès à des dossiers/fichiers sensibles comme .env, .pem, les clés AWS ou SSH
- Le mécanisme conserverait la capacité de recherche dans node_modules/ à titre d'exemple, mais empêcherait la lecture et l'envoi de fichiers sensibles au modèle
- La configuration doit être déterministe, partageable entre les membres de l'équipe et supporter les paramètres utilisateur personnalisés
- La demande fait suite à une issue antérieure (#205) qui avait été fermée en faveur d'une implémentation Rust (codex-rs), mais la fonctionnalité comparable n'existe pas encore dans codex-rs en août 2025
- L'auteur se propose de contribuer à l'implémentation et aux tests

## Discussion sur Hacker News (136 commentaires)

**Avis positifs** :
- Un standard .agentignore similaire à .gitignore serait utile comme signal au modèle sur les fichiers à ignorer, même s'il ne garantit pas une sécurité totale
- Les solutions de sandboxing existantes (conteneurs, permissions Unix, namespaces Linux, bwrap) sont techniquement viables et bien connues pour résoudre ce problème
- L'adoption d'une architecture opt-in (accès explicite aux fichiers) plutôt qu'opt-out améliorerait la sécurité par défaut dans les workflows d'agents
- Les harnesses peuvent ajouter une couche de redaction entre les outils et l'LLM pour masquer les données sensibles dans les résultats avant qu'elles ne soient envoyées au modèle

**Avis négatifs** :
- Les agents LLM sont imprévisibles et peuvent contourner des restrictions (exécution de commandes shell alternatives, scripts d'exploitation) rendant une blocklist inefficace
- Une feature .agentignore donnerait une fausse sensation de sécurité alors que la vraie protection nécessite une isolation au niveau du système d'exploitation (permissions, conteneurs, VMs)
- Le problème est mal positionné : c'est à l'utilisateur et au système d'exploitation de garantir l'isolation, pas à Codex; les données sensibles ne devraient jamais être accessibles au processus
- Les agents ont besoin d'accéder aux secrets pour exécuter du code en développement, ce qui rend impossible de bloquer complètement l'accès tout en restant fonctionnel
- OpenAI n'a pas d'incitation commerciale à implémenter cette feature puisque les données collectées augmentent la valeur du produit

**Top commentaires** :

- [TheDong](https://news.ycombinator.com/item?id=48706893) : You can do this now: change the file permissions such that the user you run codex as can't read them, or run codex in a container without those files mounted. If you don't do that, the agent will be able to incidentally upload them. What if the model runs "rg foo", and one of those files contains t…
- [datsci\_est\_2015](https://news.ycombinator.com/item?id=48718849) : The fact that pretty much every comment in this thread suggests a different solution means there’s still plenty of innovation and consolidation to occur on this problem. My take is that Unix already solved all of these user access problems \(what can a user read or execute\), so the solution will pro…
- [petcat](https://news.ycombinator.com/item?id=48706943) : Hopefully they never actually implement this pointless feature because it will only give people a false sense of security given the unpredictable nature of LLMs. How could something like this even be enforced? People just need to learn how to use the tools their system already provides them. i.e.,…

---

[Article original](https://github.com/openai/codex/issues/2847) · [Discussion HN](https://news.ycombinator.com/item?id=48706714)
