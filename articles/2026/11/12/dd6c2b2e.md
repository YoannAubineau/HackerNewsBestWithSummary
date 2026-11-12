---
article_fetched_at: '2026-11-12T01:12:42.880378Z'
attempts: 0
content_source: extracted
discussion_comment_count: 199
discussion_fetched_at: '2026-11-12T01:11:48.914142Z'
error: null
guid: https://news.ycombinator.com/item?id=50455394
hn_item_id: 50455394
hn_url: https://news.ycombinator.com/item?id=50455394
image_url: https://michael.bacarella.com/assets/mbacface.jpg
is_ask_or_show_hn: false
llm_input_tokens: 19971
llm_latency_ms: 9067
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 889
our_published_at: '2026-11-12T00:35:36Z'
rewritten_title: Comment une fausse alarme incendie a failli inonder le seul datacenter
  de Jane Street à New York
source_published_at: '2026-11-11T16:38:44Z'
status: summarized
summarized_at: '2026-11-12T01:15:34.062452Z'
title: A false smoke alarm almost drowned Jane Street's only NYC datacenter
url: https://michael.bacarella.com/2026/11/10/false-smoke-alarm-jane-street-datacenter/
---

## Résumé de l'article

Jane Street, une entreprise de trading quantitatif, gardait son datacenter au cœur de son immeuble de bureaux new-yorkais pour des raisons de sécurité et de contrôle opérationnel. Un incident survenu après une fausse alarme incendie déclenchée par des travaux de construction a failli détruire l'ensemble de l'infrastructure : l'alarme a arrêté les climatiseurs de la salle serveurs, causant une montée critique de température qui risquait d'activer les sprinklers mouillant l'ensemble du matériel.

- Un membre de l'équipe système, qui vivait à 9 minutes à pied du bureau, a reçu l'alerte depuis son appartement et a dû courir jusqu'au datacenter pour débrancher manuellement tous les serveurs avant le seuil critique de 150 °F.
- La température s'est stabilisée à 143,6 °F juste à temps ; l'incident n'a causé qu'un downtime minimal puisque les marchés américains étaient fermés.
- L'entreprise a maintenu sa stratégie de garder les serveurs dans le bâtiment de bureaux plutôt que dans un datacenter distant, en renforçant les procédures de surveillance.
- L'équipe a développé un système de monitoring en OCaml interrogeant directement tous les serveurs Linux pour surveiller les surchauffes potentielles du datacenter.

## Discussion sur Hacker News (199 commentaires)

**Avis positifs** :
- L'article met en lumière l'importance cruciale de la planification des urgences et de la résilience des infrastructures critiques, même pour les entreprises réputées.
- Les commentaires valident l'aspect humain et l'ingéniosité face aux crises : l'équipe a su improviser et réagir rapidement face à une défaillance système complexe.
- Plusieurs anecdotes (Hurricane Sandy, Fog Creek) confirment que les datacenter en milieu urbain sont vulnérables aux risques naturels et nécessitent une vraie stratégie de continuité de service.
- Les discussions soulignent que les alarmes incendie connectées aux systèmes de refroidissement peuvent créer des boucles dangereuses et qu'il faut des protections contre ces défaillances en cascade.

**Avis négatifs** :
- La gestion du personnel d'on-call basée sur la proximité géographique est une mauvaise pratique : plusieurs commentaires rapportent avoir été exploités pour des tâches non rémunérées simplement parce qu'ils vivaient près du bureau.
- Utiliser des sprinklers dans un datacenter d'immeuble de bureaux est critiqué comme inefficace : le choix entre incendie ou inondation n'est pas satisfaisant comparé à des systèmes de suppression gaz ou inerte.
- L'anecdote de Hurricane Sandy illustre que célébrer des efforts héroïques masque des défaillances de planification graves : les vraies solutions sont la redondance géographique et la maintenance préventive, pas les barrel brigades.
- Les commentaires soulignent que l'absence de bouton EPO (Emergency Power Off) automatisé et de monitoring adéquat relève d'une infrastructure insuffisamment mature pour un datacenter professionnel en 2012.

**Top commentaires** :

- [reticulates](https://news.ycombinator.com/item?id=50455814) : The article reminds me of when Hurricane Sandy took out a bunch of New York DCs with 3+ feet of water and people were carrying diesel up stairs to keep generators running. “The superhuman folks at the data center are hauling 55 gallon drums of diesel fuel up 17 flights of stairs. Assuming they're a…
- [hackermailman](https://news.ycombinator.com/item?id=50455625) : In the article he talks about living within a few minutes walk to work and telling too many people so they made him the emergency office guy. Same thing happened to me, foolishly told everyone hey I can see my apartment from here so I would get panicked calls to run in and shut down servers because…
- [rdl](https://news.ycombinator.com/item?id=50455993) : Odd that they didn't have at minimum 1\) a physical Emergency Power Off \(EPO\) button inside the datacenter, such that one button could de-energize everything -- usually required as part of building a datacenter due to code variance for the "low voltage" \(\<4000V in this context...\) wiring. 2\) EPO int…

---

[Article original](https://michael.bacarella.com/2026/11/10/false-smoke-alarm-jane-street-datacenter/) · [Discussion HN](https://news.ycombinator.com/item?id=50455394)
