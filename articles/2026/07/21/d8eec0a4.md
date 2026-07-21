---
article_fetched_at: '2026-07-21T12:22:52.901917Z'
attempts: 0
content_source: extracted
discussion_comment_count: 156
discussion_fetched_at: '2026-07-21T12:22:51.734812Z'
error: null
guid: https://news.ycombinator.com/item?id=48981206
hn_item_id: 48981206
hn_url: https://news.ycombinator.com/item?id=48981206
is_ask_or_show_hn: false
llm_input_tokens: 17021
llm_latency_ms: 14245
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1177
our_published_at: '2026-07-21T11:49:56Z'
rewritten_title: Comment nous avons mesuré l'écriture assistée par IA sur arXiv et
  les limites de cette mesure
source_published_at: '2026-07-20T16:36:36Z'
status: summarized
summarized_at: '2026-07-21T12:23:29.948946Z'
title: How we measured AI writing across arXiv, and where the measurement breaks
url: https://unslop.run/blog/measuring-ai-writing-on-arxiv
---

## Résumé de l'article

Des chercheurs ont analysé 12 750 articles arXiv pour estimer la prévalence de textes générés ou fortement assistés par des modèles de langage. Leur détecteur, étalonné sur des articles scientifiques antérieurs à ChatGPT, montre que environ un tiers des articles récents présentent des caractéristiques d'écriture assistée par IA, avec une forte variation selon les disciplines.

- Le détecteur a été calibré pour maintenir un taux de faux positifs de 0,4% sur les articles pré-ChatGPT (2021-2022), servant de seuil de référence et de validation interne
- L'adoption varie fortement par domaine : l'informatique atteint 65%, tandis que les mathématiques affichent seulement 0,7%, ce qui pourrait refléter une adoption réelle faible ou une limite du détecteur face aux notations mathématiques
- Les résultats montrent un décollage rapide quelques mois après le lancement de ChatGPT, culminant à 39% au début 2026, avec deux vagues distinctes d'augmentation
- Les limites incluent la petite taille de l'échantillon de contrôle par domaine, la sensibilité variable selon les générateurs d'IA utilisés, et l'incapacité à distinguer l'édition assistée de la génération complète
- L'outil est gratuit et accessible en ligne pour tester n'importe quel article arXiv ou texte personnel

## Discussion sur Hacker News (156 commentaires)

**Avis positifs** :
- La méthodologie du détecteur semble robuste : calibrage volontaire pour éviter les faux positifs pré-ChatGPT (0,4%), ce qui rend les augmentations observées plus significatives et crédibles
- La tendance temporelle est frappante et cohérente : passage de ~0,4% à 39% en janvier 2026, avec pics distincts par discipline (65% en informatique vs 0,7% en mathématiques), suggérant une adoption réelle et différenciée par domaine
- Les limitations sont ouvertement reconnues par l'auteur : distinction entre détection statistique et preuve d'usage, possibilité que le texte soit AI-assisté plutôt que générée, et promesses de nouvelles itérations du détecteur
- Le problème réel identifié transcende la détection technique : l'inflation de publications, la perte de signaux de qualité (effort de rédaction), et la contamination du corpus scientifique par du contenu sans fondement de recherche véritable
- Plusieurs chercheurs confirment des observations empiriques convergentes (Pangram, analyse corpus) et reconnaissent l'utilité pragmatique de tels outils malgré leurs imperfections

**Avis négatifs** :
- Les détecteurs de texte AI sont structurellement peu fiables : tous les détecteurs commerciaux ont été débunkés, l'article du blog est lui-même flaggé par le détecteur, et aucune garantie de reproductibilité ou d'interprétabilité méthodologique n'existe
- Fuite de données probable dans l'entraînement du détecteur : pas de véritable contrôle que le texte pré-ChatGPT n'a pas influencé l'apprentissage, et les taux de faux positifs élevés (27-74% sur des textes humains de 2011-2015) invalident les seuils de classification
- Biais et confusions methodologiques : évolution naturelle du langage académique, nouvelles terminologies post-2022 (« large language model »), et convergence inévitable entre humains lisant du texte IA et imitation stylistische rendent impossible la distinction fiable
- Utilisation légitime d'IA ignorée : correction grammaticale pour locuteurs non natifs, polissage rédactionnel pour clarté, et amélioration du style ne constituent pas du contenu généré mais sont systématiquement flaggés, ce qui pénalise injustement des chercheurs vulnérables
- Le vrai problème n'est pas la détection mais la qualité et l'intégrité scientifiques : les hallucinations d'IA (citations fictives, données fabriquées, preuves inventées) requièrent une relecture humaine rigoureuse plutôt qu'une détection statistique inefficace

---

[Article original](https://unslop.run/blog/measuring-ai-writing-on-arxiv) · [Discussion HN](https://news.ycombinator.com/item?id=48981206)
