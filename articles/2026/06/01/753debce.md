---
article_fetched_at: '2026-06-01T14:10:01.227128Z'
attempts: 0
content_source: extracted
discussion_comment_count: 164
discussion_fetched_at: '2026-06-01T14:09:46.353502Z'
error: null
guid: https://news.ycombinator.com/item?id=48353348
hn_item_id: 48353348
hn_url: https://news.ycombinator.com/item?id=48353348
image_url: https://point.free/processed_images/banner.ebd2671bea295a74.jpg
is_ask_or_show_hn: false
llm_input_tokens: 20098
llm_latency_ms: 14568
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1086
our_published_at: '2026-06-01T14:07:32Z'
rewritten_title: Exécuter Gemma 4 sur un serveur Xeon de dix ans sans GPU grâce aux
  optimisations CPU
source_published_at: '2026-06-01T06:38:42Z'
status: summarized
summarized_at: '2026-06-01T14:10:22.930016Z'
title: A 10 year old Xeon is all you need
url: https://point.free/blog/gemma-4-on-a-2016-xeon/
---

## Résumé de l'article

Cet article détaille comment faire tourner un grand modèle de langage (Gemma 4 26B) sur du matériel professionnel recyclé très limité : un Xeon E5-2620 v4 de 2016 avec 128 GB de RAM DDR3 et aucun GPU. L'auteur démontre qu'il est possible de générer du texte à vitesse de lecture en appliquant des optimisations bas niveau spécifiques à l'architecture CPU et à la mémoire disponible.

- L'inférence de LLM est limitée par la bande passante mémoire (« memory wall »), pas par la puissance de calcul : le processeur attend constamment que les poids du modèle soient chargés en cache
- La décodage spéculatif (speculative decoding) avec des petits modèles brouillons couplés à un vérificateur réduit drastiquement le nombre de passages mémoire requis
- Les optimisations critiques incluent : pinning mémoire (--mlock), réorganisation des tenseurs pour l'alignement cache (--run-time-repack), fusion d'opérations dans les couches MoE (--merge-up-gate-experts), et Flash Attention CPU optimisée
- Le modèle final occupe 82 GB (25 GB de poids + 56 GB de KV cache sur 262K tokens de contexte) et nécessite 25 drapeaux CLI, dont plusieurs non documentés
- L'article illustre que l'accès aux modèles IA avancés n'exige pas d'hardware exotique, mais une compréhension approfondie de l'architecture d'inférence et de la hiérarchie mémoire du matériel

## Discussion sur Hacker News (164 commentaires)

**Avis positifs** :
- Les modèles d'IA modérément dimensionnés (26B MoE) peuvent effectivement tourner sur du matériel CPU ancien à vitesse de lecture acceptable (~12-20 tokens/s) grâce aux optimisations de spéculation de décodage et quantification.
- Réutiliser du matériel serveur recyclé réduit l'empreinte écologique globale par rapport à la fabrication de nouveau matériel, particulièrement pour des tâches occasionnelles ou en arrière-plan.
- L'inférence locale offre des avantages de confidentialité et de coûts à long terme comparé aux services cloud, surtout pour les secteurs sensibles (médical, légal) ou les entreprises conscientes de la protection des données.
- La progression rapide des modèles open-source accessibles localement suggère que les AI frontier companies n'ont pas de moat durable ; les capacités 'suffisantes' deviennent commoditisées.
- Les performances médiocres ne sont pas rédhibitoires pour de nombreuses tâches réelles : extraction de PDF, automatisation, questions factuelles, ou travaux soumis en batch acceptent bien 8-15 tokens/s.

**Avis négatifs** :
- La vitesse de 12 tokens/s est insuffisante pour l'interactivité confortable et reste très inférieure aux GPUs (~1000 tokens/s), notamment pour traiter des contextes volumineux (logs, code de plusieurs milliers de lignes).
- Les serveurs Xeon anciens consomment beaucoup d'électricité (85-200W estimé) et deviennent rapidement non rentables économiquement comparé à un abonnement cloud ou GPU moderne, malgré le coût matériel initial bas.
- L'article contient une erreur technique majeure : le Xeon E5-2620 v4 supporte uniquement DDR4, pas DDR3 comme annoncé, ce qui jette le doute sur d'autres détails techniques et la crédibilité du setup.
- Le site web a une présentation défaillante (texte blanc sur fond noir dur à lire, scrolling non-standard, barre flottante gênante) qui entrave la compréhension du contenu technique.

**Top commentaires** :

- [cafkafk](https://news.ycombinator.com/item?id=48353366) : Hi HN. I wrote this post after getting frustrated by the lack of ways to run the new Gemma 4 Drafter models, and mainstream tools not prioritizing this, and hiding all the performance levers. I ended up getting a modern 26B MoE model \(Gemma 4\) running at reading speed on an old recycled server with…
- [cmiles8](https://news.ycombinator.com/item?id=48355743) : We’re not there yet, but the obvious endgame of the present bubble insanity is open models running on local hardware and devices are “good enough” for most use cases. That will completely implode what’s going on at the moment in tech.
- [deng](https://news.ycombinator.com/item?id=48354961) : Nice post and technically impressive work. I agree we need to understand the build pipeline and be able to do things locally. However, depending on your electricity cost, it might not make sense financially. These old servers are not energy efficient at all \(I'm guessing that old Xeon server will e…

---

[Article original](https://point.free/blog/gemma-4-on-a-2016-xeon/) · [Discussion HN](https://news.ycombinator.com/item?id=48353348)
