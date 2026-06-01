---
article_fetched_at: '2026-06-01T05:35:45.222858Z'
attempts: 0
content_source: extracted
discussion_comment_count: 49
discussion_fetched_at: '2026-06-01T05:35:44.673071Z'
error: null
guid: https://news.ycombinator.com/item?id=48346019
hn_item_id: 48346019
hn_url: https://news.ycombinator.com/item?id=48346019
image_url: https://worker.jart.workers.dev/rseq/rseq.png
is_ask_or_show_hn: false
llm_input_tokens: 14499
llm_latency_ms: 13380
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1172
our_published_at: '2026-06-01T04:50:21Z'
rewritten_title: Les séquences redémarrables rseq permettent des structures de données
  sans verrous sur Linux
source_published_at: '2026-05-31T14:38:48Z'
status: summarized
summarized_at: '2026-06-01T05:36:04.955846Z'
title: Restartable Sequences
url: https://justine.lol/rseq/
---

## Résumé de l'article

Les séquences redémarrables (rseq) sont une fonctionnalité Linux 4.18+ qui permet de créer des structures de données thread-safe sans verrous ni opérations atomiques, en utilisant une communication partagée avec le noyau pour éviter les interruptions critiques. Le noyau surveille l'exécution d'une courte séquence d'instructions et redémarre le thread automatiquement s'il est préempté, offrant des gains de performance spectaculaires sur les systèmes à nombreux cœurs.

- Les séquences rseq fonctionnent en enregistrant une région critique auprès du noyau via une structure `rseq_cs` ; le noyau vérifie le compteur de programme lors d'une préemption et force un redémarrage si nécessaire, éliminant les costs des verrous traditionnels (15 nanosecondes) comparés aux opérations thread-locales (1 nanoseconde)
- Les gains de performance mesurés atteignent 34x à 43x sur les allocateurs mémoire (malloc/jemalloc) et jusqu'à un million de fois plus rapide qu'une solution naïve avec mutex, notamment sur les CPU haute performance (96-192 cœurs)
- L'implémentation requiert actuellement du code assembleur à la main sur Linux ; les exemples fournis montrent comment coder des opérations push/pop sur listes chaînées shardées par CPU, avec support x86-64 et ARM64 (Ampere)
- Le sharding des structures de données par CPU (chaque CPU disposant de son propre mutex et cacheline) reste nécessaire en standard, mais rseq élimine complètement les verrous pour les opérations courtes et non interruptibles
- Cosmopolitan Libc intègre déjà rseq dans ses implémentations malloc/glibc, et d'autres allocateurs (tcmalloc, jemalloc) en bénéficient ; l'adoption devrait s'accélérer avec les CPU haute densité devenant abordables

## Discussion sur Hacker News (49 commentaires)

**Avis positifs** :
- Les restartable sequences (rseq) offrent une solution élégante pour synchroniser des structures de données par CPU sans mutex ni atomiques, avec un coût d'abstraction quasi nul grâce à la communication kernel en mémoire partagée
- La technique est bien établie et générale : elle permet d'éviter les faux partages de cache ligne (false sharing) en shardant les données par CPU, ce qui peut accélérer dramatiquement les performances multicore
- rseq devrait être plus accessible aux développeurs Linux : il existe une bibliothèque (librseq) avec helpers pour cas courants (compteurs, listes) qui éliminent le besoin d'écrire de l'assembleur
- Le concept n'est pas nouveau (technique ~25 ans) et s'applique bien au-delà des cas d'usage simples, offrant une introspection générique des points de préemption
- Pour les développeurs indépendants et chercheurs, les coûts pour tester ces optimisations ne sont pas prohibitifs (instances cloud à la demande, machines de production existantes)

**Avis négatifs** :
- L'article débute par une rhétorique peu professionnelle sur les besoins en matériel ($20k) qui détourne du sujet technique ; cela ressemble à une justification auto-gratifiante plutôt qu'une introduction accessible
- La présentation de rseq dans l'article n'est pas très accessible et devrait mentionner que la bibliothèque librseq existe pour éviter d'écrire de l'assembleur dans la plupart des cas
- L'affirmation que les mutexes userspace sont meilleurs que ceux du CPU/matériel est mal formulée et confuse : c'est en réalité un algorithme différent (sharding par CPU) qui évite les contentions, pas une supériorité inhérente du software
- Pour les développeurs d'applications générales et de bibliothèques multi-thread, rseq présente des défis pratiques ; ce n'est vraiment avantageux que si on contrôle tous les threads ou qu'on peut utiliser des données per-CPU
- La communication bidirectionnelle kernel-userspace via mémoire partagée soulève des questions légitimes de sécurité et de stabilité qui méritent d'être adressées

**Top commentaires** :

- [GlenTheMachine](https://news.ycombinator.com/item?id=48346479) : If you had no idea what a restorable sequence is the takeaway is about halfway down the OP: “This is why Linux now provides rseq\(\) which is a much more enlightened solution. With restartable sequences, you actually can get rid of both the mutex and atomics, while the OS continues to fully abstract…
- [senderista](https://news.ycombinator.com/item?id=48347339) : I'm surprised there was no reference to the librseq library, maintained by the rseq implementer: https://github.com/compudj/librseq This has helpers for common use cases like counters and linked lists. You shouldn't need to write assembly at all to use rseq in most applications.
- [khuey](https://news.ycombinator.com/item?id=48346469) : Maybe I'm just getting old but the "if you don't spend $20,000 on a workstation you're going to be left behind like a dinosaur" at the top of this article is a huge turn off to reading any further. And I say that as someone who owns a workstation with more cores than the author's.

---

[Article original](https://justine.lol/rseq/) · [Discussion HN](https://news.ycombinator.com/item?id=48346019)
