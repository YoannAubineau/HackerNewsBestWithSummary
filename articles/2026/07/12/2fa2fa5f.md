---
article_fetched_at: '2026-07-12T23:43:47.455127Z'
attempts: 0
content_source: extracted
discussion_comment_count: 93
discussion_fetched_at: '2026-07-12T23:43:45.902302Z'
error: null
guid: https://news.ycombinator.com/item?id=48884853
hn_item_id: 48884853
hn_url: https://news.ycombinator.com/item?id=48884853
image_url: https://scrapfly.dev/img/og-default.png
is_ask_or_show_hn: false
llm_input_tokens: 12299
llm_latency_ms: 11019
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1024
our_published_at: '2026-07-12T23:30:51Z'
rewritten_title: Chrome 148 rend Math.tanh utilisable pour identifier le système d'exploitation
  de l'utilisateur
source_published_at: '2026-07-12T21:12:11Z'
status: summarized
summarized_at: '2026-07-12T23:44:05.380151Z'
title: Since Chromium 148, Math.tanh is now fingerprintable to link underlying OS
url: https://scrapfly.dev/posts/browser-math-os-fingerprint/
---

## Résumé de l'article

Depuis Chrome 148, la fonction Math.tanh retourne des bits différents selon le système d'exploitation, car V8 a remplacé son implémentation interne (fdlibm) par l'appel direct à la librairie mathématique du système (libm). Cette différence permet d'identifier si un navigateur s'exécute sur Linux (glibc), macOS (libsystem_m) ou Windows (UCRT) en comparant les derniers bits du résultat pour une même entrée.

- Avant Chrome 148, Math.tanh retournait les mêmes bits sur tous les OS car V8 utilisait sa propre implémentation portable ; depuis, il utilise std::tanh qui lit la libm du système hôte
- Les trois librairies mathématiques (glibc, libsystem_m, UCRT) produisent des coefficients minimax différents et divergent sur environ 25 % des entrées, souvent d'une unité en dernière position (1 ULP)
- Au-delà de Math.tanh, les fonctions CSS de trigonométrie (sin, cos, tan, etc.) et certains chemins Web Audio fuient aussi le système d'exploitation en appelant directement la libm du système
- Pour masquer cette fuite, il faut reproduire bit-à-bit les algorithmes de chaque libm avec les mêmes coefficients et constantes, compiler sans fusion multiply-add automatique, et valider contre du matériel réel
- Scrapfly (un service de web scraping) a implémenté cette reproduction pour que son navigateur reste indistinguishable d'un vrai Chrome, quel que soit le système d'exploitation annoncé

## Discussion sur Hacker News (93 commentaires)

**Avis positifs** :
- La découverte d'une nouvelle surface de fingerprinting via Math.tanh est légitime et soulève des questions importantes sur la sécurité des navigateurs, indépendamment de la qualité de la rédaction.
- Les fonctions transcendantales correctement arrondies (correctly rounded) sont une solution prometteuse pour réduire ces vecteurs de fingerprinting, et c'est un domaine où les progrès récents sont significatifs.
- Le problème des vectors de fingerprinting est systémique : combinaisons de timing, arrondis et résolutions créent des signatures quasi-impossibles à masquer, justifiant une approche législative et sociétale.
- Même les navigateurs axés sur la vie privée (Tor Browser, Mullvad) ont renoncé à masquer l'OS en raison de la multiplicité des vecteurs de fingerprinting, montrant l'ampleur du défi.

**Avis négatifs** :
- La rédaction de l'article est clairement générée par LLM avec un style répétitif et superficiel, ce qui distrait du contenu technique et nuit à la crédibilité du rapport.
- L'article ignore que le fingerprinting par version de navigateur est déjà largement possible via des milliers d'autres vecteurs (nouvelles fonctionnalités, bugs), rendant cette découverte spécifique incrémentale plutôt que révolutionnaire.
- La menace de fingerprinting est surévaluée : la plupart des utilisateurs ne spoofent pas leur User-Agent pour un autre OS, et les solutions de détection de bots se concentrent sur d'autres techniques plus fiables que Math.tanh.
- Interdire le fingerprinting légalement s'avère techniquement impossible à définir sans empêcher des usages légitimes (fraud detection, reconnaissance d'appareils volés), créant un problème de définition plutôt que de solution.
- Les scrapers abusifs mentionnés ont intérêt à promouvoir ces découvertes pour que les vecteurs soient «fixés» et rendre leurs activités moins détectables, remettant en question les motifs derrière cet article.

**Top commentaires** :

- [Aurornis](https://news.ycombinator.com/item?id=48885018) : « One tanh call on the right input is a per-OS signature. Claim macOS, return Linux math bits, and you have contradicted your own User-Agent. » They \(or rather the LLM that wrote this\) missed that this is possibly fingerprintable to browser version range, which is slightly more interesting. Most us…
- [jeroenhd](https://news.ycombinator.com/item?id=48885035) : Kind of a smart move by this company: write up an AI analysis of all fingerprinting techniques in hopes they get fixed after outrage so their scraping company can make more money. If it weren't for companies like this, fingerprinting wouldn't be so ubiquitous and the internet would be a better plac…
- [sjrd](https://news.ycombinator.com/item?id=48884945) : I guess that's one more good reason to push for correctly rounded transcendental functions. I recently learned that they're basically solved now. \[1\] \[1\] https://arith2026.org/program.html \(2nd keynote\)

---

[Article original](https://scrapfly.dev/posts/browser-math-os-fingerprint/) · [Discussion HN](https://news.ycombinator.com/item?id=48884853)
