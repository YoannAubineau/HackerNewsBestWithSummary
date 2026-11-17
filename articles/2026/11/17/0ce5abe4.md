---
article_fetched_at: '2026-11-17T04:54:14.503694Z'
attempts: 0
content_source: extracted
discussion_comment_count: 236
discussion_fetched_at: '2026-11-17T04:54:10.064404Z'
error: null
guid: https://news.ycombinator.com/item?id=50524736
hn_item_id: 50524736
hn_url: https://news.ycombinator.com/item?id=50524736
image_url: https://xusheng.dev/posts/windows-coding-agent-telemetry/agent-names.jpeg
is_ask_or_show_hn: false
llm_input_tokens: 21418
llm_latency_ms: 8261
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 972
our_published_at: '2026-11-17T03:59:05Z'
rewritten_title: Windows 11 enregistre les outils de codage et agents d'IA que vous
  utilisez via les données de diagnostic
source_published_at: '2026-11-16T22:58:20Z'
status: summarized
summarized_at: '2026-11-17T04:54:40.746007Z'
title: Windows 11 Is Collecting Data on Which Coding Agents and Developer Tools You
  Use
url: https://xusheng.dev/posts/windows-coding-agent-telemetry/
---

## Résumé de l'article

Windows 11 contient un composant système (MissionControlAggregator.dll) qui détecte et consigne l'utilisation d'agents de codage comme Claude, Codex et Cursor, ainsi que d'outils de développement comme Python, Node.js et GCC. Ces informations sont enregistrées localement et transmises à Microsoft via le service de diagnostic DiagTrack, sauf si vous avez désactivé les données de diagnostic optionnelles.

- Le composant MissionControlAggregator.dll surveille l'exécution de programmes spécifiques en écoutant les événements ETW (Event Tracing for Windows) natifs du système, sans nécessiter une activation manuelle de l'utilisateur.
- Les agents détectés incluent quatre agents CLI (Copilot, Claude, Codex, Agy) et cinq agents de bureau (GitHub, Claude, Codex, Cursor, Antigravity), plus des outils de développement courants comme GCC, Clang et des compilateurs.
- Les données collectées sont converties en bitmaps représentant les catégories d'outils observés et envoyées dans un rapport nommé Segments.SubCohorts, sans capturer les détails de durée d'utilisation ou de contenu.
- Cette collecte de données est classée comme « diagnostic optionnel » et est activée par défaut sur les installations Windows 11 US, ce qui signifie que les rapports sont automatiquement mis en file d'attente pour transmission à Microsoft.
- Les utilisateurs peuvent désactiver cette collecte en accédant à Paramètres → Confidentialité et sécurité → Diagnostic et commentaires et en désactivant les données de diagnostic optionnelles.

## Discussion sur Hacker News (236 commentaires)

**Avis positifs** :
- La collecte de données par Windows 11 sur les outils de développement est une continuation logique de comportements établis depuis Windows 10, donc peu surprenante pour ceux qui suivent
- Microsoft offre des contrôles de confidentialité (désactiver les données de diagnostic optionnelles) et un outil pour consulter les événements collectés, avec une divulgation claire dans l'interface
- Cette collecte peut servir à légitimement identifier les priorités de développement et les besoins en matière de bac à sable pour les agents IA, domaine où Windows a pris du retard
- Les données collectées ne sont envoyées que si l'utilisateur active le partage de diagnostic optionnel, contrairement aux autres OS commerciaux (iOS, Android, macOS) qui tracent activement sans distinction

**Avis négatifs** :
- Windows réactive automatiquement la télémétrie après les mises à jour et les paramètres utilisateur, obligeant à réappliquer les désactivations régulièrement, contrairement aux paramètres de stratégie de groupe qui persistent
- Windows 11 représente une dégradation majeure par rapport aux versions antérieures avec davantage de télémétrie invasive et des changements hostiles à l'utilisateur, ce qui justifie l'indignation alors que les autres OS ont toujours offert moins de liberté
- Microsoft est pire qu'annoncé : Defender continue de tourner en arrière-plan avec une consommation massive de ressources malgré les tentatives de désactivation via paramètres, stratégie de groupe, PowerShell et scripts tiers
- Linux est désormais une alternative viablefonctionnelle en 2026 pour la plupart des cas d'usage (jeux, développement, bureautique) grâce à Proton et aux efforts de Valve, rendant Windows optionnel plutôt que nécessaire

**Top commentaires** :

- [s\_dev](https://news.ycombinator.com/item?id=50525401) : Just as AI has advanced massively in the past two years, I think a lot of gamers would be shocked at how viable Linux is as a genuine gaming platform in 2026. I already have plans to switch from Windows to Linux, I even have Linux running from an external drive to play with it. The vast vast majori…
- [dead\_hn\_theory](https://news.ycombinator.com/item?id=50525754) : For anyone on the fence about switching from Windows to Linux: it takes about a week, if that, of adjusting. If most of what you do is on the Web already \(and the services you use provide a Web-based client\), you have nothing to lose but your chains. Take your pick - Ubuntu, Fedora, someone else me…
- [herf](https://news.ycombinator.com/item?id=50527266) : Windows has been very slow to make a sandbox for AI agents - they launched MXC just a month ago \(Oct 7\) and Claude Code doesn't even support it yet. So we have people running un-sandboxed agents on Windows, or they use WSL instead. All of this to say, yes I hope they have some non-invasive telemetr…

---

[Article original](https://xusheng.dev/posts/windows-coding-agent-telemetry/) · [Discussion HN](https://news.ycombinator.com/item?id=50524736)
