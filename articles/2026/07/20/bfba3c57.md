---
article_fetched_at: '2026-07-20T17:25:30.406535Z'
attempts: 0
content_source: extracted
discussion_comment_count: 214
discussion_fetched_at: '2026-07-20T17:25:21.754469Z'
error: null
guid: https://news.ycombinator.com/item?id=48978112
hn_item_id: 48978112
hn_url: https://news.ycombinator.com/item?id=48978112
is_ask_or_show_hn: false
llm_input_tokens: 25504
llm_latency_ms: 15354
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1143
our_published_at: '2026-07-20T17:18:52Z'
rewritten_title: Défauts de sécurité et problèmes d'ergonomie majeurs d'OpenCode,
  agent IA de codage
source_published_at: '2026-07-20T12:45:55Z'
status: summarized
summarized_at: '2026-07-20T17:27:06.823632Z'
title: Annoying and alarming things about OpenCode
url: https://wren.wtf/shower-thoughts/stop-using-opencode/
---

## Résumé de l'article

OpenCode est un agent IA de codage populaire (161k stars sur GitHub) qui permet aux modèles de langage d'exécuter des commandes bash et d'accéder aux fichiers d'une machine locale. L'auteur détaille de graves failles de sécurité et des défauts de conception qui rendent le logiciel dangereux à utiliser.

- **Défauts d'ergonomie** : Le cache de prompt est invalide à chaque interruption ou changement de mode, les transitions agent-utilisateur génèrent des pauses de 10+ minutes, et l'interface texte consomme 1GB de RAM avec des problèmes de saisie (newlines cassées, scroll pendant la sélection, Ctrl+C ferme la session).
- **Sandbox inefficace** : Le filtrage textuel des commandes bash est contournable par des alias, des variables d'environnement, du base64, des sous-processus Python ou des heredocs ; bloquer git échoue contre 10+ techniques d'évasion.
- **Escalade de permissions** : Une fois qu'on approuve une commande avec "Always", toutes les commandes avec le même préfixe sont approuvées (ex. : approuver `python3` permet la lecture des clés SSH).
- **Validation de chemins cassée** : Les redirections shell (`echo > /sys/class/gpio/export`) ne sont jamais validées ; les paths dans les redirections ne sont pas vérifiées car `echo` n'est pas dans la liste des commandes censées accéder aux fichiers.
- **Télémétrie et configuration dangereuse** : Par défaut, OpenCode se connecte à un serveur distant ; une nouvelle installation ne demande aucune configuration et peut connecter un modèle distant à un shell local ; une CVE antérieure exposait une API non authentifiée pour exécuter des commandes arbitraires avec CORS permissif.

## Discussion sur Hacker News (214 commentaires)

**Avis positifs** :
- Les problèmes de cache et les mutations du prompt système à chaque tour sont réels et créent des pertes significatives d'efficacité, notamment aux passages à minuit ou lors de modifications du fichier AGENTS.md
- OpenCode accumule un nombre massif de problèmes non résolus (3690+ issues ouvertes) avec peu d'acceptation de pull requests externes, reflétant un manque de maintenance active
- Les problèmes de sécurité documentés sont graves : RCE, accès HTTP non sécurisé, permissions insuffisantes, et un positionnement dangereux par défaut sur les modèles cloud plutôt que locaux
- Le système de filtrage textuel des commandes est inefficace et donne une fausse impression de sécurité, contrairement aux véritables primitives de sandbox au niveau du système d'exploitation
- L'approche générale des harnesses d'IA révèle des problèmes structurels : surcharge mémoire/CPU excessive, compaction mal implémentée, et absence de première couche de sandboxing intégrée

**Avis négatifs** :
- Le titre et la tonalité hypercritique sont exagérés : plusieurs critiques portent sur des comportements raisonnables (incorporation immédiate des changements AGENTS.md) ou concernent tous les harnesses IA, pas uniquement OpenCode
- OpenCode reste le harness le plus productif pour beaucoup d'utilisateurs et demeure largement utilisé par les grandes entreprises malgré ses défauts ; les alternatives (Pi, Claude Code, etc.) présentent des problèmes similaires
- Certaines plaintes sont datées ou incorrectes : la compaction et le pruning ont été désactivés par défaut depuis longtemps, et v2 introduit un nouveau système de prompt qui évite les miss de cache
- Les critiques sur Docker et les commandes bash reflètent une incompréhension : le sandboxing doit être une responsabilité externe (VM, flatpak, bubblewrap) plutôt que du harness, et les allowlists visent à guider les modèles, pas à la sécurité
- L'article manque de solutions constructives et d'alternatives crédibles comparables ; il conclut presque à 'ne pas utiliser les LLM' plutôt que de proposer une meilleure approche

**Top commentaires** :

- [LaurensBER](https://news.ycombinator.com/item?id=48978591) : I feel that a better title for this article would be: "Some minor annoyances that, when fixed, would improve OpenCode" \# Prompt Cache Misses \> It globs your filesystem and re-reads AGENTS.md \(injected in turn-0 system prompt\) on every SSE turn. If you put a quick note in AGENTS.md to be read in the…
- [lucideer](https://news.ycombinator.com/item?id=48978907) : This is a good summary of the dangers of using agentic clis, but the title & general focus on opencode is odd for two reasons: 1. Most obviously & importantly this is a complaint without a straightforward suggested alternative. A sibling commenter mentions suggesting fixes to Opencode would be more…
- [chuckadams](https://news.ycombinator.com/item?id=48978566) : « If you don’t know what OpenCode is, imagine a boot stamping on a human face forever. The boot is made of TypeScript and the face is everything we have learned about security and systems software since the invention of the electronic computer in the 1940s. » I nominate this for a Bulwer-Lytton pri…

---

[Article original](https://wren.wtf/shower-thoughts/stop-using-opencode/) · [Discussion HN](https://news.ycombinator.com/item?id=48978112)
