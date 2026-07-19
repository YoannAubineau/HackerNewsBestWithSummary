---
article_fetched_at: '2026-07-19T05:14:28.932348Z'
attempts: 0
content_source: extracted
discussion_comment_count: 139
discussion_fetched_at: '2026-07-19T05:14:28.295655Z'
error: null
guid: https://news.ycombinator.com/item?id=48959392
hn_item_id: 48959392
hn_url: https://news.ycombinator.com/item?id=48959392
is_ask_or_show_hn: false
llm_input_tokens: 15492
llm_latency_ms: 11702
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1032
our_published_at: '2026-07-19T04:19:15Z'
rewritten_title: Configuration pas à pas d'un Mac de secours pour contrôler Claude
  Code à distance
source_published_at: '2026-07-18T16:12:08Z'
status: summarized
summarized_at: '2026-07-19T05:15:02.345472Z'
title: Setting up your spare Mac for Claude Code to control, a step-by-step guide
url: https://ykdojo.github.io/claude-controls-mac/
---

## Résumé de l'article

Claude Code est un outil d'IA capable d'exécuter du code et de contrôler un ordinateur. Ce guide explique comment configurer un Mac de secours dédié que Claude Code peut contrôler entièrement, en le rendant accessible depuis votre téléphone via l'app Claude ou depuis votre Mac principal via SSH, tout en éliminant les risques de sécurité liés à l'exécution sur votre machine personnelle.

- Préparer le Mac cible en l'effaçant, en activant SSH, en configurant l'accès sans mot de passe pour sudo, et en désactivant la mise en veille
- Établir la connexion SSH entre le Mac principal et le Mac cible via clés SSH, en utilisant le nom d'hôte local (recommandé) ou l'adresse IP
- Installer Claude Code sur le Mac cible et configurer les permissions (GitHub CLI optionnel, authentification Anthropic)
- Activer la fonctionnalité de contrôle informatique via un script (setup-computer-use.sh) qui maintient un serveur tmux persistent dans la session GUI pour contourner les limitations de macOS
- Utiliser l'outil `ic.sh` sur le Mac principal pour spawner et gérer des sessions Claude Code sur le Mac cible, avec options pour le contrôle à distance depuis le téléphone, le partage d'écran (VNC), et l'extension Claude pour Chrome permettant le contrôle du navigateur
- Optionnellement, configurer Tailscale pour étendre l'accès au-delà du réseau local avec chiffrement pair-à-pair

## Discussion sur Hacker News (139 commentaires)

**Avis positifs** :
- Permet de contourner les limitations des solutions conteneurisées (Dispatch, Cowork) qui rencontrent des problèmes de permissions pour télécharger des fichiers, gérer Git ou exécuter certaines commandes système
- Offre des cas d'usage réels et valides : monitoring d'alertes en production, triage automatique de bugs, analyses de données longue durée, automatisation de tâches récurrentes, travail sur des projets parallèles sans surveillance
- Permet d'utiliser les capacités complètes de Claude Code avec accès au système de fichiers local et aux applications natives (iMessage, HomeKit, navigateur avec GUI) sans contraintes de sandbox
- Recyclage utile des anciens Mac qui s'accumulent, avec un rapport coût/performance acceptable pour l'isolation et l'experimentation

**Avis négatifs** :
- Absence de véritables cas d'usage convaincants : beaucoup d'utilisateurs admettent ne pas avoir trouvé d'application pratique justifiant cette complexité de mise en place
- Risques de sécurité majeurs : donner à Claude un accès root ou privilégié sur une machine est dangereux et pourrait permettre des fuites réseau ; les agents hallucinant régulièrement, le laisser tourner sans supervision crée des problèmes (code dupliqué, requêtes DB inefficaces, bugs à corriger)
- Problèmes de qualité du code généré : les agents produisent du code défaillant qui nécessite une supervision constante ; les laisser travailler 24/7 sans contrôle humain revient à accepter des dégâts qu'il faut ensuite réparer
- Modèle économique complexe et coûteux : les tarifs Anthropic sont confus, avec des risques de dépassements onéreux ; les limites d'usage horaires frustrantes même avec les plans premium, poussant à des configurations élaborées pour peu de bénéfice réel
- Phénomène de hype technologique creux : soupçons que beaucoup de ces configurations servent surtout à créer du contenu pour se justifier à posteriori plutôt que de résoudre des problèmes concrets

**Top commentaires** :

- [esaym](https://news.ycombinator.com/item?id=48960606) : Outside of the article's mentioned graphics development, there is no reason to isolate an agent using actual hardware. I threw together this script\[0\] using libvirt to give claude its own graphical desktop env to be able to do user acceptance testing with Chrome. It has full root and can do what ev…
- [catoc](https://news.ycombinator.com/item?id=48960252) : I just cannot come up with a good AI-is-actually-24/7-helping-me-out use case. Please help: I wánt to need this!
- [arxari](https://news.ycombinator.com/item?id=48960412) : « setting up your spare Mac » as one has

---

[Article original](https://ykdojo.github.io/claude-controls-mac/) · [Discussion HN](https://news.ycombinator.com/item?id=48959392)
