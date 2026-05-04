---
article_fetched_at: '2026-05-04T00:25:46.381160Z'
attempts: 0
content_source: extracted
discussion_comment_count: 85
discussion_fetched_at: '2026-05-04T00:25:45.411005Z'
error: null
feed_summary: '<p>Article URL: <a href="https://isene.org/2026/05/Audience-of-One.html">https://isene.org/2026/05/Audience-of-One.html</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=47997947">https://news.ycombinator.com/item?id=47997947</a></p>

  <p>Points: 207</p>

  <p># Comments: 76</p>'
guid: https://news.ycombinator.com/item?id=47997947
hn_item_id: 47997947
hn_url: https://news.ycombinator.com/item?id=47997947
is_ask_or_show_hn: false
llm_input_tokens: 8563
llm_latency_ms: 14457
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1122
our_published_at: '2026-05-03T23:34:07Z'
rewritten_title: Un développeur remplace progressivement tous ses outils par des versions
  qu'il a conçues lui-même
source_published_at: '2026-05-03T15:32:05Z'
status: summarized
summarized_at: '2026-05-04T00:26:07.561909Z'
title: A desktop made for one
url: https://isene.org/2026/05/Audience-of-One.html
---

## Résumé de l'article

Un développeur décrit son expérience de construction d'un environnement informatique personnel entièrement customisé sur vingt-cinq ans, remplaçant les logiciels standards par des outils qu'il a développés lui-même. Grâce aux outils modernes comme Rust et Claude Code, il a pu accomplir en quelques jours ou semaines ce qui aurait pris des années auparavant.

- Le développeur a remplacé vim après 25 ans d'utilisation par « scribe », un éditeur modal personnalisé qu'il a créé en 72 heures, conservant les features essentielles et ajoutant des améliorations spécifiques à son flux de travail
- Son système actuel repose sur CHasm (couche d'assemblage x86_64 pure), Fe₂O₃ (couche applicative en Rust), avec seulement WeeChat et Firefox comme logiciels tiers conservés
- La baisse du coût de développement logiciel grâce aux frameworks modernes et à l'IA rend maintenant viable la création d'outils personnalisés en quelques soirées au lieu de années
- Ces outils ne sont pas destinés au partage public : ils sont volontairement construits pour une seule personne, sans besoin de configurabilité, documentation ou support utilisateur
- L'avantage majeur : éliminer la complexité logicielle liée à l'accommodation d'utilisateurs multiples permet de créer des outils plus petits, rapides et précisément adaptés au flux personnel

## Discussion sur Hacker News (85 commentaires)

**Avis positifs** :
- Le concept de logiciel extrêmement personnalisé (« home-cooked software ») représente une révolution : chacun peut désormais se créer des outils parfaitement adaptés à ses besoins spécifiques sans investissement massif en temps ou argent
- Les gains de performance et d'efficacité sont mesurables : utilisation très légère des ressources (5-6W au lieu de 9W), démarrage instantané, absence de dépendances inutiles, ce que les langages traditionnels peinent à égaler
- Cette approche libère la créativité et l'apprentissage : pas besoin de polir le code pour d'autres, on peut explorer des territoires techniques inconnus sans crainte, et les temps d'itération (5-15 minutes) rendent les projets hobby vraiment viables
- Les APIs et standards ouverts restent critiques : même avec du logiciel personnel généré, l'interopérabilité, les bibliothèques solides et les outils déterministes deviennent plus importants, créant un nouveau marché
- L'accélération des petits projets compense largement le coût des tokens : 60h de travail personnel + Claude Max pour une suite logicielle complète est un rapport prix/valeur imbattable en comparaison historique

**Avis négatifs** :
- Le style d'écriture de l'article présente des marqueurs caractéristiques d'une génération LLM (« Claudeslop »), ce qui soulève des questions de fiabilité et d'authenticité du contenu au-delà du projet technique lui-même
- Dépendre fortement des LLMs pour du code critical crée un risque : on maîtrise mal ce qu'on n'a pas écrit soi-même, ce qui limite la capacité à déboguer, modifier ou adapter le code par la suite
- Les risques de sécurité liés au logiciel artisanal généré en masse ne doivent pas être minimisés : absence d'audit collectif, d'expertise distribuée et de revues de sécurité comme pour les projets maintenus professionnellement
- Cette tendance ne devrait pas éclipser la réalité historique : les développeurs créaient déjà du logiciel personnel avant les LLMs, le vrai frein était probablement la motivation ou la gestion du temps, pas la capacité technique
- Le risque d'une fragmentation logicielle extrême : millions d'applications incompatibles et non maintenables à long terme, chacune optimisée pour un seul utilisateur, pourrait créer des cauchemars d'intégration et de pérennité

**Top commentaires** :

- [redfloatplane](https://news.ycombinator.com/item?id=47999529) : I \(and I'm sure many others\) have been thinking about this a lot over the last couple of months. I called it "Extremely Personal Software" in a blog post a few months ago \(https://redfloatplane.lol/blog/14-releasing-software-now/\) but there are lots of names and concepts floating about for the same…
- [blks](https://news.ycombinator.com/item?id=48003039) : This is nice, but is also leagues away from something you’re written yourself. Take LLMs out of equation, and you have piles of code that you barely recognise and barely can edit or tweak by yourself.
- [cadamsdotcom](https://news.ycombinator.com/item?id=48002902) : This is really exciting. Some of the folks who make things will go on to make things that suit not just their preferences but also those of a small audience. Some of those audiences will go on to grow and grow and disrupt the big players. The capital intensive part of software construction is melti…

---

[Article original](https://isene.org/2026/05/Audience-of-One.html) · [Discussion HN](https://news.ycombinator.com/item?id=47997947)
