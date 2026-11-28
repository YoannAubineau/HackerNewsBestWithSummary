---
article_fetched_at: '2026-11-28T02:24:45.965431Z'
attempts: 0
content_source: extracted
discussion_comment_count: 103
discussion_fetched_at: '2026-11-28T02:24:38.573135Z'
error: null
guid: https://news.ycombinator.com/item?id=50655868
hn_item_id: 50655868
hn_url: https://news.ycombinator.com/item?id=50655868
image_url: https://themouseless.dev/images/book_cover_mouseless_2_300.jpg
is_ask_or_show_hn: false
llm_input_tokens: 11043
llm_latency_ms: 8081
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 910
our_published_at: '2026-11-28T01:57:46Z'
rewritten_title: Un développeur publie un manuel complet pour apprendre Vim avec 170
  exercices pratiques
source_published_at: '2026-11-26T14:44:22Z'
status: summarized
summarized_at: '2026-11-28T02:26:58.906198Z'
title: 'Show HN: I wrote an entire Vim manual over 4 years'
url: http://themouseless.dev/vim/
---

## Résumé de l'article

Matthieu, un développeur français, a rédigé sur 4 ans un manuel d'apprentissage de Vim, l'éditeur de texte en ligne de commande. Le livre propose une progression pédagogique structurée avec de nombreux exercices pour maîtriser cet outil performant et personnalisable.

- Le manuel contient au moins 170 exercices pratiques conçus pour construire progressivement les compétences et la mémoire musculaire, avec chaque chapitre s'appuyant sur les précédents.
- L'ouvrage se concentre sur des applications réelles et pratiques de Vim, complété par une section de référence en annexe, sans détails inutiles ou sans rapport.
- Vim est présenté comme un éditeur gratuit, léger et stable, permettant de travailler au clavier uniquement pour gagner en productivité et en fluidité de travail sans avoir à basculer vers la souris.
- Le livre vise à démystifier la courbe d'apprentissage de Vim, affirmant que les bases peuvent s'acquérir en quelques heures si l'on accepte qu'il fonctionne différemment des IDE conventionnels.
- L'auteur garantit que même les utilisateurs de Vim expérimentés découvriront des techniques utiles, avec possibilité de remboursement sinon.

## Discussion sur Hacker News (103 commentaires)

**Avis positifs** :
- Rédaction humaine de qualité avec intention pédagogique claire, contrastant favorablement avec le contenu généré par IA, souvent dense et verbeux
- Effort substantiel et durable (4+ ans, 1244 heures) démontre un engagement authentique ; ressource pédagogique précieuse face au manque de matériel d'enseignement humain
- Approche riche en exemples pratiques et exercices corrigés, dépassant les capacités du vimtutor ou de la documentation officielle
- Vim reste un outil flexible et puissant ; les bases s'apprennent rapidement mais les fonctionnalités avancées (macros, registres, quickfix, scripting) justifient l'approfondissement
- Accessibilité via échantillon gratuit de 74 pages permet aux lecteurs de vérifier la qualité avant achat

**Avis négatifs** :
- Un manuel de 21 chapitres pour un éditeur de texte soulève des questions sur la complexité architecturale inhérente à Vim lui-même
- hjkl comme schéma de navigation par défaut manque d'optimalité ergonomique et reste justifié par tradition plutôt que par ingénierie réfléchie, limitant l'adoption par les nouveaux utilisateurs
- Vim souffre de limitations techniques notables (ralentissements avec les longues lignes dus au moteur de coloration syntaxique regex), rendant certains flux de travail impratiques
- Absence de source texte brute/lisible dans Vim directement ; format PDF/ePub uniquement réduit l'intégration avec l'écosystème shell préconisé par l'auteur
- Contenu sur Neovim volontairement limité en raison de cibles mouvantes, réduisant la pertinence pour les utilisateurs modernes adoptant Neovim plutôt que Vim classique

**Top commentaires** :

- [giladd](https://news.ycombinator.com/item?id=50663937) : This is very cool and approachable, thank you. For anyone who suspects use of LLMs - just read some of the book. The language captured my attention in a manner no model is capable of.
- [aktenlage](https://news.ycombinator.com/item?id=50659031) : Nice work. Luckily I think I don't need it anymore after using vim for 20+ years. As a motivation for new vim users, I'd like to mention that LLMs make it even more awesome to use such a malleable editor. When I think of some functionality I need, I'll just let Copilot write a small function and ke…
- [NoboruWataya](https://news.ycombinator.com/item?id=50667950) : It's great to see a non-LLM manual like this, well done :\) Personally I use Helix whenever I need a decent terminal-based editor \(though most of my coding is done in a JetBrains IDE\). I found neovim's plugin ecosystem great in theory but fragile in practice - it seems whenever I install a load of p…

---

[Article original](http://themouseless.dev/vim/) · [Discussion HN](https://news.ycombinator.com/item?id=50655868)
