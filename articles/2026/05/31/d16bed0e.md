---
article_fetched_at: '2026-05-31T18:22:42.937482Z'
attempts: 0
content_source: extracted
discussion_comment_count: 69
discussion_fetched_at: '2026-05-31T18:22:38.506794Z'
error: null
guid: https://news.ycombinator.com/item?id=48327809
hn_item_id: 48327809
hn_url: https://news.ycombinator.com/item?id=48327809
image_url: https://pierre.computer/pierre-co-diffs-og.png
is_ask_or_show_hn: false
llm_input_tokens: 14246
llm_latency_ms: 13784
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1123
our_published_at: '2026-05-31T17:47:18Z'
rewritten_title: Pierre Computer Company publie CodeView, un composant de virtualisation
  pour rendre efficacement les diffs de code à grande échelle
source_published_at: '2026-05-29T19:04:54Z'
status: summarized
summarized_at: '2026-05-31T18:23:19.135931Z'
title: On Rendering Diffs
url: https://pierre.computer/writing/on-rendering-diffs
---

## Résumé de l'article

Pierre Computer Company a lancé CodeView, un composant React de virtualisation spécialisé dans l'affichage des diffs de code, capable de rendre efficacement des modifications de code de taille arbitraire dans un navigateur. L'article détaille les défis techniques rencontrés lors du rendu de larges revues de code et les solutions architecturales développées pour les résoudre.

- **Technique Inverse Sticky** : une approche novatrice qui combine le défilement natif du navigateur avec une virtualisation sans scintillement, maintenant le contenu rendu collé aux bords de la fenêtre d'affichage si JavaScript ne peut pas suivre la vitesse de défilement
- **Optimisations de mise en page** : utilisation d'estimations rapides (hauteur × nombre de lignes), recherche binaire avec points de contrôle, et ancrage de défilement personnalisé pour maintenir la stabilité et éviter les calculs répétitifs
- **Réduction mémoire** : détachement des chaînes analysées du fichier patch source original (réduisant l'utilisation mémoire de 2,4 GB à 1,15 GB sur le diff Linux v6↔v7), mise en pool des éléments DOM, et partage d'état de configuration entre tous les fichiers
- **Mise en évidence syntaxique différée** : déplacement du traitement Shiki dans des workers threads avec cache LRU pour éviter de bloquer le thread principal lors du rendu de nombreux fichiers
- **Limites restantes** : coûts CSS et paint importants lors d'un défilement agressif, sérialisation onéreuse de la mise en évidence pour les très longs fichiers, et virtualisation limitée au-delà du scrolling horizontal et des lignes extrêmement longues

## Discussion sur Hacker News (69 commentaires)

**Avis positifs** :
- L'approche d'optimisation du rendu des diffs est techniquement impressionnante et résout un vrai problème de performance en navigateur, particulièrement pour les très gros fichiers (jusqu'à 36 millions de lignes)
- L'investissement dans l'optimisation de l'expérience utilisateur est justifié : même sans examiner 100k lignes, pouvoir naviguer rapidement dans des diffs complexes (snapshots de tests, branches de longue durée) réduit la friction pour les développeurs
- L'approche générale de virtualisation intelligente et l'Inverse Sticky Technique permettent d'obtenir un défilement fluide à 120Hz sans intervention JavaScript constant, ce qui n'était pas trivial à résoudre
- La qualité de l'écriture technique et la clarté de l'explication rendent accessible un sujet complexe ; l'article mérite d'être partagé comme référence pour l'optimisation frontend
- Le travail sur les diffs sémantiques futurs répond à des demandes légitimes pour améliorer la compréhension des changements au-delà du simple diff textuel

**Avis négatifs** :
- L'accent sur la performance des très gros diffs est un exercice académique ('un meme') ; en pratique, les vrais problèmes concernent les diffs intelligents (AST diffing, détection des mouvements de code) plutôt que le rendu brut
- La complexité introduite par la virtualisation du DOM crée des bugs et casse des optimisations navigateur natives ; il faudrait plutôt investir dans l'amélioration des moteurs de rendu eux-mêmes
- L'expérience sur mobile reste mauvaise (stuttering, sentiment de 'JS hacking scrolling') malgré les optimisations annoncées ; la comparaison avec CodeMirror montre que d'autres solutions gèrent mieux cet aspect
- Les navigateurs modernes devraient pouvoir nativement rendre de grandes pages sans ces contournements complexes ; virtualiser le DOM plutôt que d'améliorer le navigateur fragmente la solution
- La recherche navigateur (Ctrl+F) et les annotations dynamiques restent problématiques avec cette approche ; l'absence de solution élégante pour la recherche sur 36M de lignes laisse subsister une limitation majeure

**Top commentaires** :

- [cipherself](https://news.ycombinator.com/item?id=48328362) : For anyone else who's suffering, paste this in the console in devtools: document.getElementsByTagName\('main'\)\[0\].style.margin = '0 auto';
- [gloria\_mundi](https://news.ycombinator.com/item?id=48331441) : I don't understand the point of the inverse sticky technique. Scrolling too fast still breaks the experience \(content refuses to scroll\), and in a way that, at least to me, feels more disruptive than blanking for a fraction of a second. I might just be too used to blanking. Also ... shouldn't brows…
- [darkamaul](https://news.ycombinator.com/item?id=48329497) : What an interesting article. I did not assume I would read it until the end when I opened it, but the writing was super clear and easy to follow. At the end, I admire the craft and patience to try to solve code diff rendering, and wish the folks at GitHub could put the same effort to improve their…

---

[Article original](https://pierre.computer/writing/on-rendering-diffs) · [Discussion HN](https://news.ycombinator.com/item?id=48327809)
