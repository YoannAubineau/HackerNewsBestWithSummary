---
article_fetched_at: '2026-07-07T16:20:51.418754Z'
attempts: 0
content_source: extracted
discussion_comment_count: 221
discussion_fetched_at: '2026-07-07T16:20:48.070050Z'
error: null
guid: https://news.ycombinator.com/item?id=48816959
hn_item_id: 48816959
hn_url: https://news.ycombinator.com/item?id=48816959
is_ask_or_show_hn: false
llm_input_tokens: 18641
llm_latency_ms: 13511
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1185
our_published_at: '2026-07-07T15:52:11Z'
rewritten_title: Pourquoi un taux de 98% masque des défaillances graves selon le contexte
source_published_at: '2026-07-07T12:45:14Z'
status: summarized
summarized_at: '2026-07-07T16:22:03.049474Z'
title: 98% Isn't Much
url: https://whynothugo.nl/journal/2026/07/03/98-isnt-very-much/
---

## Résumé de l'article

Un article d'ingénierie qui décortique pourquoi le taux de 98% — souvent présenté comme excellent — est en réalité très insuffisant pour les services ou fonctionnalités critiques, bien qu'il soit acceptable pour des améliorations exceptionnelles. Le problème s'aggrave quand on considère que « 98% de la population générale » ne reflète pas nécessairement « 98% de mon audience ».

- Pour les services de base (santé, sécurité, fiabilité), 98% signifie que 2% des utilisateurs subissent un dommage régulier : intoxications alimentaires hebdomadaires, oublis de paiement, pannes critiques
- Un site web affichant « 98% de support navigateur » exclut ~150 millions de personnes ; même « largement supporté » implique une dégradation gracieuse, sinon c'est un échec
- La distribution réelle du public diffère de la moyenne générale : une fonctionnalité « standard depuis 2023 » peut ne fonctionner que pour 70% des visiteurs d'un site donné, excluant de facto 30%
- L'ingénierie robuste ne consiste pas à servir la majorité, mais à gérer les cas limites sans rupture : si une nouvelle fonctionnalité ne se dégrade pas gracieusement, elle échoue pour 2% des utilisateurs en dur

## Discussion sur Hacker News (221 commentaires)

**Avis positifs** :
- Les pourcentages masquent l'ampleur réelle : 2% de 8 milliards représente 150 millions de personnes, et à grande échelle (ex. 99% de précision en IA conduisant à des erreurs dans presque chaque session), les petits pourcentages deviennent problématiques.
- Le contexte et les cas d'usage critiques exigent des standards bien plus élevés : la sécurité alimentaire, les parachutes, les opérations chirurgicales ou l'infrastructure essentielles ne peuvent accepter 98% ; les décisions devraient reposer sur le coût de l'échec, pas le pourcentage seul.
- La dégradation gracieuse est possible et souhaitable : les sites peuvent fonctionner partiellement pour les 2% sans les exclure totalement, en offrant une expérience réduite mais utilisable plutôt qu'une rupture complète.
- Le contexte commercial justifie l'exclusion sélective : certains clients à hauts revenus (bureaux, secteur B2B) représentent une part disproportionnée du chiffre d'affaires malgré leur petit nombre, rendant le support ancien navigateur rentable dans certains secteurs.
- Les décisions cumulatives sont dangereuses : si 35 décisions acceptent chacune l'exclusion de 2%, plus de la moitié de la population se retrouve exclue, créant une dette technique irréversible.

**Avis négatifs** :
- L'article utilise des analogies fallacieuses en comparant des domaines incomparables : refuser l'entrée à un restaurant n'est pas comparable à une dégradation légère d'interface web ; les sites peuvent fonctionner partiellement.
- 98% est souvent suffisant en contexte : pour les navigateurs, les utilisateurs devraient mettre à jour leurs logiciels sécurité ; forcer l'obsolescence incite au progrès ; les cas d'usage réels (petits sites e-commerce) n'ont pas besoin de cibler les 10% de la population.
- Le coût/bénéfice prime sur le pourcentage : soutenir les anciens navigateurs ralentit le développement pour la majorité sans retour tangible ; certaines entreprises seraient mieux loties en abandonnant les clients non rentables et en investissant ailleurs.
- La responsabilité incombe aux utilisateurs, pas aux développeurs : les gens peuvent mettre à jour leurs navigateurs ou appareils ; les anciens systèmes représentent des risques de sécurité ; exiger que tous les sites soutiennent IE11 après 15 ans est déraisonnable.
- L'article ignore les vrais enjeux : les statistiques sont souvent biaisées (bots, utilisateurs non payants) ; la vraie question est qui sont ces 2% et valent-ils vraiment l'effort d'ingénierie ; le pragmatisme dicte souvent qu'ignorer la queue longue est la bonne décision.

**Top commentaires** :

- [wccrawford](https://news.ycombinator.com/item?id=48817236) : Alternatively, 98% is plenty. If your business plan requires you to capitalize on more than 98% of the market, it's already a failure. It'll never happen. As always, it's an "it depends" situation. If your userbase is largely luddites, then maybe you need to support 10+ year old browsers that can't…
- [nemo1618](https://news.ycombinator.com/item?id=48818886) : After Christmas this year, I removed the tree from our living room, and in the process of being moved, it shed of needles everywhere. I swept them up, but I missed a few areas on my first pass. So I did a second pass, but when I looked again, I saw there were still a handful left. It struck me how…
- [MatekCopatek](https://news.ycombinator.com/item?id=48817281) : While I agree with the general sentiment, the problem here isn't developers not being familiar with statistics, it's the simple fact all of this is profit driven most of the time. I tried to purchase tickets for an event last week. I had to go through Ticketmaster as it was the only official way. T…

---

[Article original](https://whynothugo.nl/journal/2026/07/03/98-isnt-very-much/) · [Discussion HN](https://news.ycombinator.com/item?id=48816959)
