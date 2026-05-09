---
article_fetched_at: '2026-04-28T13:34:30.038841Z'
attempts: 0
content_source: extracted
discussion_comment_count: 98
discussion_fetched_at: '2026-04-28T13:34:29.813062Z'
error: null
feed_summary: '<p>Article URL: <a href="https://muffin.ink/blog/scratch-svg-sanitization/">https://muffin.ink/blog/scratch-svg-sanitization/</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=47922957">https://news.ycombinator.com/item?id=47922957</a></p>

  <p>Points: 242</p>

  <p># Comments: 97</p>'
guid: https://news.ycombinator.com/item?id=47922957
hn_item_id: 47922957
hn_url: https://news.ycombinator.com/item?id=47922957
is_ask_or_show_hn: false
llm_input_tokens: 13143
llm_latency_ms: 12694
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1112
our_published_at: '2026-04-28T12:44:48Z'
rewritten_title: Historique des failles de sécurité liées aux SVG chez Scratch et
  limites de l'approche d'assainissement
source_published_at: '2026-04-27T15:31:36Z'
status: summarized
summarized_at: '2026-04-28T13:34:48.960286Z'
title: The woes of sanitizing SVGs
url: https://muffin.ink/blog/scratch-svg-sanitization/
---

## Résumé de l'article

Scratch a connu une série continue de vulnérabilités liées aux SVG depuis 2019, malgré des tentatives répétées de sécuriser le traitement des contenus SVG générés par les utilisateurs. L'approche d'assainissement progressif du code s'est avérée inefficace et insoutenable, car chaque correction révèle de nouvelles failles.

- Entre 2019 et 2026, au moins 8 vulnérabilités majeures ont été découvertes : XSS via balises script, fuites HTTP via href et @import CSS, fuites via url() et image-set(), et redimensionnement de page complet via transitions CSS
- Les défauts d'assainissement persistent malgré des correctifs répétés : expressions d'échappement CSS, variables CSS, parseurs CSS imparfaits (css-tree), et futures spécifications CSS non encore implémentées (src(), image())
- L'approche actuelle de sanitization ajoute constamment de la complexité, rendant impossible le suivi de toutes les façons qu'ont les SVG de faire des requêtes externes ou d'exécuter du code
- TurboWarp a adopté une alternative : isoler les SVG dans une iframe sandbox avec Content-Security-Policy restrictive, confiant à la sécurité native du navigateur plutôt que de maintenir une liste exhaustive de patterns dangereux
- Cette approche par isolation empêche les SVG d'affecter la page principale et bénéficie automatiquement des futures améliorations de sécurité du navigateur, sans intervention manuelle

## Discussion sur Hacker News (98 commentaires)

**Avis positifs** :
- SVG est un langage de balisage, pas un simple format d'image, ce qui rend sa sécurisation fondamentalement différente d'autres formats graphiques et nécessite une vigilance comparable à celle de l'HTML
- La création d'un sous-ensemble SVG standardisé (comme SVG Tiny, SVG Native ou tinyVG) pourrait couvrir 90% des cas d'usage réels tout en éliminant les vecteurs d'attaque, avec des précédents comme SVG Tiny PS pour BIMI
- Les solutions de sandboxing existantes (CSP headers, iframe srcdoc, traitement des SVG dans des balises img) sont efficaces et sous-exploitées ; CSP reste le correctif le plus crédible pour les fuites HTTP
- L'ajout d'attributs de contrôle simples (comme exec="false" ou sandbox) au niveau du navigateur serait plus sûr et plus facile que de compter sur la sanitization côté développeur
- SVG ne devrait jamais avoir supporté les scripts et les animations complexes ; inclure ces fonctionnalités dans un format censé être une image a créé des décennies de problèmes de sécurité

**Avis négatifs** :
- Limiter SVG à un sous-ensemble statique éliminerait des fonctionnalités légitimes (animations SMIL/CSS, gradients, texte enveloppé, polices embarquées) que les concepteurs utilisent régulièrement et qui sont triviales dans les éditeurs vectoriels
- Les solutions de containment existantes (img tags, iframe) ne permettent pas les manipulations dynamiques du DOM depuis le parent ou l'accès aux variables CSS, ce qui limite les cas d'usage interactifs légitimes
- Toute nouvelle norme ou format (tinyVG, SVG Tiny) risque de ne jamais gagner une adoption suffisante car les outils existants continueront de générer le SVG complet, forçant les développeurs à convertir/transpiler manuellement
- La sanitization par regex ou blacklist échouera inévitablement à mesure que les spécifications CSS et les navigateurs évoluent, comme le montre l'historique de Scratch avec ses multiples contournements réussis
- Distinguer et contrôler comment un même SVG se comporte selon sa méthode d'intégration (img, object, inline) crée une surface d'attaque confuse où les développeurs testent avec img puis déploient en inline sans se rendre compte du changement de permissions

**Top commentaires** :

- [simonw](https://news.ycombinator.com/item?id=47923915) : I'm glad this article includes the only credible fix for the HTTP leak problems: CSP. A useful thing I learned recently is that, while CSP headers are usually set using HTTP headers, you can also reliably set them directly in HTML - for example for HTML generated directly on a page where HTTP heade…
- [andybak](https://news.ycombinator.com/item?id=47923270) : My first thought is "support a tiny subset of svg that probably still covers 90% of real-world use cases". I do feel that's there's two distinct types of svg - "bunch of paths with fills" and "clever dangerous stuff" where most real SVGs are of the former type. Fully expect this to be shot down by…
- [nmilo](https://news.ycombinator.com/item?id=47928331) : I'm sorry because I love the scratch project but this has to be said: they found XSS in SVGs in a surface with attacker-controlled access to Node and their fix was sanitizing it using regex??? And this was discovered by a user on scratch? Even worse, OP's latest post "Every version of Scratch is vu…

---

[Article original](https://muffin.ink/blog/scratch-svg-sanitization/) · [Discussion HN](https://news.ycombinator.com/item?id=47922957)
