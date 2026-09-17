---
article_fetched_at: '2026-09-17T17:57:18.193204Z'
attempts: 0
content_failure_reason: connection failed
content_source: feed_fallback
discussion_comment_count: 130
discussion_fetched_at: '2026-09-17T17:56:53.624769Z'
error: null
guid: https://news.ycombinator.com/item?id=49715813
hn_item_id: 49715813
hn_url: https://news.ycombinator.com/item?id=49715813
is_ask_or_show_hn: false
llm_input_tokens: 9567
llm_latency_ms: 8475
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 654
our_published_at: '2026-09-17T17:16:31Z'
rewritten_title: Fujitsu lance le processeur de nouvelle génération fabriqué au Japon
  FUJITSU-MONAKA
source_published_at: '2026-09-15T17:28:38Z'
status: summarized
summarized_at: '2026-09-17T17:59:07.776022Z'
title: Fujitsu launches made-in-Japan next-generation CPU FUJITSU-MONAKA
url: https://global.fujitsu/en-global/pr/news/2026/09/14-02
---

## Résumé de l'article

(unable to load content: connection failed)

## Discussion sur Hacker News (130 commentaires)

**Avis positifs** :
- Fujitsu poursuit une stratégie cohérente d'innovation HPC en s'appuyant sur ARM (comme précédemment avec SPARC), avec une architecture personnalisée utilisant ARMv9.3-A avec extensions AI/ML (FP8) et SVE2 en 256-bit
- Le design Fujitsu offre une excellente efficacité énergétique pour l'inférence AI, rivalisant avec les GPU modernes (844 GB/s de bande passante mémoire, 4.3-6 TFLOPS) tout en consommant moins d'énergie
- C'est une bonne initiative pour la diversification du marché HPC et une alternative compétitive face à la domination NVIDIA, poussant l'innovation dans un secteur concentré
- Fujitsu a historiquement excellé dans la conception de microarchitectures (meilleures implémentations SPARC que Sun), les équipes d'ingénierie japonaise sont réputées excellentes en hardware

**Avis négatifs** :
- La communication est délibérément opaque sur la fabrication réelle : le CPU est conçu au Japon mais fabriqué par TSMC en Taïwan (processus 2nm), contredisant le discours de 'souveraineté' affirmé
- Le terme 'souveraineté' est trompeur car la dépendance à TSMC et aux licences ARM (dont SoftBank est propriétaire, conglomérat japonais, mais non-contrôlé) persiste; aucune protection réelle contre les sanctions ou les ruptures de chaîne d'approvisionnement
- L'absence initial de SME (Scalable Matrix Extension) et les limitations architecturales rendent le processeur moins compétitif que les GPU haut de gamme; seul 2 CPUs par nœud contre 4-8 GPUs habituellement
- Historique grave de Fujitsu : le scandale du Post Office britannique révèle des défaillances logicielles critiques et une collusion éthique, érodant la confiance; les performances logicielles japonaises restent généralement faibles
- Disponibilité restreinte (Japon, Europe, secteur défense uniquement; pas USA) limite drastiquement le marché potentiel et la rentabilité commerciale; modèle économique questionnable face à la concurrence établie

**Top commentaires** :

- [a11r](https://news.ycombinator.com/item?id=49742389) : Back in 2008 Fujitsu has one of the best performing 10Gbps Switches. We were building 40 Gbps packet sniffers at Google \(4x 10 Gbps NICs\) and needed switches that could do things like mirror traffic across ports at line rate. Fujitsu was way ahead of the pack. I always wondered what held them back…
- [jaen](https://news.ycombinator.com/item?id=49743357) : More detailed presentations about the Monaka CPU: wccftech summary: https://wccftech.com/fujitsus-monaka-chip-3d-stacks-2nm-cpu-... 2026: https://global.fujitsu/-/media/Project/Fujitsu/Fujitsu-HQ/te... 2023: https://global.fujitsu/-/media/Project/Fujitsu/Fujitsu-HQ/te... FugakuNEXT, the supercomput…
- [irusensei](https://news.ycombinator.com/item?id=49742842) : If anyone is curious and want to skip all the PR talk: \>Combined with SVE2 vector operations and software optimization, It’s ARMv9.

---

[Article original](https://global.fujitsu/en-global/pr/news/2026/09/14-02) · [Discussion HN](https://news.ycombinator.com/item?id=49715813)
