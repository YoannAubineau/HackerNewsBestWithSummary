---
article_fetched_at: '2026-05-22T20:32:10.838758Z'
attempts: 0
content_source: extracted
discussion_comment_count: 118
discussion_fetched_at: '2026-05-22T20:32:09.936831Z'
error: null
guid: https://news.ycombinator.com/item?id=48234090
hn_item_id: 48234090
hn_url: https://news.ycombinator.com/item?id=48234090
image_url: https://modelrift.com/og/blog/openscad-llm-benchmark.png
is_ask_or_show_hn: false
llm_input_tokens: 12798
llm_latency_ms: 12891
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1156
our_published_at: '2026-05-22T19:40:07Z'
rewritten_title: Antigravity 2.0 et Gemini 3.5 Flash gagnent le benchmark OpenSCAD
  de modélisation 3D architecturale
source_published_at: '2026-05-22T10:38:26Z'
status: summarized
summarized_at: '2026-05-22T20:32:49.150555Z'
title: Antigravity 2.0 Tops the OpenSCAD Architectural 3D LLM Benchmark
url: https://modelrift.com/blog/openscad-llm-benchmark/
---

## Résumé de l'article

ModelRift a évalué plusieurs outils d'IA en leur demandant de générer du code OpenSCAD pour construire le Panthéon à partir d'images de référence. OpenSCAD est un langage de description textuel pour la modélisation 3D paramétrique, particulièrement adapté aux formes géométriques constructives et aux opérations booléennes.

- Antigravity 2.0 avec Gemini 3.5 Flash a obtenu le meilleur résultat autonome (4,5/5) en recherchant les paramètres réels du Panthéon et en implémentant les détails intérieurs distinctifs comme les 5 anneaux de 28 caissons du plafond
- La qualité n'a pas corrélé avec la vitesse : Cursor a été le plus rapide mais le plus faible (1,9/5), tandis que Claude Sonnet a pris plus de temps pour un résultat plus cohérent (3,4/5)
- Codex 5.5 High a produit le modèle le plus détaillé avec une inscription en latin, mais l'export STL final présentait des défauts de géométrie que les aperçus ne révélaient pas
- L'interaction visuelle a surpassé l'autonomie : ModelRift avec Gemini 3.0 et feedback annotés a atteint 3,8/5, démontrant que les corrections spatiales pointées directement sur le rendu sont plus efficaces que les descriptions textuelles
- Les cinq outils testés (Antigravity, Codex, Claude Code, Cursor, ModelRift) ont tous utilisé avec succès la chaîne OpenSCAD locale, confirmant que l'accès aux outils n'était pas le facteur limitant mais plutôt le jugement géométrique et la qualité spatiale du modèle

## Discussion sur Hacker News (118 commentaires)

**Avis positifs** :
- Les modèles LLM montrent des capacités impressionnantes en génération 3D, notamment Antigravity qui a reproduit les détails intérieurs du Panthéon (les coffres du plafond) que les autres ont manqués.
- L'utilisation d'images de référence améliore significativement la qualité par rapport aux approches textuelles seules, rendant la génération 3D plus accessible aux non-experts.
- Les LLM démocratisent l'accès à la modélisation CAD et OpenSCAD en abaissant les barrières d'entrée, permettant à des utilisateurs occasionnels de créer facilement des pièces fonctionnelles pour l'impression 3D.
- La progression technologique est remarquable : en trois ans, la génération 3D est passée de l'inimaginable à une réalité utilisable, même avec des imperfections.
- Les cas d'usage pratiques (pièces de remplacement, boîtiers électroniques) montrent une valeur réelle au-delà de la démonstration académique.

**Avis négatifs** :
- Le produit Antigravity 2.0 souffre de graves problèmes d'UX : authentification récurrente, synchronisation des credentials défaillante, IDE non fonctionnel, et migration forcée avant la parité des fonctionnalités.
- Google a un historique troublant de réduction rétroactive des limites d'utilisation et de cessation de produits sans préavis clair, créant une méfiance envers la pérennité et la fiabilité de ses offres AI.
- Ce benchmark ne teste qu'un seul objet une seule fois de manière subjective, sans cadre d'évaluation rigoureux ni cas d'usage réels définis—c'est de l'évaluation cosmétique plutôt qu'une métrique robuste.
- Les LLM peinent à itérer et déboguer efficacement : ils ne peuvent pas correctement visualiser les modifications successives, rendant le processus de raffinement extrêmement frustrant.
- Les limites de l'approche texte/image restent : les modèles génèrent des géométries imprécises en tolérance, manquent de contraintes dimensionnelles naturelles et produisent souvent des géométries inutilisables sans expert pour les corriger manuellement.

**Top commentaires** :

- [jhot](https://news.ycombinator.com/item?id=48234672) : Last weekend I bought my wife a bike off marketplace. It was in good condition but was missing one of the internal cable routing grommets. I gave Claude pictures of the pill-shaped hole by itself and with my digital calipers in the long and short directions. Gave it a short prompt and it gave me an…
- [jonasmaturana](https://news.ycombinator.com/item?id=48241111) : I've been using Claude to generate OpenSCAD scripts for the last few months, then exporting to Bambu Studio. Never really liked the OpenSCAD editing part though, so I built a little personal tool: https://webscad.aicentralen.dk/ One neat thing is that each color becomes a separate object on export…
- [jlhawn](https://news.ycombinator.com/item?id=48238207) : « Antigravity was the only autonomous agent that implemented the Pantheon’s signature interior ceiling pattern: repeated square coffers visible through the oculus. » That is seriously really impressive. I looked at the 3D model and didn't even thing to LOOK INSIDE the building before reading this.…

---

[Article original](https://modelrift.com/blog/openscad-llm-benchmark/) · [Discussion HN](https://news.ycombinator.com/item?id=48234090)
