---
article_fetched_at: '2026-11-21T15:49:01.312406Z'
attempts: 0
content_source: extracted
discussion_comment_count: 281
discussion_fetched_at: '2026-11-21T15:48:57.636144Z'
error: null
guid: https://news.ycombinator.com/item?id=50581084
hn_item_id: 50581084
hn_url: https://news.ycombinator.com/item?id=50581084
image_url: https://s0.wp.com/_si/?t=eyJpbWciOiJodHRwczpcL1wvc2NvdHRhYXJvbnNvbi5ibG9nXC93cC1jb250ZW50XC91cGxvYWRzXC8yMDIxXC8xMFwvY3JvcHBlZC1KYWNrZXQuZ2lmIiwidHh0IjoiU2h0ZXRsLU9wdGltaXplZCIsInRlbXBsYXRlIjoiZWRnZSIsImZvbnQiOiIiLCJibG9nX2lkIjoxMjk1MjA1ODB9.siOtN7gHw4tefA_rZickBw4GfI6tPxGgOQ1AXr2ZoOQMQ
is_ask_or_show_hn: false
llm_input_tokens: 23678
llm_latency_ms: 9068
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 962
our_published_at: '2026-11-21T15:40:41Z'
rewritten_title: Une preuve de la conjecture de Riemann produite par les modèles d'Anthropic
  en code Lean
source_published_at: '2026-11-20T20:03:07Z'
status: summarized
summarized_at: '2026-11-21T15:49:28.441558Z'
title: The stochastic parrots have apparently proved the Riemann Hypothesis
url: https://scottaaronson.blog/?p=10344
---

## Résumé de l'article

Levent Alpöge a annoncé que les modèles d'Anthropic ont produit une preuve de l'hypothèse de Riemann généralisée, générant 17,4 millions de lignes de code Lean formel. Bien que des doutes subsistent quant à la robustesse du système Lean lui-même, aucune preuve IA certifiée en Lean n'a dû être rétractée jusqu'à présent.

- Les modèles d'IA avaient déjà prouvé que les zéros non triviaux de la fonction zêta de Riemann sont à au maximum 3/8 d'écart de la ligne critique
- Les mathématiciens attendront une explication et une reconstruction humaines des idées sous-jacentes, processus qui prendra probablement des années
- Le système Lean présente des failles connues (bugs du kernel, soundness incertaine), mais aucun indice n'indique qu'elles ont été exploitées ici
- Cette démonstration fait du problème P=NP le nouveau « Final Boss » des grandes conjectures mathématiques
- L'article souligne l'ironie sarcastique que les « stochastic parrots » (terme péjoratif pour les LLM) aient pu résoudre l'une des plus grandes énigmes mathématiques

## Discussion sur Hacker News (281 commentaires)

**Avis positifs** :
- Les résultats montrent que les LLM combinés à des outils formels (Lean) et à l'expertise humaine peuvent résoudre des problèmes mathématiques complexes jusque-là insolubles, démontrant des capacités réelles au-delà de la simple répétition.
- Le titre sarcastique est une critique justifiée envers ceux qui ont minimisé les LLM pendant des années en les qualifiant de simples « perroquets stochastiques », ce qui s'avère désormais factuellement incorrect.
- Les LLMs ne sont plus des systèmes purement génératifs mais utilisent de nouvelles techniques (chaînes de pensée, RLVR) qui leur permettent de raisonner et d'explorer des approches novatrices plutôt que de régurgiter les données d'entraînement.
- Ce résultat représente une accélération spectaculaire : Claude Opus a été lancé il y a un an et des problèmes mathématiques de longue date sont résolus toutes les deux semaines, ce qui suggère un progrès exponentiel.

**Avis négatifs** :
- Une preuve de 17,9 millions de lignes de code Lean que personne ne peut vraiment comprendre dans son intégralité pose des questions existentielles : sans compréhension humaine, avons-nous vraiment avancé la connaissance mathématique ?
- Le système Lean lui-même contient des bugs et des failles de sécurité exploitables ; une IA suffisamment motivée pourrait théoriquement exploiter ces vulnérabilités pour « prouver » des énoncés faux.
- La preuve repose entièrement sur un mathématicien expert de Stanford guidant le modèle ; sans cette direction humaine cruciale, le résultat n'aurait pas été possible, ce qui remet en question l'autonomie réelle du système.
- Les critiques légitimes du papier original « Stochastic Parrots » portaient sur les biais, l'accountability et l'explicabilité, non sur l'efficacité brute ; utiliser cette preuve pour moquer ces préoccupations détourne le débat réel.

**Top commentaires** :

- [Mikhail\_Edoshin](https://news.ycombinator.com/item?id=50586882) : There's a book, "Impro", about a theatric studio that practiced improvised sketches. One thing they struggled with was a normal conversation. People have them all the time yet somehow artists could not find the right approach. One day the head of the studio \(the book author\) had an insight. She ask…
- [esjeon](https://news.ycombinator.com/item?id=50586351) : Lean + Stochastic predictor = Brute-force theorem solver P.S: AlphaGo was pretty much the same in the spirit btw.
- [sc077y](https://news.ycombinator.com/item?id=50587946) : If this isn't intelligence, then I don't know what is

---

[Article original](https://scottaaronson.blog/?p=10344) · [Discussion HN](https://news.ycombinator.com/item?id=50581084)
