---
article_fetched_at: '2026-07-04T20:44:30.965618Z'
attempts: 0
content_source: extracted
discussion_comment_count: 115
discussion_fetched_at: '2026-07-04T20:44:28.850755Z'
error: null
guid: https://news.ycombinator.com/item?id=48785485
hn_item_id: 48785485
hn_url: https://news.ycombinator.com/item?id=48785485
is_ask_or_show_hn: false
llm_input_tokens: 10108
llm_latency_ms: 10008
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 882
our_published_at: '2026-07-04T20:24:48Z'
rewritten_title: Fuite de session et cache détectée entre instances workspace ou comptes
  consommateurs
source_published_at: '2026-07-04T14:03:40Z'
status: summarized
summarized_at: '2026-07-04T20:44:47.840922Z'
title: Potential session/cache leakage between workspace instances or consumer accounts
url: https://github.com/anthropics/claude-code/issues/74066
---

## Résumé de l'article

Un utilisateur Enterprise ZDR d'une plateforme (probablement Claude) rapporte une fuite de session potentielle : l'agent IA a soudainement commencé à discuter de construction d'un temple Minecraft et en a parlé dans son résumé, alors que l'utilisateur travaillait sur un sujet sans rapport. L'utilisateur soupçonne soit une pollution du cache intra-workspace, soit une fuite depuis un compte consommateur, ce qui poserait des problèmes sérieux de sécurité pour les sessions sensibles en Enterprise.

- L'agent a mentionné spontanément des détails Minecraft non liés à la conversation en cours et a inclus ce contenu dans son récapitulatif
- L'utilisateur a confirmé que ce contenu n'était pas issu de son propre setup (il a documenté d'autres pollutions causées par sa configuration personnelle, distinctes de celle-ci)
- La préoccupation majeure concerne l'isolement du cache supposément garantis dans les workspaces Enterprise ZDR et le risque que du contenu sensible transite entre utilisateurs
- Le rapport inclut des métadonnées d'environnement (macOS, version 2.1.199) et un ID de feedback pour traçabilité

## Discussion sur Hacker News (115 commentaires)

**Avis positifs** :
- Les incidents rapportés méritent investigation sérieuse malgré les explications alternatives, car la transparence est insuffisante chez les fournisseurs pour affirmer avec certitude qu'il n'y a pas de fuite
- Les bugs de cache multi-tenant sur GPU sont plausibles : optimisations de performance agressives, isolation au niveau logiciel plutôt que matériel, et infrastructure immature créent des conditions propices aux fuites inter-utilisateurs
- Des incidents similaires ont été confirmés chez plusieurs fournisseurs (GPT, Claude, Gemini) avec des postmortems montrant des défauts réels d'infrastructure (erreurs HTTP/100, problèmes de routage en vol), pas seulement des hallucinations
- Les hallucinations ne correspondent pas au pattern observé (output complètement implausible et cohérent, pas des réponses plausibles incorrectes typiques), suggérant une autre cause systémique

**Avis négatifs** :
- La présence de 'minecraft.py' dans le contexte (800K+ tokens) fait qu'une hallucination classique est l'explication la plus probable, aggravée par la longueur excessive de la session
- Les utilisateurs expérimentés déclarent ne jamais avoir observé ce comportement avec Claude/GPT malgré une utilisation intensive, contredisant un bug systémique répandu
- Aucune vérification basique n'a été faite (demander aux collègues si Minecraft a été discuté), ce qui suggère un manque de rigueur dans l'analyse du problème
- Les modèles affichent parfois du non-sens, changements de langue aléatoires et boucles infinies normalement expliqués par des hallucinations, pas des fuites de données
- Les commentaires de Anthropic confirment que c'est une hallucination et expriment la confiance de l'équipe, bien qu'un manque de transparence persistant empêche certitude absolue

**Top commentaires** :

- [throwaway260704](https://news.ycombinator.com/item?id=48786654) : Using a throwaway account for obvious reasons, but I’m very involved in this space using LLMs from multiple providers. I’m aware of at least two instances in which the intermediate infrastructure “swapped” responses, once impacting Claude models and once impacting GPT models, from two different pro…
- [dofm](https://news.ycombinator.com/item?id=48786218) : Just add a line in AGENTS.md that says "never talk about Minecraft unless you're explicitly asked", I'm sure it'll be fine after that.
- [jonhohle](https://news.ycombinator.com/item?id=48786876) : I’ve been seeing this in Gemini in the past few days. Often during a prompt with a reasonably large input set, I’ll get answers that appear to belong to someone else. It may be trigger hallucination, but it seems like it may be cache collisions or something else. I’ve not seen anything to suggest p…

---

[Article original](https://github.com/anthropics/claude-code/issues/74066) · [Discussion HN](https://news.ycombinator.com/item?id=48785485)
