---
article_fetched_at: '2026-10-09T19:56:41.981965Z'
attempts: 0
content_source: extracted
discussion_comment_count: 139
discussion_fetched_at: '2026-10-09T19:56:09.883988Z'
error: null
guid: https://news.ycombinator.com/item?id=50018817
hn_item_id: 50018817
hn_url: https://news.ycombinator.com/item?id=50018817
image_url: https://opengraph.githubassets.com/a145a46d1f54ca74dfe0cf12be50a8757694ccae8f28f1b0fb754456854f101f/franzenzenhofer/big-arrow-on-the-screen
is_ask_or_show_hn: false
llm_input_tokens: 13048
llm_latency_ms: 13961
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 946
our_published_at: '2026-10-09T19:43:47Z'
rewritten_title: bigarrow, un outil macOS pour que les agents IA pointent les éléments
  à l'écran avec des flèches
source_published_at: '2026-10-09T11:03:48Z'
status: summarized
summarized_at: '2026-10-09T19:59:44.048244Z'
title: 'Show HN: Let your AI agents paint big arrows, boxes and text on your screen'
url: https://github.com/franzenzenhofer/big-arrow-on-the-screen
---

## Résumé de l'article

bigarrow est un outil en ligne de commande pour macOS qui dessine des flèches, des boîtes et du texte sur l'écran pour guider les utilisateurs vers des éléments spécifiques. Il fonctionne comme une compétence pour Claude Code et les agents IA, permettant à ces derniers de pointer des boutons ou des contrôles au lieu de simplement imprimer des instructions textuelles dans un terminal invisible.

- Dessine une couche transparente au-dessus de toutes les fenêtres sur tous les écrans et espaces virtuels ; les clics et le focus clavier passent à travers, sauf sur la flèche elle-même qui s'efface quand on clique dessus
- Propose de nombreuses options visuelles (formes : bend, straight, zigzag, spiral ; styles : arrow, ring, box ; tailles S/M/L ; couleurs configurables ; bordures variées)
- Cible les éléments par label, par coordonnées, par fenêtre/onglet, ou par ID Peekaboo ; peut aussi afficher le texte à l'écran et lire le texte à haute voix
- Résout le problème des agents IA qui ne peuvent pas appuyer sur des boutons nécessitant une interaction humaine (permissions, 2FA, CAPTCHAs, décisions) ou qui doivent montrer à un utilisateur comment effectuer une action
- Écrit en Swift pur, sans daemon ni télémétrie, sous licence MIT ; compte 360 étoiles GitHub en deux jours auprès de développeurs d'entreprises tech et d'instituts de recherche

## Discussion sur Hacker News (139 commentaires)

**Avis positifs** :
- Outil potentiellement utile pour le guidage d'utilisateurs non-techniques (parents âgés, novices) à travers des interfaces complexes sans prise de contrôle à distance
- Applications légitimes en didactique : apprentissage de logiciels complexes (Blender, FreeCAD) où la complexité est inhérente et justifiée
- Cas d'usage intéressant pour les tutoriels et la documentation, remplaçant les screenshots statiques par du guidage visuel interactif
- Potentiel pour l'accessibilité et les personnes handicapées, comparable aux tutoriels embarqués des anciens PC
- Approche créative rendue possible par les IA : ce type de projet n'aurait probablement jamais été construit auparavant

**Avis négatifs** :
- Symptôme d'une UX défaillante : si une IA doit pointer les boutons, c'est que l'interface elle-même devrait être mieux conçue
- Préoccupations éthiques : risque d'utilisation pour manipuler les personnes âgées ou malveillantes (scams), contournement des dialogues de confirmation
- Inefficacité énergétique et coûteuse : utiliser un datacenter distant pour dessiner des flèches au lieu de résoudre le problème à la source
- Qualité d'exécution médiocre : les flèches du prototype sont mal alignées, les textes générés sont peu clairs, absence d'effort réel au-delà de la génération automatique
- Risque de déresponsabilisation : les utilisateurs ne comprennent plus ce qu'ils font, juste où cliquer, renforçant une dépendance à l'IA pour des tâches banales

**Top commentaires** :

- [sicktriple](https://news.ycombinator.com/item?id=50022929) : Man, just when it seemed like we had it all. Computers were cheap, efficient and powerful. Somehow we figured out a way to accomplish tasks we already had solved except now it's 1000x more expensive, requires the combined electricity of the entire world, is reliant on someone else's rented compute,…
- [hn8726](https://news.ycombinator.com/item?id=50019459) : I tried to read the "Does it need Screen Recording or Accessibility?" part, but it's slopped to the point I have no clue what it's trying to say. But if it can draw on top of permission prompts, what's stopping it from drawing box that hides the "decline" button and changing the "approve" button co…
- [tangotaylor](https://news.ycombinator.com/item?id=50021210) : "It is an arrow, so we spent an unreasonable amount of time on how it looks." Brilliant. This is exactly the kind of content I seek when I visit Hacker News. Truly art.

---

[Article original](https://github.com/franzenzenhofer/big-arrow-on-the-screen) · [Discussion HN](https://news.ycombinator.com/item?id=50018817)
