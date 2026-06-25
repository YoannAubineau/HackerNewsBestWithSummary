---
article_fetched_at: '2026-06-25T07:08:18.809276Z'
attempts: 0
content_source: extracted
discussion_comment_count: 183
discussion_fetched_at: '2026-06-25T07:08:17.019923Z'
error: null
guid: https://news.ycombinator.com/item?id=48660178
hn_item_id: 48660178
hn_url: https://news.ycombinator.com/item?id=48660178
image_url: https://blogs.nvidia.com/wp-content/uploads/2026/06/45CLiquidCooling.jpg
is_ask_or_show_hn: false
llm_input_tokens: 17832
llm_latency_ms: 14980
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1236
our_published_at: '2026-06-25T06:26:15Z'
rewritten_title: Les serveurs IA refroidis à 45°C réduisent la consommation d'eau
  des data centers à presque zéro
source_published_at: '2026-06-24T14:10:11Z'
status: summarized
summarized_at: '2026-06-25T07:08:49.029115Z'
title: 45°C cooling design cuts data center water use to near zero
url: https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/
---

## Résumé de l'article

NVIDIA a développé une architecture de refroidissement par liquide à 45°C pour ses serveurs IA Rubin, capable de réduire drastiquement la consommation d'eau et d'énergie des data centers. Cette technologie représente le premier système d'IA avec refroidissement liquide intégral, où chaque composant est refroidi par un circuit fermé sans ventilateurs.

- Le refroidissement liquide à 45°C (113°F) élimine pratiquement toute consommation d'eau : réduction de 2,6 millions de gallons par mégawatt par an à quasi zéro dans les climats favorables
- Le refroidissement représentait jusqu'à 40% de la consommation électrique des data centers ; augmenter la température d'un degré peut réduire les coûts de 4%, soit plus de 4 millions de dollars annuels d'économies pour une installation de 50 mégawatts
- L'architecture élimine les ventilateurs de refroidissement (réduction du bruit) et les configurations « allées chaudes/froides », permettant une plus haute densité de racks (6 unités comprimées en 2)
- Le liquide de refroidissement (75% eau, 25% propylène glycol) capture la chaleur directement aux puces et la transporte vers des radiateurs secs externes ; en climat froid, aucun refroidisseur mécanique n'est nécessaire
- Cette efficacité énergétique devient critique car la demande de calcul pour l'IA croît plus vite que presque toute autre catégorie d'infrastructure

## Discussion sur Hacker News (183 commentaires)

**Avis positifs** :
- La conception à 45°C réduit significativement la consommation énergétique des datacenters grâce à des échangeurs de chaleur plus efficaces, ce qui diminue aussi indirectement la consommation d'eau liée à la production d'électricité.
- Le système offre des opportunités de valorisation locale via le chauffage urbain : les communautés pourraient bénéficier de quelques millions de dollars par an en énergie thermique gratuite, transformant un impact négatif potentiel en avantage économique.
- L'innovation adresse deux plaintes majeures des régions : l'élimination quasi-totale de la consommation d'eau (comparée au refroidissement par évaporation actuel) et la réduction du bruit des ventilateurs puisque le système ne repose pas sur le refroidissement par air.
- Cette approche est techniquement viable : les universités allemandes et d'autres institutions l'utilisent déjà avec succès, et les calculs théoriques montrent un COP supérieur à 20, bien meilleur que les systèmes traditionnels.
- Le refroidissement liquide à haute température permet une meilleure utilisation locale de la chaleur résiduelle pour le chauffage des bâtiments en hiver, où les besoins énergétiques dépassent largement ceux de l'été.

**Avis négatifs** :
- Les affirmations de « consommation d'eau quasi-nulle » sont trompeuses : elles ne comparent que l'eau d'évaporation immédiate, ignorant que la majorité de l'eau consommée par les datacenters provient indirectement de la production électrique, et que ces systèmes requièrent toujours un premier remplissage.
- La technologie du refroidissement liquide complet n'est pas vraiment innovante : Cray utilisait déjà cette approche dans les années 1980, et les datacenters disposent depuis longtemps de solutions équivalentes. Il s'agit plutôt d'optimisation marketing que de rupture technologique.
- Le système dépend fortement du climat local : il ne fonctionne efficacement que si la température extérieure reste en dessous de ~37°C, nécessitant quand même des tours de refroidissement ou compresseurs actifs dans les régions chaudes, où le besoin s'en ferait le plus sentir.
- Les allégations environnementales servent probablement à contrer les critiques publiques plutôt que de représenter un changement systémique. Cette démarche ressemble à du « greenwashing » permettant aux datacenters de continuer à se développer avec peu de restrictions réelles.
- Les impacts locaux demeurent : les microclimats thermiques générés, le bruit des équipements externes pour refroidir l'eau de 55°C à 45°C, et l'implantation dans des zones aux ressources limitées restent des problèmes non résolus malgré cette innovation.

**Top commentaires** :

- [amluto](https://news.ycombinator.com/item?id=48661501) : This opens up an interesting synergy: district heating. 45C is low but not unworkable for a district heating loop, and a data center might be able to make a nice pitch to a community if the data center offers to provide heat to a district heating system for free. This brings the value to the local…
- [why\_at](https://news.ycombinator.com/item?id=48666419) : Maybe I'm being dumb, but I don't understand what the innovation is here. I get that they're using liquid coolant at higher than usual temperatures, but why couldn't they do that before? Most of the comparison in the article is for air cooled datacenters but what about other liquid cooled ones? Sur…
- [kayo\_20211030](https://news.ycombinator.com/item?id=48665764) : « In favorable climates, NVIDIA’s 45-degree liquid-cooling architecture .... » What's a favorable climate, apart from, obviously, Greenland? The piece is a little light on details on the correlation between outside temperatures and efficiency & cost. It'd be nice to see even a broad-strokes discuss…

---

[Article original](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) · [Discussion HN](https://news.ycombinator.com/item?id=48660178)
