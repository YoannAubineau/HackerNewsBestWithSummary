---
article_fetched_at: '2026-05-19T15:02:59.919478Z'
attempts: 0
content_source: feed_fallback
discussion_comment_count: 116
discussion_fetched_at: '2026-05-19T15:02:58.772167Z'
error: null
guid: https://news.ycombinator.com/item?id=48191602
hn_item_id: 48191602
hn_url: https://news.ycombinator.com/item?id=48191602
image_url: https://s3-eu-west-1.amazonaws.com/images.playcanvas.com/splat/84df8849/v1/xl.webp
is_ask_or_show_hn: false
llm_input_tokens: 7294
llm_latency_ms: 11407
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 705
our_published_at: '2026-05-19T14:10:10Z'
rewritten_title: Gaussian Splat of a Strawberry
source_published_at: '2026-05-19T10:38:47Z'
status: summarized
summarized_at: '2026-05-19T15:03:32.940677Z'
title: Gaussian Splat of a Strawberry
url: https://superspl.at/scene/84df8849
---

## Résumé de l'article

(unable to load content)

## Discussion sur Hacker News (116 commentaires)

**Avis positifs** :
- La technique du Gaussian Splatting offre une qualité visuelle remarquable pour la capture de détails fins, comme en témoigne la reconstruction impressionnante de la fraise avec ses 7920 photos en 20 minutes seulement
- Le dégradé progressif et 'rêveur' des Gaussian Splats en cas de zoom ou rapprochement offre une expérience visuelle unique, intermédiaire entre photographie et modèle 3D, sans le saccade habituel des LOD
- La technologie est très performante sur GPU et peut tourner fluidement même sur des appareils mobiles (iPhone 12 mini), avec des fichiers compressés de taille raisonnable grâce aux formats LOD
- Les applications potentielles sont vastes : remplacement des rendus 3D dans Google Maps, capture d'événements (concerts), jeux vidéo, avec des fichiers très légers pour des vidéos animées haute qualité
- Les outils et ressources se démocratisent (COLMAP datasets gratuits, PlayCanvas, Apple ML-Sharp) rendant la technologie progressivement plus accessible aux créateurs

**Avis négatifs** :
- La qualité se dégrade rapidement lors des zooms profonds ou des vues hors-distribution ; les algorithmes de suivi et d'alignement peinent avec les objets petits ou détaillés (profondeur de champ très réduite en macro)
- La technologie ne gère mal ni la réfraction, ni la réflexion, ni les reflets spéculaires, générant des artefacts de translucidité visibles et une 'face cachée' difficile à capturer complètement
- Le processus de capture reste complexe et coûteux, nécessitant des centaines à milliers de photos multi-angle avec focus stacking, un matériel spécialisé (macros de qualité, écrans bleus) et un réglage minutieux du montage
- Les Gaussian Splats n'encodent pas la géométrie réelle mais plutôt des champs de radiance ; l'intérieur des objets (comme l'intérieur de la fraise) est reconstruit de façon peu plausible ou 'peint'
- L'interface de création reste peu intuitive pour les amateurs ; le suivi des positions de caméra est particulièrement difficile, et la documentation/formation demeure limitée pour les débutants

**Top commentaires** :

- [ArekDymalski](https://news.ycombinator.com/item?id=48194167) : As I have learned about Gaussian Splatting just a few weeks ago, I have \(perhaps funny/naive/stupid\) question: is there any progress or at least theoretical chance to have dynamic lighting?
- [Tade0](https://news.ycombinator.com/item?id=48192077) : Beautiful. What I love about gaussian splats is the way they degrade - instead of a hard cutoff or LoD changing spheres into cubes etc., they get increasingly "dreamy" - the basic idea is still there, just less detailed. Take for example this scene: https://superspl.at/scene/e721ea7c If you navigat…
- [chimpanzee2](https://news.ycombinator.com/item?id=48192335) : Just wow! As I scrolled through the website, I was even more impressed with this one though! https://superspl.at/scene/c67edb74

---

[Article original](https://superspl.at/scene/84df8849) · [Discussion HN](https://news.ycombinator.com/item?id=48191602)
