---
article_fetched_at: '2026-08-13T04:01:47.683459Z'
attempts: 0
content_source: extracted
discussion_comment_count: 40
discussion_fetched_at: '2026-08-13T04:01:46.727892Z'
error: null
guid: https://news.ycombinator.com/item?id=49270040
hn_item_id: 49270040
hn_url: https://news.ycombinator.com/item?id=49270040
image_url: https://woxi.ad-si.com/images/social-preview.png
is_ask_or_show_hn: false
llm_input_tokens: 5185
llm_latency_ms: 11587
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 849
our_published_at: '2026-08-13T03:23:26Z'
rewritten_title: Woxi, une réimplémentation open-source du langage Wolfram
source_published_at: '2026-08-12T10:06:29Z'
status: summarized
summarized_at: '2026-08-13T04:02:23.010007Z'
title: 'Show HN: Woxi - Open-source Mathematica / Wolfram Language reimplementation'
url: https://woxi.ad-si.com
---

## Résumé de l'article

Woxi est une réimplémentation open-source du langage Mathematica/Wolfram, un système de calcul symbolique et numérique. Le projet est distribué sous forme de noyau Jupyter, accessible à la fois localement et via une instance JupyterLite directement dans le navigateur.

- Fonctionne comme noyau Jupyter, intégrable dans l'environnement Jupyter classique
- Installation locale possible via la commande `woxi install-kernel`
- Expérience de notebook complète disponible en ligne via JupyterLite, sans installation requise

## Discussion sur Hacker News (40 commentaires)

**Avis positifs** :
- Le projet a progressé massivement avec 7 000+ commits et une couverture jusqu'à Mathematica version 6.0, rendant une réimplémentation sérieuse et utilisable pour ceux qui ne peuvent se permettre la licence propriétaire.
- Woxi offre une intégration cohérente et un langage bien conçu après 30 ans de développement Mathematica, consolidant efficacement ce qui serait autrement des centaines de bibliothèques Python/Julia mal intégrées entre elles.
- L'implémentation en Rust permet des performances compétitives en calcul symbolique, surpassant notablement SymPy et offrant une alternative viable à Sage pour les utilisateurs frustrés par sa fragmentation.
- Le projet démocratise l'accès à un outil de calcul scientifique de qualité, libérant les utilisateurs du modèle d'abonnement propriétaire et préservant l'accès à des codebases Wolfram Language existantes.
- Les réimplementations open-source de technologies matures ne sont pas vaines : elles facilitent l'intégration dans de nouveaux workflows et posent des questions valides sur les modèles commerciaux restrictifs.

**Avis négatifs** :
- L'interface de studio actuelle manque de capacités de typesetting mathématique interactif et de notation visuelle, réduisant la lisibilité des notebooks comparée à Mathematica et limitant l'adoption pour ceux habitués à des entrées mathématiques richement formatées.
- Des bugs de compatibilité subsistent ($VersionNumber retourne une chaîne au lieu d'un nombre, $InputFileName incorrect lors de imports), et des fonctionnalités clés manquent (Parallel functions, WSTP, MathLink).
- Réimplémenter Mathematica perpétue une approche conservative en open-source plutôt que d'explorer des paradigmes radicalement nouveaux ; même les créateurs reconnaissent l'intérêt d'une syntaxe/interface alternative future.
- Les performances restent inégales sur les fonctions non optimisées et les cas complexes, avec des préoccupations légitimes sur les brevets et droits d'auteur concernant les réimplementations d'API propriétaires.
- Des fonctionnalités scientifiques importantes manquent (EDP, systèmes de contrôle, approximations physiques) et la capacité à exécuter des notebooks Mathematica existants dépend de la couverture d'une fraction inconnue du code utilisateur.

**Top commentaires** :

- [peterus](https://news.ycombinator.com/item?id=49273294) : I get the reasons for not supporting out of order execution and the % variable, it makes for more readable and usable notebooks. Unfortunately most of the time I use Mathematica it is not to make a readable and repeatable notebook but just to help with uni work, so I do take shortcuts like putting…
- [xvilka](https://news.ycombinator.com/item?id=49275017) : Wish you luck. Hope one day instead of Sage that is a bunch of Python glue for completely different and disjointed systems like Maxima, SymPy, Octave, GAP, PARI/GP, etc we will get a one well-integrated \(and blazingly fast because written in Rust\). I am a big supporter of open-source but after stru…
- [ethanc8](https://news.ycombinator.com/item?id=49275219) : I tried out the multivariable calculus visualizations from https://nmd.web.illinois.edu/classes/2024/241/schedule.html \(search for "visualization"\) and Woxi Studio seems to be able to display them. I'm not sure if it's entirely correct \(there might be a few bugs\) since I don't have Mathematica curr…

---

[Article original](https://woxi.ad-si.com) · [Discussion HN](https://news.ycombinator.com/item?id=49270040)
