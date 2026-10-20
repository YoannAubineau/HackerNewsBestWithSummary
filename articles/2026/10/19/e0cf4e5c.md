---
article_fetched_at: '2026-10-20T01:23:36.758772Z'
attempts: 0
content_source: extracted
discussion_comment_count: 17
discussion_fetched_at: '2026-10-20T01:23:33.109807Z'
error: null
guid: https://news.ycombinator.com/item?id=50140001
hn_item_id: 50140001
hn_url: https://news.ycombinator.com/item?id=50140001
image_url: https://opengraph.githubassets.com/6f8417659f46499de963a62a0f213ffcbc5b7b342d58d9cc0f8625774f402e9b/0x23/MicroManipulatorStepper
is_ask_or_show_hn: false
llm_input_tokens: 5028
llm_latency_ms: 12885
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 958
our_published_at: '2026-10-19T00:04:22Z'
rewritten_title: Open MicroManipulator, plateforme de contrôle 3D sub-micromètre open
  source
source_published_at: '2026-10-18T11:16:22Z'
status: summarized
summarized_at: '2026-10-20T01:23:58.026774Z'
title: Open MicroManipulator – A sub-micrometer 3D motion control plattform
url: https://github.com/0x23/MicroManipulatorStepper
---

## Résumé de l'article

Open MicroManipulator est une plateforme motorisée open source et peu coûteuse pour le contrôle de précision XYZ en 3D, capable d'atteindre une résolution de 50 nanomètres grâce à une approche de « démultiplication magnétique » appliquée à des capteurs rotatifs bon marché. Conçue pour l'alignement optique, le test de composants électroniques et la microscopie, elle utilise des moteurs pas à pas standards, une structure cinématique parallèle et des rotules miniatures pour assurer rigidité et grande plage de mouvement.

- La plateforme se commande via des commandes G-Code simples sur interface USB série et dispose d'un firmware complet avec planification de trajectoire et interpolation 6DOF, permettant une intégration facile dans d'autres projets
- Les fichiers CAO sont conçus en FreeCAD (logiciel libre), les composants sont usinables sur fraiseuse CNC 3 axes ou imprimables en 3D, et aucune soudure CMS n'est requise pour assembler le PCB
- Une interface graphique Python avec contrôle à la souris, affichage vidéo en direct et exécution de G-Code facilite l'utilisation et le test du dispositif
- La version matérielle v4.0 corrige plusieurs problèmes de conception antérieurs (collision lors de l'initialisation, rigidité des articulations, constance de la longueur des barres de liaison, friction excessive)
- Le firmware v1.0.4 ajoute le support des outils (gravure laser), améliore l'étalonnage et l'initialisation, et introduit plusieurs nouvelles commandes G-Code pour homing parallèle et gestion des moteurs

## Discussion sur Hacker News (17 commentaires)

**Avis positifs** :
- Le projet impressionne par sa qualité d'ingénierie en DIY et sa documentation vidéo très complète, montrant qu'un amateur peut créer un manipulateur sub-micromètre sans promotion commerciale
- Le contrôle en boucle fermée extrêmement précis fonctionne bien et démontre que le design est fonctionnel pour des applications pratiques comme la microscopie
- L'approche open-source inspire d'autres projets similaires (RepRapMicron, hexapodes) et offre une base accessible pour expérimenter en micromécanique
- Les roulements préchargés avec élastiques imprimés en 3D et le concept global du design sont élégants et réplicables par des bricoleurs avec des outils basiques

**Avis négatifs** :
- Pour des applications réelles en métrologie précise, il reste des lacunes importantes : gestion thermique insuffisante, absence de capteurs de position haute résolution, et dérive thermique des pièces plastiques
- À une certaine précision, les capteurs de position deviennent le vrai coût limitant, ce qui explique pourquoi les systèmes industriels établis (pi-usa stages) restent compétitifs malgré leur prix élevé
- Le projet manque d'absolue précision (seulement une précision relative), nécessite une compensation par le logiciel et ne remplace pas complètement les solutions industrielles pour les vraies tâches critiques
- D'autres approches existantes (deltabot pour pick-and-place, actionneurs piézoélectriques stick-slip) offrent potentiellement plus de plage de mouvement ou une meilleure résolution, selon les besoins

**Top commentaires** :

- [option\_greek](https://news.ycombinator.com/item?id=50140419) : This guy is a legend. His whole series on building this along with other videos is worth watching on YouTube. It amazes me how some random guy simply drops a sub um manipulator diy on YouTube and disappears into the ether. No promotions nothing.
- [namibj](https://news.ycombinator.com/item?id=50149334) : Does anyone have a link to a 6DOF version of what this does? Like, the design principle would easily function for a hexapod \(swap the dual-rod linkages for single-rod and manage to pre-load the result; add 3 more motors, change how the actuators are arranged relative to the platform they manipulate…
- [alted](https://news.ycombinator.com/item?id=50143791) : It's also possible to DIY piezoelectric stick-slip actuators with potentially sub-nanometer\(!\) resolution, albeit at greater expense \(~$1k\) \[1\]. \[1\] "Low-cost, open-source XYZ nanopositioner for high-precision analytical applications", https://doi.org/10.1016/j.ohx.2022.e00317

---

[Article original](https://github.com/0x23/MicroManipulatorStepper) · [Discussion HN](https://news.ycombinator.com/item?id=50140001)
