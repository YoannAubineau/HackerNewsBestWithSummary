---
article_fetched_at: '2026-10-17T17:39:30.899651Z'
attempts: 0
content_source: extracted
discussion_comment_count: 104
discussion_fetched_at: '2026-10-17T17:39:24.709357Z'
error: null
guid: https://news.ycombinator.com/item?id=50118688
hn_item_id: 50118688
hn_url: https://news.ycombinator.com/item?id=50118688
image_url: https://starskirmish.com/assets/og.png
is_ask_or_show_hn: false
llm_input_tokens: 11841
llm_latency_ms: 12967
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1063
our_published_at: '2026-10-17T17:32:19Z'
rewritten_title: 'StarSkirmish Bench v0.2 : les LLMs créent des bots StarCraft en
  une heure'
source_published_at: '2026-10-16T14:18:44Z'
status: summarized
summarized_at: '2026-10-17T17:40:30.877669Z'
title: 'Show HN: Gemini 4 Argon plays StarCraft'
url: https://starskirmish.com/bench/v0-2/
---

## Résumé de l'article

StarSkirmish Bench est un benchmark qui évalue la capacité des grands modèles de langage à écrire des bots StarCraft compétitifs en une heure. Les modèles reçoivent un squelette de bot Protoss en C++ et des outils pour compiler, jouer des parties d'entraînement et analyser les résultats, avant d'être notés sur leur taux de victoire contre des bots écrits par des humains et d'autres LLMs.

- GPT-6 Astra obtient le meilleur score (v0.2), suivi de GPT-6.1 Sol, tandis que Gemini 4 Argon, Claude Opus 5.5 et Claude Fable 5.1 sont à peu près au même niveau (37-39 points)
- GPT-6.1 Sol offre le meilleur rapport qualité-prix, classé deuxième mais coûtant dix fois moins cher par exécution que GPT-6 Astra
- Les bots humains écrits (Stardust, PurpleWave, BananaBrain) dominent largement : même le meilleur LLM ne gagne que 7 % de ses parties contre eux
- Le principal prédicteur de performance est le nombre de parties d'entraînement contre les 7 bots les plus forts du roster : les meilleurs modèles pratiquent tôt contre des adversaires difficiles
- Gemini 4 Argon affiche une variance d'exécution beaucoup plus élevée que les autres flagships (écart de 18 points entre ses meilleures et pires exécutions, contre 8-9 pour GPT-6 Astra et Claude Opus 5.5)

## Discussion sur Hacker News (104 commentaires)

**Avis positifs** :
- C'est un benchmark intéressant avec contrainte temporelle (1 heure), ce qui est rare et plus réaliste que d'autres évaluations d'IA.
- Les résultats montrent des corrélations significatives avec d'autres benchmarks (Go, programmation olympiade, tâches ML), suggérant que cela mesure une forme d'intelligence générale chez les LLM.
- Le benchmark révèle des capacités d'adaptation intéressantes : les modèles changent de stratégie face à des opposants plus forts (passage du Dragoon au proxy gate rush, puis aux Dark Templar).
- Les bots générés ne reproduisent pas simplement le code d'entraînement : l'analyse du code montre des approches modulaires et fonctionnelles distinctes des bots humains existants.
- C'est une excellente démonstration de ce que les LLMs peuvent accomplir dans la génération de code complexe avec des délais stricts.

**Avis négatifs** :
- Le benchmark mesure trop de choses à la fois (génération de code, analyse logique, compréhension du jeu, stratégie) sans clarifier les proportions de chacune, ce qui rend difficile l'interprétation des résultats.
- Les performances médiocres contre les bots S-tier (1-10% de taux de victoire) suggèrent que les modèles ne font que reproduire ou adapter légèrement du code d'entraînement plutôt que d'innover réellement.
- Le format favorise les stratégies simplifiées et réductrices (rushes, jeux à court terme) plutôt que la compréhension profonde du jeu, ce qui biaise l'évaluation.
- L'absence de code source d'opposants et les limitations du harness (pas d'accès web) rendent difficile la comparaison équitable avec les vraies compétitions de bots.
- Les résultats sont fortement dépendants du harness utilisé (CLI, outils disponibles, niveaux de reasoning), ce qui rend difficile la généralisation des conclusions sur les capacités réelles des modèles.

**Top commentaires** :

- [GodelNumbering](https://news.ycombinator.com/item?id=50119857) : Wow this is interesting to me from another angle. A friend of mine created a benchmark to evaluate LLMs on 9x9 Go \(using KataGo opponents as Elo anchors\) \[1\]. The relative rankings of this \(StarSkirmish Bench v0.2\) benchmark \(GPT-6 Astra \> GPT-6.1 Sol \> Gemini 4 Argon \> Claude Opus 5.5 \> Claude Fab…
- [gritzko](https://news.ycombinator.com/item?id=50130727) : StarCraft probably has hundreds of bot implementations lying on GitHub. Which makes this bench a recall-from-the-training-set competition, essentially. I tried that method on old games that certainly do not have a ton of bot implementations on GitHub. It revealed some interesting aspects about LLM…
- [cgearhart](https://news.ycombinator.com/item?id=50119842) : Is there anything interesting to learn from the agent written bots? Or are they just inferior versions of the best bots because the time limit is so short? Is there any indication that they’re trained on the code from the human written bots \(like, do they magically “guess” creating functionality th…

---

[Article original](https://starskirmish.com/bench/v0-2/) · [Discussion HN](https://news.ycombinator.com/item?id=50118688)
