---
article_fetched_at: '2026-06-18T18:45:56.753510Z'
attempts: 0
content_source: extracted
discussion_comment_count: 169
discussion_fetched_at: '2026-06-18T18:45:46.284280Z'
error: null
guid: https://news.ycombinator.com/item?id=48584135
hn_item_id: 48584135
hn_url: https://news.ycombinator.com/item?id=48584135
is_ask_or_show_hn: false
llm_input_tokens: 21011
llm_latency_ms: 13145
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 994
our_published_at: '2026-06-18T18:23:26Z'
rewritten_title: Les nouvelles fonctionnalités d'Emacs 31 testées en utilisation quotidienne
source_published_at: '2026-06-18T12:10:53Z'
status: summarized
summarized_at: '2026-06-18T18:46:35.873661Z'
title: 'Emacs 31 is around the corner: The changes I''m daily driving'
url: https://www.rahuljuliato.com/posts/emacs-31-around-the-corner
---

## Résumé de l'article

Emacs 31, le prochain numéro majeur de l'éditeur, introduit plusieurs améliorations que l'auteur teste depuis plusieurs mois en version développement. L'article détaille les changements qu'il utilise actuellement et juge suffisamment utiles pour intégrer sa configuration sans paquets externes.

- **Tree-sitter simplifié** : les grammaires se configurent automatiquement et s'installent sur demande, éliminant les étapes manuelles complexes précédentes, bien que les binaires compilés ne soient pas isolés par architecture sur les systèmes multi-plateformes
- **Mode Markdown natif (expérimental)** : nouveau `markdown-ts-mode` avec navigation à la manière d'Org, coloration de blocs de code avec leurs vrais modes syntaxiques, et aperçu d'images intégrées au texte
- **Améliorations de l'édition** : buffers xref maintenant éditables inline comme grep et Dired, completion minibuffer plus réactive avec `completion-eager-update`, nouvelle commande `kill-region-dwim` qui supprime un mot au lieu d'erreur quand pas de sélection active
- **Interface et qualité** : Speedbar en fenêtre latérale au lieu de cadre flottant, nouvelles commandes de rétagement de fenêtres (transpose, rotate, flip), terminal `term` corrigé qui ne supprime plus de lignes lors du redessin
- **Thèmes Modus natifs** : huit variantes de thèmes Modus inclus directement, avec optimisations pour la deutéranopie et tritanopie

## Discussion sur Hacker News (169 commentaires)

**Avis positifs** :
- Emacs connaît une revitalisation avec tree-sitter et LSP, rendant les nouvelles versions excitantes après une période creuse
- Les améliorations d'Emacs 31 (auto-installation des grammaires, layouts de fenêtres, xref éditable) répondent à des demandes longtemps restées sans réponse
- L'intégration avec les assistants IA (Claude, Codex) rend Emacs plus accessible en permettant la configuration et customisation en langage naturel
- Emacs reste superior pour l'affichage de grandes portions de code sur écran et offre une flexibilité incomparable comparée aux IDEs modernes
- La communauté Emacs perdure et s'améliore avec des packages comme Vertico, Consult, Embark et une meilleure expérience terminal (Ghostel)

**Avis négatifs** :
- La courbe d'apprentissage reste élevée et l'idée de configuration 'out-of-the-box' heurtée par la philosophie de customisation, rendant Emacs difficile à recommander aux nouveaux utilisateurs
- Les solutions préexistantes comme Doom Emacs et Spacemacs ne règlent pas vraiment le problème car elles s'éloignent trop d'Emacs vanilla ou changent fondamentalement les keybindings
- Utiliser les LLMs pour générer sa configuration crée des init.el incompréhensibles et non maintenables à long terme, perdant l'avantage d'une customisation consciente
- Les performances restent problématiques sur Windows et au démarrage (45 secondes sur macOS), et certaines intégrations (TRAMP distant, terminal) traînent toujours de la latence
- L'obsession de la configuration personnalisée contraste avec une réalité où de nombreux utilisateurs abandonnent après VSCode/autres éditeurs, suggérant qu'Emacs rattrape plutôt qu'innove réellement

**Top commentaires** :

- [antics9](https://news.ycombinator.com/item?id=48589590) : « kill-region-dwim fixes a decades-old papercut. Set it to 'emacs-word and hitting C-w with no active region kills a word backwards instead of signalling an error. » Thank you! No more: \(defun cutregion-or-killword \(beginning end\) "Kills region if marked else backward kills word." \(interactive "r"\)…
- [mesrik](https://news.ycombinator.com/item?id=48586285) : "Is anyone still using emacs?" Yes, 34 years and no plans to switch. Emacs cursor movement keystrokes are quite widely supported elsewhere too which use GNU readline or implement at least subset themselves. Those work well also besides shells with Chromium/Chrome/Safari etc. many browsers input fie…
- [jerf](https://news.ycombinator.com/item?id=48584824) : "Is anyone still using emacs?" Yes. I had to briefly visit the world of VSCode during a period of time when it had better AI integration than emacs did, but since I got Claude working well inside of emacs I've returned to 100% emacs. There just isn't anything like the old editors, built in the 80x2…

---

[Article original](https://www.rahuljuliato.com/posts/emacs-31-around-the-corner) · [Discussion HN](https://news.ycombinator.com/item?id=48584135)
