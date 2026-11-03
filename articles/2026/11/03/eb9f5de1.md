---
article_fetched_at: '2026-11-03T18:52:32.618188Z'
attempts: 0
content_source: extracted
discussion_comment_count: 116
discussion_fetched_at: '2026-11-03T18:51:41.466524Z'
error: null
guid: https://news.ycombinator.com/item?id=50354960
hn_item_id: 50354960
hn_url: https://news.ycombinator.com/item?id=50354960
is_ask_or_show_hn: false
llm_input_tokens: 9610
llm_latency_ms: 7864
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 951
our_published_at: '2026-11-03T18:30:35Z'
rewritten_title: Postman installe automatiquement des plugins d'IA et tente de modifier
  les configurations d'autres agents
source_published_at: '2026-11-03T17:22:37Z'
status: summarized
summarized_at: '2026-11-03T18:53:58.835752Z'
title: Postman silently auto-installs AI plugins and attempts to share all API data
url: https://github.com/postmanlabs/postman-app-support/issues/14370
---

## Résumé de l'article

Postman, un client API populaire, a automatiquement installé des plugins (Codex, Claude Code) et des hooks de démarrage sans consentement explicite, modifiant les configurations globales d'autres outils comme Codex et Claude sur macOS. L'installateur a également tenté d'approuver lui-même ses propres hooks de confiance et d'activer une connexion MCP distante vers des serveurs Postman.

- L'ouverture de Postman 12.33.4 a déclenché une installation automatique de plugins via un processus « auto-existing-upgrade » enregistré dans les logs de l'application, sans interaction utilisateur explicite
- Des fichiers de configuration globaux (~/.codex/config.toml, ~/.claude/settings.json) ont été modifiés pour ajouter des plugins Postman et marquer des hooks comme approuvés via des hachages de confiance
- Un hook de démarrage a été installé qui force les tâches d'ingénierie API à charger les compétences Postman, dépassant largement une utilisation explicite de Postman par l'utilisateur
- L'installateur a exécuté du code côté client pour approuver ses propres hooks de sécurité (approvePostmanHook) plutôt que de laisser l'utilisateur décider dans chaque application hôte
- Une connexion MCP distante vers https://mcp.postman.com/mcp a été activée mais échoue avec une erreur d'authentification, indiquant une tentative de connexion à des serveurs Postman sans consentement explicite

## Discussion sur Hacker News (116 commentaires)

**Avis positifs** :
- L'installation silencieuse de plugins IA et le partage non autorisé de données API confirment le pattern d'enshittification de Postman après son financement massif (400M$ de capital-risque pour un simple client HTTP).
- Plusieurs alternatives meilleures existent désormais (Bruno, Insomnia anciennes versions, Yaak, Kreya) et offrent une expérience locale, sans compte obligatoire, avec stockage git.
- Le problème illustre un phénomène systémique : les outils VC-financés doivent justifier leur valorisation en forçant logins, collecte de données et monétisation, au détriment de l'expérience utilisateur.
- Bruno et alternatives similaires maintiennent une approche minimaliste (git-first, offline-first, sans cloud) proche de ce que curl offre, sans la complexité ajoutée.

**Avis négatifs** :
- Certains défendent la nécessité de monétiser : les ingénieurs méritent d'être payés, et une interface graphique a une valeur légitime par rapport à curl brut, même si la question de comment capter cette valeur reste ouverte.
- Même les alternatives (Bruno, Insomnia, Yaak) affichent des pages de pricing ou freemium, suggérant qu'aucune solution n'est immunisée contre une future enshittification, créant un cycle perpétuel de migration.
- Postman reste populaire dans certains contextes (freelancers, développeurs moins à l'aise avec CLI) et conserve une part de marché B2B substantielle malgré les critiques HN, questionnant l'urgence perçue du problème.
- Certains commentaires suggèrent que les outils deviennent obsolètes face aux agents IA et curl, repoussant le problème plutôt que de le résoudre vraiment.

**Top commentaires** :

- [pants2](https://news.ycombinator.com/item?id=50355299) : It's a shame what happened to Postman. It started as an excellent little developer tool for testing APIs. Then for some reason they raised over $400M in funding and hired 1,500+ employees, for what should have been a tiny OSS/passion project like curl or little snitch. Instead they now have to just…
- [senfiaj](https://news.ycombinator.com/item?id=50355878) : Who still uses Postman? In my experience it became insanely slow and bloated. Switched to Bruno. IMO, Postman is like uTorrent, everybody heard about it and many install because of inertia.
- [bottombutton](https://news.ycombinator.com/item?id=50356050) : Working in healthcare, and Postman got decertified by our Cyber team for this. We all switched to Bruno overnight. Their sales team is pinging us like gangbusters though.

---

[Article original](https://github.com/postmanlabs/postman-app-support/issues/14370) · [Discussion HN](https://news.ycombinator.com/item?id=50354960)
