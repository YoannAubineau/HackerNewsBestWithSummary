---
article_fetched_at: '2026-05-13T23:24:15.893737Z'
attempts: 0
content_source: extracted
discussion_comment_count: 245
discussion_fetched_at: '2026-05-13T23:24:14.841080Z'
error: null
guid: https://news.ycombinator.com/item?id=48110529
hn_item_id: 48110529
hn_url: https://news.ycombinator.com/item?id=48110529
image_url: https://cdn.arstechnica.net/wp-content/uploads/2021/09/getty-amazon-warehouse-1152x648.jpg
is_ask_or_show_hn: false
llm_input_tokens: 18229
llm_latency_ms: 9391
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 866
our_published_at: '2026-05-13T22:40:41Z'
rewritten_title: Des employés d'Amazon gonflent artificiellement leur usage de l'IA
  pour répondre aux attentes managériales
source_published_at: '2026-05-12T16:29:21Z'
status: summarized
summarized_at: '2026-05-13T23:25:19.988542Z'
title: Amazon employees are "tokenmaxxing" due to pressure to use AI tools
url: https://arstechnica.com/ai/2026/05/amazon-employees-are-tokenmaxxing-due-to-pressure-to-use-ai-tools/
---

## Résumé de l'article

Amazon déploie largement MeshClaw, un outil IA interne permettant d'automatiser des tâches professionnelles. Face à une pression accrue pour utiliser quotidiennement ces technologies et à un suivi public de la consommation de tokens (unités de données traitées par les modèles), certains employés automatisent des tâches inutiles simplement pour augmenter leurs statistiques d'utilisation.

- Amazon a fixé des objectifs exigeant que plus de 80 % des développeurs utilisent l'IA chaque semaine et publie les classements de consommation de tokens en interne
- Bien que l'entreprise affirme que ces statistiques n'influenceront pas les évaluations de performance, plusieurs employés rapportent que les managers surveillent activement ces données
- Cette pression crée des « incitations perverses » selon les témoignages, certains employés devenant compétitifs sur ces métriques plutôt que sur la qualité réelle du travail
- Amazon investit 200 milliards de dollars en dépenses d'équipement cette année, principalement dans l'infrastructure IA et les centres de données, ce qui explique la volonté de démontrer un retour sur investissement

## Discussion sur Hacker News (245 commentaires)

**Avis positifs** :
- L'adoption forcée d'AI peut être justifiée comme une exploration nécessaire pour découvrir des cas d'usage réels, similaire à la transition des ingénieurs vers les outils de synthèse RTL dans les années 1990
- Certains domaines techniques (chip design, diagnostic de simulation) montrent des gains de productivité authentiques et mesurables avec les LLM actuels
- Il existe des cas légitimes d'utilisation intensive de tokens : intégration avec les systèmes internes (sprint boards, wikis), travail exploratoire en TDD, ou recherche en sécurité

**Avis négatifs** :
- Mesurer la performance via les tokens consommés est une application textbook de la loi de Goodhart : dès qu'une métrique devient un objectif, elle cesse d'être une bonne mesure, incitant à du gaming pur plutôt qu'à une utilisation productive
- Cette approche reproduit les erreurs historiques de mesure par lignes de code écrites ou commits produits, ignorant les leçons passées sur l'inefficacité des métriques de surface
- Le comportement tokenmaxxing révèle une incompétence managériale fondamentale : Amazon préfère surveiller l'input (tokens) plutôt que l'output (valeur métier), incitant à des boucles d'IA auto-alimentées et du gaspillage délibéré
- Les témoignages d'employés Amazon contredisent les dénégations officielles : plusieurs rapportent une pression réelle et l'utilisation des leaderboards de tokens pour influencer les décisions managériales, même si ce n'est pas formellement officiel
- Cette dynamique alimente une bulle de dépense en IA déconnectée de la valeur réelle, avec des managers cherchant à justifier des investissements massifs plutôt qu'à résoudre des problèmes concrets

**Top commentaires** :

- [i7l](https://news.ycombinator.com/item?id=48110972) : The fact that management signed off on measuring AI use through token usage shows how incompetent management really is, including in allegedly technical conmpanies like Amazon. Tokenmaxxing was an entirely expected and rational response. IOW You measure employees in stupid ways, you're going to get…
- [Argonaut998](https://news.ycombinator.com/item?id=48111048) : I swear the industry is being Garry Tanned. Senior management let go our localisation staff. Now they want us to use AI to translate. They still want manual review. We use Github Copilot at work, we get a measly 300 requests with the budget to go over if necessary. Opus 4.7 or GPT 5.5 would eat all…
- [asdfman123](https://news.ycombinator.com/item?id=48111106) : Saw a good joke on twitter about it. Something like: "You spent $23, over the $20 food limit. Be more careful next time. You spent $600 on tokens, $200 more than the average. Congratulations!"

---

[Article original](https://arstechnica.com/ai/2026/05/amazon-employees-are-tokenmaxxing-due-to-pressure-to-use-ai-tools/) · [Discussion HN](https://news.ycombinator.com/item?id=48110529)
