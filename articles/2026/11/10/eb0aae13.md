---
article_fetched_at: '2026-11-10T01:48:56.498111Z'
attempts: 0
content_source: extracted
discussion_comment_count: 20
discussion_fetched_at: '2026-11-10T01:48:51.385084Z'
error: null
guid: https://news.ycombinator.com/item?id=50429734
hn_item_id: 50429734
hn_url: https://news.ycombinator.com/item?id=50429734
image_url: https://e-means.github.io/assets/emeans_vs_lloyd_readme_v9.png
is_ask_or_show_hn: false
llm_input_tokens: 4742
llm_latency_ms: 8052
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 927
our_published_at: '2026-11-10T01:20:51Z'
rewritten_title: 'E-means : un algorithme de clustering plus rapide que k-means pour
  atteindre la convergence'
source_published_at: '2026-11-09T18:45:43Z'
status: summarized
summarized_at: '2026-11-10T01:50:55.952799Z'
title: 'E-means: Outperforming k-means in one-tenth the epochs'
url: https://e-means.github.io/
---

## Résumé de l'article

E-means est une variante optimisée de l'algorithme k-means qui atteint une perte d'entraînement équivalente à celle de Lloyd's en 25 fois moins d'itérations (1,2 à 3 epochs au lieu de 25), grâce à des mises à jour par moyennes mobiles exponentielles sur mini-batches. L'algorithme offre des gains de vitesse de 10 à 45× sur GPU et 8 à 15× sur CPU par rapport aux implémentations existantes, tout en obtenant une meilleure qualité de clustering.

- E-means utilise des mises à jour des centroïdes par moyennes mobiles exponentielles sur mini-batches, oubliant progressivement les anciennes assignations plutôt que de garder toute l'historique (Lloyd) ou d'accumuler sans limite (MacQueen)
- L'algorithme définit automatiquement la taille des batches et le taux d'apprentissage via des lois d'échelle dérivées empiriquement, éliminant tout besoin de tuning d'hyperparamètres
- E-means améliore la stratégie de relancement des clusters « morts » (sans points assignés) en les divisant plutôt que de les réinitialiser aléatoirement, préservant mieux la capacité du codebook
- Les mini-batches bruyants du nouvel algorithme échappent mieux aux minima locaux que Lloyd, qui converge prématurément vers des solutions sous-optimales
- Le code est disponible dans le dépôt Faiss (faiss/contrib/e_means) et validé sur 24 datasets différents, de 100k à 100M points

## Discussion sur Hacker News (20 commentaires)

**Avis positifs** :
- L'algorithme E-means est impressionnant et semble évident avec le recul ; les visualisations l'expliquent bien et il devrait être intégré à scipy pour une meilleure disponibilité
- Les résultats pratiques sont remarquables : accélérations de 45x à 146x sur GPU, avec réductions de 50-80% des temps de construction d'index et de l'utilisation CPU
- La technique est robuste pour l'assignation des centroïdes et échappe mieux aux minima locaux grâce aux mises à jour bruitées du mini-batch, ce qui a une vraie utilité pratique
- L'approche illustre pourquoi les solutions approximatives pour les problèmes NP-difficiles peuvent être suffisantes quand elles sont beaucoup plus rapides en pratique

**Avis négatifs** :
- Les lois de sélection automatique des hyperparamètres ne semblent pas intuitives et manquent de justification claire
- Les hyperparamètres semblent avoir été ajustés rétrospectivement plutôt que dérivés de principes fondamentaux
- La technique n'est pas fondamentalement nouvelle : les mini-batch k-means avec mise à jour par moyenne mobile exponentielle existent depuis longtemps ; la contribution principale est surtout la mesure et la publication du code
- Les résultats ne tiennent pas compte de la scalabilité réelle : à grande échelle distribuée, les communications deviennent le goulot d'étranglement dominant, annulant les gains d'efficacité théoriques, et l'amélioration du clustering avec plus de travail local montre des rendements décroissants

**Top commentaires** :

- [saagarjha](https://news.ycombinator.com/item?id=50435033) : As far as I can tell this isn't particularly new, people have been doing minibatch k-means for a while, including with an EWA update. I assume the contribution here is that they tried to measure how much better it is and provided code? I'm not sure I agree with their claims though, because they did…
- [jlhawn](https://news.ycombinator.com/item?id=50432676) : I wonder if this could be used anywhere as an alternative to Lloyd's algorithm. I have a hobby project which uses Lloyd's to "relax" an icosohedral equal area mesh on the surface of a sphere \[1\]. I'm going to try to swap it out with an adaptation of this and see if it's much better or if I can affo…
- [robbienukes](https://news.ycombinator.com/item?id=50434982) : What is most impressive about this excellent work is not just the staggering time savings but the robustness of the technique in its assignment of single centroids where legacy may create two due to artefacting or worse one centroid for two blobs. Their explanation that: mini-batches provide more n…

---

[Article original](https://e-means.github.io/) · [Discussion HN](https://news.ycombinator.com/item?id=50429734)
