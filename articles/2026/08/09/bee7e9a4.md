---
article_fetched_at: '2026-08-09T14:25:29.656249Z'
attempts: 0
content_source: extracted
discussion_comment_count: 115
discussion_fetched_at: '2026-08-09T14:25:27.050490Z'
error: null
guid: https://news.ycombinator.com/item?id=49226923
hn_item_id: 49226923
hn_url: https://news.ycombinator.com/item?id=49226923
image_url: https://os8088.com/img/og.png
is_ask_or_show_hn: false
llm_input_tokens: 10935
llm_latency_ms: 14198
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1092
our_published_at: '2026-08-09T14:14:56Z'
rewritten_title: os8088, un système d'exploitation graphique de style Macintosh pour
  IBM PC/XT en 256K de RAM
source_published_at: '2026-08-08T23:37:27Z'
status: summarized
summarized_at: '2026-08-09T14:26:10.470486Z'
title: 'Os8088: A powerful Mac-like OS for the IBM XT, 286, 386'
url: https://os8088.com/
---

## Résumé de l'article

os8088 est un système d'exploitation graphique hobbyiste écrit en assembleur pour les ordinateurs Intel 8086/8088 (IBM PC/XT), bootable depuis une disquette. Il offre une interface de bureau similaire au Macintosh System 1 avec fenêtres superposées, menus déroulants et multitâche préemptif -- une fonctionnalité que le Macintosh d'origine en 1984 n'avait pas.

- Noyau de 78 950 octets fonctionnant en mode réel, tenant entièrement dans 256K de RAM
- Interface graphique avec fenêtres redimensionnables, menus déroulants, dock inférieur et support de la souris série
- Support de trois modes d'affichage : VGA 16 couleurs (640x480), Hercules mono (720x348), CGA mono (640x200)
- Multitâche préemptif jusqu'à 12 tâches, sans DOS ni ligne de commande
- Restauration historique d'une idée de GEM (1985) que le PC a brièvement eu avant qu'Apple ne force l'abandon des fenêtres superposées ; le code source en NASM assembleur est disponible sur GitHub

## Discussion sur Hacker News (115 commentaires)

**Avis positifs** :
- Démonstration impressionnante des capacités de Claude en assembleur réel-mode : le code ressemble à du travail humain plutôt qu'à de la compilation, sans bloat évident et avec des opportunités d'optimisation non évidentes à première vue.
- Réalisation concrète d'un concept historique intéressant : multitâche préemptif, interface graphique et support d'applications sur du matériel ancien (XT/286) avec seulement 256 KB de RAM, testée sur du vrai matériel.
- Outil pédagogique valuable : permet d'apprendre les techniques d'optimisation utilisées par les anciens systèmes d'exploitation (Lisa, MacOS, Windows, GEOS) et de comprendre les contraintes du segmentage mémoire 8086.
- Transformation du développement amateur : les outils LLM permettent désormais à un hobbyiste de réaliser en quelques jours ce qui aurait pris des mois ou années, ouvrant des portes auparavant fermées.
- Précédents historiques : rappelle que des projets comme GeoWorks ou Visi On ont tenté des interfaces graphiques innovantes sur PC, montrant ce qui aurait pu être possible à l'époque.

**Avis négatifs** :
- Problème de transparence et de présentation : le projet a initialement revendiqué du code « entièrement écrit à la main » alors qu'il était généré par Claude, ce qui a alimenté la méfiance et des critiques sur l'honnêteté intellectuelle.
- Perte de la profondeur pédagogique et du processus créatif : les longs processus de débogage et d'itération sont essentiels à la compréhension approfondie ; déléguer cela à l'IA signifie perdre cette expérience formative, même si le résultat fonctionne.
- Absence de protection mémoire et vulnérabilité : tout programme peut réécrire les gestionnaires d'interruption, ce qui rend le système facile à casser comparé aux systèmes modernes, bien que cela soit normal pour l'époque.
- Qualité du code optimisable : analyse détaillée révèle plusieurs opportunités d'optimisation non exploitées (push/pop inutiles, utilisation de registres inefficace), suggérant que le code IA n'égale pas réellement le travail d'un assembleur humain expérimenté.
- Manque de documentation et de communication humaine : même l'auteur reconnaît que la page d'accueil et le README semblent générés par IA, ce qui décourage les lecteurs de prendre le projet au sérieux et suggère un manque d'engagement personnel du créateur.

**Top commentaires** :

- [adrianmonk](https://news.ycombinator.com/item?id=49228286) : « The graphical operating system that could have been for the IBM XT » Visi On\[1\] was a graphical operating system for the IBM PC that actually existed as a commercial product, though definitely not a very successful one. It was made by VisiCorp, the same company that created VisiCalc \(the first sp…
- [Narishma](https://news.ycombinator.com/item?id=49227524) : « Hand-written real-mode 8086. No C, no linker, no runtime library. » More like hand-prompted...
- [LeoPanthera](https://news.ycombinator.com/item?id=49227720) : It's funny how virtually everyone on HN is using AI to write code and simultaneously dismisses all interesting new software as written by AI.

---

[Article original](https://os8088.com/) · [Discussion HN](https://news.ycombinator.com/item?id=49226923)
