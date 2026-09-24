---
article_fetched_at: '2026-09-24T15:36:46.071419Z'
attempts: 0
content_source: extracted
discussion_comment_count: 176
discussion_fetched_at: '2026-09-24T15:36:34.267187Z'
error: null
guid: https://news.ycombinator.com/item?id=49822555
hn_item_id: 49822555
hn_url: https://news.ycombinator.com/item?id=49822555
image_url: https://fly.io/static/images/fly-social-square.webp
is_ask_or_show_hn: false
llm_input_tokens: 15804
llm_latency_ms: 12208
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1017
our_published_at: '2026-09-24T15:04:03Z'
rewritten_title: VSCode intègre un agent SSH complet avec accès système via WebSocket
source_published_at: '2026-09-23T21:01:48Z'
status: summarized
summarized_at: '2026-09-24T15:37:19.177908Z'
title: VSCode's SSH Agent Is Bananas (2025)
url: https://fly.io/blog/vscode-ssh-wtf/
---

## Résumé de l'article

VSCode dispose d'une fonctionnalité de remote editing sur SSH qui fonctionne de manière radicalement différente de son équivalent Emacs (Tramp). Au lieu d'utiliser les commandes shell disponibles sur la connexion distante, VSCode déploie un agent complet incluant Node.js binaire et établit une connexion WebSocket portualisée offrant des capacités étendues.

- VSCode télécharge et exécute un agent binaire complet sur le serveur distant, contrairement à Tramp qui exploite les ressources existantes
- L'agent établit une connexion WebSocket chiffrée au client VSCode et peut parcourir le système de fichiers, modifier des fichiers arbitraires, créer des processus PTY et se persister
- Cette architecture pose des risques de sécurité significatifs si utilisée sur des serveurs de développement ou de production, en particulier lors d'incidents
- L'intérêt pour VSCode vient du potentiel à intégrer des agents LLM en boucle fermée sur des environnements isolés, pour réduire les hallucinations du code généré
- Cette approche diffère philosophiquement de celle d'Emacs/Tramp, qui privilégie la légèreté et l'utilisation des outils existants sur le système distant

## Discussion sur Hacker News (176 commentaires)

**Avis positifs** :
- VSCode Remote SSH améliore significativement l'expérience utilisateur en matière de développement distant avec faible latence, notamment comparé à TRAMP ou VNC/RDP, en gardant les buffers éditeur locaux tout en utilisant les ressources distantes pour les compilations et serveurs de langage
- L'architecture est appropriée pour les équipes de développement qui veulent un environnement de dev cohérent et centralisé, avec gestion d'accès simplifiée et facilité de portabilité entre machines (Linux/macOS)
- La restriction SSH peut être configurée arbitrairement pour adapter les garde-fous de sécurité selon les besoins spécifiques, et l'installation du binaire VSCode server sur la machine distante est une solution naturelle lorsque la machine distante n'a pas accès à Internet
- Comparé à certaines alternatives comme JetBrains Remote Development (qui ouvre une nouvelle connexion SSH chaque seconde), VSCode Remote SSH offre une meilleure gestion des sessions persistantes

**Avis négatifs** :
- La bidirectionnalité du protocole WebSocket permet à la machine distante compromise d'exécuter du code arbitraire sur le client local, transformant le concept de sandbox en illusion dangereuse, surtout en situation d'incident de sécurité en production
- L'installation automatique de Node.js et de centaines de megaoctets de dépendances npm sur des serveurs distants élargit significativement la surface d'attaque sans vraie nécessité, particulièrement sur des machines critiques où le contrôle strict des logiciels installés est requis
- Le dossier ~/.vscode-server peut croître jusqu'à plusieurs gigaoctets en accumulant plusieurs versions du runtime Node et node_modules, avec peu de mécanisme de nettoyage automatique, ce qui pose problème sur des systèmes aux ressources limitées
- L'opacité du binaire propriétaire Microsoft (non open-source) rend difficile l'audit de sécurité et la compréhension complète de ce qui s'exécute réellement sur les machines distantes, contrastant avec TRAMP qui n'utilise que du shell standard
- L'extension manque de support pour des fonctionnalités essentielles d'administration système (MotD, reuse de sessions SSH, réconnexion fiable), crée des centaines de sessions orphelines au fil du temps et ne transmet pas les messages critiques aux utilisateurs contrairement à SSH classique

**Top commentaires** :

- [danielklnstein](https://news.ycombinator.com/item?id=49823036) : Missing a \(2025\) FYI VSCode's SSH Agent is a godsend for remote development - the "disadvantages" that Fly lists are part of its advantages. I've worked in several teams that have made extensive use of the extension, and it's never been an issue. You can restrict SSH access arbitrarily to ensure wh…
- [qwertox](https://news.ycombinator.com/item?id=49827465) : 2026-09-24 09:35:24 dev ~ du -h -d 0 .vscode-server 6.0G .vscode-server This is what makes it bananas for me. I don't know what Microsoft is thinking if they allow this.
- [10000truths](https://news.ycombinator.com/item?id=49823327) : So a program that is specifically designed to edit files and run arbitrary commands on a remote machine... can do so. Not sure where the bananas part comes in. Sending a binary over SSH/SFTP might sound weird at first glance, but VSCode can't assume that your remote machine can access the wider int…

---

[Article original](https://fly.io/blog/vscode-ssh-wtf/) · [Discussion HN](https://news.ycombinator.com/item?id=49822555)
