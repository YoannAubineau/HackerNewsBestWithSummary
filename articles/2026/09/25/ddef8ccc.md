---
article_fetched_at: '2026-09-25T20:54:31.368061Z'
attempts: 0
content_source: extracted
discussion_comment_count: 177
discussion_fetched_at: '2026-09-25T20:54:29.112986Z'
error: null
guid: https://news.ycombinator.com/item?id=49839664
hn_item_id: 49839664
hn_url: https://news.ycombinator.com/item?id=49839664
image_url: https://d1jt649tmk2is2.cloudfront.net/?url=https%3A%2F%2Fjardo.dev%2Fog-previews%2Fwhat-about-rails&w=1200&h=630&sig=d345cfdde64b4770fbc9ef64b69d5bec84e26429c4aaa6d4bbde30ec1a19ece8
is_ask_or_show_hn: false
llm_input_tokens: 24272
llm_latency_ms: 13794
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1028
our_published_at: '2026-09-25T20:36:46Z'
rewritten_title: David Heinemeier Hansson annonce le pivot de Rails vers les LLM et
  quitte la plateforme pour Hey
source_published_at: '2026-09-25T02:50:16Z'
status: summarized
summarized_at: '2026-09-25T20:56:27.814545Z'
title: What About Rails?
url: https://jardo.dev/what-about-rails
---

## Résumé de l'article

David Heinemeier Hansson, créateur de Ruby on Rails, a utilisé le keynote d'ouverture de Rails World 2024 pour annoncer que 37signals réécrit Hey en applications natives utilisant des LLM plutôt que Rails. Il affirme que la programmation manuelle n'est plus économiquement viable et que les humains ne devraient plus lire le code généré par l'IA.

- DHH se décrit désormais comme un « maker » plutôt qu'un programmeur professionnel et soutient que l'anglais est le meilleur langage de programmation pour les LLM
- La nouvelle stratégie de 37signals utilise Rust côté serveur (langage qu'il juge « hideux ») et des applications natives sur tous les plateformes, abandonnant l'approche web-first historique de Rails
- Sa production de code en août (150k lignes) contraste fortement avec sa moyenne pré-LLM (30k/an), Ruby ne représentant que 3% de son travail récent
- L'article critique les comparaisons trompeuses du keynote (Ruby vs Rust, lignes de code, chiffres de productivité) et l'absence de stratégie claire pour Rails au-delà de promesses d'optimisme
- La tension majeure : DHH a quitté Rails lors du principal sommet Rails mondial sans présenter une vision pour l'avenir du framework, ne proposant que des encouragements creux aux développeurs Rails restants

## Discussion sur Hacker News (177 commentaires)

**Avis positifs** :
- Les langages statiquement typés et compilés (Go, Rust) offrent de meilleures performances et sécurité mémoire, particulièrement avantageux pour les agents IA qui génèrent du code sans relecture humaine
- Rails avait pour force principale la productivité développeur ; avec les LLM, cette différence s'efface et d'autres critères (performance, typage, maintenabilité) deviennent primordiaux
- Les LLM changent fondamentalement l'équation : ce qui compte n'est plus la lisibilité pour humains mais l'efficacité en tokens et la capacité des agents à itérer correctement
- La migration vers les apps natives par 37signals pour Hey montre que quand le coût de développement chute drastiquement, les trade-offs historiques (web vs native) se réévaluent
- Rails a eu son époque ; la maturité acquise permet de passer en mode maintenance stable sans innovation disruptive

**Avis négatifs** :
- DHH annonçant l'abandon de Rails depuis la conférence Rails World qu'il a lui-même créée est perçu comme un affront à la communauté qui a bâti l'écosystème
- Les LLM produisent du code avec hallucinations, manquent de compréhension architecturale et créent de la dette technique (requêtes N+1, duplication, pas de séparation des responsabilités) qui ne se révèle que sur la durée
- Affirmer que 'les langages ne comptent plus' ignore que les abstractions bien pensées (map/filter, typage) capturent des concepts que les LLM ont appris ; programmer en assembly directement n'est pas plus efficace
- L'argument des performances est exagéré : la plupart des apps sont I/O-bound (DB, réseau), pas CPU-bound ; optimiser le langage plutôt que les requêtes est un mauvais choix
- Rails reste robuste et mature pour les CRUD et LoB apps ; l'enthousiasme LLM occulte que personne ne lit vraiment le code depuis 20 ans (autocomplétion, outils) et que les réels problèmes résident dans l'UX, la conception produit, pas la pile technique

**Top commentaires** :

- [jeffreyrogers](https://news.ycombinator.com/item?id=49849435) : Most managers don't read the code of their direct reports. They just trust that the code is "good enough" and that there are enough other processes in place to catch bugs before they cause too much damage. I think I'm a pretty skilled programmer, or I'm at least good enough at interviewing to convi…
- [Twey](https://news.ycombinator.com/item?id=49842066) : « 37signals differentiates their products with opinionated UI/UX, not novel features. They are rewriting Hey as six native apps because the web fidelity isn’t good enough. So UI matters enough to justify complete rewrites, but also everyone just wants CLIs? » I've seen this one a few times lately.…
- [captainclam](https://news.ycombinator.com/item?id=49845320) : "If every product is used by an agent driving a CLI, what’s going to differentiate Basecamp or Fizzy from the cheapest alternative?" At that point, why even bother with "driving a CLI"? I have a hard time seeing how this all doesn't go away soon. At the current trajectory, I am not seeing a future…

---

[Article original](https://jardo.dev/what-about-rails) · [Discussion HN](https://news.ycombinator.com/item?id=49839664)
