---
article_fetched_at: '2026-06-23T21:32:08.201716Z'
attempts: 0
content_source: extracted
discussion_comment_count: 198
discussion_fetched_at: '2026-06-23T21:32:07.571046Z'
error: null
guid: https://news.ycombinator.com/item?id=48643180
hn_item_id: 48643180
hn_url: https://news.ycombinator.com/item?id=48643180
image_url: https://lucumr.pocoo.org/social/2026-06-23-the-coming-loop-social.png
is_ask_or_show_hn: false
llm_input_tokens: 28473
llm_latency_ms: 12560
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1127
our_published_at: '2026-06-23T21:09:06Z'
rewritten_title: Les boucles de systèmes d'IA autonomes transforment l'ingénierie
  logicielle et menacent la compréhension humaine du code
source_published_at: '2026-06-23T11:06:41Z'
status: summarized
summarized_at: '2026-06-23T21:32:27.331660Z'
title: The Coming Loop
url: https://lucumr.pocoo.org/2026/6/23/the-coming-loop/
---

## Résumé de l'article

Boris Cherny, ingénieur logiciel, explore la montée des « harness loops » — des boucles de contrôle externe où des machines exécutent, évaluent et itèrent sur des tâches de codage sans intervention humaine directe. Ces boucles diffèrent des boucles internes aux agents d'IA (où le modèle appelle des outils et produit un résultat), en plaçant un orchestrateur extérieur qui décide si le travail est terminé ou doit continuer.

- Les boucles externes fonctionnent bien pour certains domaines (portage de code, exploration de performances, recherche en sécurité) où le code est temporaire ou soumis à vérification mécanique, mais produisent du code défensif, complexe et peu compréhensible pour un usage durable.
- Les modèles d'IA actuels amplifient les mauvaises pratiques : ajout de défenses locales plutôt que de rendre les états malveillants impossibles, ce qui rend le code moins lisible tout en paraissant plus robuste à chaque itération.
- La pression compétitive et la nécessité de défense contre les attaques automatisées poussent les équipes à adopter ces boucles, risquant de créer des bases de code que seules les machines peuvent maintenir et comprendre.
- La dépendance croissante envers ces systèmes pose un risque : perte de compréhension humaine du code, dépendance cognitive aux machines, vulnérabilité aux restrictions commerciales ou aux hausses de coûts des modèles puissants.
- Cherny conclut que la question n'est pas si les boucles arriveront, mais comment préserver le jugement humain, la responsabilité et la capacité de supervision dans cette future autonomisée.

## Discussion sur Hacker News (198 commentaires)

**Avis positifs** :
- Les boucles agentic peuvent augmenter la productivité pour des tâches bien définies et répétitives, notamment en permettant d'explorer les espaces problématiques et d'accélérer le prototypage.
- Ces outils libèrent les développeurs de tâches répétitives et fastidieuses, permettant de se concentrer sur l'architecture et les décisions de haut niveau plutôt que sur l'implémentation mécanique.
- Les modèles s'améliorent constamment et pourraient résoudre les problèmes actuels de qualité de code; le progrès des capacités justifie l'optimisme à long terme sur la viabilité des boucles agentic.
- La technologie a déjà prouvé son utilité pour les développeurs moins expérimentés et pour accélérer le travail sur des problèmes à faible risque ou des prototypes.

**Avis négatifs** :
- Les modèles actuels produisent intrinsèquement du code médiocre: trop défensif, complexe, sans invariants forts, avec duplications et abstractions faibles, reproduisant simplement les défauts du corpus d'entraînement.
- L'absence de compréhension humaine crée un risque de dette technique massif et d'atrophie cognitive; déléguer le code sans le comprendre rend les systèmes fragiles et impossibles à maintenir à long terme.
- Les organisations ignorent les coûts réels (tokens, maintenance, révision, qualité déclinante) et poussent les boucles agentic par effet de mode ou pression exécutive, sans cas d'affaires solides démontrant une augmentation réelle de la profitabilité.
- La culture émergente de la 'vibe coding' (générer du code sans le vérifier) crée une épuisement chez les développeurs séniors contraints de réviser des tonnes de PRs incompréhensibles, tandis que les décideurs refusent d'admettre la baisse de qualité.
- Le fatigue existentielle et la perte de plaisir à programmer affectent même les professionnels expérimentés; beaucoup questionnent leur carrière ou leur engagement dans ce domaine face à l'accélération imposée et l'absence de compréhension attendue.

**Top commentaires** :

- [firefax](https://news.ycombinator.com/item?id=48651720) : I haven't been this confused by a headline since Keir Starmer declared himself a "gooner". I think a big issue with a lot of AI enabled coding is that tokens are currently heavily subsidized, and that refusing to learn how to write psudocode and pound out bugs in shell scripts is a fundamental step…
- [mccoyb](https://news.ycombinator.com/item?id=48644130) : Loops work when you spend the proper amount of time to understand what you want ahead of time. The prerequisite is clarity — enough clarity that you could write a careful specification that you could hand off to a junior colleague. Often, it takes 5-6 broken crappy versions of a thing until you und…
- [mmillin](https://news.ycombinator.com/item?id=48644568) : « Yet even with a lot of manual steering, that type of code does not come out of LLMs naturally, and even if the code comes out naturally like that, they will still attempt to handle now impossible errors. » This is something I’ve struggled to fight against in many PR reviews. Especially once alrea…

---

[Article original](https://lucumr.pocoo.org/2026/6/23/the-coming-loop/) · [Discussion HN](https://news.ycombinator.com/item?id=48643180)
