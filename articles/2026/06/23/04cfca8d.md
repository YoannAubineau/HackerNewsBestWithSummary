---
article_fetched_at: '2026-06-23T13:52:52.594150Z'
attempts: 0
content_source: extracted
discussion_comment_count: 140
discussion_fetched_at: '2026-06-23T13:52:52.113675Z'
error: null
guid: https://news.ycombinator.com/item?id=48640196
hn_item_id: 48640196
hn_url: https://news.ycombinator.com/item?id=48640196
is_ask_or_show_hn: false
llm_input_tokens: 16313
llm_latency_ms: 13509
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1129
our_published_at: '2026-06-23T13:45:08Z'
rewritten_title: Comparaison des capacités de détection de bugs de sécurité entre
  Mythos et autres modèles d'IA
source_published_at: '2026-06-23T04:15:04Z'
status: summarized
summarized_at: '2026-06-23T13:53:12.632997Z'
title: Will It Mythos?
url: https://swelljoe.com/post/will-it-mythos/
---

## Résumé de l'article

Un chercheur a créé un benchmark pour tester si les modèles d'IA publiquement disponibles peuvent égaler Mythos, un outil propriétaire d'Anthropic réputé excellent pour trouver des failles de sécurité. Mythos est actuellement réservé à des utilisateurs restreints, et l'auteur examine si c'est vraiment dû à sa supériorité technique ou à d'autres raisons commerciales.

- Le benchmark utilise 9 bugs de sécurité réels récemment divulgués, confirmés comme détectables par Opus quand celui-ci est guidé, ce qui rend la tâche comparable à ce que Mythos aurait pu trouver
- Mythos a surpassé tous les modèles testés en découvrant 4 bugs qu'aucun autre n'a trouvé, mais plusieurs modèles publics (Claude Opus 4.8, GPT 5.5, MiMo, DeepSeek) se sont montrés compétitifs sur les autres bugs
- Les modèles chinois bon marché (DeepSeek, MiMo) offrent un excellent rapport qualité-prix, détectant autant de bugs qu'Opus 4.8 pour environ un dixième du coût
- Qwen 3.6 27B et Gemma 4 MoE ont surperformé les attentes pour des modèles de petite ou moyenne taille, tandis que Gemini 3.5 Flash, Mistral Medium et d'autres ont sous-performé
- Les conclusions restent nuancées : Mythos pourrait effectivement être supérieur, mais l'auteur soupçonne que les modèles publics avec des outils et des invites mieux adaptés pourraient fermer l'écart

## Discussion sur Hacker News (140 commentaires)

**Avis positifs** :
- Mythos/Fable démontre une amélioration substantielle et mesurable en détection de bugs de sécurité, particulièrement en raisonnement spatial et persistance dans l'analyse, confirmée par plusieurs utilisateurs avec exemples concrets (reverse engineering, géométrie computationnelle, bugs de concurrence).
- Le benchmark révèle que les protections de sécurité US strictes ne sont pas la cause principale des écarts de performance : Gemma 4 31B (sans guardrails excessifs) rivalise avec les meilleurs modèles, contredisant l'hypothèse d'un handicap volontaire.
- Fable démontrait une qualité supérieure de raisonnement et d'autonomie (moins besoin de guidance, meilleure compréhension contextuelle) par rapport à Opus, fonctionnant comme un collègue plutôt qu'un étudiant, selon plusieurs développeurs.
- Le travail d'évaluation du benchmark lui-même est rigoureux : méthodologie clarifiée, transparence des limites budgétaires, résultats détaillés, et contribution à établir des standards de mesure pour les capacités de sécurité des modèles.

**Avis négatifs** :
- Mythologies autour de Fable/Mythos : les améliorations pourraient être largement dues à un meilleur étiquetage social et à la confiance radiée plutôt qu'à des capacités réellement supérieures, similaire aux cycles de hype précédents (Sonnet vs Opus, etc.).
- Absence de preuves rigoureuses dans les tests utilisateur : la plupart des comparaisons sont anecdotiques et subjectives (« vibes »), sans évaluations en aveugle, rendant difficile la distinction entre amélioration réelle et biais cognitif.
- Modèles de frontier étant limités par la compute en inference, les laboratoires ont probablement réduit les ressources des anciens modèles pour promouvoir les nouveaux, créant une illusion de dégradation plutôt qu'une véritable amélioration mesurable.
- Les guardrails de sécurité stricts imposés par Anthropic et Google rendent l'accès international inégal (européens, africains exclus), tandis que les modèles chinois non-régulés offrent équivalent ou supérieur avec moins de restrictions.

**Top commentaires** :

- [Tossrock](https://news.ycombinator.com/item?id=48640849) : As I posted in another comment, I found Fable to be substantially more powerful than any previous model. However, this isn't just an ungrounded opinion - I uploaded my full session transcript and code created working on a very complex implementation, so people can judge for themselves, if they're i…
- [airstrike](https://news.ycombinator.com/item?id=48641159) : Around February, Opus 4.6 was excellent. Smart, fast, proactive. Then it got lobotomized and it's never been the same after that nerf. 4.7 came along and it too was disappointing—not unlike 4.8, which despite feeling a smidge smarter, tends to write word salad and is basically unusable for some wor…
- [sfjailbird](https://news.ycombinator.com/item?id=48644060) : 1. Release new model, allocate all available compute. 2. Market as best model ever. 3. Garner hype reviews. 4. Quietly nerf. 5. Goto 1. Btw, there is no 'profit' step.

---

[Article original](https://swelljoe.com/post/will-it-mythos/) · [Discussion HN](https://news.ycombinator.com/item?id=48640196)
