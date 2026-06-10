---
article_fetched_at: '2026-06-10T05:29:54.115216Z'
attempts: 0
content_source: extracted
discussion_comment_count: 145
discussion_fetched_at: '2026-06-10T05:29:53.324843Z'
error: null
guid: https://news.ycombinator.com/item?id=48469658
hn_item_id: 48469658
hn_url: https://news.ycombinator.com/item?id=48469658
image_url: https://repository-images.githubusercontent.com/993475914/123bf50d-9ae2-48d9-94f7-7a345bf82c15
is_ask_or_show_hn: false
llm_input_tokens: 10001
llm_latency_ms: 10730
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 895
our_published_at: '2026-06-10T05:11:33Z'
rewritten_title: 'macOS Container Machines : environnement Linux intégré avec montage
  de répertoires et services persistants'
source_published_at: '2026-06-10T00:29:01Z'
status: summarized
summarized_at: '2026-06-10T05:30:11.341087Z'
title: macOS Container Machines
url: https://github.com/apple/container/blob/main/docs/container-machine.md
---

## Résumé de l'article

Les container machines macOS fournissent un environnement Linux léger et persistant qui s'intègre à macOS, permettant d'éditer sur le Mac tout en compilant et exécutant des applications dans un Linux isolé. Basées sur des images OCI standard, elles partagent automatiquement le nom d'utilisateur et le répertoire home entre les deux systèmes.

- Montage bidirectionnel du répertoire home : les dépôts et fichiers dotfiles situés dans $HOME sur macOS sont accessibles à `/Users/<username>` dans la container machine, permettant d'utiliser les éditeurs macOS tout en compilant dans Linux
- Exécution de vrais services Linux : support de systemd permet de lancer des bases de données ou autres services système (par exemple `systemctl start postgresql`) pour tester l'application
- Gestion multi-distributions : créer plusieurs container machines pour différentes distributions cibles (alpine, ubuntu, debian) avec le même home et dotfiles
- Commandes essentielles : `container machine create`, `run`, `stop`, `rm` et l'alias court `m` pour manipuler les container machines ; possibilité de configurer les ressources (CPU, mémoire) et les permissions de montage
- Images personnalisées : toute image Linux OCI incluant `/sbin/init` fonctionne ; option de script de provisionnement personnalisé via `/etc/machine/create-user.sh` à la première démarrage

## Discussion sur Hacker News (145 commentaires)

**Avis positifs** :
- Réduit l'overhead des solutions actuelles (Docker Desktop, Colima) en utilisant des VMs plus légères et isolées nativement sur macOS, avec meilleure gestion mémoire
- Intégration transparente avec le système de fichiers et les répertoires utilisateur, facilitant le développement local sans friction
- Approche sensée pour Apple : exploiter les forces de son écosystème (Virtualization Framework) plutôt que de s'éparpiller sur des projets serveur intenables
- Supporte systemd et les services Linux standard, permettant des environnements de développement réalistes (PostgreSQL, etc.) sans complexité inutile
- Valeur ajoutée majeure pour les développeurs macOS qui doivent travailler avec des conteneurs Linux, segment de marché important et peu servi jusqu'à présent

**Avis négatifs** :
- Limité aux Macs Apple Silicon (ARM) ; aucun support pour Intel, avec un cycle de dépréciation agressif (Rosetta disparaîtra après macOS 27)
- Chaque conteneur = une VM complète, contrairement aux vrais conteneurs légers ; pas de partage de kernel ni d'isolation granulaire comparable à Linux namespaces
- Performances du système de fichiers insuffisantes pour les charges avec beaucoup de petits fichiers (Node, Rust dev) ; OrbStack et Colima offrent de meilleures optimisations
- Mémoire ballon réservée par défaut (moitié de la RAM hôte) sans libération possible actuellement ; toujours un compromise vs. solutions alternatives
- Représente l'abandon par Apple des ambitions de plateforme (serveurs, conteneurs Linux natifs) au profit d'une simple couche wrapper, symptôme du déclin technique de macOS face à Linux

**Top commentaires** :

- [katspaugh](https://news.ycombinator.com/item?id=48471794) : I've looked into replacing Lima with this for https://runmachine.dev. However, unlike Lima it's not a full VM, so you can SSH to it, or forward SSH-agent signatures into a machine. So it's more of a devcontainer story, which is also a great use case. Nice to see Apple creating tooling around their…
- [timsneath](https://news.ycombinator.com/item?id=48469985) : To clarify a few comments here: this is not only OCI containers: container machines add support for persistence and filesystem mounting, making container machines a great lightweight Linux environment for developers using macOS. More details here: https://developer.apple.com/videos/play/wwdc2026/389
- [golem14](https://news.ycombinator.com/item?id=48471700) : I belong to a rare breed of very opportunistic hobby-developers that like to use MacOS but also like to use linux machines or BSDs \(rpi etc\) sometimes. I can create docker-images with docker compose, or use something like colima, which this seems to be close to \(that should have some advantages ove…

---

[Article original](https://github.com/apple/container/blob/main/docs/container-machine.md) · [Discussion HN](https://news.ycombinator.com/item?id=48469658)
