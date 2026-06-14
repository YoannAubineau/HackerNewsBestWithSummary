---
article_fetched_at: '2026-06-14T22:24:45.208673Z'
attempts: 0
content_source: extracted
discussion_comment_count: 119
discussion_fetched_at: '2026-06-14T22:24:44.315959Z'
error: null
guid: https://news.ycombinator.com/item?id=48528371
hn_item_id: 48528371
hn_url: https://news.ycombinator.com/item?id=48528371
is_ask_or_show_hn: false
llm_input_tokens: 8780
llm_latency_ms: 9169
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 833
our_published_at: '2026-06-14T21:50:48Z'
rewritten_title: Le modèle de langage de Rio de Janeiro serait un mélange de modèles
  existants
source_published_at: '2026-06-14T15:37:31Z'
status: summarized
summarized_at: '2026-06-14T22:25:16.977312Z'
title: Rio de Janeiro's "homegrown" LLM appears to be a merge of an existing model
url: https://github.com/nex-agi/Nex-N2/issues/4
---

## Résumé de l'article

Le modèle Rio-3.5-Open-397B présenté par la mairie de Rio de Janeiro comme un développement original n'est en réalité qu'une fusion pondérée d'un modèle existant (Nex) et du modèle Qwen officiel, selon l'organisation Nex-AGI qui publie cette analyse.

- Le modèle de Rio est une combinaison mathématique directe à 60% de Nex et 40% de Qwen, sans trace de nouvel entraînement propre
- Lorsque le prompt système « You are Rio » est désactivé, le modèle s'identifie comme « Nex » dans 79% des cas et reprend mot-pour-mot l'histoire de marque de Nex-AGI
- Les poids de chaque couche du réseau reproduisent cette même proportion 0.6/0.4 sur les 60 couches et tous les composants

## Discussion sur Hacker News (119 commentaires)

**Avis positifs** :
- Le concept de fusion de modèles est techniquement valide et bien établi depuis 2022 ; cela fonctionne particulièrement quand les modèles partagent la même architecture de base (comme Nex-N2 qui est une fine-tune de Qwen)
- Rio a au moins tenté une initiative d'IA ambitieuse, ce qui est remarquable pour un département informatique municipal et montre une certaine audace entrepreneuriale
- La fusion de modèles pour obtenir de meilleures performances sur certains benchmarks est un résultat réel et scientifiquement intéressant, même si ce n'est pas novateur
- L'absence totale de post-training dans le modèle uploadé pourrait effectivement être une simple erreur (upload du mauvais fichier) plutôt qu'une tromperie délibérée

**Avis négatifs** :
- Rio a présenté une simple fusion de modèles existants comme une réalisation majeure de post-training homogène, ce qui constitue une tromperie substantielle sur les capacités de recherche de l'équipe
- L'absence d'attribution à Nex-N2 Pro est une omission grave ; la non-divulgation d'une composante aussi importante (40% du modèle) montre une malhonnêteté intentionnelle plutôt qu'une négligence
- Le refus de publier les fichiers correctement entraînés malgré les accusations suggère que Rio n'a pas réellement de modèle avec post-training et espère que les critiques s'oublieront
- C'est un détournement de fonds publics : les contribuables brésiliens ont financé un projet présenté comme une innovation majeure alors qu'il s'agit simplement d'une fusion de modèles open-source existants
- Les performances améliorées sur quelques benchmarks spécifiques sont probablement non représentatives ; les vrais fusions de modèles montrent généralement des dégradations sur des tâches réelles et des benchmarks complexes

**Top commentaires** :

- [rafaquintanilha](https://news.ycombinator.com/item?id=48531780) : I have no affiliation with them but here's what I think happened: 1. They claim the official model is based on Qwen 397B. It's likely they didn't disclose Nex Pro at all because Nex itself is based on the same base model \(not saying they shouldn't\). 2. The improvement would come from merging the we…
- [hintymad](https://news.ycombinator.com/item?id=48530360) : « Every weight tensor in Rio is, to thousands of standard deviations, the same 0.6/0.4 blend of Nex and Qwen — across all 60 layers and every component of the network. Other finetunes cannot be explained as interpolations. » I find it amazing how robust the current deep learning models are. A simpl…
- [zinodaur](https://news.ycombinator.com/item?id=48529326) : Oh no, someone is profiting off of their work without proper attribution!?!?

---

[Article original](https://github.com/nex-agi/Nex-N2/issues/4) · [Discussion HN](https://news.ycombinator.com/item?id=48528371)
