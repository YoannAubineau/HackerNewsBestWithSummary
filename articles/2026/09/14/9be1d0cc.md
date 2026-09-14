---
article_fetched_at: '2026-09-14T15:29:02.677185Z'
attempts: 0
content_source: extracted
discussion_comment_count: 300
discussion_fetched_at: '2026-09-14T15:28:57.593847Z'
error: null
guid: https://news.ycombinator.com/item?id=49690554
hn_item_id: 49690554
hn_url: https://news.ycombinator.com/item?id=49690554
is_ask_or_show_hn: false
llm_input_tokens: 29406
llm_latency_ms: 14510
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1163
our_published_at: '2026-09-14T15:13:10Z'
rewritten_title: Pourquoi le format JPEG XL ne convient pas au Web malgré ses capacités
  techniques
source_published_at: '2026-09-14T01:02:37Z'
status: summarized
summarized_at: '2026-09-14T15:30:10.539582Z'
title: The case against JPEG XL
url: https://giannirosato.com/blog/post/case-against-jxl/
---

## Résumé de l'article

JPEG XL est un codec d'image techniquement avancé et polyvalent, mais un article technique détaillé argue qu'il n'est pas adapté aux besoins spécifiques du Web comparé à AVIF et WebP.

- JPEG XL n'offre aucun avantage significatif en compression lossy (la majorité des cas d'usage Web), son seul intérêt réel étant la compression lossless qui ne représente que 12% de gains sur un volume d'images négligeable.
- En efficacité de compression lossy perceptuelle, AVIF surpasse désormais JPEG XL sur toute la gamme de fidélité ; les encodeurs modernes d'AVIF et AV1 sont mieux optimisés grâce à un tuning perceptuel contrôlé, tandis que JPEG XL souffre de limitations structurelles (absence de directional prediction, pas de deblocking filter classique).
- Le temps de décodage de JPEG XL est significativement plus lent que WebP, AVIF et JPEG, créant un risque de sécurité : le format permet de construire des images malveillantes qui prennent des dizaines de secondes à décoder, créant des possibilités d'attaques par déni de service (JXL-bombing) sur appareils bas de gamme.
- JPEG XL est conçu pour être universel (4096 canaux, profondeur arbitraire, recompression JPEG, etc.), ce qui en fait un mauvais choix pour le Web qui nécessite des codecs étroitement ciblés, efficaces et rapides, avec une compatibilité facile.
- L'auteur conclut que bien que JPEG XL soit une technologie pertinente pour les professionnels (suite Adobe, fabricants de caméras), le Web n'en a pas besoin pour le moment ; AVIF et WebP répondent mieux aux contraintes réelles du Web.

## Discussion sur Hacker News (300 commentaires)

**Avis positifs** :
- AVIF offre de meilleures performances globales pour les cas d'usage web typiques et fonctionne bien sur tous les types d'images, contrairement à JPEG XL qui performe moins bien sur les illustrations et captures d'écran
- Le décodage plus rapide d'AVIF (particulièrement en mono-thread sur les appareils mobiles) compense largement les modestes économies de bande passante de JPEG XL, sauf sur les connexions très lentes
- Fragmenter le paysage des formats d'image (WebP, AVIF, JPEG XL) complique déjà suffisamment l'adoption et crée des maux de tête pour les développeurs web et les utilisateurs
- JPEG XL comporte des problèmes de sécurité sérieux (DoS via images malveillantes exploitant la complexité du mode prédictif), notamment lorsque intégré aux PDF
- AVIF dispose maintenant du rendu progressif et a reçu des améliorations significatives grâce aux efforts de développement continus, réduisant l'avantage historique de JPEG XL

**Avis négatifs** :
- JPEG XL offre une meilleure compression sans perte et supporte la réencodage lossless des JPEG avec ~20% d'économie de taille, ce qui AVIF ne peut faire, offrant une valeur réelle pour les archives photo
- JPEG XL supporte le mode lossless plus efficace que WebP/PNG, crucial pour les cas d'usage web ignorés : art communautaires, comparaisons d'images, captures d'écran, art pixel et contenu professionnel
- Le décodage plus lent de JPEG XL reflète une implémentation immature (jxl-rs) et non une limitation intrinsèque du format ; les encodeurs libjxl offrent bien meilleures vitesses que les chiffres présentés
- AVIF se limite à 12 bits par canal et 4:2:0 en profil de base, problématique pour l'illustration, les screenshots et le contenu non-photographique où ces limitations causent une dégradation visible
- JPEG XL devrait être adopté car il unifie lossless et lossy dans un seul format versatile applicable partout (appareils photo, archives, édition professionnelle, web), évitant la fragmentation multi-formats

**Top commentaires** :

- [arthur-st](https://news.ycombinator.com/item?id=49697233) : Strange blog post. Given that it's from a developer of proprietary and paid commercial encoders, the inclusion of their upcoming "aperture-alpha" encoder on the charts that are purportedly about JPEG XL makes this feel like a marketing piece of some fashion. Certainly, they advertise their Iris-Web…
- [cbolton](https://news.ycombinator.com/item?id=49693599) : The article makes a good point: JPEG XL is amazing but not specifically for the typical Web use cases, compared to AVIF. But the conclusion doesn't follow. Having an excellent and versatile format supported by browsers is very useful! Maybe a lossless re-encoding of my website JPEGs to gain 20% siz…
- [Daiz](https://news.ycombinator.com/item?id=49692494) : A potentially major issue I have with AVIF is that because it is based on a video format, any hardware decoding support AVIF will get is likely to be restrained to common video scenarios. This can result in eg. only 4:2:0 YUV being supported by hardware decoders, as that's the upper limit of AV1 Ma…

---

[Article original](https://giannirosato.com/blog/post/case-against-jxl/) · [Discussion HN](https://news.ycombinator.com/item?id=49690554)
