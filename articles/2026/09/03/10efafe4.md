---
article_fetched_at: '2026-09-03T07:31:59.131996Z'
attempts: 0
content_source: extracted
discussion_comment_count: 206
discussion_fetched_at: '2026-09-03T07:31:56.746592Z'
error: null
guid: https://news.ycombinator.com/item?id=49524863
hn_item_id: 49524863
hn_url: https://news.ycombinator.com/item?id=49524863
image_url: https://dbushell.com/images/articles/2026-09-01-text-editor.png
is_ask_or_show_hn: false
llm_input_tokens: 20283
llm_latency_ms: 10915
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 913
our_published_at: '2026-09-03T07:09:31Z'
rewritten_title: 'Construire un éditeur de texte web : comparaison de trois approches
  techniques'
source_published_at: '2026-09-01T17:12:15Z'
status: summarized
summarized_at: '2026-09-03T07:32:36.051821Z'
title: Fine, I'll build my own text editor
url: https://dbushell.com/2026/09/01/text-editor/
---

## Résumé de l'article

Un développeur explore trois méthodes pour créer un éditeur de texte dans le navigateur : le rendu sur canvas, l'élément contenteditable et textarea. Chaque approche offre des compromis entre contrôle visuel et accessibilité, performance et facilité d'implémentation.

- **Canvas** : offre un contrôle maximal mais nécessite de tout implémenter manuellement (sélection, undo/redo, scrolling) et pose des problèmes d'accessibilité insurmontables
- **Contenteditable plaintext-only** : déverrouille gratuitement la sélection native, l'historique undo et l'accessibilité du navigateur, mais souffre de ralentissements imprévisibles au-delà d'un certain nombre de caractères, particulièrement sur Chromium
- **Textarea** : bien plus performant pour les textes longs et permet un rendu syntaxique en couches sans impact majeur sur les performances
- L'auteur choisit textarea comme base viable, notant que la plupart des fonctionnalités peuvent être ajoutées progressivement
- Points techniques : désactiver spellcheck pour éviter les pics de latence, gérer correctement les graphèmes Unicode plutôt que les unités de code UTF-16

## Discussion sur Hacker News (206 commentaires)

**Avis positifs** :
- Sublime Text reste un excellent éditeur performant pour les gros fichiers, contrairement aux alternatives modernes qui consomment beaucoup plus de ressources mémoire
- La construction d'un éditeur personnel est une excellente opportunité d'apprentissage sur le rendu, l'interaction utilisateur et les détails techniques souvent invisibles
- Les éditeurs web comme VS Code offrent une expérience utilisateur cohérente multiplateforme avec de bonnes valeurs par défaut et un écosystème d'extensions riche
- L'approche contenteditable est finalement plus robuste que canvas pour les éditeurs texte web, car le navigateur gère déjà l'accessibilité et les quirks
- Les développeurs devraient construire sur des bases existantes (Emacs, Vim, KTextEditor) plutôt que de recommencer zéro, ce qui économise du temps et capitalise sur l'existant

**Avis négatifs** :
- La plateforme web est fondamentalement limitée pour les éditeurs texte : pas d'API OS adéquate, contraintes de rendu HTML/browser, difficultés d'intégration système
- Presque tous les éditeurs modernes souffrent d'une latence visible lors de la saisie et de modifications, même sur de petits fichiers, ce qui révèle une régression depuis les éditeurs des années 80
- Construire un vrai éditeur texte avec fonctionnalités comme l'autocomplétion, la coloration syntaxe et LSP devient rapidement aussi volumineux que les éditeurs qu'on cherche à remplacer
- VS Code et les éditeurs basés sur JS/Electron consomment beaucoup trop de mémoire (1-2GB) comparé à des alternatives légères (200-300MB pour Sublime) pour les mêmes fichiers
- Le web n'est pas le bon choix pour un éditeur : complexité inutile des technologies web, problèmes de synchronisation asynchrone, pas besoin de capacités navigateur pour éditer du texte

**Top commentaires** :

- [tzs](https://news.ycombinator.com/item?id=49532312) : Sometime around 1980-81 I had a part time job while an undergraduate in college doing system programming/admin for the Caltech High Energy Physics department. Rob Pike was the system programmer/admin before me when he was a grad student in high energy physics, but he left to go work at Bell Labs. O…
- [akersten](https://news.ycombinator.com/item?id=49532213) : Yes, who would have guessed that the \<textarea\> element, designed specifically for this use case and built into browsers for 3 decades, would be the most performant and behaviorally consistent way to implement editable text. I'm kind of sad the author stopped shedding unneeded complexity there thou…
- [kqp](https://news.ycombinator.com/item?id=49536438) : Seems to me that in the short term everybody screams “DO NOT OPTIMIZE THAT CODE”, in the medium term everybody shrugs “buy a new computer”, and in the long term everybody gradually migrates to the solutions that optimized that code. I think the mainstream narrative around performance optimization i…

---

[Article original](https://dbushell.com/2026/09/01/text-editor/) · [Discussion HN](https://news.ycombinator.com/item?id=49524863)
