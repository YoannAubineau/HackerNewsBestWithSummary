---
article_fetched_at: '2026-07-13T17:08:11.002176Z'
attempts: 0
content_source: tweet
discussion_comment_count: 232
discussion_fetched_at: '2026-07-13T17:08:09.155787Z'
error: null
guid: https://news.ycombinator.com/item?id=48892512
hn_item_id: 48892512
hn_url: https://news.ycombinator.com/item?id=48892512
image_url: https://pbs.twimg.com/media/HNGOF9QXwAAU_jp.png?name=orig
is_ask_or_show_hn: false
llm_input_tokens: 16024
llm_latency_ms: 8200
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 644
our_published_at: '2026-07-13T17:05:06Z'
rewritten_title: Grok a téléchargé mon répertoire utilisateur sur les serveurs de
  xAI
source_published_at: '2026-07-13T13:39:59Z'
status: summarized
summarized_at: '2026-07-13T17:08:27.617512Z'
title: Grok uploaded my user directory to xAI's servers
url: https://twitter.com/a_green_being/status/2076598897779020159
---

## Résumé de l'article

Tweet de @a_green_being :

> @XBToshi Okay, grok has uploaded my entire user directory to xAI's servers. It contains my SSH keys, my password manager database, my documents, photos, videos, everything...

## Discussion sur Hacker News (232 commentaires)

**Avis positifs** :
- Cet incident confirme que les outils d'IA basés sur le cloud doivent être exécutés dans des environnements sécurisés isolés (VM, conteneurs, utilisateurs Unix restreints) pour éviter l'exposition de données sensibles.
- Les fichiers Markdown comme directives de sécurité sont inefficaces contre des outils non-déterministes ; seules des barrières techniques au niveau du système d'exploitation et des conteneurs offrent une protection réelle.
- Les agents d'IA devraient être traités comme des logiciels tiers non fiables auxquels on ne donne accès qu'aux ressources explicitement nécessaires, en suivant les principes de sécurité éprouvés depuis des décennies.
- Le comportement de Grok révèle des défaillances d'ingénierie graves chez xAI : télécharger automatiquement l'intégralité d'un répertoire utilisateur sans consentement explicite est inacceptable.
- Ce problème met en lumière une tendance dangereuse où les pratiques de sécurité basiques sont ignorées au profit de la commodité et de l'innovation rapide.

**Avis négatifs** :
- Exécuter un agent cloud-based depuis le répertoire personnel ($HOME) sans sandboxing était une décision imprudente de l'utilisateur, comparable à exécuter un script téléchargé sans inspection.
- Pour que les agents d'IA fonctionnent efficacement avec inférence distante, ils ont besoin d'un contexte complet ; télécharger le répertoire peut être une nécessité architecturale plutôt qu'une malveillance.
- L'utilisateur a accepté les conditions d'utilisation en s'inscrivant ; blâmer xAI ignore la responsabilité personnelle d'utiliser les outils de manière sécurisée.
- Les clés SSH non chiffrées stockées sans protections supplémentaires (IP restrictions, mots de passe) représentent une mauvaise pratique de l'utilisateur, indépendamment de l'agent utilisé.
- Plusieurs commentaires soulignent que ce problème affecte aussi Claude et d'autres agents ; l'incident n'est pas unique à Grok mais révèle plutôt une mauvaise compréhension généralisée des risques liés aux agents d'IA.

**Top commentaires** :

- [LetsGetTechnicl](https://news.ycombinator.com/item?id=48892849) : So many of the replies are saying that they should've restricted access using .md files and whatnot. Is really any guarantee that they even follow those? It seems like even if you ask pretty please don't touch those files, there's a chance they will. So many people have just willingly installed spy…
- [simonw](https://news.ycombinator.com/item?id=48893329) : Important to clarify that this was not the Grok agent deciding to read the files. I don't think the LLM had anything to do with this decision at all. It looks like the Grok tool starts a session by deterministically kicking off a full upload of the user's current repository \(and maybe their directo…
- [lobo\_tuerto](https://news.ycombinator.com/item?id=48893015) : The real solution to these kind of problems is sandboxing. I use podman through a bash script to launch a container whenever I want an agent to work on one of my repos. When done I just generate git patches and port back everything generated. In this way I'm not afraid of letting the agents totally…

---

[Article original](https://twitter.com/a_green_being/status/2076598897779020159) · [Discussion HN](https://news.ycombinator.com/item?id=48892512)
