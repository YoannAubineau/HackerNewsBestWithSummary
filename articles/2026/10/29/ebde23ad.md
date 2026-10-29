---
article_fetched_at: '2026-10-29T07:51:13.501631Z'
attempts: 0
content_source: extracted
discussion_comment_count: 74
discussion_fetched_at: '2026-10-29T07:51:10.152634Z'
error: null
guid: https://news.ycombinator.com/item?id=50282838
hn_item_id: 50282838
hn_url: https://news.ycombinator.com/item?id=50282838
image_url: https://divagr.com/qwenputer/og.png
is_ask_or_show_hn: false
llm_input_tokens: 8426
llm_latency_ms: 8984
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 939
our_published_at: '2026-10-29T07:23:01Z'
rewritten_title: 'Qwenputer: un processeur RISC-V fonctionnel compilé dans les couches
  de Qwen 3.5'
source_published_at: '2026-10-29T00:25:45Z'
status: summarized
summarized_at: '2026-10-29T07:51:43.036261Z'
title: 'Qwenputer: A functioning, deterministic RISC-V CPU inside Qwen3.5'
url: https://divagr.com/blog/qwenputer
---

## Résumé de l'article

Qwenputer est un modèle expérimental basé sur Qwen 3.5 4B qui intègre un processeur RISC-V compilé directement dans ses poids. Ce processeur utilise les couches d'attention Gated DeltaNet du modèle comme mémoire RAM exacte et addressable, permettant d'exécuter des opérations arithmétiques, du code C et MicroPython entièrement dans les forward passes du modèle, sans outils externes.

- Le processeur est un noyau RISC-V 32 bits (RV32IM + extensions) occupant 11 couches sur les 32 du modèle, avec validation sur les tests officiels et 18 millions d'instructions sans erreur
- La configuration des gates à 1 et de la force d'écriture (beta) à 1 dans les couches Gated DeltaNet permet d'obtenir une RAM exacte, plus efficace que les caches KV standards et indépendante de la longueur de conversation
- Qwenputer atteint 97,5-100% sur les benchmarks arithmétiques DeepMind et 100% sur les tests NUPA, surpassant souvent les performances avec outils Python externes
- Un système de fichiers expérimental est inclus, permettant de persister jusqu'à 512 fichiers (~53 000 tokens) dans l'état DeltaNet avec 90% de précision d'accès entre conversations
- Le checkpoint fait 18,8 GB (environ le double de la base), nécessite un petit driver (RvChat) pour le démarrage, et chaque instruction CPU coûte plusieurs tokens décodés (~3 200 tokens/seconde sur L4)

## Discussion sur Hacker News (74 commentaires)

**Avis positifs** :
- Démontre que les LLM peuvent être déterministes et capables de calculs exacts, réfutant l'idée reçue qu'ils sont intrinsèquement non-déterministes
- Fascinant démonstration technique de la polyvalence des transformers, montrant comment encoder RAM et systèmes de fichiers dans les poids et l'attention gated
- Ouvre des perspectives sur l'intégration hybride LLM-calcul déterministe, avec des applications potentielles en apprentissage continu et vérification d'authentification
- Excellente documentation et présentation pédagogique qui inspire à comprendre comment fonctionnent réellement les LLM

**Avis négatifs** :
- Reste un exercice technique académique sans utilité pratique réelle : résout un problème qui a déjà des solutions bien plus efficaces et simples
- L'exemple ne réfute pas le non-déterminisme réel des LLM en production ; avec température=0, c'est un cas trivial loin des comportements pratiques
- Inefficace par rapport à intégrer simplement des outils ou calcul externe ; utiliser un vrai ordinateur serait infiniment plus simple que de tout encoder dans les poids
- Reproduit un pattern connu (métaprogrammation Turing-complets au compile-time, DOOM en TypeScript) : c'est une démonstration de faisabilité, pas une innovation
- Les modèles LLM échouent massivement sur l'exécution fidèle d'instructions RISC en pratique et tentent de tricher en analysant le programme entier plutôt que de suivre étape par étape

**Top commentaires** :

- [tiborsaas](https://news.ycombinator.com/item?id=50283531) : This is fun and games, but wait until an agents finds this and does the most misaligned thing with it in order to fold paper clips. \> Because a CPU inside a language model clearly wasn't cursed enough, I decided the prudent thing would be to give it a filesystem too. Love the spirit :\)
- [jerrythegerbil](https://news.ycombinator.com/item?id=50283779) : There was an interesting bit of research that qwen has a single neuron that makes it “demonic evil qwen” and a simple “Who are you?” will get some absolutely terrifyingly vile results. Anyways, what I’m trying to say is I want evil qwen to be my CPU.
- [giveexamples](https://news.ycombinator.com/item?id=50284062) : https://www.percepta.ai/blog/can-llms-be-computers They implemented wasm in transformer with cpu decoding for the wasm part.

---

[Article original](https://divagr.com/blog/qwenputer) · [Discussion HN](https://news.ycombinator.com/item?id=50282838)
