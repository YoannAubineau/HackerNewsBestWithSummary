---
article_fetched_at: '2026-11-12T23:01:25.405886Z'
attempts: 0
content_source: extracted
discussion_comment_count: 46
discussion_fetched_at: '2026-11-12T23:01:20.942703Z'
error: null
guid: https://news.ycombinator.com/item?id=50452655
hn_item_id: 50452655
hn_url: https://news.ycombinator.com/item?id=50452655
is_ask_or_show_hn: false
llm_input_tokens: 8163
llm_latency_ms: 12254
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1105
our_published_at: '2026-11-12T22:52:34Z'
rewritten_title: Un programme linéaire peut remplacer la recherche par essais-erreurs
  pour éditer les poids des réseaux de neurones
source_published_at: '2026-11-11T12:30:17Z'
status: summarized
summarized_at: '2026-11-12T23:03:02.245987Z'
title: Can a Linear Program Do Weight-Space Programming?
url: https://nathan.rs/posts/weight-space-lp/
---

## Résumé de l'article

Un chercheur montre que l'édition de poids d'un petit réseau neuronal effectuée par GPT-6 Astra pour corriger les boucles infinies de raisonnement dans Qwen3.5-0.8B peut être reformulée comme un programme linéaire (LP), permettant de reproduire les gains de précision avec 8 fois moins de modifications de poids.

- Astra a modifié 0,016 % des poids pour améliorer la précision en mathématiques de 7,9 % à 48,1 %, mais a passé 8 heures à chercher par essais-erreurs quelle était la meilleure configuration ; deux résolutions de programme linéaire prennent environ une minute chacune et obtiennent le même résultat.
- Le problème consiste à trouver un vecteur v minimisant la norme L1, soumis à des contraintes linéaires : pousser fortement les tokens de boucle loin d'une direction u identifiée, tout en laissant les tokens productifs inchangés.
- Le solveur LP partagé avec Astra la direction u et les couches cibles (15 et 19), mais sélectionne seulement 8 colonnes par couche (contre 64 pour Astra) ; avec une direction heuristique sans LLM, il récupère 93 % des gains.
- L'édition de poids est quasi équivalente à ajouter un vecteur de direction constant au flux résiduel à chaque token (steering vector) : à la force 1×, le vecteur directeur seul restaure essentiellement la correction, sans modifier les poids du modèle.
- L'approche reste limitée à ce modèle et dépend encore partiellement de Astra pour identifier les couches ; elle pourrait s'appliquer à d'autres comportements ajustables par une seule direction (refus, sycophantie).

## Discussion sur Hacker News (46 commentaires)

**Avis positifs** :
- L'utilisation de la programmation linéaire (algorithmes des années 1940) pour éditer les poids est une approche élégante et simple qui devrait se produire naturellement lors de l'entraînement via régularisation
- Cette méthode représente une redécouverte d'outils mathématiques classiques oubliés, offrant une alternative plus efficace et auditable aux approches d'essai-erreur des LLM modernes
- L'édition de poids via des contraintes linéaires (suppression de comportements indésirables, préservation d'autres) est un processus mathématiquement rigoureux comparable à des techniques d'interprétabilité établies
- Cette capacité à optimiser les poids d'autres modèles est une étape significative vers l'auto-amélioration, ouvrant des possibilités comme l'optimisation incrémentale en déploiement sans retraining complet

**Avis négatifs** :
- Les titres médiatiques ont déformé les résultats en suggérant que les LLM possèdent une compréhension spéciale des poids, alors qu'ils exécutent simplement des algorithmes classiques comme le ferait un ingénieur humain
- Contrairement aux affirmations initiales, Astra n'a pas directement compris ou manipulé les poids de façon consciente, mais a utilisé des outils externes et des appels de fonction, ce qui est fondamentalement différent de la réécriture directe du code compilé
- L'édition de poids dans l'espace hautement dimensionnel des neurones est imprécise : une direction 'bonne' pour un test peut facilement causer des régressions sur d'autres cas, contrairement à l'édition de code source avec certitude absolue
- Les vecteurs de direction favorables n'existent pas systématiquement ; trouver ces 'steering vectors' reste difficile et rare, et la méthode utilisée pour améliorer Qwen en mathématiques n'a résolu qu'un problème spécifique (boucles) sans vraie compréhension

**Top commentaires** :

- [jsw97](https://news.ycombinator.com/item?id=50453507) : Maybe this is what the author is getting at, but if LP solvers are useful tools for editing weights, then Astra access to this methodology might make it more effective at weight editing. The interpretation here is not so much that an LP can do Astra's work -- after all the Astra prompt was "improve…
- [rbnafo](https://news.ycombinator.com/item?id=50453946) : Very interesting analysis. It would be great to see the LP comeback and optimize. I always have the impression that we have settled to suboptimal solutions in many areas just because we have become too attached to LLMs, wary of numerical analysis.
- [dansitu](https://news.ycombinator.com/item?id=50452953) : Nice analysis. The simplicity of this indicates that it should be happening during training via regularization.

---

[Article original](https://nathan.rs/posts/weight-space-lp/) · [Discussion HN](https://news.ycombinator.com/item?id=50452655)
