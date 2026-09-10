---
article_fetched_at: '2026-09-10T22:07:02.134528Z'
attempts: 0
content_source: extracted
discussion_comment_count: 495
discussion_fetched_at: '2026-09-10T22:06:56.077108Z'
error: null
guid: https://news.ycombinator.com/item?id=49639408
hn_item_id: 49639408
hn_url: https://news.ycombinator.com/item?id=49639408
is_ask_or_show_hn: false
llm_input_tokens: 42978
llm_latency_ms: 13284
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1193
our_published_at: '2026-09-10T21:25:07Z'
rewritten_title: Mathématicien remet en question la transparence d'OpenAI sur l'accès
  aux données de recherche non publiées
source_published_at: '2026-09-10T06:49:43Z'
status: summarized
summarized_at: '2026-09-10T22:08:01.953583Z'
title: More questions about whether researchers can trust OpenAI with unpublished
  math
url: https://mathstodon.xyz/@andreasthom/117240535270608201
---

## Résumé de l'article

Un chercheur en mathématiques expose des préoccupations concernant la confiance que les mathématiciens peuvent accorder à OpenAI pour traiter leurs travaux non publiés. Après que OpenAI ait annoncé la découverte d'un groupe non sofique, le chercheur avait demandé à OpenAI si ses conversations privées avec ChatGPT sur des problèmes mathématiques avaient été utilisées dans l'entraînement ou l'accès du modèle. La réponse catégorique d'OpenAI (« cela ne s'est pas produit ») lui semble délibérément ambiguë et insuffisamment transparente.

- Un mathématicien avait discuté activement sur ChatGPT du problème d'appariement d'expanseurs et d'extensions de travaux en collaboration, puis demandé explicitement si ces conversations avaient influencé les résultats d'OpenAI
- OpenAI a répondu de manière catégorique mais sans clarifier si la réponse concernait uniquement l'accès direct ou aussi l'inclusion dans les données d'entraînement
- Dans une affaire ultérieure (Buckmaster-Alpöge), OpenAI déclare ne pas avoir accédé à des données utilisateur spécifiques mais admet ne pouvoir exclure que des données « désidentifiées » aient amélioré ses modèles
- Le chercheur juge cette réponse malhonnête et craint que le manque de transparence d'OpenAI ne compromette davantage la collaboration scientifique que les résultats générés par l'IA ne la bénéficient

## Discussion sur Hacker News (495 commentaires)

**Avis positifs** :
- Les modèles d'IA démontrent des capacités réelles en mathématiques et peuvent potentiellement résoudre des problèmes complexes indépendamment, ce qui constituerait un progrès scientifique véritable.
- L'utilisation de données de conversation pour l'entraînement des modèles est une pratique courante et les chercheurs devraient prendre des mesures préventives (désactiver explicitement l'entraînement, utiliser des modèles locaux) plutôt que de s'en remettre entièrement aux promesses des entreprises.
- La découverte scientifique a toujours reposé sur la synthèse d'idées existantes et l'interaction entre esprits; attribuer tout le crédit à OpenAI plutôt que de reconnaître les contributions antérieures serait un problème de citation académique standard, pas un vol.
- Les mathématiciens accusateurs n'avaient pas finalisé leurs preuves et n'ont donc pas réellement résolu les problèmes; OpenAI aurait pu arriver indépendamment à des solutions avec ses modèles puissants et ses ressources massives de calcul.

**Avis négatifs** :
- OpenAI a entendu des rumeurs que des problèmes avaient été résolus, puis a lancé immédiatement une tentative de les résoudre avec des ressources massives (millions de dollars, 300 milliards de tokens) en utilisant potentiellement un modèle entraîné après que les chercheurs aient fourni leurs données de chat.
- Le timing suspect et les techniques spécialisées utilisées par le modèle OpenAI correspondent étroitement aux approches que les mathématiciens exploraient dans leurs conversations privées, suggérant un plagiat plutôt qu'une découverte indépendante.
- OpenAI a menacé les chercheurs de « ruiner leur carrière » et tenté de les forcer à exclure un collaborateur d'Anthropic de l'attribution, puis a omis de citer proprement les travaux antérieurs pertinents, ce qui constitue une malveillance délibérée au-delà d'une simple négligence.
- OpenAI affirme ne pas pouvoir vérifier si les données ont été utilisées tout en refusant d'audit transparent; cette opacité intentionnelle, combinée à l'historique de non-respect des engagements de confidentialité, suggère une culpabilité plutôt qu'une innocence.
- Le modèle commercial d'OpenAI repose intrinsèquement sur l'extraction et l'utilisation non attribuée de données propriétaires d'utilisateurs; permettre aux chercheurs de continuer à utiliser ces services crée un cycle où leurs propres avancées financent leurs futurs concurrents.

**Top commentaires** :

- [nezi](https://news.ycombinator.com/item?id=49648436) : I think it's a useful analogy to compare OpenAI to a human collaborator. These researchers willingly collaborated with an OpenAI model, giving it ideas, and OpenAI provided useful replies. Then, OpenAI goes ahead and publishes work along the lines of this collaboration, without attributing the rese…
- [sashank\_1509](https://news.ycombinator.com/item?id=49645695) : Both things can be true: 1. OpenAI when using your chats in pretraining is improving its model’s intuition. The model parameter size is massive, and while the data is OOM larger it is plausible that model remembers stuff about chats that improves its latent representation. 2. During RL on verifiabl…
- [bertonvv](https://news.ycombinator.com/item?id=49641828) : I've been wondering whether AI really is improving rapidly at open problems or we're being fooled. - OpenAI invites researchers to use their models, in fact giving at least 100,000 researchers free access\[1\], but there are also those that pay - Internal OpenAI models are reportedly solving open pro…

---

[Article original](https://mathstodon.xyz/@andreasthom/117240535270608201) · [Discussion HN](https://news.ycombinator.com/item?id=49639408)
