---
article_fetched_at: '2026-11-05T22:33:12.564628Z'
attempts: 0
content_source: extracted
discussion_comment_count: 300
discussion_fetched_at: '2026-11-05T22:33:07.684943Z'
error: null
guid: https://news.ycombinator.com/item?id=50378625
hn_item_id: 50378625
hn_url: https://news.ycombinator.com/item?id=50378625
image_url: https://platform.theverge.com/wp-content/uploads/sites/2/2025/03/acastro_STK062_01.jpg?quality=90&strip=all&crop=0%2C10.732984293194%2C100%2C78.534031413613&w=1200
is_ask_or_show_hn: false
llm_input_tokens: 20500
llm_latency_ms: 8222
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 852
our_published_at: '2026-11-05T22:16:04Z'
rewritten_title: Discord abandonne Electron pour une nouvelle application en Rust
  consommant moins de RAM
source_published_at: '2026-11-05T13:05:28Z'
status: summarized
summarized_at: '2026-11-05T22:34:14.387310Z'
title: Discord is ditching Electron and its new app uses less RAM
url: https://www.theverge.com/news/1027379/discord-ditching-electron-web-app
---

## Résumé de l'article

Discord, plateforme de communication en ligne, abandonne le framework Electron pour réécrire entièrement son application de bureau en Rust, un langage de programmation orienté vers la performance et la sécurité mémoire. Cette migration devrait réduire considérablement la consommation de ressources système.

- Discord utilise Rust depuis 2018 pour son infrastructure et sa technologie vocale ; l'objectif est désormais de porter entièrement le client sur ce langage
- Le nouvel app Windows utilise seulement 290 MB de RAM, contre 1 GB ou plus avec l'application actuelle basée sur Electron
- Electron et React Native seront supprimés ; les applications mobiles conserveront une interface native mais partageront le code applicatif avec le bureau via Rust
- Le calendrier exact du déploiement complet n'est pas annoncé, mais Discord envisage des tests utilisateur dans un avenir proche

## Discussion sur Hacker News (300 commentaires)

**Avis positifs** :
- La migration vers le Rust/GPUI devrait significativement réduire la consommation RAM et améliorer les performances, une tendance positive pour l'écosystème logiciel face à la crise des ressources système.
- Les outils d'IA rendent maintenant possible ce qui aurait été prohibitif avant : réécrire des applications entières vers des langages natifs performants devient viable économiquement et techniquement.
- C'est un signe que les développeurs reconnaissent enfin le coût réel d'Electron et des abstractions superflues ; abandonner les navigateurs embarqués au profit de code natif optimisé est une bonne ingénierie.
- Cette tendance pourrait inspirer d'autres grandes applications (Slack, Teams, VSCode) à quitter Electron, créant un effet domino bénéfique pour la performance globale du bureau.
- Discord démontre que même les équipes sans expertise Rust peuvent migrer rapidement via l'IA ; cela ouvre la voie à des réécritures natives chez d'autres entreprises.

**Avis négatifs** :
- Le code généré par IA crée un risque de perte de connaissance architecturale : personne ne comprendra vraiment comment fonctionne l'application, la rendant fragile et difficile à maintenir long terme.
- GPUI est un choix problématique : fragmenté en multiples forks, manquant d'accessibilité native, et sans support à long terme ; cela pourrait bloquer les utilisateurs en situation de handicap.
- Réécrire en Rust/GPUI réintroduit des complexités oubliées (gestion RTL, IME, accessibilité, a11y) que les navigateurs géraient gratuitement ; on risque de recréer un navigateur moins bon avec plus de bugs.
- 290 MB reste élevé pour une application de chat ; la réduction n'est pas aussi révolutionnaire que présentée, et le temps de compilation Rust ralentit l'itération de développement.
- La migration rend le modding beaucoup plus difficile voire impossible, détruisant un écosystème de personnalisation que les utilisateurs appréciaient avec Electron.

**Top commentaires** :

- [throwaway2037](https://news.ycombinator.com/item?id=50384929) : From the website https://gpui.rs/, I see this description: \> GPU-accelerated UI framework for Rust Can someone explain to me why a text editor needs to be GPU-accelerated? Literally, you are only blitting a few icons and painting text. What am I missing? To be clear, I am not here to doubt that the…
- [the\_\_alchemist](https://news.ycombinator.com/item?id=50379999) : I had trouble reading more than the opening volley of the article due to popups. Am a Discord user, and rust application programmer: What GUI framework are they using? EGUI? GPUI? Something custom? GPUI from comments? I meant to try GPUI, but backed off after an announcement pending its maintenance…
- [kayson](https://news.ycombinator.com/item?id=50379724) : I'm very interested in \(and a total novice in\) cross platform GUI application development. Hadn't heard of GPUI, though I had heard of Tauri. I looked at the GPUI front page and saw this mess of almost-CSS method chaining... Surely there's a better way? This seems horrible to me. \> div\(\) .flex\(\) .f…

---

[Article original](https://www.theverge.com/news/1027379/discord-ditching-electron-web-app) · [Discussion HN](https://news.ycombinator.com/item?id=50378625)
