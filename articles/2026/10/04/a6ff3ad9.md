---
article_fetched_at: '2026-10-04T23:44:19.472365Z'
attempts: 0
content_source: extracted
discussion_comment_count: 164
discussion_fetched_at: '2026-10-04T23:43:51.785571Z'
error: null
guid: https://news.ycombinator.com/item?id=49957116
hn_item_id: 49957116
hn_url: https://news.ycombinator.com/item?id=49957116
image_url: https://repository-images.githubusercontent.com/1394989252/13dcf083-d511-4f51-9681-c6ccbda3cae9
is_ask_or_show_hn: false
llm_input_tokens: 12664
llm_latency_ms: 11562
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 911
our_published_at: '2026-10-04T23:08:12Z'
rewritten_title: 'RemoveMacAI : désactiver Apple Intelligence sur macOS 27 et récupérer
  l''espace disque'
source_published_at: '2026-10-04T19:42:25Z'
status: summarized
summarized_at: '2026-10-04T23:45:10.283045Z'
title: Turn off Apple Intelligence on macOS 27 and get its disk space back
url: https://github.com/omlahore/RemoveMacAI
---

## Résumé de l'article

RemoveMacAI est un outil qui désactive les fonctionnalités Apple Intelligence sur macOS 27, supprime les modèles téléchargés et empêche le système de les retélécharger. Contrairement aux versions précédentes, macOS 27 n'offre plus un simple commutateur pour Apple Intelligence et conserve les modèles sur le disque même après désactivation des fonctionnalités.

- L'outil fonctionne via un script bash téléchargeable ou via Homebrew, installant un profil de configuration que l'utilisateur doit approuver dans les paramètres système
- Désactive Siri, les outils d'écriture, Genmoji, Image Playground, les résumés dans Mail/Messages/Safari, les prédictions de texte et autres fonctionnalités liées à Apple Intelligence
- Supprime les modèles fondamentaux d'Apple Intelligence et les modèles de génération d'images via le service d'assets d'Apple, sans modifier directement les fichiers système
- Bloque le retéléchargement en redirigeant les demandes de modèles vers un port local fermé, et persiste à travers les mises à jour de macOS
- Toutes les modifications peuvent être annulées avec la commande `revert` ; l'outil ne fait aucune requête réseau et ne collecte pas de données

## Discussion sur Hacker News (164 commentaires)

**Avis positifs** :
- L'approche open source du projet permet aux utilisateurs de vérifier le code et d'éviter les téléchargements malveillants, contrairement aux outils propriétaires.
- Apple Intelligence consomme 10-14 GB de stockage précieux sur des machines avec des configurations limitées (256-512 GB), ce qui justifie son désinstallation pour les utilisateurs n'en ayant pas besoin.
- Le problème reflète une tendance générale : macOS suit Windows dans l'ajout de fonctionnalités non désirées (bloatware) sans option facile de suppression, malgré l'héritage d'Apple de garder l'OS épuré.
- L'absence de contrôle utilisateur sur les modèles téléchargés automatiquement constitue un comportement anti-utilisateur, particulièrement problématique quand Apple revend des appareils avec stockage non-upgradable à prix élevé.

**Avis négatifs** :
- Le script d'installation via curl | bash pose des risques de sécurité importants : bien que le projet utilise des attestations de provenance, elles ne sont pas vérifiées lors du piping vers bash, et le script lui-même reste mutable.
- Apple Intelligence fonctionne réellement bien pour beaucoup d'utilisateurs et améliore l'expérience (notamment Spotlight/Siri), rendant son retrait injustifié pour ceux qui l'apprécient.
- Le débat oublie que toute installation de logiciel implique de la confiance (npm, pip, homebrew, DMG signés) : le problème ne se limite pas à curl | bash mais s'étend à l'écosystème entier.
- Apple Intelligence est une fonctionnalité optionnelle explicitement activable et non pas du véritable bloatware comme les anciennes version Windows avec essais logiciels du constructeur, rendant les comparaisons inéquitables.

**Top commentaires** :

- [ryandrake](https://news.ycombinator.com/item?id=49958088) : Reminds me of all the de-crufting you've always needed to do when you install Windows. Looks like we've gotten to the point on macOS too, where you need to run third party scripts on a new OS installation to gain back control of your system resources and remove unwanted crapware.
- [Grombobulous](https://news.ycombinator.com/item?id=49958375) : I no longer have a Mac as I’ve moved over to Linux, but my iOS device leaves me very frustrated that I can no longer disable this AI stuff with a simple toggle. It seems insane given that Apple’s competitors \(Microsoft, Firefox, probably others\) moved toward a global AI switch to make the choice ea…
- [hypfer](https://news.ycombinator.com/item?id=49957589) : This is stuff on the level of O&O ShutUp10. Which is a good tool, but also, a Windows tool for very \(back in the day\) Windows-specific nonsense. What's going on at Apple product strategy?

---

[Article original](https://github.com/omlahore/RemoveMacAI) · [Discussion HN](https://news.ycombinator.com/item?id=49957116)
