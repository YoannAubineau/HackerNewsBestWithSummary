---
article_fetched_at: '2026-10-09T00:51:57.816366Z'
attempts: 0
content_source: extracted
discussion_comment_count: 52
discussion_fetched_at: '2026-10-09T00:51:47.797152Z'
error: null
guid: https://news.ycombinator.com/item?id=49986882
hn_item_id: 49986882
hn_url: https://news.ycombinator.com/item?id=49986882
image_url: https://substackcdn.com/image/fetch/$s_!huqE!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea228abe-574d-4d58-9922-775c987f1f7b_1920x1080.webp
is_ask_or_show_hn: false
llm_input_tokens: 6770
llm_latency_ms: 11648
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 855
our_published_at: '2026-10-09T00:18:56Z'
rewritten_title: Créer un tableau de bord Home Assistant avec une illustration dessinée
  à la main
source_published_at: '2026-10-07T01:41:03Z'
status: summarized
summarized_at: '2026-10-09T00:54:11.445000Z'
title: I hired an illustrator to draw my house. Now it's my Home Assistant dashboard
url: https://antonfrolov.substack.com/p/i-hired-an-illustrator-to-draw-my
---

## Résumé de l'article

Home Assistant est une plateforme domotique open-source. L'auteur a engagé un illustrateur pour transformer sa maison en illustration interactive servant de tableau de bord, permettant à toute la famille de contrôler les appareils intelligents de manière visuelle et attrayante.

- L'auteur a documenté précisément les besoins techniques pour l'illustrateur : plans architecturaux, photos de référence, fichiers PNG avec transparence pour chaque appareil en version jour/nuit, et animations WebP des états « allumé/éteint ».
- Le tableau de bord utilise la carte « picture-elements » de Home Assistant : l'illustration est le fond, et les appareils/capteurs sont positionnés par-dessus avec des changements d'image selon leur état (animations WebP lues automatiquement par le navigateur).
- Un mode jour/nuit bascule automatiquement au coucher/lever du soleil, avec des versions distinctes de l'illustration pour chaque état.
- L'ensemble de la maison s'affiche sur un écran TV via un module HAOS Kiosk Display, tandis que des vues individuelles par étage restent accessibles sur téléphones et ordinateurs.
- La configuration YAML permet de réutiliser les éléments entre plusieurs vues sans duplication, et les fichiers hébergés localement se rechargent facilement après modification.

## Discussion sur Hacker News (52 commentaires)

**Avis positifs** :
- L'approche d'embaucher un illustrateur humain est louable et a produit un résultat visuellement magnifique qui transforme l'interface de contrôle domotique en quelque chose de bien plus attrayant qu'un tableau de bord standard
- C'est un projet de bricolage créatif et personnel qui montre comment combiner design et technologie de manière pratique; les conseils sur les calques pour l'animation sont utiles pour la communauté
- Le coût n'est pas prohibitif (quelques centaines de dollars) pour rémunérer des artistes ayant besoin de portfolios, contrairement à l'idée que seul le 1% peut se l'offrir
- La visualisation sur un plan de maison rend la domotique plus intuitive et accessible que des listes de commandes abstraites, particulièrement pour localiser rapidement les interrupteurs et thermostats

**Avis négatifs** :
- L'illustrateur n'a pas reçu un crédit suffisamment prominent dans l'article pour le travail réalisé, ce qui questionne la valeur accordée au travail humain
- Le coût de 900$ pour une illustration est considérable pour la plupart des gens et rend la solution peu accessible malgré les prétentions contraires; l'IA aurait probablement pu produire un résultat équivalent à coût quasi nul
- Cette approche déclenche inévitablement des demandes d'imitations par IA, ce qui pourrait dévaluer le travail des illustrateurs et éroder le style artistique
- Désactiver complètement la climatisation lors d'une absence peut être moins efficace énergétiquement que d'ajuster simplement la température désirée

**Top commentaires** :

- [ideasphere](https://news.ycombinator.com/item?id=50012378) : This is the illustrator: https://linktr.ee/owenyeconiel It’s cool they hired an actual person but if I was so happy with their work to write-up a whole article about it, I’d be crediting them in a much more prominent way!
- [topham](https://news.ycombinator.com/item?id=50014372) : "When everyone leaves, all the air conditioners switch off." That's often substantially more inefficient than keeping it at the temperature desired, or adjusting the desired temperature to mitigate it somewhat.
- [palmotea](https://news.ycombinator.com/item?id=50012723) : 1. Hiring a human illustrator is the right thing to do, and I applaud this guy. 2. AI kinda ruined this style for me. The first thing I did when I saw it was start searching for AI incongruities which is sad.

---

[Article original](https://antonfrolov.substack.com/p/i-hired-an-illustrator-to-draw-my) · [Discussion HN](https://news.ycombinator.com/item?id=49986882)
