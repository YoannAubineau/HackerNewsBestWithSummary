---
article_fetched_at: '2026-05-07T00:26:25.166288Z'
attempts: 0
content_source: extracted
discussion_comment_count: 385
discussion_fetched_at: '2026-05-07T00:26:24.920305Z'
error: null
feed_summary: '<p>Article URL: <a href="https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/">https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=48037128">https://news.ycombinator.com/item?id=48037128</a></p>

  <p>Points: 314</p>

  <p># Comments: 340</p>'
guid: https://news.ycombinator.com/item?id=48037128
hn_item_id: 48037128
hn_url: https://news.ycombinator.com/item?id=48037128
is_ask_or_show_hn: false
llm_input_tokens: 38272
llm_latency_ms: 13666
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1186
our_published_at: '2026-05-06T23:33:27Z'
rewritten_title: Les frontières entre vibe coding et ingénierie agentique s'estompent
source_published_at: '2026-05-06T15:06:37Z'
status: summarized
summarized_at: '2026-05-07T00:26:45.153926Z'
title: Vibe coding and agentic engineering are getting closer than I'd like
url: https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/
---

## Résumé de l'article

Simon Willison, ingénieur logiciel, examine comment les outils de codage par IA brouillent la distinction qu'il avait établie entre le « vibe coding » (développement sans vérification du code) et l'« ingénierie agentique » (utilisation responsable des outils IA par des professionnels expérimentés). À mesure que les agents de codage deviennent plus fiables, même lui cesse de réviser chaque ligne de code en production, ce qui le place dans une zone grise morale.

- Les outils IA de codage (comme Claude Code) produisent du code suffisamment fiable que les développeurs commencent à les traiter comme des boîtes noires plutôt que de vérifier chaque ligne, similaire à la confiance accordée à d'autres équipes dans les organisations.
- La production de code augmente dramatiquement (de 200 à 2 000 lignes par jour), ce qui bouleverse tout le cycle de développement logiciel traditionnellement conçu autour d'une cadence plus lente.
- Les critères d'évaluation changent : un projet avec documentation et tests générés rapidement par IA est visuellement identique à un projet développé avec soin, rendant l'évaluation de la qualité plus difficile ; l'usage réel devient plus pertinent que les métriques formelles.
- L'expérience professionnelle reste décisive : les outils IA amplifient les compétences existantes plutôt que de les remplacer, et les entreprises préféreront toujours des solutions de SaaS éprouvées à des développements maison risqués.
- Il existe un risque de « normalisation de la déviance » : chaque succès du modèle renforce la confiance, augmentant le danger de défaillance future non détectée.

## Discussion sur Hacker News (385 commentaires)

**Avis positifs** :
- Les outils d'IA amplifient l'expertise existante : les développeurs expérimentés peuvent produire beaucoup plus rapidement avec ces outils, tandis que la qualité dépend surtout de leur compétence initiale et de leur capacité à superviser.
- L'IA permet de se concentrer sur l'architecture et la conception plutôt que sur les détails mécaniques : moins de temps sur le boilerplate et les tâches répétitives signifie plus de temps pour des décisions d'ingénierie critiques.
- Les tests et la validation deviennent plus accessibles et puissants : générer des tests extensifs, des vérifications de propriétés et des validations multicouches est maintenant économique et peut remplacer la relecture manuelle de code.
- L'IA force une meilleure organisation du code : structurer le code en modules et composants petits et testables devient naturellement plus efficace avec les agents, améliorant globalement la maintenabilité.
- Les frameworks de validation robustes créent une responsabilité sans dépendre de la perfection du code : on peut obtenir de bons résultats même avec du code imparfait grâce à des tests, des métriques et des vérifications interlockées.

**Avis négatifs** :
- Le modèle n'a pas de responsabilité professionnelle : contrairement aux humains, les IA n'ont pas de réputation à perdre, pas de fierté ou de propriété du code, ce qui crée un différentiel de motivation dangereux pour la qualité.
- La vérification devient cognitive et inévitable : le code généré est trop abondant pour être lu manuellement, et les erreurs subtiles (bugs logiques, failles de sécurité, choix architecturaux douteux) se dissimulent dans du code apparemment correct.
- Le risque d'une spirale de qualité décroissante : si les LLM ne voient que du code généré par d'autres LLM moins bons, la qualité continue de se dégrader; de plus, les pressions commerciales pour livrer fast risquent de dominer les considérations d'architecture.
- La perte du loop d'apprentissage par la pratique : écrire du code est un moyen d'apprendre et de construire une intuition ; ne faire que superviser les agents affaiblit la capacité des développeurs à détecter les vrais problèmes.
- L'absence de normes commune crée du chaos : sans processus strict, les organisations versent rapidement dans du code ésotérique, mal compris, dépendant des fournisseurs d'IA et coûteux à modifier ou maintenir.

**Top commentaires** :

- [jwpapi](https://news.ycombinator.com/item?id=48043423) : « I know full well that if you ask Claude Code to build a JSON API endpoint that runs a SQL query and outputs the results as JSON, it’s just going to do it right. It’s not going to mess that up. You have it add automated tests, you have it add documentation, you know it’s going to be good. » I feel…
- [etothet](https://news.ycombinator.com/item?id=48037871) : Vibe Coding \(and LLMs\) did not create undisciplined engineering organizations or engineers. They exposed and accelerated them. Plenty of engineers have loose \(or no!\) standards and practices over how they write coee. Similarly, plenty of engineering teams have weak and loose standards over how code…
- [zarzavat](https://news.ycombinator.com/item?id=48037827) : Perhaps I've missed a few weeks worth of progress, but I don't think that AIs have become more trustworthy, the errors are just more subtle. If the code doesn't compile, that's easy to spot. If the code compiles but doesn't work, that's still somewhat easy to spot. If the code compiles and works, b…

---

[Article original](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/) · [Discussion HN](https://news.ycombinator.com/item?id=48037128)
