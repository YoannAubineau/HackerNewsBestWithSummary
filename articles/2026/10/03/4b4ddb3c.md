---
article_fetched_at: '2026-10-03T18:27:33.166057Z'
attempts: 0
content_source: extracted
discussion_comment_count: 215
discussion_fetched_at: '2026-10-03T18:27:29.636029Z'
error: null
guid: https://news.ycombinator.com/item?id=49942706
hn_item_id: 49942706
hn_url: https://news.ycombinator.com/item?id=49942706
image_url: https://aleph-alpha.com/_astro/00-cover.Du35XCGh_zJqw.jpeg
is_ask_or_show_hn: false
llm_input_tokens: 21454
llm_latency_ms: 13526
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1175
our_published_at: '2026-10-03T17:35:13Z'
rewritten_title: Aleph Alpha lance Kolibri, un modèle multilingue allemand-anglais
  de 78 milliards de paramètres
source_published_at: '2026-10-03T09:36:04Z'
status: summarized
summarized_at: '2026-10-03T18:28:12.194262Z'
title: 'Kolibri Has Landed: A Sovereign Open-Weight Model'
url: https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/
---

## Résumé de l'article

Kolibri est un modèle de langage Mixture-of-Experts bilingue allemand-anglais développé par Aleph Alpha, conçu pour les missions critiques en administration publique, aérospatiale et industrie. Avec 78 milliards de paramètres totaux mais seulement 3 milliards actifs, il supporte des contextes jusqu'à 1 million de tokens et est disponible en open-weight sous licence Apache 2.0.

- Kolibri a été développé en trois mois via un pipeline d'entraînement automatisé, passant de 30 à 78 milliards de paramètres et de 65k à 1M tokens de contexte, entraîné sur 20 trillions de tokens dont 21,3% en allemand organique
- Le modèle excelle en raisonnement, mathématiques et tâches agentic, correspondant aux performances de modèles quatre fois plus grands tout en étant plus efficace à servir (28% plus rapide en décodage)
- Kolibri réduit les hallucinations en utilisant le protocole Merlin-Arthur pour l'entraînement à l'abstention, s'abstenant de répondre sans preuve documentaire 44% plus souvent que la version précédente
- Un tokenizer bilingue spécialisé (UniBPE) compresse mieux l'allemand que les modèles concurrents, réduisant le nombre de tokens et les coûts d'inférence
- Le modèle inclut des suites d'évaluation contextualisées pour secteurs spécifiques (secteur public allemand, aviation, automobile) permettant de mesurer la performance en conditions réelles sans accès aux données client

## Discussion sur Hacker News (215 commentaires)

**Avis positifs** :
- Transparence exceptionnelle : le rapport technique détaille la méthodologie de création du modèle, l'acquisition de données et les pipelines d'entraînement, établissant un nouveau standard d'ouverture dans le domaine
- Spécialisation pragmatique en allemand : le modèle exploite des cas d'usage réels (traitement de documents allemands, workflows spécifiques) ignorés par les modèles généralistes, avec un tokenizer personnalisé et une réduction des hallucinations
- Abstention bien calibrée : entraîné à dire « je ne sais pas » plutôt que de produire des réponses confiantes mais erronées, offrant une base solide pour des applications critiques
- Importance stratégique de l'indépendance technologique : un modèle souverain contrôlé localement réduit la dépendance envers les États-Unis et la Chine, crucial pour la sécurité des données et l'autonomie décisionnelle en Europe
- Performance acceptable en petit modèle : avec seulement 3,5B paramètres actifs sur 78B totaux, le modèle offre un bon compromis entre rapidité et performance, adapté à l'auto-hébergement et aux ressources limitées

**Avis négatifs** :
- Performance en retrait sur les benchmarks : Qwen3.8 27B surpasse Kolibri sur la plupart des tests, y compris ceux spécifiques à l'allemand (79,9 vs 70,8), questionnant la compétitivité réelle du modèle
- Absence de comparaison directe avec les modèles MoE récents : le rapport omet de comparer avec Qwen3.8 Flash, un concurrent pertinent dans l'espace petit modèle avec architecture similaire
- Limitation à deux langues seulement : contrairement aux modèles frontières multilingues qui combinent les connaissances de plusieurs langues, Kolibri restreint à l'allemand et l'anglais réduit sa polyvalence
- Doute sur le caractère véritablement souverain : la fusion avec Cohere (Canada) et l'utilisation de données Common Crawl questionnent l'indépendance réelle et la propriété contrôlée des données d'entraînement
- Débat sur la viabilité stratégique : le positionnement sur la « souveraineté » peut masquer une performance insuffisante et créer un faux sentiment de succès, sans garantir une trajectoire concurrentielle à long terme face aux laboratoires chinois et américains

**Top commentaires** :

- [miellaby](https://news.ycombinator.com/item?id=49944996) : The paper explains absolutely everything as if it was a tutorial "how to made your own modern agentic LLM". They even tell how they made their dataset. https://aleph-alpha.com/downloads/tech-report.pdf ; It's the first time I see this level of openness.
- [peterBlue75](https://news.ycombinator.com/item?id=49946275) : The thing to note here, besides the transparency and the fact that it’s actually a good model that also works well on coding and agentic tasks, is that it’s the first release by a team formed less than a year ago, with a strong focus on iteration velocity. There’s more to come. disclaimer: I‘m part…
- [andai](https://news.ycombinator.com/item?id=49946138) : « We trained Kolibri with abstention data and with our Merlin-Arthur protocol. As a result, it is trained to say "I don't know" when the answer isn't in the context. » https://aleph-alpha.com/en/blog/bounding-hallucinations-merl...

---

[Article original](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/) · [Discussion HN](https://news.ycombinator.com/item?id=49942706)
