---
article_fetched_at: '2026-08-14T15:42:35.852963Z'
attempts: 0
content_source: extracted
discussion_comment_count: 91
discussion_fetched_at: '2026-08-14T15:42:33.220625Z'
error: null
guid: https://news.ycombinator.com/item?id=49285327
hn_item_id: 49285327
hn_url: https://news.ycombinator.com/item?id=49285327
image_url: https://cdn.sanity.io/images/o0o2tn5x/production/61190f2745496c269dd071680edec773a29eaef7-1800x1013.png
is_ask_or_show_hn: false
llm_input_tokens: 12439
llm_latency_ms: 12899
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1156
our_published_at: '2026-08-14T15:27:52Z'
rewritten_title: 'Comparaison de onze modèles d''IA avec le même prompt : résultats
  et coûts en crédits'
source_published_at: '2026-08-13T13:05:29Z'
status: summarized
summarized_at: '2026-08-14T15:44:09.832440Z'
title: 'Choosing an AI model: one prompt, 11 models, different results'
url: https://www.netlify.com/blog/one-prompt-11-models-very-different-results/
---

## Résumé de l'article

Netlify a lancé un partenariat avec OpenRouter pour élargir l'accès aux modèles d'IA via sa plateforme. L'entreprise a testé onze modèles différents (Claude Opus et Sonnet, GPT-4 déclinaisons, Gemini, Kimi, GLM, DeepSeek) en les sollicitant avec le même prompt pour générer des sites web, afin de montrer comment les résultats et les coûts en crédits varient considérablement selon le modèle choisi.

- Claude Opus 5 produit les designs les plus élaborés avec vecteurs graphiques détaillés, mais consomme en moyenne 3 à 4 fois plus de crédits que les autres modèles, parfois jusqu'à 1 055 crédits pour une simple page de site statique
- GPT 5.6 Sol en mode low-effort offre un bon équilibre : résultats comparables à Opus en termes de richesse du contenu pour 141 crédits en moyenne au lieu de 184
- GPT 5.6 Terra (niveau inférieur) génère des résultats visuellement différents mais acceptables pour seulement 39 crédits en moyenne
- Les modèles open-source comme DeepSeek V4 Flash 0731 consomment très peu de crédits (2,4 en moyenne) avec des résultats variables, tandis que Gemini 3.1 Pro produit du contenu très basique
- Pour les tâches simples de conception, le choix du modèle dépend du budget et de la stratégie : solution clé en main sophistiquée coûteuse versus approche itérative avec des modèles moins chers et des ajustements manuels

## Discussion sur Hacker News (91 commentaires)

**Avis positifs** :
- Les résultats similaires entre modèles reflètent un comportement normal : à tâche générique et peu contrainte, les LLM produisent des réponses moyennes et convergentes, comme des humains suivant un processus standard
- Ces comparaisons exploratoires offrent une valeur intéressante pour explorer les 'personnalités' des modèles et comment ils développent des sensibilités en matière de design, au-delà des benchmarks traditionnels
- Il y a une réelle utilité à avoir un site web propre pour les petits commerces : accès à des données actualisées, indépendance par rapport aux plateformes tierces (Google Maps, Facebook), accessibilité et contrôle de sa présence numérique
- Les modèles plus petits/économiques (DeepSeek, Gemini 3.1) produisent parfois des designs plus fonctionnels et lisibles, avec moins de fioritures superflues rendant l'information difficile à trouver
- Cette comparaison teste utilement la cohérence et la qualité du code généré au-delà de l'apparence visuelle, montrant comment les modèles organisent les abstractions et structurent le travail

**Avis négatifs** :
- Un seul passage (N=1) avec seulement 3 exécutions par modèle ne permet pas de conclusions fiables : la variance stochastique des LLM rend les résultats hautement sensibles au hasard et non représentatifs pour des comparaisons sérieuses
- Le prompt initial est trop minimaliste et peu réaliste : laisser aux modèles le choix des horaires, prix et adresses crée une tâche sans réponse correcte, artificiellement avantageuse pour les modèles, et ne teste pas leur capacité à gérer des contraintes réelles
- Ces évaluations one-shot ne reflètent pas comment les professionnels utilisent réellement les LLM : avec des instructions détaillées, itératives et multi-tour, pas des prompts génériques en deux phrases
- L'article omet des tests cruciaux comme la responsivité mobile et les performances de chargement, alors que la plupart des utilisateurs consulteraient le site sur téléphone avec une connexion lente
- Les benchmarks génériques deviennent obsolètes car les modèles intègrent les données publiques de test dans leur entraînement ; seules des évaluations spécifiques au domaine et à des cas réels de travail ont du sens

**Top commentaires** :

- [Systemerror7A69](https://news.ycombinator.com/item?id=49285824) : Am I wrong or are these evaluations, while interesting, not really meaningful for anyone doing serious development work? I'm asking because I personally only use AI with specific and detailed instructions, building my projects piece-by-piece. I mostly don't look at the low level code and some of it…
- [isqueiros](https://news.ycombinator.com/item?id=49285571) : « Build a one-page site for a neighbourhood coffee shop: opening hours, the address, a short menu and a photo. Nothing on it changes unless I edit it myself. » If that's the entire prompt, it's quite depressing how much alike these all look. I appreciate some of the details from the Opus 5 version,…
- [jwr](https://news.ycombinator.com/item?id=49285776) : I've been doing a lot of benchmarking for a long time now with a number of local models for the purposes of spam filtering. The major observation is that there is a lot of variance in model performance. This should not be surprising, as these are probabilistic machines based on random numbers, so y…

---

[Article original](https://www.netlify.com/blog/one-prompt-11-models-very-different-results/) · [Discussion HN](https://news.ycombinator.com/item?id=49285327)
