---
article_fetched_at: '2026-05-02T20:10:57.775761Z'
attempts: 0
content_source: extracted
discussion_comment_count: 46
discussion_fetched_at: '2026-05-02T20:10:57.483099Z'
error: null
feed_summary: '<p>Article URL: <a href="https://nethack.org/v500/release.html">https://nethack.org/v500/release.html</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=47988776">https://news.ycombinator.com/item?id=47988776</a></p>

  <p>Points: 222</p>

  <p># Comments: 42</p>'
guid: https://news.ycombinator.com/item?id=47988776
hn_item_id: 47988776
hn_url: https://news.ycombinator.com/item?id=47988776
is_ask_or_show_hn: false
llm_input_tokens: 5515
llm_latency_ms: 11834
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 817
our_published_at: '2026-05-02T19:54:04Z'
rewritten_title: NetHack 5.0.0 annoncé pour mai 2026 avec améliorations architecturales
source_published_at: '2026-05-02T18:03:42Z'
status: summarized
summarized_at: '2026-05-02T20:11:15.831937Z'
title: NetHack 5.0.0
url: https://nethack.org/v500/release.html
---

## Résumé de l'article

NetHack 5.0.0 est une nouvelle version majeure du jeu d'exploration de donjons NetHack, un classique des jeux textuels descendant de Rogue. Cette version introduit des améliorations architecturales significatives et des corrections de bugs, tout en marquant un point de rupture avec les versions antérieures.

- Le code source est désormais conforme à la norme C99 et supporte le cross-compilation (compilation pour une plateforme différente de celle d'exécution)
- Les compilateurs basés sur yacc/lex et l'utilitaire makedefs ont été remplacés par des alternatives en Lua chargées lors du lancement du jeu
- Les sauvegardes et fichiers bones des versions précédentes ne sont pas compatibles avec 5.0.0
- La vérification d'intégrité des téléchargements peut se faire via certUtil sur Windows ou via la commande nethack --showpaths sur la plupart des plateformes
- Les utilisateurs sont encouragés à signaler les bugs via le formulaire officiel et à consulter la liste des bugs connus

## Discussion sur Hacker News (46 commentaires)

**Avis positifs** :
- Le remplacement de yacc/lex par Lua simplifie le build et rend le modding plus accessible ; c'est une modernisation logique malgré la fin d'une ère
- Les améliorations qualité de vie (tutoriel, confirmation pour actions dangereuses, filtrages de messages, code couleur santé) devraient augmenter la base de joueurs
- Les changements d'équilibre majeurs (Excalibur plus difficile, unicorn horn nerfé, résistances extrinsèques renforcées, quête faisable plus tôt) diversifient et compliquent le mid/late-game, rendant les runs plus intéressants
- Le jeu reste remarquablement deep avec des interactions émergentes fascinantes, méritant son statut de projet open source exceptionnellement durable après des décennies
- La persistance du développement actif (3100 corrections/changements) est impressionnante pour un jeu prédatant Lua de plusieurs années

**Avis négatifs** :
- Les save games existants ne sont pas compatibles avec 5.0.0, frustrant les joueurs avec des progressions anciennes
- Le jeu reste extrêmement difficile même avec les guides, décourageant les nouveaux joueurs malgré les QoL improvements
- Certains changements d'équilibre sont controversés et modifient le plaisir de jeu pour les vétérans habitués aux anciennes mécaniques
- L'absence de résumé clair des 3100 changements rend difficile la compréhension de ce qui a vraiment changé au-delà du rebranding 3.7→5.0
- La communauté hésite sur les bénéfices réels des mises à jour graphiques/3D comparé à l'ASCII puristique traditionnel

**Top commentaires** :

- [foresto](https://news.ycombinator.com/item?id=47989092) : Last time I played, after many close calls, I finally got my hands on the amulet. Knowing that the journey back to daylight was likely to be at least as dangerous as the way I had come, I took a breath, saved, and set the game aside. That was about seventeen years ago. I still have the save file. T…
- [saulpw](https://news.ycombinator.com/item?id=47988841) : « The build-time "yacc and lex"-based level compiler, the "yacc and lex"-based dungeon compiler, and the quest text file processing previously done by NetHack's "makedefs" utility, have been replaced with Lua text alternatives that are loaded and processed by the game during play. » This is very li…
- [haunter](https://news.ycombinator.com/item?id=47988864) : I can highly recommend the 3D client especially because it works almost everywhere, hope it will be updated for 5.0.0 soon https://github.com/JamesIV4/nethack-3d Web https://jamesiv4.github.io/nethack-3d/

---

[Article original](https://nethack.org/v500/release.html) · [Discussion HN](https://news.ycombinator.com/item?id=47988776)
