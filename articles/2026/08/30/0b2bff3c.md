---
article_fetched_at: '2026-08-30T18:17:36.601003Z'
attempts: 0
content_source: extracted
discussion_comment_count: 177
discussion_fetched_at: '2026-08-30T18:17:25.381131Z'
error: null
guid: https://news.ycombinator.com/item?id=49499854
hn_item_id: 49499854
hn_url: https://news.ycombinator.com/item?id=49499854
is_ask_or_show_hn: false
llm_input_tokens: 14922
llm_latency_ms: 11411
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 933
our_published_at: '2026-08-30T17:53:23Z'
rewritten_title: Omarchy versions antérieures à 4.0.1 permettaient l'escalade de privilèges
  root via Docker
source_published_at: '2026-08-30T15:59:49Z'
status: summarized
summarized_at: '2026-08-30T18:18:00.918604Z'
title: 'Omarchy: Any User Process Can Escalate to Root'
url: https://0xcc.io/posts/omarchy-root-creds/
---

## Résumé de l'article

Omarchy, une distribution Linux destinée aux développeurs, contenait une faille de sécurité dans sa configuration Docker par défaut : l'utilisateur standard était membre du groupe docker, ce qui permettait à tout processus de la session utilisateur d'obtenir l'accès root sans mot de passe ni sudo.

- L'utilisateur par défaut d'Omarchy était configuré comme membre du groupe Linux docker, permettant d'exécuter des commandes docker sans sudo
- Les membres du groupe docker peuvent accéder au socket Docker (/var/run/docker.sock), ce qui permet de lancer des conteneurs en tant que root et monter des portions du système de fichiers hôte
- Tout processus de la session utilisateur hérité du groupe docker, y compris les navigateurs web, éditeurs, agents IA et outils de développement, pouvait escalader vers root
- Cette configuration était opt-out (appliquée par défaut) plutôt qu'opt-in, sans mention claire des implications de sécurité
- Les versions antérieures à 4.0.1 sont affectées ; la faille a été corrigée le 24 août 2026 suite à un signalement responsable en juin 2025

## Discussion sur Hacker News (177 commentaires)

**Avis positifs** :
- La vulnérabilité du groupe Docker est une découverte légitime et utile qui mérite d'être documentée, montrant l'importance du pentest sérieux face au bruit médiatique en sécurité
- Omarchy répond à un besoin réel : offrir une expérience Mac-like sur Linux avec une configuration Hyprland prête à l'emploi, plus rapide et cohérente qu'Arch brut pour les développeurs cherchant la commodité
- Le problème identifié (ajout de l'utilisateur au groupe Docker par défaut) est courant sur de nombreuses distributions et guides officiels, ce qui souligne un enjeu systémique au-delà d'Omarchy
- L'équipe a corrigé rapidement le problème une fois signalé, démontrant une réactivité face aux défauts de sécurité
- Rootless Podman existe depuis longtemps comme solution alternative viable et devrait être la norme plutôt que l'exception

**Avis négatifs** :
- Configurer Docker avec un accès root pour l'utilisateur par défaut, sans avertissement explicite, viole les principes de sécurité par défaut et constitue une opt-out dangereuse plutôt qu'une opt-in
- La distro semble être principalement développée par AI sans revue humaine adéquate, comme en témoignent les commits détectant plusieurs problèmes de sécurité même pour des modèles d'IA basiques
- Le projet souffre d'une philosophie contradictoire : vendre une image de supériorité technique tout en sacrifiant la sécurité pour la commodité, reproduisant les erreurs passées du VPS era
- Au-delà du problème Docker, une vulnérabilité avec les descripteurs USB USB montrant un code vibecoded non révisé suggère d'autres lacunes systémiques et un processus de qualité insuffisant
- Même si la sécurité du groupe Docker est commune, la rendre transparente par défaut sans consentement informé différencie une distro responsable d'une qui délègue les choix de sécurité à l'utilisateur sans lui demander

**Top commentaires** :

- [concinds](https://news.ycombinator.com/item?id=49500466) : A few days ago someone found they were flowing USB descriptors straight into the shell. https://github.com/omacom/omarchy/commit/9285b19d6a72eba3df8... Don't use vibecoded distros. It doesn't matter whether they fix this or that, or whether you care about a particular vuln. This is not sensible. It…
- [trentnix](https://news.ycombinator.com/item?id=49501263) : The Docker configuration issue was reported and changes were made quickly to address it. Sounds like this is a great example of the system working well. Omarchy looks like a simple way for a developer like me to test drive hyprland and write code. It also looks like a great way for my kids to get i…
- [addajones](https://news.ycombinator.com/item?id=49501257) : There were many amazing distros before Omarchy and there will be many after. Use whatever you want, vibecoded or not. Don't tell people what to do. Make your own decisions.

---

[Article original](https://0xcc.io/posts/omarchy-root-creds/) · [Discussion HN](https://news.ycombinator.com/item?id=49499854)
