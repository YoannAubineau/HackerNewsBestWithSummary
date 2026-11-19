---
article_fetched_at: '2026-11-19T02:54:32.039814Z'
attempts: 0
content_source: extracted
discussion_comment_count: 52
discussion_fetched_at: '2026-11-19T02:53:22.852606Z'
error: null
guid: https://news.ycombinator.com/item?id=50543989
hn_item_id: 50543989
hn_url: https://news.ycombinator.com/item?id=50543989
image_url: https://energy-based-reasoners.github.io/static/images/ebr_landscape_abc_v1.png
is_ask_or_show_hn: false
llm_input_tokens: 7270
llm_latency_ms: 7306
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 996
our_published_at: '2026-11-19T02:23:54Z'
rewritten_title: 'Energy-Based Reasoners: modèles de raisonnement récurrents guidés
  par une fonction d''énergie'
source_published_at: '2026-11-18T09:29:32Z'
status: summarized
summarized_at: '2026-11-19T02:55:39.464782Z'
title: 'Energy-Based Reasoners: 385x more efficient inference'
url: https://energy-based-reasoners.github.io/
---

## Résumé de l'article

Les Energy-Based Reasoners (EBRs) sont des modèles de raisonnement qui apprennent une fonction d'énergie sur les états latents et formulent les mises à jour itératives comme une descente de gradient. Cette approche guide explicitement le raffinement des solutions, fournit un critère d'arrêt clair et améliore l'efficacité du raisonnement algorithmique.

- Les EBRs utilisent une fonction d'énergie pour évaluer la compatibilité des états de raisonnement avec le problème initial, son gradient guidant l'amélioration et le gradient petit servant de critère d'arrêt
- Sur quatre benchmarks de raisonnement algorithmique, les EBRs atteignent 99,9% de précision sur Sudoku-Extreme avec 345× moins de calcul d'inférence que le meilleur modèle concurrent
- Une approche d'entraînement basée sur l'exploration découvre des solutions additionnelles et façonne mieux le paysage énergétique sur un ensemble plus large d'états
- Sur les benchmarks multi-solutions, les EBRs atteignent la couverture de pointe des solutions valides distinctes tout en maintenant une précision proche de 100%
- Les puzzles faciles se résolvent en peu d'étapes tandis que les puzzles difficiles continuent itérativement jusqu'à convergence

## Discussion sur Hacker News (52 commentaires)

**Avis positifs** :
- Les modèles basés sur l'énergie offrent une approche intéressante pour les problèmes avec des règles discrètes bien définies (Sudoku, jeux logiques) où les approches traditionnelles de recherche seraient inefficaces
- Cette perspective énergétique fournit un cadre conceptuel utile pour comprendre le raisonnement comme navigation dans un paysage énergétique, aligné avec la théorie de l'information et la complexité de Kolmogorov
- Les modèles basés sur l'énergie pourraient s'avérer plus efficaces que les LLMs pour certains problèmes discrets à espace de solution limité, particulièrement en inference locale sur du matériel peu puissant
- Cette approche complète les forces des LLMs en abordant des domaines où ils performent traditionnellement mal, comme le calcul primaire et le comptage

**Avis négatifs** :
- La méthode ne fonctionne actuellement que sur des problèmes très spécifiques avec règles fixes et espace de solutions contraint ; l'extension au raisonnement arbitraire et au langage naturel reste hautement problématique
- L'entraînement des EBMs est extrêmement difficile et nécessite des paires correctes/incorrectes fortement étiquetées, contrairement aux LLMs qui exploitent d'énormes quantités de données non étiquetées
- Pour la plupart des cas d'usage pratiques, la programmation classique et la programmation dynamique restent plus efficaces qu'une approche neuronale ; résoudre le Sudoku traditionnellement est 10-100x plus rapide
- Le terme « énergie » n'est pas clairement justifié scientifiquement dans le contexte de ces modèles et semble être une analogie peu fondée par rapport à la théorie de l'énergie libre ou à des principes physiologiques établis
- Malgré l'engouement académique, les EBMs n'ont pas bénéficié des décennies d'optimisation technologique complète (GPU, TPU, frameworks) que les LLMs ont reçues, rendant les comparaisons prématurées

**Top commentaires** :

- [Topfi](https://news.ycombinator.com/item?id=50545266) : Recommend checking out Logical Intelligence, chaired by among others Yann LeCun, for more context on EBMs \[0\]. Has great potential in areas that LLMs traditionally do not perform that well in and, because they want to show the advantages of EBMs, also tends to be a great source of examples LLMs str…
- [program\_whiz](https://news.ycombinator.com/item?id=50545736) : A clarifying way to think about this for sudoku: For every clue, mark the probability of sampling its number in the row/col to zero. Also mark the probability of selecting a "clue cell" for modification to 0. Pick a random cell for modification, based on its "energy" \(higher energy get modified fir…
- [mocmoc](https://news.ycombinator.com/item?id=50546168) : I've spent a year on this. EBMs while ... how to say it, they are impressive validators , it's insanely hard to train them. They are very niche specific. While LLMs , being not right all the time and clumsy and so on, they help the people to get the job done at the end. EBM sudoku is not that hard…

---

[Article original](https://energy-based-reasoners.github.io/) · [Discussion HN](https://news.ycombinator.com/item?id=50543989)
