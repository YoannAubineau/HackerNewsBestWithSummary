---
article_fetched_at: '2026-10-01T17:12:32.540307Z'
attempts: 0
content_source: extracted
discussion_comment_count: 82
discussion_fetched_at: '2026-10-01T17:12:17.655295Z'
error: null
guid: https://news.ycombinator.com/item?id=49920160
hn_item_id: 49920160
hn_url: https://news.ycombinator.com/item?id=49920160
is_ask_or_show_hn: false
llm_input_tokens: 7754
llm_latency_ms: 10901
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 858
our_published_at: '2026-10-01T16:29:51Z'
rewritten_title: StreetComplete sur iOS entre en phase bêta publique avec une stratégie
  Kotlin Multiplatform
source_published_at: '2026-10-01T10:59:57Z'
status: summarized
summarized_at: '2026-10-01T17:14:54.696859Z'
title: StreetComplete on iOS is now in public beta
url: https://github.com/streetcomplete/StreetComplete/issues/5421
---

## Résumé de l'article

StreetComplete est une application mobile open-source qui permet aux utilisateurs de contribuer à OpenStreetMap en répondant à des questions simples sur leur environnement. Une version iOS est actuellement en développement en phase bêta publique, utilisant Kotlin Multiplatform et Compose Multiplatform pour partager le code entre Android et iOS.

- Le portage iOS utilise Kotlin Multiplatform plutôt que Flutter, permettant de conserver une base de code unique et minimisant les maintenance futures
- La migration du code existant comprend trois étapes : séparer la logique applicative du code spécifique à Android, migrer l'interface Android vers Jetpack Compose, puis vers Compose Multiplatform
- Le développement est estimé à un an de travail au total ; environ 50% du projet était complété à la mi-2024
- Les contributeurs sont invités à prendre en charge des tâches du tableau de bord du projet, à se familiariser avec Compose Multiplatform, ou à soutenir financièrement le développement
- Un tableau Kanban détaillé et des diapositives de présentation de SotM Europe 2024 sont disponibles pour coordonner les efforts de contribution

## Discussion sur Hacker News (82 commentaires)

**Avis positifs** :
- StreetComplete abaisse drastiquement la barrière à l'entrée pour contribuer à OpenStreetMap, rendant l'édition de données accessibles sans connaissances techniques préalables
- L'approche basée sur des questions simples avec réponses à choix multiples et illustrations rend la contribution intuitive et efficace, même pour les novices
- Kotlin Multiplatform s'avère globalement fluide à utiliser avec peu de code spécifique à chaque plateforme, facilitant le partage de logique entre Android et iOS
- Plusieurs utilisateurs rapportent avoir contribué davantage à OSM en quelques minutes avec StreetComplete qu'en années précédentes, malgré quelques frictions UX
- Le financement public allemand et le soutien de NLnet témoignent de la valeur reconnue du projet pour l'infrastructure numérique open source

**Avis négatifs** :
- L'expérience utilisateur comporte des frictions : navigation confuse (gestes implicites sous iOS), pas de bouton visible pour annuler une question, obligation de force-close l'app dans certains cas
- Le système de quêtes peut manquer de nuance (ex. pas d'option pour un trottoir présent seulement d'un côté) et l'interface pour contourner ces limites reste peu intuitive
- Certains utilisateurs ont eu des expériences négatives avec des contributeurs OSM qui revertaient des edits StreetComplete pour des raisons pédantes ou arbitraires, gâchant l'expérience collaborative
- Les contributions disparaissent visuellement de la carte après soumission, sans feedback clair de progression, limitant le sentiment d'accomplissement
- La limite de 10 000 utilisateurs TestFlight risque d'être rapidement dépassée en cas de viralité sur HN, créant une frustration pour les utilisateurs intéressés

**Top commentaires** :

- [JBiserkov](https://news.ycombinator.com/item?id=49920261) : From the README: StreetComplete is an easy to use editor of OpenStreetMap data available for Android. It can be used without any OpenStreetMap-specific knowledge. It asks simple questions, with answers directly used to edit and improve OpenStreetMap data. The app is aimed at users who do not know a…
- [atollk](https://news.ycombinator.com/item?id=49924223) : I love the project idea, unfortunately I had bad experiences with the community. I had lots of fun walking my neighbourhood to perform quests in the app until like one or two other users started reverting my edits. I checked their comments and it was some weird pedantic arguments, like I shouldn't…
- [Fnoord](https://news.ycombinator.com/item?id=49921800) : Thank you, German government: \> Within the frame of Prototype Fund round 15 \(March 2024 to August 2024\), the German Federal Ministry of Education and Research sponsored Tobias Zwick to work on StreetComplete for iOS \(see progress report\) And NLnet.

---

[Article original](https://github.com/streetcomplete/StreetComplete/issues/5421) · [Discussion HN](https://news.ycombinator.com/item?id=49920160)
