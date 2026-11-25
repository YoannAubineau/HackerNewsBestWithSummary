---
article_fetched_at: '2026-11-25T15:13:02.214669Z'
attempts: 0
content_source: extracted
discussion_comment_count: 58
discussion_fetched_at: '2026-11-25T15:12:16.486749Z'
error: null
guid: https://news.ycombinator.com/item?id=50637056
hn_item_id: 50637056
hn_url: https://news.ycombinator.com/item?id=50637056
image_url: https://greydanus.github.io/assets/pengpt/thumbnail.png
is_ask_or_show_hn: false
llm_input_tokens: 6398
llm_latency_ms: 9080
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1004
our_published_at: '2026-11-25T14:22:58Z'
rewritten_title: 'PenGPT : un transformeur génératif pour l''écriture manuscrite et
  les croquis'
source_published_at: '2026-11-25T00:54:49Z'
status: summarized
summarized_at: '2026-11-25T15:14:18.571552Z'
title: 'PenGPT: A Generative Transformer for Handwriting and Sketches'
url: https://greydanus.github.io/2026/11/12/pengpt/
---

## Résumé de l'article

PenGPT est un petit modèle transformeur capable de générer de l'écriture manuscrite et des dessins à partir de texte. Le projet a porté principalement sur la qualité des données (80% de l'effort), l'optimisation de la vitesse d'entraînement (15%) et l'architecture du modèle (5%), illustrant le principe du « Bitter Lesson » en apprentissage automatique.

- Deux modèles ont été entraînés : un de 6M paramètres pour l'écriture manuscrite (cursive et print) capable d'adapter son style à partir de quelques mots d'une nouvelle main, et un de 54M paramètres pour générer des dessins à partir de descriptions textuelles
- Les données proviennent de 495 590 mots manuscrits de 1 255 auteurs (issus de collections de recherche et d'archives) et de 477 670 croquis provenant de dix bases de données publiques (notamment Quick, Draw!)
- L'élément clé de l'adaptation de style est simple : chaque séquence d'entraînement contient jusqu'à quatre mots du même auteur, ce qui apprend au modèle que les mots ultérieurs ressemblent aux précédents
- Les améliorations architecturales sophistiquées (encodeur de style, vocabulaire large, LSTM contre Transformer) ont eu un impact minimal comparé à l'effet des données de qualité et de l'augmentation des données
- Le modèle de dessin fusionne les concepts mais ne les lie pas précisément : il peut combiner une théière et un visage, mais confond les directions (« facing left » et « facing right » génèrent le même dessin)

## Discussion sur Hacker News (58 commentaires)

**Avis positifs** :
- L'efficacité et la compacité du modèle (50 MB) est impressionnante et aurait pu être réalisée des décennies plus tôt avec les bonnes approches algorithmiques
- L'accent mis sur la qualité des données plutôt que sur l'architecture ingénieuse est une application pragmatique et efficace de la « Bitter Lesson »
- Le projet offre une utilité pratique immédiate : génération de données synthétiques pour l'OCR, transcription handwriting, et créativité ludique avec le mode dessin
- La transparence de l'auteur sur l'utilisation de Claude pour l'écriture du post montre une priorisation judicieuse : investir l'effort dans le code/données/ablations plutôt que dans la rédaction
- Le modèle démontre une diversité impressionnante de styles et capture des phénomènes réalistes comme la dégradation de la lisibilité avec des mots répétés

**Avis négatifs** :
- Le modèle a des difficultés manifestes avec les caractères non-latins (espagnol accentué, caractères polonais, chinois) et nécessiterait un réentraînement pour chaque langue
- Les lignes droites présentent des wobbles artificiels visibles dues à la quantification sur grille, révélant une limitation du prétraitement des données qui plus de données ne peut pas corriger
- Les capacités compositionnelles sont limitées : combiner plusieurs concepts (par ex. pélican sur vélo) génère de l'art semi-abstrait incohérent
- Le texte du post était entièrement écrit par Claude, ce qui rend la lecture moins fluide et crédible malgré l'excellence du travail technique sous-jacent
- Le modèle échoue sur des entrées complexes (arrêt prématuré, caractères spéciaux mal gérés) et les capacités de dessin restent basiques comparées à ce qu'on pourrait attendre

**Top commentaires** :

- [keyle](https://news.ycombinator.com/item?id=50637580) : The most interesting part to me is this mention of the Bitter Lesson \[1\] "The results are interesting and the project was a pleasure to work on. And yet there was no clever architectural idea behind it. About 80% of my effort went into building the biggest, cleanest datasets possible and doing lots…
- [samgreydanus](https://news.ycombinator.com/item?id=50638604) : Author here! Given that I only trained these on an 8xH100 it's not exactly the most spectacular illustration of the Bitter Lesson. All I can say is that historically I always wanted to impress people with better model architectures or training techniques. This time I just put all my energy into dat…
- [baalimago](https://news.ycombinator.com/item?id=50642777) : I took the liberty of adding the models to penelope.ink. So now when the model is transcribing, I get contextual doodles generated from past notes. Looks a little bit like this: https://i.ibb.co/21Z4mWV7/AI-doodles.png \(coffee-cup, "emai deliverabiliti was ..." etc.\) Very fun! Thanks OP!

---

[Article original](https://greydanus.github.io/2026/11/12/pengpt/) · [Discussion HN](https://news.ycombinator.com/item?id=50637056)
