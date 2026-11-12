---
article_fetched_at: '2026-11-12T01:12:43.045831Z'
attempts: 0
content_source: extracted
discussion_comment_count: 113
discussion_fetched_at: '2026-11-12T01:11:49.862101Z'
error: null
guid: https://news.ycombinator.com/item?id=50443090
hn_item_id: 50443090
hn_url: https://news.ycombinator.com/item?id=50443090
image_url: https://substackcdn.com/image/fetch/$s_!R25V!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff0ea2d4-ea2d-440b-ad51-1bc99a695511_2022x1382.png
is_ask_or_show_hn: false
llm_input_tokens: 13882
llm_latency_ms: 11657
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1322
our_published_at: '2026-11-12T00:35:36Z'
rewritten_title: 'Architecture des processeurs Zen 6 d''AMD : améliorations de la
  prédiction de branches et restructuration des moteurs d''exécution'
source_published_at: '2026-11-10T17:02:32Z'
status: summarized
summarized_at: '2026-11-12T01:15:51.723067Z'
title: 'AMD''s Zen 6 Family: Feeding the Beast'
url: https://chipsandcheese.com/p/amds-zen-6-family-feeding-the-beast
---

## Résumé de l'article

AMD a dévoilé sa famille de cœurs Zen 6, la prochaine génération après Zen 5, avec des changements architecturaux majeurs rappelant la transition Zen 1 à Zen 2. La gamme inclut deux variantes : Zen 6 optimisé pour les fréquences élevées et Zen 6c conçu pour absorber la latence mémoire avec des structures out-of-order plus grandes.

- Le prédicteur de branchement de Zen 6 affiche une latence réduite (3 à 3,5 ns par mauvaise prédiction contre 3,5 à 4 ns sur Zen 5) et peut traiter deux branchements par cycle dans le cache L1 d'instructions
- L'unité de multiplication entière passe de trois à deux unités, tandis que les capacités VNNI doublent (2 à 4 unités), portant le débit 512-bit VNNI de 1,99 à 3,88 instructions par cycle
- Le moteur out-of-order diffère entre les deux variantes : Zen 6c dispose d'un buffer de réordonnancement de 640 entrées (vs 576 sur Zen 6), d'un fichier de registres vecteur de 180 unités (vs 138), et d'une file de chargement de 330 (vs 280)
- En SPEC CPU 2026, l'EPYC 9686F (Zen 6) devance l'EPYC 9996 (Zen 6c) d'environ 18% en taux entier et flottant, mais Zen 6c bénéficie d'un cache L3 plus grand (128 MB vs 48 MB) sur les charges mémoire-intensives
- La latence L3 s'accroît significativement (55 cycles pour Zen 6, 66 pour Zen 6c contre 47 pour Zen 5), compensée en nanosecondes par les fréquences d'horloge plus élevées de Zen 6

## Discussion sur Hacker News (113 commentaires)

**Avis positifs** :
- AMD offre une segmentation efficace avec plusieurs options de canaux mémoire (2 en consumer, 4 en Threadripper, jusqu'à 16 en EPYC Zen 6) adaptées aux différents besoins de bande passante sans surcoûts inutiles pour les workloads non limités par la mémoire.
- Les améliorations de Zen 6c sont impressionnantes : 32 cœurs par CCD avec cache L3 accru et structures OoO élargies pour masquer la latence mémoire, montrant une optimisation réfléchie de l'architecture pour les hauts core counts.
- Les optimisations du prédicteur de branche et de l'exécution spéculative restent cruciales et bénéfiques, notamment grâce à la prédiction bidirectionnelle qui aide à absorber la latence mémoire croissante.
- La nouvelle puce I/O sur nœud plus petit pour Zen 6 consumer promet d'améliorer significativement le contrôleur mémoire, un problème connu de Zen 4/5 où la stabilité à 4 sticks reste difficile.
- Les structures de charge vectorielle améliorées (4 par cycle à 256 bits) et les pipes VNNI renforcés ciblent efficacement les workloads modernes sans surcharge excessive.

**Avis négatifs** :
- Ajouter plus de contrôleurs mémoire est physiquement et économiquement prohibitif : les pins du socket, le routage sur carte mère et la complexité des PCB coûtent cher, limitant les possibilités d'amélioration memory bandwidth côté consumer.
- Le vrai problème reste la latence mémoire, non la bande passante ; peu de workloads sont réellement limités par la bande passante, et même avec plus de contrôleurs, cela ne résout pas les problèmes de latence qui paralysent les performances.
- La fragmentation socket entre Threadripper et EPYC est contre-productive : elle empêche la réutilisation et l'upgrade des anciennes cartes mère, forçant les clients à racheter du matériel sans raison technique valide.
- La latence L3 augmente significativement sur Zen 6c (16.4ns vs 10.3ns sur Zen 5), symptôme d'un problème de scaling avec 32 cœurs par CCD monolithique qui pourrait nécessiter une partitionnement futur.
- Le graphique SPEC2026 omettait délibérément les P-cores Apple dont les scores (9.8 en entier, 13 en FP) surpassent tout le reste, jetant le doute sur la représentativité du benchmark pour les performances réelles optimisées (notamment AVX-512 sur Zen).

**Top commentaires** :

- [bmenrigh](https://news.ycombinator.com/item?id=50445782) : The worst thing about consumer \(AM5\) Zen4 and Zen5 is the I/O die chiplet and memory controller on it. I've heard they're finally going to ship a new I/O chiplet in Zen6 on a much smaller node. Their existing AM5 Zen4/5 memory controller when using both memory channels is terrible. Extremely hard o…
- [joebonrichie](https://news.ycombinator.com/item?id=50443687) : The instruction level parallelism in the 2-ahead branch prediction is super cool stuff, I know zen5 had this feature but it's kind of crazy that memory is so slow relative to the cores that this complexity is beneficial and worthwhile.
- [Remnant44](https://news.ycombinator.com/item?id=50444146) : What looks like a lot of small balanced improvements to the core itself. Four vector loads per cycle at 256b of less, I wonder if the gather performance is finally acceptable? Another balance example, they actually reduced the number of integer multipliers down to two. I wonder if that was to make…

---

[Article original](https://chipsandcheese.com/p/amds-zen-6-family-feeding-the-beast) · [Discussion HN](https://news.ycombinator.com/item?id=50443090)
