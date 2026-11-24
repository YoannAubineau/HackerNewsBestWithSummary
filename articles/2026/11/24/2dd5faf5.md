---
article_fetched_at: '2026-11-24T01:25:07.782782Z'
attempts: 0
content_source: extracted
discussion_comment_count: 162
discussion_fetched_at: '2026-11-24T01:24:57.766113Z'
error: null
guid: https://news.ycombinator.com/item?id=50610318
hn_item_id: 50610318
hn_url: https://news.ycombinator.com/item?id=50610318
image_url: https://opengraph.githubassets.com/1b133e3b4ef92d80f575caf804ca70800314982a6733b31d3fc71a3933766ae1/os6/nospeaker
is_ask_or_show_hn: false
llm_input_tokens: 11656
llm_latency_ms: 7975
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 801
our_published_at: '2026-11-24T01:09:42Z'
rewritten_title: Nospeaker utilise le moteur haptique du trackpad MacBook pour produire
  de la parole
source_published_at: '2026-11-23T11:31:54Z'
status: summarized
summarized_at: '2026-11-24T01:26:15.655454Z'
title: Nospeaker ─ Make your MacBook's trackpad talk using its haptic motor
url: https://github.com/os6/nospeaker
---

## Résumé de l'article

Nospeaker est un utilitaire open-source qui transforme le moteur haptique du trackpad des MacBook en haut-parleur miniature, capable de synthétiser et reproduire de la parole sans aucun haut-parleur physique. En pilotant le moteur jusqu'à 4 000 fois par seconde, l'outil fait vibrer la surface vitrée du trackpad pour générer des sons audibles.

- Le logiciel analyse la voix macOS (formants, pitch, loudness) et les reproduit en deux tonalités qui simulent une voix plutôt qu'un sifflement
- Il fonctionne via un seul commande shell et dure environ 90 secondes, fonctionnant uniquement sur les MacBook avec Force Touch (2015+) ou Magic Trackpad 2+ et macOS 12/13+
- Le son est plus audible à proximité immédiate du trackpad (sur les genoux) et couvre la plage 100 Hz à 4 kHz, avec une meilleure clarté autour de 1 kHz
- L'implémentation utilise le framework privé MultitouchSupport de macOS et respecte les limites de puissance du moteur pour éviter tout dommage
- Le code se réduit à un seul fichier Swift sans dépendances externes, publié sous licence MIT

## Discussion sur Hacker News (162 commentaires)

**Avis positifs** :
- Projet créatif et impressionnant de réutilisation de matériel existant, dans la lignée historique des détournements de composants (moteur de lecteur disquette, haut-parleur PC ancien, etc.)
- Le moteur haptique du MacBook est suffisamment robuste pour cette utilisation ; des précédents existent avec les moteurs similaires (Steam Controller, Joy-Con) sans dommages significatifs
- Démontre l'underutilisation des capacités haptiques d'Apple, qui pourraient servir à bien d'autres interactions (retours haptiques sur défilement, alignement, etc.)
- Crée une illusion sonore impressionnante : le moteur peut produire un son surprenamment audible et de qualité acceptable à 4000 cycles/seconde

**Avis négatifs** :
- Préoccupations légitimes sur l'usure prématurée du moteur haptique via une utilisation intensive non prévue, sans certitude sur la durabilité et les garanties Apple
- Manque de documentation : aucune vidéo dans le README original, nécessitant de chercher ailleurs pour vraiment comprendre le résultat sonore
- L'installation via script shell (`curl | sh`) pose des risques de sécurité, même si le code est consultable
- Certains utilisateurs rapportent que les trackpads Apple ne sont pas universellement appréciés (problèmes de détection de clic avec mains sèches, dragging imprécis selon les individus)

**Top commentaires** :

- [sirwhinesalot](https://news.ycombinator.com/item?id=50611507) : As impressive as this is, the fact that clicking that unmoving slab feels like pressing a button is far more impressive.
- [emptybits](https://news.ycombinator.com/item?id=50612625) : For those “into” this sort of thing, and of a certain vintage, you’ll know about using the motor in the Commodore 1541 floppy drive to similar effect. But I only just discovered this ... generating video and audio from just the floppy drive, no computer, since the drive has its own 6502-ish CPU. ht…
- [postalcoder](https://news.ycombinator.com/item?id=50611439) : This reminds me of the good ol days when computers had a tiny piezoelectric speaker to play rudimentary beeps. I remember keeling over laughing when a friend showed me you could actually play music through it \(terribly\). It was so absurd.

---

[Article original](https://github.com/os6/nospeaker) · [Discussion HN](https://news.ycombinator.com/item?id=50610318)
