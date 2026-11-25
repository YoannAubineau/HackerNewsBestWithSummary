---
article_fetched_at: '2026-11-25T15:12:18.777695Z'
attempts: 0
content_failure_reason: content not usable
content_source: feed_fallback
discussion_comment_count: 444
discussion_fetched_at: '2026-11-25T15:12:15.201544Z'
error: null
guid: https://news.ycombinator.com/item?id=50637220
hn_item_id: 50637220
hn_url: https://news.ycombinator.com/item?id=50637220
image_url: https://opengraph.githubassets.com/288c9ea432a308e7a05a6af2c1582aa0e361437c7df0d80914515216b0cb4503/openai/math
is_ask_or_show_hn: false
llm_input_tokens: 34739
llm_latency_ms: 7328
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 695
our_published_at: '2026-11-25T14:22:58Z'
rewritten_title: La multiplication matricielle a une complexité de Θ(n^2.25)
source_published_at: '2026-11-25T01:19:26Z'
status: summarized
summarized_at: '2026-11-25T15:13:52.630962Z'
title: Matrix Multiplication is Θ(n^2.25) [pdf]
url: https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf
---

## Résumé de l'article

(unable to load content: content not usable)

## Discussion sur Hacker News (444 commentaires)

**Avis positifs** :
- C'est un résultat fondamental qui établit la borne optimale exacte (ω = 9/4) pour la multiplication matricielle, éliminant définitivement la recherche d'algorithmes asymptotiquement plus rapides.
- Le framework théorique sous-jacent (géométrie tensorielle) est un véritable progrès mathématique qui a des applications bien au-delà de ce problème spécifique.
- Ce type de problème avec vérification formelle (Lean) représente un signal d'entraînement idéal et incontaminé pour améliorer les modèles IA, contrastant avec les benchmarks manipulables.
- Le résultat démontre la capacité remarquable des LLMs à faire des sauts logiques complexes et à orchestrer des preuves sur des centaines de pages, comparables à des percées mathématiques humaines.
- Ces avancées ouvrent la voie à la formalisation et vérification d'autres domaines scientifiques là où c'était impossible avant.

**Avis négatifs** :
- Le titre et descriptions incorrects (O vs Θ) reflètent une confusion conceptuelle fondamentale : confondre la propriété d'une fonction optimale avec le problème lui-même est pédantiquement important mais révèle une imprécision.
- Les preuves générées sont souvent inintelligibles pour les humains et ne contribuent pas à la compréhension mathématique ; ce sont des 'preuves brutes' plutôt que des contributions au savoir mathématique élégant et connecté.
- L'algorithme O(n^2.25) connu est galactique et totalement impratique ; dans la réalité, les matrices sont toujours multipliées en O(n^3) ou avec Strassen, donc zéro impact économique immédiat.
- Ces résultats risquent d'écraser l'avenir des mathématiques humaines en rendant les contributions individuelles obsolètes, créant une barrière à l'entrée infranchissable pour les jeunes mathématiciens.
- Il n'est pas clair que la publication des résultats cryptographiquement sensibles soit exhaustive ou honnête, étant donné les incitations économiques et les préoccupations de sécurité nationale.

**Top commentaires** :

- [zone411](https://news.ycombinator.com/item?id=50637782) : For context, OpenAI's 4 new papers resolve 8 problems of the Top 500 Open Problems in Math list \(LLM ranked, https://proofatlas.ai/open-problems/\). They include: \#25 — Matrix-multiplication exponent equals two. The paper gives the exact exponent 9/4 over every field, refuting the conjecture. \#89 —…
- [StableAlkyne](https://news.ycombinator.com/item?id=50637909) : We've seen so much interesting work come out of OpenAI and Anthropic in the last few weeks. It really feels like both have tapped into the pioneering spirit of the old Bell Labs. But, Bell Labs existed as part of an agreement with the government that AT&T's monopoly would be used for the public goo…
- [BoppreH](https://news.ycombinator.com/item?id=50640069) : There's a snowball's chance in hell that they haven't found any cryptographically-relevant results. And given how security averse the NSA has been \(they pushed NIST to standardize a backdoored random number generator then paid the RSA company $10 million to use it\[1\]\), I have the feeling that the f…

---

[Article original](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf) · [Discussion HN](https://news.ycombinator.com/item?id=50637220)
