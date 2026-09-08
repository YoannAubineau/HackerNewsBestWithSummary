---
article_fetched_at: '2026-09-08T12:26:18.536626Z'
attempts: 0
content_source: extracted
discussion_comment_count: 187
discussion_fetched_at: '2026-09-08T12:26:16.199278Z'
error: null
guid: https://news.ycombinator.com/item?id=49605915
hn_item_id: 49605915
hn_url: https://news.ycombinator.com/item?id=49605915
is_ask_or_show_hn: false
llm_input_tokens: 20263
llm_latency_ms: 15473
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1369
our_published_at: '2026-09-08T12:04:01Z'
rewritten_title: Tristan Buckmaster annonce des résultats de fini-temps blow-up et
  décrit les pressions d'OpenAI
source_published_at: '2026-09-08T05:42:28Z'
status: summarized
summarized_at: '2026-09-08T12:26:41.377444Z'
title: Navier-Stokes – Tristan Buckmaster [pdf]
url: https://cims.nyu.edu/~tristanb/statement.pdf
---

## Résumé de l'article

Tristan Buckmaster, mathématicien à Princeton, a publié avec Levent Alpöge trois résultats de fini-temps blow-up (explosion en temps fini) pour des équations aux dérivées partielles : pour les milieux poreux incompressibles, Boussinesq et l'Euler 3D incompressible, en utilisant des modèles de langage (Claude, GPT-5.6 Sol) pour formaliser et affiner les approches de recherche initiées par Córdoba et Martínez-Zoroa. Ces travaux sont publiés avec des preuves formalisées en Lean.

Cependant, Buckmaster expose également comment OpenAI l'a contacté après que des rumeurs aient circulé sur son travail, prétendant qu'un modèle interne avait résolu le problème du Navier-Stokes forcé. Durant les appels, OpenAI aurait révélé progressivement l'implication d'une équipe entière, d'une formation antérieure sur le problème, et d'une quantité massive de ressources informatiques. OpenAI aurait proposé que Buckmaster signe seul un article présentant le résultat OpenAI (tentant de retirer Levent Alpöge, qui travaille chez Anthropic), avec des menaces implicites si Buckmaster rendait l'incident public.

- Buckmaster et Alpöge ont formalisé en Lean trois résultats majeurs de blow-up en temps fini en s'appuyant sur le programme lancé par Córdoba et Martínez-Zoroa, en utilisant des LLM pour atteindre le forçage lisse
- OpenAI a contacté Buckmaster le 6 septembre 2024 affirmant qu'un modèle interne avait résolu le blow-up forcé du Navier-Stokes après que des rumeurs circulent
- Au cours des appels, OpenAI a admis progressivement qu'une équipe, pas un simple modèle, travaillait dessus depuis plusieurs jours avec énormément de ressources informatiques
- OpenAI a proposé deux arrangements : soit publier simultanément, soit que Buckmaster signe seul un article reconnaissant le résultat OpenAI (en retirant Alpöge) ; Buckmaster a refusé les deux
- Buckmaster affirme avoir été menacé implicitement (« pourquoi veux-tu ruiner ta carrière ? ») et appelle à la transparence sur ce qui s'est réellement passé

## Discussion sur Hacker News (187 commentaires)

**Avis positifs** :
- Les accusations de Buckmaster révèlent un schéma problématique : OpenAI aurait lancé son effort après avoir entendu parler de son travail, chose admise par OpenAI elle-même, ce qui soulève légitimement des questions éthiques sur la compétition entre labs.
- Le refus d'OpenAI de répondre directement aux questions sur l'utilisation des données d'entraînement et des sessions Codex est hautement suspect et contraste avec la transparence attendue en académie.
- L'exigence d'OpenAI de retirer Alpöge (employé d'Anthropic) de la liste des auteurs est contraire aux normes académiques et constitue une forme de discrimination basée sur l'affiliation institutionnelle.
- Le timing hautement suspect—OpenAI assemblerait une équipe entière en quelques jours après les rumeurs, en utilisant la même approche peu évidente qu'un petit groupe de chercheurs—suggère une connaissance interne du travail de Buckmaster.
- Les menaces implicites (« pourquoi tu détruirais ta carrière ? » suivi de « si tu ne veux pas que je sois gentil, je ne serai pas gentil ») constituent un véritable chantage académique selon plusieurs observateurs.

**Avis négatifs** :
- Il n'existe aucune preuve concrète que les données de Codex ont été utilisées ; Buckmaster lui-même déclare ne pas en être certain, et les employés d'Anthropic jugent cette hypothèse extrêmement improbable.
- L'approche via forcing provenant d'un article publié en 2023 était déjà dans les données d'entraînement des modèles ; OpenAI aurait pu la redécouvrir indépendamment avec une puissance de calcul massive.
- Le récit de Buckmaster est unilatéral et partiellement basé sur des spéculations sur les intentions d'OpenAI ; la compréhension complète requiert la version d'OpenAI, qui n'est pas encore disponible.
- Confondre deux chercheurs utilisant des services cloud externes OpenAI avec l'espionnage relève de naïveté : conserver du secret en envoyant des données à des tiers est problématique par design.
- Les chercheurs auraient dû négocier formellement à l'avance plutôt que d'utiliser les modèles d'OpenAI tout en s'attendant à un secret complet, ce qui reflète une mauvaise planification plutôt qu'une malveillance claire.

**Top commentaires** :

- [qnleigh](https://news.ycombinator.com/item?id=49606568) : « It was also said that if OpenAI posted after us, they would say that we deserved the Clay Prize, and that we were the “closest humans to the problem”. I declined both offers. I said that if OpenAI released its result in the way proposed I would go public with what happened. The reply was, “Why »…
- [n2d4](https://news.ycombinator.com/item?id=49607239) : Drama/accusation summary: - Aug 15th: Tristan Buckmaster & Levent Alpöge make progress on a few important math problems, "finite-time blowup with smooth forcing for incompressible porous media, for Boussinesq, and for 3d incompressible Euler." - they do NOT have a proof for the $1,000,000 Millenium…
- [mayakacz](https://news.ycombinator.com/item?id=49606404) : I'm not one to comment often but this really pisses me off. OpenAI looked at user data, stole world class researchers' work, and then tried to threaten those researchers to do what would make their corporation profit \(which they would anyways!\). Imagine you have been working on a terribly difficult…

---

[Article original](https://cims.nyu.edu/~tristanb/statement.pdf) · [Discussion HN](https://news.ycombinator.com/item?id=49605915)
