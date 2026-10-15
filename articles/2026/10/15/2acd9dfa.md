---
article_fetched_at: '2026-10-15T01:07:38.274693Z'
attempts: 0
content_source: extracted
discussion_comment_count: 116
discussion_fetched_at: '2026-10-15T01:07:35.419139Z'
error: null
guid: https://news.ycombinator.com/item?id=50094994
hn_item_id: 50094994
hn_url: https://news.ycombinator.com/item?id=50094994
image_url: https://anoma.ly/notes/og/opencode-2-0.png
is_ask_or_show_hn: false
llm_input_tokens: 9084
llm_latency_ms: 13533
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 984
our_published_at: '2026-10-15T00:44:33Z'
rewritten_title: OpenCode 2.0 introduit une architecture serveur centralisée et une
  nouvelle API
source_published_at: '2026-10-14T20:48:24Z'
status: summarized
summarized_at: '2026-10-15T01:07:59.211450Z'
title: OpenCode 2.0
url: https://anoma.ly/notes/opencode-2-0/
---

## Résumé de l'article

OpenCode 2.0 est une refonte majeure d'un agent de codage qui s'appuie sur les retours de millions d'utilisateurs quotidiens. La plateforme est passée d'un modèle client/serveur optionnel à un service de fond automatique, et propose une API repensée ainsi que de nouvelles capacités d'orchestration.

- Un service background unique centralise désormais tous les clients (TUI, web, desktop, CLI, SDK) qui communiquent avec un même processus central sur la machine
- L'API a été entièrement reconstruite à partir de zéro pour supporter les cas d'usage réels observés chez les millions d'utilisateurs et permet à l'agent d'appeler ses propres fonctionnalités
- Le mode Code embarque un interpréteur JavaScript minimal qui convertit les serveurs MCP et endpoints OpenAPI en fonctions appelables, réduisant les appels réseau et le contexte consommé
- Les tâches de fond permettent au modèle de lancer des sous-agents ou des commandes shell asynchrones en parallèle sans bloquer l'agent principal
- Le système de plugin a été renforcé avec 80+ plugins internes, hot-reload automatique et promotion des plugins TUI au statut stable ; OpenCode peut maintenant être utilisé comme bibliothèque SDK

## Discussion sur Hacker News (116 commentaires)

**Avis positifs** :
- OpenCode 2.0 apporte des améliorations significatives : rechargement automatique des skills/plugins, meilleure architecture, modèle client/serveur puissant, système de plugins flexibles et capacité à backgrounder les tâches.
- Le modèle serveur/client distribué permet de lancer des sessions sur des machines distantes et d'utiliser le daemon natif, ce que concurrents comme Claude Code ne proposent pas aussi bien.
- Le projet a un bon rapport qualité-prix avec OpenCode Go ($10/mois avec quotas généreux), une excellente affaire comparée aux autres services d'accès aux modèles.
- Les développeurs sont réactifs aux bugs : plusieurs contributeurs rapportent avoir fait merger des PRs et résoudre des issues rapidement cette semaine.
- L'interface web/desktop distingue OpenCode : c'est la seule solution open-source testée offrant une interface hors TUI, plus adaptée aux interactions basées sur du texte long.

**Avis négatifs** :
- Régressions de sécurité majeures en v2 : le chargement de configuration était cassé, les plugins hot-reloadables permettent à un agent de modifier l'environnement immédiatement, les outils contournent désormais le sandbox utilisé en v1.
- Consommation de mémoire excessive et ralentissements : le site est très lourd (WebGL intensif), l'installateur curl|sh prenait 6 minutes pour 10% de progression, plusieurs utilisateurs signalent des blocages et blocages de navigateur.
- Gestion des issues chaotique : 3200+ issues GitHub ouvertes, triage défaillant, manque de CI/CD moderne, regressions fréquentes expédiées, absence de bots d'organisation, processus de support Discord peu fiable avec réponses ignorées.
- Problèmes de tarification et facturation : écarts entre les tarifs publiés et les frais réels (ex: GPT Luna 2x plus cher), clients oubliés après signalement de bug sur Discord, manque de transparence et suivi.
- Regressions d'expérience utilisateur : disparition de la disposition ancienne, interface moins intuitive qu'avant, des annoyances de v1 persistent (modèle qui reste bloqué, pas de timeout par défaut pour les permissions).

**Top commentaires** :

- [denysvitali](https://news.ycombinator.com/item?id=50095874) : Their installer \(curl | sh\) was taking so long yesterday for me. It turns out it's incredibly slow... because of the progress bar rendering. This is insane. The installer took 6 minutes to reach 10%: curl -fsSL https://opencode.ai/v2/install | bash Managed to fix it by running this instead: curl -f…
- [hi\_hi](https://news.ycombinator.com/item?id=50097645) : Took me a little while to figure out this was a llm harness for coding \(also called an agent, I suppose, but that term seems overloaded and ambiguous to me\) There are many of these available, alongside the provider ones. Are there any benchmarks which help me decide which ones I should try over the…
- [solarkraft](https://news.ycombinator.com/item?id=50096138) : It's good. Many of the annoyances from V1 are gone. Skills and plugins reload automatically \(finally\). Tasks can be backgrounded \(though I think this doesn't happen automatically yet\). There's a built-in skill for editing the configuration \(finally I can retire mine\). The front-end got some love. A…

---

[Article original](https://anoma.ly/notes/opencode-2-0/) · [Discussion HN](https://news.ycombinator.com/item?id=50094994)
