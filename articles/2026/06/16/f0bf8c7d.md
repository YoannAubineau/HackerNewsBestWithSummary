---
article_fetched_at: '2026-06-16T11:46:01.491949Z'
attempts: 0
content_source: extracted
discussion_comment_count: 97
discussion_fetched_at: '2026-06-16T11:46:00.243465Z'
error: null
guid: https://news.ycombinator.com/item?id=48550693
hn_item_id: 48550693
hn_url: https://news.ycombinator.com/item?id=48550693
image_url: https://devblogs.microsoft.com/oldnewthing/wp-content/uploads/sites/38/2019/02/ShowCover.jpg
is_ask_or_show_hn: false
llm_input_tokens: 8408
llm_latency_ms: 10724
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 975
our_published_at: '2026-06-16T10:55:11Z'
rewritten_title: Comment l'équipe d'émulation x86 a détecté et corrigé un code catastrophiquement
  mal optimisé
source_published_at: '2026-06-16T04:46:36Z'
status: summarized
summarized_at: '2026-06-16T11:46:55.854034Z'
title: The time the x86 emulator team found code so bad they fixed it during emulation
url: https://devblogs.microsoft.com/oldnewthing/20260615-00/?p=112419
---

## Résumé de l'article

Un émulateur x86-32 Windows utilisait la traduction binaire pour convertir le code x86 en code natif. L'équipe a découvert qu'un programme contenait une fonction extrêmement mal optimisée qui utilisait 256 KB de code pour initialiser seulement 64 KB de données en mémoire.

- Le compilateur d'origine avait déroulé complètement une boucle d'initialisation en 65 536 instructions individuelles d'écriture (4 bytes chacune) au lieu de générer une boucle compacte
- Face à cette inefficacité flagrante, l'équipe d'émulation a ajouté du code spécial au traducteur pour détecter cette fonction défectueuse
- Lors de la détection, le traducteur remplaçait automatiquement le code hypertrophié par une boucle serrée équivalente, récupérant ainsi les performances perdues

## Discussion sur Hacker News (97 commentaires)

**Avis positifs** :
- Les couches de compatibilité (Proton, Wine) et les pilotes GPU contiennent systématiquement des correctifs pour contourner les bugs des logiciels mal codés, ce qui permet de rendre accessibles des programmes défaillants sans attendre une correction des développeurs.
- Cette approche s'est avérée nécessaire historiquement : Windows 95 a dû corriger SimCity, les pilotes GPU détectent les jeux par nom d'exécutable pour appliquer des optimisations spécifiques, démontrant que les contournements sont préférables à laisser les utilisateurs avec des logiciels inutilisables.
- Les pilotes et émulateurs découvrent souvent des inefficacités graves (boucles non déroulées, appels système répétés) qui ralentissent considérablement les programmes, ce que seule une intervention externe peut résoudre rapidement.
- Les architectes matériels et les équipes de compatibilité ont historiquement voyagé directement auprès des développeurs pour les sensibiliser aux problèmes, confirmant que les workarounds externalisés peuvent être acceptables quand la communication directe échoue.

**Avis négatifs** :
- Cette approche de correction en couche externe est fragile et insoutenable : elle crée une spirale où chaque mise à jour de pilote ou de couche de compatibilité peut casser les contournements existants ou créer des comportements imprévisibles d'autres programmes.
- Détecter les programmes par nom d'exécutable pour appliquer des optimisations est un anti-pattern : renommer l'exécutable peut causer des crashes ou dégradations de performance inattendues, et cela brise l'abstraction que devraient maintenir les pilotes.
- Ces workarounds risquent de prolonger la durée de vie des bugs des développeurs : si les contournements fonctionnent, pourquoi les développeurs fixeraient-ils le problème ? Cela crée une perverse incitation à ne pas corriger le code source.
- Les optimisations appliquées pour un jeu (par ex. Half-Life 2) peuvent ralentir d'autres applications : le pilote ignore l'abstraction du contrat API en faveur de heuristiques fragiles spécifiques à chaque programme détecté.
- À l'époque des années 80-90, certains compilateurs supportaient des flags aberrants (comme « dérouler tous les boucles sans limite ») qui ont produit des binaires pathologiques, suggérant que le problème était autant du côté de la chaîne de compilation qu'une véritable mauvaise programmation.

**Top commentaires** :

- [psanchez](https://news.ycombinator.com/item?id=48551299) : This reminds me of a story from 15 years ago, where I was developing a technology to download games on demand by hooking into the OS calls. There was a particular game that was superslow when this tech was applied. Original game loading took around 15-20 seconds, whereas once the tech was applied i…
- [dlcarrier](https://news.ycombinator.com/item?id=48551052) : SimCity had a read-after-free bug that Microsoft patched in Windows 95. That was a lot easier for customers than having Maxis fix it, which could have required exchanging copies of the game.
- [hodgehog11](https://news.ycombinator.com/item?id=48550898) : I think we're starting to see more of this sort of thing happening now with Proton and Wine gaining prominence in the Linux community. Some games \(Elden Ring comes to mind\) have bad enough PC ports when they come out that the compatibility layer can incorporate a hotfix to improve performance, whil…

---

[Article original](https://devblogs.microsoft.com/oldnewthing/20260615-00/?p=112419) · [Discussion HN](https://news.ycombinator.com/item?id=48550693)
