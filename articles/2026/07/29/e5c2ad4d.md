---
article_fetched_at: '2026-07-29T08:23:20.854333Z'
attempts: 0
content_source: extracted
discussion_comment_count: 73
discussion_fetched_at: '2026-07-29T08:23:20.051011Z'
error: null
guid: https://news.ycombinator.com/item?id=49090607
hn_item_id: 49090607
hn_url: https://news.ycombinator.com/item?id=49090607
image_url: https://opengraph.githubassets.com/f3b7913171093bf2087335c06dc1ff09efbf6db4a5d077c3e1e2e0b0c1460337/twalichiewicz/HNewhere
is_ask_or_show_hn: false
llm_input_tokens: 6123
llm_latency_ms: 7261
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 648
our_published_at: '2026-07-29T08:18:04Z'
rewritten_title: HNewhere, un userscript qui affiche les discussions Hacker News dans
  une barre latérale
source_published_at: '2026-07-28T22:09:06Z'
status: summarized
summarized_at: '2026-07-29T08:23:35.148384Z'
title: 'Show HN: I was tired of opening 2 tabs for every HN link, so I made a userscript'
url: https://github.com/twalichiewicz/HNewhere
---

## Résumé de l'article

HNewhere est un userscript léger qui détecte automatiquement les articles partagés sur Hacker News et charge leurs discussions dans une barre latérale, sans quitter la page en cours de lecture.

- Ajoute une barre latérale affichant les commentaires Hacker News à côté de l'article consulté
- Détecte automatiquement les discussions correspondantes sur HN et suit les liens provenant de la plateforme
- Barre latérale redimensionnable et rétractable, avec largeur préservée entre les visites
- Requiert un gestionnaire de userscript (Tampermonkey, Violentmonkey, ou Userscripts pour Safari)
- Les liens de réponse ouvrent directement sur Hacker News; publié sous licence MIT

## Discussion sur Hacker News (73 commentaires)

**Avis positifs** :
- Beaucoup d'utilisateurs reconnaissent le problème : ouvrir systématiquement deux onglets pour lire l'article et les commentaires HN est une friction quotidienne légitime
- La transparence du userscript (code source visible et inspectable) est un avantage par rapport aux extensions, facilitant la confiance et la modification rapide
- L'idée de fusionner les sections de commentaires pour les soumissions dupliquées pourrait enrichir significativement la valeur de l'outil
- Le script remplit un besoin réel même pour les articles découverts en dehors de HN : trouver les discussions HN existantes sur n'importe quel contenu

**Avis négatifs** :
- Les navigateurs modernes (Chrome, Firefox) disposent déjà de fonctionnalités natives de split view ou d'ouverture dans des onglets divisés, rendant le besoin moins aigu
- La transmission de chaque URL à l'API Algolia de HN pose des questions de vie privée ; les utilisateurs partagent systématiquement leurs activités de navigation avec un tiers
- Un format extension natif serait plus accessible que de demander aux utilisateurs d'installer Tampermonkey ou ViolentMonkey au préalable
- Le script complexifie plutôt que de résoudre le problème : l'approche traditionnelle (clic droit + ouvrir dans nouvel onglet) reste plus simple pour beaucoup

**Top commentaires** :

- [jstrieb](https://news.ycombinator.com/item?id=49094342) : If you use Firefox \(and will pardon me plugging my own project\), you might be interested in a version of this I made a while ago as a browser extension: https://github.com/jstrieb/hackernews-button My project is somewhat different from the userscript in that mine uses Bloom filters to check whether…
- [kccqzy](https://news.ycombinator.com/item?id=49092742) : Feature 2 is really useful. When I land on a technical article I know chances are there will be a nice HN discussion, that may sometimes even refute the main point of the article. Feature 1 is IMO less useful. It just suggests that people are bad at window management. We didn't like overlapping win…
- [perpil](https://news.ycombinator.com/item?id=49091059) : This is slick. 2 things. 1. If you name your script with the extension .user.js it is easier to click on to automatically install at least with tampermonkey. 2. When I went to this link from the main page, on mobile I had to scroll to the right to see the \(-\) to minimize because the sidebar was too…

---

[Article original](https://github.com/twalichiewicz/HNewhere) · [Discussion HN](https://news.ycombinator.com/item?id=49090607)
