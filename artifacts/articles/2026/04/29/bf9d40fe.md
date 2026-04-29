---
article_fetched_at: '2026-04-29T10:35:34.870461Z'
attempts: 0
content_source: extracted
discussion_comment_count: 132
discussion_fetched_at: '2026-04-29T10:35:34.442476Z'
error: null
feed_summary: '<p>Article URL: <a href="https://corrode.dev/blog/bugs-rust-wont-catch/">https://corrode.dev/blog/bugs-rust-wont-catch/</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=47943499">https://news.ycombinator.com/item?id=47943499</a></p>

  <p>Points: 292</p>

  <p># Comments: 121</p>'
guid: https://news.ycombinator.com/item?id=47943499
hn_item_id: 47943499
hn_url: https://news.ycombinator.com/item?id=47943499
image_url: https://corrode.dev/blog/bugs-rust-wont-catch/social.png
is_ask_or_show_hn: false
llm_input_tokens: 20108
llm_latency_ms: 14989
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1354
our_published_at: '2026-04-29T09:57:25Z'
rewritten_title: Les bugs que le compilateur Rust ne peut pas détecter dans les outils
  système
source_published_at: '2026-04-29T02:19:11Z'
status: summarized
summarized_at: '2026-04-29T10:35:56.109620Z'
title: Bugs Rust won't catch
url: https://corrode.dev/blog/bugs-rust-wont-catch/
---

## Résumé de l'article

Une analyse détaillée de 44 CVE découvertes dans uutils, la réimplémentation en Rust des GNU coreutils, révèle une classe importante de bugs que le compilateur Rust et ses outils d'analyse statique ne peuvent pas prévenir. Bien que Rust élimine les débordements de tampon et les fuites mémoire, les outils système restent vulnérables aux problèmes de logique métier, particulièrement à la frontière entre le code contrôlé et le monde extérieur imprévisible.

- **TOCTOU (Time-Of-Check-Time-Of-Use) et symlinks** : La majorité des CVE provient d'appels système multiples sur le même chemin, permettant aux attaquants de remplacer les chemins par des symlinks entre les vérifications et les actions. Utiliser `create_new()`, les descripteurs de fichiers et opérations relatives au lieu des chemins directs.

- **Encodage UTF-8 inapproprié** : Les chemins Unix, arguments et contenus de flux sont des octets bruts, pas du texte UTF-8. Convertir avec `from_utf8_lossy()` corrompt silencieusement les données ; utiliser `OsStr`, `Path` et `Vec<u8>` pour rester dans le domaine des octets.

- **Paniques non contrôlées** : Chaque `unwrap()`, `expect()` ou opération d'indexation sur des entrées non fiables est un déni de service potentiel. Préférer `?`, `get()`, et `checked_*()` pour gérer les erreurs proprement dans le code traitant des entrées externes.

- **Erreurs ignorées ou perdues** : Des CVE résultent de l'utilisation de `.ok()`, `.unwrap_or_default()` ou `let _ =` qui masquent des erreurs critiques. Toujours tracer et signaler les erreurs, en particulier les échecs d'opérations de fichiers.

- **Incompatibilité comportementale avec GNU** : Les scripts shell supposent la compatibilité avec GNU coreutils. Les divergences en codes de sortie, gestion des cas limites ou sémantique des options deviennent des failles de sécurité; uutils exécute maintenant la suite de tests GNU en CI.

## Discussion sur Hacker News (132 commentaires)

**Avis positifs** :
- Rust a bien livré sur la sécurité mémoire promise, éliminant des classes entières de bugs (débordements de buffer, use-after-free) impossibles en code sûr, ce qui reste un progrès significatif par rapport à C/C++
- Les bugs trouvés révèlent des problèmes systémiques des APIs Unix/POSIX elles-mêmes (TOCTOU, NSS dynamique) plutôt que des failles du langage, ce qui pourrait s'améliorer via une meilleure stdlib ou des APIs de haut niveau comme openat()
- Le projet uutils a démarré comme un exercice d'apprentissage Rust en 2013, pas comme une tentative professionnelle de remplacer coreutils; les bugs découverts et les tests du test suite GNU en CI représentent une amélioration continue appropriée
- Comparer à GNU coreutils au démarrage (années 1980) en bugs/CVEs aurait probablement montré des problèmes similaires; le rewrite pourrait atteindre la maturité de l'original en quelques années si bien maintenu
- La sécurité filesystem en général est 'absolument atroce' selon les experts (cf blog de Sebastian Wick); le problème ne se limite pas à Rust mais affecte tous les langages confrontés aux APIs Unix complexes

**Avis négatifs** :
- Un rewrite de zéro réintroduit inévitablement des bugs fixes depuis des décennies dans GNU coreutils; ces bugs ne sont pas des 'problèmes Rust' mais l'artefact d'ignorer l'expertise accumulée du logiciel original
- Les auteurs uutils ont volontairement évité de lire le code source GNU coreutils pour des raisons de licence (MIT vs GPL), se privant des leçons apprises et des cas limites documentés dans 25+ ans de bugfixes
- Les erreurs listées sont des bévues amateurales évidentes (comparer un Path à '/' au lieu de vérifier l'inode, perdre les erreurs critiques de chmod) qui montrent un manque de compréhension basique des APIs POSIX, pas un manque de compétences Rust
- Ubuntu a accepté ce code immature en production sans les tests/audits nécessaires d'abord, tout en affirmant que 'Rust = plus sûr' était suffisant; la stdlib Rust std::fs expose les APIs bas-niveau Unix sans abstractions sécuritaires alternatives de haut niveau
- Les développeurs n'ont pas étudié pourquoi GNU coreutils fonctionnent comme ils le font (p.ex. opérations sur descripteurs au lieu de chemins); ces 'gotchas' Unix nécessitent une expertise système que le compilateur Rust ne peut pas compenser

**Top commentaires** :

- [collinfunk](https://news.ycombinator.com/item?id=47944267) : Hi, I am one of the maintainers of GNU Coreutils. Thanks for the article, it covers some interesting topics. In the little Rust that I have used, I have felt that it is far too easy to write TOCTOU races using std::fs. I hope the standard library gets an API similar to openat eventually. I just wan…
- [wahern](https://news.ycombinator.com/item?id=47944210) : « What’s notable is that all of these bugs landed in a production Rust codebase, written by people who knew what they were doing » They knew how to write Rust, but clearly weren't sufficiently experienced with Unix APIs, semantics, and pitfalls. Most of those mistakes are exceedingly amateur from t…
- [lionkor](https://news.ycombinator.com/item?id=47945961) : I struggle to find anything on this post that wouldn't be caught by some kind of unit test or manual review, especially when comparing with the GNU source for the coreutils. The whole coreutils rewrite is a terrible idea\[1\] and clearly being done in the wrong way \(without the knowledge gained from…

---

[Article original](https://corrode.dev/blog/bugs-rust-wont-catch/) · [Discussion HN](https://news.ycombinator.com/item?id=47943499)
