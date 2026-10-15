---
article_fetched_at: '2026-10-15T06:46:02.444600Z'
attempts: 0
content_source: extracted
discussion_comment_count: 128
discussion_fetched_at: '2026-10-15T06:45:59.782244Z'
error: null
guid: https://news.ycombinator.com/item?id=50094694
hn_item_id: 50094694
hn_url: https://news.ycombinator.com/item?id=50094694
image_url: https://sunshowers.io/images/og-image.png
is_ask_or_show_hn: false
llm_input_tokens: 9892
llm_latency_ms: 12090
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1055
our_published_at: '2026-10-15T06:17:16Z'
rewritten_title: Le système de contrôle de version Scion d'Anthropic s'inspire fortement
  de Mononoke
source_published_at: '2026-10-14T20:30:54Z'
status: summarized
summarized_at: '2026-10-15T06:46:42.041611Z'
title: Anthropic's Scion is heavily inspired by Mononoke
url: https://sunshowers.io/posts/anthropic-mononoke/
---

## Résumé de l'article

Anthropic a lancé Scion, un nouveau système de contrôle de version utilisant le concept de « données dérivées » pour optimiser des opérations comme les blâmes. Ce concept et cette approche sont largement inspirés par Mononoke, un serveur de contrôle de source open source développé par une équipe chez Meta (dont l'auteur du message), qui avait déjà appliqué cette même stratégie autour de 2017-2018.

- Scion reproduit le design de Mononoke en utilisant les « données dérivées » pour améliorer l'efficacité des opérations de contrôle de version, une idée que l'équipe Meta a développée il y a plus d'une décennie
- Anthropic a crédité Sapling pour ses « leçons difficiles » mais n'a pas mentionné Mononoke, ce que l'auteur considère comme frôlant le plagiat
- Les LLM comme Claude indexent probablement Mononoke et d'autres designs existants depuis leur formation sur d'énormes corpus de textes publics, y compris le code open source
- L'auteur ne s'oppose pas à ce qu'Anthropic reprenne le design de Mononoke, mais souligne que l'attribution des crédits est maintenant plus facile et plus importante, notamment à mesure que les LLM guident la conception de nouveaux systèmes

## Discussion sur Hacker News (128 commentaires)

**Avis positifs** :
- L'open source a toujours visé à permettre la réutilisation et l'amélioration des idées existantes ; critiquer une entreprise pour s'inspirer de logiciels open source va à l'encontre de cet objectif fondamental.
- Anthropic a mentionné Sapling comme source d'inspiration dans son annonce, et Mononoke est un composant de Sapling, ce qui constitue une attribution appropriée du contexte.
- Les grandes organisations (Google, Meta) construisent depuis longtemps leurs propres systèmes de contrôle de versions pour supporter les monorepos massifs ; Anthropic suit simplement un pattern établi face à des défis d'échelle réels.
- Il est courant que les ingénieurs de grandes tech réutilisent les solutions qu'ils ont déjà développées dans leurs emplois précédents ; c'est un processus naturel de transfert de connaissances.
- La réimplémentation de zéro est légalement admissible et conforme aux licences open source ; les cadres juridiques des années 1980 établissent clairement que cela ne viole pas les droits d'auteur.

**Avis négatifs** :
- Bien que légalement acceptable, citer explicitement la source d'inspiration serait une question de décence basique et de normes éthiques ; l'omission de mention de Mononoke dans l'annonce apparaît délibérée.
- Anthropic a pointé directement Claude vers le code de Mononoke pour le réingéniérer, confirmé en correspondance privée ; cela va bien au-delà d'une simple inspiration et ressemble davantage à du plagiat assisté par IA.
- La couverture médiatique visant à présenter cela comme une innovation des agents pour l'ère de l'IA sert clairement une stratégie de valorisation IPO plutôt que de refléter une véritable nécessité technique.
- Les modèles d'IA « blanchissent » la provenance en regénérant du code à partir de données d'entraînement ; cela risque de réduire les incitations à partager ouvertement des idées et d'éroder la collaboration diverse dans l'écosystème.
- Le post d'Anthropic omet les noms complets des contributeurs et ne compare pas Scion à des systèmes comparables ou à des travaux antérieurs, rendant impossible au lecteur d'évaluer le contexte ou les antécédents du projet.

**Top commentaires** :

- [BryantD](https://news.ycombinator.com/item?id=50095356) : From the Anthropic announcement: “Source control for huge monorepos has prior art, notably Google’s Piper and Meta’s Sapling, so we were able to build Scion with their hard-won lessons in mind.” Mononoke is a component of Sapling, as I understand it. In fact, the repo link provided in this article…
- [MeetingsBrowser](https://news.ycombinator.com/item?id=50095572) : When Fable first released, I had it "one shot" a project using an initial spec and a team of agents. I was blown away with how good the results were. And then I noticed some links to images from random small github projects and realized somewhere along the way agents had searched for existing proje…
- [evolve-maz](https://news.ycombinator.com/item?id=50097980) : I've always worried about the level of "IP laundering" which is done by LLMs. While that's not technically the case here \(given Mononoke's license\) it is still quite negative in my view. We will have fewer people wanting to share ideas openly since LLMs are so good at not only finding them, but als…

---

[Article original](https://sunshowers.io/posts/anthropic-mononoke/) · [Discussion HN](https://news.ycombinator.com/item?id=50094694)
