---
article_fetched_at: '2026-09-21T21:27:47.106802Z'
attempts: 0
content_source: extracted
discussion_comment_count: 51
discussion_fetched_at: '2026-09-21T21:27:45.172810Z'
error: null
guid: https://news.ycombinator.com/item?id=49783133
hn_item_id: 49783133
hn_url: https://news.ycombinator.com/item?id=49783133
image_url: https://opengraph.githubassets.com/50787836f0a035be6053a28f30eea7809ff5e2f58da946828a8e702cd14db003/volotat/mini-AGI
is_ask_or_show_hn: false
llm_input_tokens: 12119
llm_latency_ms: 13826
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1131
our_published_at: '2026-09-21T21:22:58Z'
rewritten_title: 'Mini-AGI : modèle de langage continu entraîné sur 8 Go de VRAM avec
  apprentissage dynamique'
source_published_at: '2026-09-21T04:42:37Z'
status: summarized
summarized_at: '2026-09-21T21:28:57.061799Z'
title: 'Show HN: Mini-AGI – Dynamic continual learning model trained on 8GB VRAM'
url: https://github.com/volotat/mini-AGI/
---

## Résumé de l'article

Mini-AGI est un modèle de langage au niveau des octets qui effectue un apprentissage continu sur du matériel grand public (8 Go de VRAM). Le modèle construit dynamiquement sa propre architecture avec une méthode de mélange d'experts (Mixture of Experts), stocke ses poids sur disque et les charge en mémoire selon les besoins, ce qui lui permet de croître au-delà des limites de la VRAM.

- Le modèle utilise une architecture récurrente adaptative avec sélection d'experts par passage de caractère, permettant une profondeur de calcul variable selon la difficulté du texte traité
- Pour éviter l'oubli catastrophique, le taux d'apprentissage du tronc (embeddings, routeurs, halting head) est réduit à 0,1x celui des experts, conservant 99,84 % du progrès sur les autres sujets
- L'apprentissage est continu et sans fin : le modèle lit un flux de caractères, applique un pas de gradient à chaque étape, et le même code sert pour l'entraînement et la génération
- Le code, corpus et infrastructure sont entièrement open source ; l'utilisateur peut entraîner le modèle sur ses propres données sans surcoût matériel majeur
- Actuellement au stade expérimental (243M caractères lus, 169 experts), le modèle démontre que l'apprentissage continu sans catastrophic forgetting est réalisable sur du matériel de consommation

## Discussion sur Hacker News (51 commentaires)

**Avis positifs** :
- Architecture innovante inspirée du cerveau humain avec croissance/suppression naturelle des experts et sélection naturelle en arrière-plan, offrant une approche organique du continual learning.
- Démontre une réduction mesurable de l'oubli catastrophique : maintien de performance sur autres domaines après entraînement intensif sur données chess (524K caractères), contrairement aux modèles traditionnels.
- Accessibilité remarquable : fonctionnement sur GPU 8GB (RTX 3070 laptop) ouvre la possibilité d'AGI local, répondant à la demande de contrôle décentralisé face aux grands laboratoires.
- Approche simple et élégante : ralentir le learning rate du trunk tout en gardant celui des experts suffit à éliminer la plupart de l'oubli catastrophique, sans algorithme exotique.
- Engagement constructif du créateur : promesse de partager poids entraînés, benchmarks établis et vidéo explicative détaillée pour valider la démarche.

**Avis négatifs** :
- Prétention de nom et résultats prématurés : appeler cela 'AGI' et faire une annonce HN sans entraînement complet ni benchmarks établis est une surutilisation marketing; les sorties actuelles sont à peine cohérentes, pire que GPT-2.
- Aucune démonstration de généralisation réelle : le modèle produit du non-sens (exemple chess : mouvements illégaux impossibles), confondant mémorisation avec apprentissage véritable; context window de seulement 64 tokens limite les capacités.
- Manque total de rigueur académique : pas d'algorithme formalisé, pas de relation aux travaux connexes, pas d'étude d'ablation, juste du hand-waving; le markdown 'How continual learning works' n'est pas une description d'algorithme.
- L'oubli catastrophique n'est pas vraiment résolu : réduire le learning rate du trunk limite certes la dégradation mais arrête aussi l'acquisition de nouvelles connaissances; le problème est contourné plutôt que résolu, et le trunk subit encore de l'oubli progressif.
- Envergure insuffisante pour les revendications : 8M paramètres avec context 64, entraîné sur 524K caractères (100KB) sur enwik9 crée un fossé abyssal avec les vrais LLM (billions de paramètres, trillions de tokens); les résultats ne justifient pas le battage médiatique.

**Top commentaires** :

- [abeppu](https://news.ycombinator.com/item?id=49787729) : I have not looked carefully but it seems like this is over-promising on avoiding catastrophic forgetting. The "trunk learning rate" is set at 0.1x the learning rate for the experts, so learning on different subjects disproportionately happens in the experts, and the trunk portion is comparatively m…
- [HarHarVeryFunny](https://news.ycombinator.com/item?id=49791369) : Mini-AGI is a totally inappropriate name - it seems what this project is shooting for, but not delivering on, is being a language model with "continual learning". Where it seems to fail, by design, on this goal is in delivering continual learning that is more than just "memorization with LRU catast…
- [whizzter](https://news.ycombinator.com/item?id=49784149) : Nobody will throw rocks, I think most people are curious/suspicious about the big players and wants more hands-on since we suspect that this all will come down in cost soon enough.

---

[Article original](https://github.com/volotat/mini-AGI/) · [Discussion HN](https://news.ycombinator.com/item?id=49783133)
