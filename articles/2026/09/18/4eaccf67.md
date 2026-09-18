---
article_fetched_at: '2026-09-18T19:20:16.202433Z'
attempts: 0
content_source: extracted
discussion_comment_count: 71
discussion_fetched_at: '2026-09-18T19:20:14.036216Z'
error: null
guid: https://news.ycombinator.com/item?id=49750094
hn_item_id: 49750094
hn_url: https://news.ycombinator.com/item?id=49750094
is_ask_or_show_hn: false
llm_input_tokens: 18099
llm_latency_ms: 14939
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1215
our_published_at: '2026-09-18T18:25:44Z'
rewritten_title: 'Les défis de l''émulation x86 sur ARM : modèle mémoire TSO et solutions
  matérielles'
source_published_at: '2026-09-18T04:09:48Z'
status: summarized
summarized_at: '2026-09-18T19:20:58.543551Z'
title: The scourge of x86 emulation
url: https://fex-emu.com/Scourge-of-emulation/
---

## Résumé de l'article

FEX est un émulateur x86 pour ARM qui doit reproduire le modèle de mémoire x86-TSO (Total Store Ordering), beaucoup plus strict que le modèle faible d'ARM, ce qui crée des problèmes de performance majeurs dans les applications émulées.

- Le modèle TSO d'x86 garantit une cohérence immédiate des écritures mémoire entre processeurs, tandis qu'ARM permet des optimisations matérielles en utilisant un modèle faible ; FEX compense par des instructions load-acquire et store-release qui ralentissent drastiquement les applications, notamment sur AmpereOne (jusqu'à 85 % de perte de performance).

- Les extensions ARM FEAT_LRCPC (à partir d'ARMv8.3) et FEAT_LSE2 réduisent partiellement le surcoût, mais ne résolvent que les cas alignés ; Apple Silicon et Qualcomm Oryon-3 ajoutent du support matériel natif du TSO, supprimant presque entièrement cette pénalité de performance.

- Les accès mémoire non alignés (split-locks) causent des défauts d'alignement nécessitant des appels kernel-userspace répétés, rendant l'émulation extrêmement lente (~1000× plus lent que x86 natif) ; seul Oryon-3 implémente des « cachelines cohérentes » approchant le comportement x86.

- La mémoire write-combine (uncached) utilisée pour les GPU PCIe devient un goulot d'étranglement insurmontable : les écritures sont jusqu'à 816× plus lentes qu'en natif, rendant certains jeux (Hollow Knight: Silksong, Subnautica 2) injouables à moins d'une FPS ; les systèmes UMA contournent ce problème.

- Une solution matérielle proposée : une instruction CASP 128-bit permettant d'enjamber les frontières de granule atomique tout en restant sûre, ou d'autres extensions futures (FEAT_LRCPC4), sont nécessaires pour progresser davantage.

## Discussion sur Hacker News (71 commentaires)

**Avis positifs** :
- L'émulation x86 sur ARM est une solution pragmatique et générale bénéficiant à l'ensemble de l'industrie, contrairement à une approche bytecode propriétaire à Valve
- Apple a démontré qu'ajouter le mode TSO à ses puces ARM permet de résoudre efficacement les problèmes de cohérence mémoire, malgré quelques cas limites
- Forcer une recompilation bytecode serait irréaliste : le catalogue de Steam contient des milliers de jeux dont le code source est perdu ou inaccessible, avec des propriétés intellectuelles complexes
- L'intégration verticale d'Apple (conception propre des CPU) lui permet des optimisations matérielles impossibles pour Linux qui doit supporter n'importe quel matériel
- Des projets comme FEX montrent que l'émulation x86 vers ARM a atteint un niveau de maturité remarquable, viable même pour des appareils mobiles avec une autonomie améliorée

**Avis négatifs** :
- Le modèle mémoire TSO strict de x86 impose des coûts matériels significatifs (buffers de write, latences) que ARM relaxé n'a pas, mais les bénéfices de performance réels du modèle relaxé sont débattus et potentiellement faibles (étude récente montrerait ~3%)
- L'émulation x86 reste intrinsèquement plus lente que la compilation native, tandis qu'une approche bytecode with compilation JIT à l'installation (comme Android) pourrait théoriquement offrir de meilleures performances pour les nouveaux titres
- Les différences architecturales fondamentales entre x86 et ARM (instructions de longueur variable vs fixe, nombre de registres, memory ordering) créent des défis d'émulation incontournables avec des compromis de performance
- Mandater une approche bytecode pourrait apparaître comme anticonccurrentiel et créer un risque de procès antitrust, même si le bénéfice serait réel à long terme
- Certains coins sombres de TSO (atomiques avec LOCK prefix) ne sont toujours pas traités par le mode TSO d'Apple, montrant les limites même des solutions matérielles les plus sophistiquées

**Top commentaires** :

- [pdw](https://news.ycombinator.com/item?id=49751784) : The intro of this article repeats the common assertion that \> ARM is the most relaxed, allowing significant hardware optimizations; and x86 is the most strict, enforcing a very strong coherency model that doesn’t allow a lot of room for optimization but I've seen some compelling arguments that a re…
- [dagmx](https://news.ycombinator.com/item?id=49750760) : For reference , Fex is a translation framework for x86 to ARM much like Apple’s Rosetta2 and Microsoft’s Prism. Valve sponsor development as it’s also the way the new Steam Frame supports x86 games. It’s also being used \(as a fork\) in Crossover Beta to replace the use of Rosetta2.
- [asksomeoneelse](https://news.ycombinator.com/item?id=49751314) : Great article ! This is the kind of content I always hope to find on HN's front page. I really wonder how things are organized at Apple to allow for vertical integration to work so well. That feature alone must have involved so many people from so many different teams.

---

[Article original](https://fex-emu.com/Scourge-of-emulation/) · [Discussion HN](https://news.ycombinator.com/item?id=49750094)
