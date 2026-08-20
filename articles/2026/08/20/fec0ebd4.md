---
article_fetched_at: '2026-08-20T19:24:22.839283Z'
attempts: 0
content_source: extracted
discussion_comment_count: 79
discussion_fetched_at: '2026-08-20T19:24:20.697559Z'
error: null
guid: https://news.ycombinator.com/item?id=49373456
hn_item_id: 49373456
hn_url: https://news.ycombinator.com/item?id=49373456
image_url: https://simedw.com/2026/08/20/midi-autocomplete/images/rolltab_phone.jpg
is_ask_or_show_hn: false
llm_input_tokens: 9435
llm_latency_ms: 13413
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 971
our_published_at: '2026-08-20T19:16:43Z'
rewritten_title: Un modèle de 125 millions de paramètres entraîné pour l'autocomplétion
  de piano en temps réel sur appareil
source_published_at: '2026-08-20T12:04:38Z'
status: summarized
summarized_at: '2026-08-20T19:25:39.474034Z'
title: 'Show HN: I trained a 125M model to autocomplete piano on-device'
url: https://simedw.com/2026/08/20/midi-autocomplete/
---

## Résumé de l'article

RollTab est une application iOS qui utilise un transformer de 125M paramètres pour autocomplèter les performances pianistiques en temps réel (~108 notes/sec sur iPhone 15). Le modèle a été entraîné sur plusieurs centaines de milliers de fichiers MIDI classiques nettoyés, en utilisant une représentation discrète originale de la musique et optimisé via Direct Preference Optimization (DPO).

- La représentation tokenisée clé : chaque note est générée en une seule étape du transformer avec ses attributs (pitch, délai d'apparition, durée, vélocité), évitant le problème de dérive des modèles utilisant NOTE_ON/NOTE_OFF séparés
- Le nettoyage agressif des données s'est avéré plus important que l'augmentation du volume : un dataset 5× plus grand a produit des modèles moins bons à cause du bruit
- DPO a apporté l'amélioration majeure après le préentraînement, passant à plus de 69% de continuations préférées en comparaison par paire, en utilisant Gemini 3.5 Flash pour l'évaluation plutôt que des scores absolus
- L'augmentation incluait transposition globale, mise à l'échelle du tempo et bruit de vélocité/durée pour adapter le modèle aux imprécisions du jeu en direct
- Le modèle a été exporté en Core ML avec quantification INT8 et gère les sessions longues en conservant les 384 notes récentes quand le contexte approche la limite de 512 notes

## Discussion sur Hacker News (79 commentaires)

**Avis positifs** :
- L'idée d'autocomplète musical en temps réel sur appareil est innovante et inspirante, comparée à des approches historiques comme le Continuator de Pachet (2003) ou Songsmith de Microsoft (2009).
- Le changement de représentation des notes (événements composés) a fourni une amélioration majeure (5×) de performance, montrant que le choix de la représentation importe plus que l'optimisation du modèle lui-même.
- Le projet illustre comment l'IA peut explorer des possibilités musicales rapidement, permettant aux musiciens de trouver des impasses ou des découvertes intéressantes plus efficacement, sans remplacer l'apprentissage musical.
- C'est un cas d'usage convaincant du MIDI et démontre que le format reste pertinent pour la production musicale professionnelle moderne.

**Avis négatifs** :
- Le modèle génère du contenu au niveau GPT-2 avec des déficits majeurs en rythme et composition, manquant de forme musicale globale et de planification à long terme nécessaires pour une vraie qualité musicale.
- Générer une accompagnement complet à partir d'une simple mélodie est extrêmement difficile et dépend de choix très subjectifs; la génération aléatoire n'égale pas la créativité intentionnelle artistique.
- Les résultats sont comparables ou pires qu'un modèle de Markov simple, révélant une lacune fondamentale entre les LLM et la compréhension musicale; une décomposition en couches harmoniques/mélodiques plus élevées serait nécessaire.
- Le projet soulève des inquiétudes : il risque de décourager l'apprentissage véritable de l'harmonie, de la technique piano et de l'improvisation, remplaçant le travail créatif par une simple pression de touches.

**Top commentaires** :

- [joshuamerrill](https://news.ycombinator.com/item?id=49378199) : Classical pianist and software product designer here. I see so much in common with this project and the numerous AI-based UX design tools out there. Whether it's music or UI, now that the "generation" portion of the work costs zero, all that remains is taste. And so much of taste comes from explori…
- [tom\_vidal](https://news.ycombinator.com/item?id=49375955) : This sort of “autocomplete” is actually fundamental to how classical composers were trained. For anyone interested, I’d highly recommend reading Robert Gjerdingen’s article Gebrauchs-Formulas. https://www.researchgate.net/publication/259731561\_Gebrauchs... You can also listen to the transcript of f…
- [axoltl](https://news.ycombinator.com/item?id=49378917) : Looks neat! I'd love for it to feed the MIDI notes back into my player piano instead of playing out of my iPhone's \(comparatively tinny\) speakers though.

---

[Article original](https://simedw.com/2026/08/20/midi-autocomplete/) · [Discussion HN](https://news.ycombinator.com/item?id=49373456)
