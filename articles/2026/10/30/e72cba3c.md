---
article_fetched_at: '2026-10-30T16:53:39.958200Z'
attempts: 0
content_source: extracted
discussion_comment_count: 140
discussion_fetched_at: '2026-10-30T16:53:34.373340Z'
error: null
guid: https://news.ycombinator.com/item?id=50296486
hn_item_id: 50296486
hn_url: https://news.ycombinator.com/item?id=50296486
image_url: https://labs.ycombinator.com/og.png
is_ask_or_show_hn: false
llm_input_tokens: 15298
llm_latency_ms: 9331
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1070
our_published_at: '2026-10-30T16:32:17Z'
rewritten_title: Des essaims d'agents IA testés dans Minecraft et Mindustry révèlent
  des différences de collaboration
source_published_at: '2026-10-29T21:40:28Z'
status: summarized
summarized_at: '2026-10-30T16:55:12.835428Z'
title: We ran AI agent swarms in Minecraft and Mindustry
url: https://labs.ycombinator.com/projects/games/index.html
---

## Résumé de l'article

Des chercheurs en IA ont exécuté des expériences avec des essaims d'agents IA (Claude et GPT) dans deux environnements de jeu : Minecraft et Mindustry. Ces environnements permettent d'étudier comment les agents multi-IA se coordonnent, communiquent et développent des hiérarchies face à des objectifs collectifs.

- Dans Minecraft, 50 agents GPT ont bâti une mini-civilisation gouvernée par des règles, un système de rationnement alimentaire et des rôles spécialisés, mais sont devenus progressivement très prudents après les premières morts.
- Aux Bed Wars, les agents GPT ont adopté une stratégie agressive et coordonnée (remportant 6 victoires sur 9) tandis que les Claude ont joué défensivement et ont été vaincus malgré une supériorité en nombre de morts.
- En Mindustry, les GPT se sont comportés comme un essaim collectif utilisant une communication condensée et hautement collaborative, tandis que les Claude ont conservé un leadership centralisé et une communication plus démocratique (votes par « +1 »).
- Les GPT ont montré plus d'initiative face aux obstacles, notamment en récupérant le code source du jeu sur le web pour l'analyser et adapter leurs stratégies.
- Les résultats suggèrent des différences fondamentales dans la manière dont les modèles d'IA forment des hiérarchies, communiquent et s'adaptent en groupe, avec des implications pour la compréhension de l'alignement multi-agents.

## Discussion sur Hacker News (140 commentaires)

**Avis positifs** :
- L'expérience met en lumière des phénomènes sociaux intéressants : les agents développent des protocoles, créent leur propre langage compressé et montrent des comportements bureaucratiques humains, ce qui révèle comment les LLM reflètent les structures des données d'entraînement.
- Les architectures à plusieurs niveaux (micro/macro, scripts déterministes + LLM pour stratégie) semblent prometteuses et économes en tokens par rapport à laisser les LLM contrôler chaque action en temps réel.
- L'article démontre que les différences entre modèles (GPT plus agressif, Claude plus défensif) se manifestent clairement même dans les jeux vidéo, validant les observations qualitatives sur les personnalités des modèles.
- Cette expérience offre une plateforme de recherche intéressante pour explorer l'architecture des swarms d'agents et leurs dynamiques de coordination, avec des applications potentielles bien au-delà du gaming.

**Avis négatifs** :
- Les agents sont handicapés par une latence excessive et une architecture pauvre : chaque action requiert un appel complet au modèle, ce qui est impraticable pour les jeux nécessitant des réactions rapides; l'approche fondamentale limite leurs capacités plutôt que d'exposer les limites des LLM.
- Les swarms de 50 agents ne surpassent pas significativement un agent unique ou une approche mieux structurée; la hiérarchie basée purement sur l'ordre alphabétique et l'identité persistante semblent produire plus de bureaucratie que de bénéfices d'efficacité.
- Les agents restent bien inférieurs aux enfants humains pour des tâches simples (casser des blocs, gérer la faim), suggérant que l'approche LLM n'est fondamentalement pas adaptée au gameplay en temps réel comparé aux architectures spécialisées comme celles utilisées par OpenAI Five en 2019.
- La configuration du harness crée des obstacles artificiels : les agents luttent avec des bases absolues d'interaction, de gestion d'outils et de coordination que une meilleure ingénierie du système pourrait résoudre, ce qui rend difficile d'isoler les vraies limites des LLMs.

**Top commentaires** :

- [peri-cl](https://news.ycombinator.com/item?id=50297039) : This is hilarious and adorable. \> "Ada tossed a cooked chicken to Noor; Esme picked it up by accident and ate it. A three-minute "no blame" inquiry produced a written protocol..." They're like super-serious little senior engineers. \(edit: or dining-philosophers\). About how much KV cache do these ki…
- [Kiboneu](https://news.ycombinator.com/item?id=50299592) : If you want to do a version of this yourself quickly -- Install Luanti with Minetest \(open source minecraft\), and instruct your agent to write a mod that gives it network access to the game's Lua interpreter. The agent can then do anything from modifying the world state directly to controlling NPCs…
- [js8](https://news.ycombinator.com/item?id=50302771) : I have been "playing" Graveyard Keeper 2 with AI \(Claude Max\) and I had a blast, it's really a new way to enjoy the game. My approach is a 3-tiered architecture: - There is a mod \(bot\) in the game that handles the fast decisions on sub 1-second timescale; it is also hot-reloadable and gives informa…

---

[Article original](https://labs.ycombinator.com/projects/games/index.html) · [Discussion HN](https://news.ycombinator.com/item?id=50296486)
