---
article_fetched_at: '2026-05-20T21:33:43.222677Z'
attempts: 0
content_source: extracted
discussion_comment_count: 255
discussion_fetched_at: '2026-05-20T21:33:35.876035Z'
error: null
guid: https://news.ycombinator.com/item?id=48212493
hn_item_id: 48212493
hn_url: https://news.ycombinator.com/item?id=48212493
image_url: https://images.ctfassets.net/kftzwdyauwt9/6WJOhxvdNpC5hDvpiSAqE0/8a11ba6abdabb6a5a674de733cfa710d/SEO-Polynomial-Construction-16x9.png?w=1600&h=900&fit=fill
is_ask_or_show_hn: false
llm_input_tokens: 20979
llm_latency_ms: 15524
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1219
our_published_at: '2026-05-20T21:30:40Z'
rewritten_title: Un modèle d'OpenAI réfute une conjecture centrale en géométrie discrète
source_published_at: '2026-05-20T19:05:30Z'
status: summarized
summarized_at: '2026-06-08T00:06:50.555090Z'
title: An OpenAI model has disproved a central conjecture in discrete geometry
url: https://openai.com/index/model-disproves-discrete-geometry-conjecture/
---

## Résumé de l'article

Un modèle d'OpenAI à usage général a résolu le problème de la distance unitaire dans le plan, une question ouverte depuis 1946 posée par Paul Erdős. Le modèle a disprové la conjecture dominante en découvrant une famille infinie de configurations de points qui dépassent les constructions sur grille carrée, en utilisant des concepts sophistiqués de théorie algébrique des nombres.

- Le problème du distance unitaire demande combien de paires de points peuvent être exactement à distance 1 dans le plan ; pendant 80 ans, on croyait que la grille carrée était essentiellement optimale.
- La preuve générée par l'IA construit des configurations avec au moins n^(4/3+c) paires de distance unitaire pour infinement de valeurs de n, améliorant significativement la limite précédente de ~n√n.
- La solution relie de manière inattendue la théorie algébrique des nombres (corps de nombres, tours de classe infinies, théorie de Golod-Shafarevich) à un problème élémentaire de géométrie euclidienne.
- Il s'agit de la première fois qu'un problème ouvert majeur au cœur d'un domaine mathématique actif est résolu autonomement par l'IA, marquée par les commentaires élogieux du médaillé Fields Tim Gowers et du théoricien des nombres Arul Shankar.
- Des mathématiciens externes ont vérifié la preuve et rédigé un article compagnon, révélant que la connexion improbable entre théorie des nombres et géométrie discrète pourrait inspirer de nouvelles recherches sur d'autres problèmes ouverts.

## Discussion sur Hacker News (255 commentaires)

**Avis positifs** :
- OpenAI a déjà établi une domination académique claire via des efforts de distribution gratuite aux universités et chercheurs, tandis que les modèles Gemini et Claude présentent des forces alternatives mais moins orientées vers la recherche mathématique pure
- L'IA pourrait démultiplier la productivité scientifique en synthétisant rapidement des décennies de littérature, expliquant des concepts complexes et traversant les domaines spécialisés, réduisant ainsi les barrières cognitives entre disciplines
- Cette preuve démontre que les LLMs ne font pas que recopier leurs données d'entraînement : ils effectuent une recombinais genuinely novel de concepts existants, ce qui n'est fondamentalement pas différent de la créativité humaine selon les philosophies dominantes
- La capacité du modèle à appliquer des outils d'algèbre théorique numéraire à un problème de géométrie combinatoire simple montre une véritable capacité de transfert interdisciplinaire, bien au-delà d'une simple interpolation
- Ce résultat avec un modèle général (sans spécialisation mathématique) ouvre la voie à une évolution rapide : les LLMs pourraient bientôt être entraînés spécifiquement sur Lean et des structures formelles pour profondeur et rigueur accrues

**Avis négatifs** :
- La preuve n'est pas constructive : elle prouve l'existence d'une meilleure solution sans montrer comment la construire, ce qui limite l'impact pratique et diffère qualitativement de la théorie-création humaine qui innove profondément
- L'absence de visualisation, d'explication accessible et d'attribution claire des résultats antérieurs dans le texte principal révèle une communication marketing faible et soulève des questions sur la transparence réelle du processus
- Les LLMs restent profondément limités hors des domaines technique : incapables de conjectures originales, de pensée véritable hors des faits établis, et de générer des insights sans base textuelle, contredisant les prétentions d'une intelligence générale
- La preuve n'a pas été vérifiée formellement en Lean et reste une preuve en langage naturel validée manuellement par des experts humains, rappelant que ces modèles dépendent toujours de l'infrastructure humaine pour la vérification rigoureuse
- Le coût et les ressources computationnelles massives (125 pages de réflexion, entraînement coûteux) contrastent fortement avec la facilité affichée, et la question demeure : combien de problèmes mathématiques ont été tentés avant ce succès ?

**Top commentaires** :

- [m-hodges](https://news.ycombinator.com/item?id=48213071) : To the “LLMs just interpolate their training data” crowd: Ayer, and in a different way early Wittgenstein, held that mathematical truths don’t report new facts about the world. Proofs unfold what is already implicit in axioms, definitions, symbols, and rules. I think that idea is deeply fascinating…
- [lubujackson](https://news.ycombinator.com/item?id=48213163) : For anyone using LLMs heavily for coding, this shouldn't be too surprising. It was just a matter of time. Mathematicians make new discoveries by building and applying mathematical tools in new ways. It is tons of iterative work, following hunches and exploring connections. While true that LLMs can'…
- [vatsachak](https://news.ycombinator.com/item?id=48212866) : As I have stated before, AI will win a fields medal before it can manage a McDonald's A difficult part was constructing a chess board on which to play math \(Lean\). Now it's just pattern recognition and computation. LLMs are just the beginning, we'll see more specialized math AI resembling StockFish…

---

[Article original](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) · [Discussion HN](https://news.ycombinator.com/item?id=48212493)
