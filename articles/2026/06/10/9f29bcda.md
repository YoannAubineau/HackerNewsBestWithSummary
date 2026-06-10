---
article_fetched_at: '2026-06-10T22:35:23.075395Z'
attempts: 0
content_source: extracted
discussion_comment_count: 202
discussion_fetched_at: '2026-06-10T22:35:22.470005Z'
error: null
guid: https://news.ycombinator.com/item?id=48479452
hn_item_id: 48479452
hn_url: https://news.ycombinator.com/item?id=48479452
is_ask_or_show_hn: false
llm_input_tokens: 15805
llm_latency_ms: 10535
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 832
our_published_at: '2026-06-10T21:45:58Z'
rewritten_title: Claude Desktop crée une machine virtuelle Hyper-V de 1,8 Go à chaque
  lancement même en mode chat
source_published_at: '2026-06-10T17:11:56Z'
status: summarized
summarized_at: '2026-06-10T22:35:40.126336Z'
title: Claude Desktop spawns 1.8 GB Hyper-V VM on every launch, even for chat-only
  use
url: https://github.com/anthropics/claude-code/issues/29045
---

## Résumé de l'article

Claude Desktop est une application Windows cliente d'Anthropic pour accéder à Claude. Un utilisateur signale que l'application lance automatiquement une machine virtuelle Hyper-V consommant 1,8 Go de RAM à chaque démarrage, même lorsque seule la fonctionnalité chat est utilisée et que les modes Cowork ou agent ne sont pas activés.

- La VM (identifiée comme Vmmem dans le Gestionnaire des tâches) se crée à chaque lancement via le service Hyper-V Host Compute, consommant 11 % de la RAM totale sur un système de 16 Go
- L'application accumule 2 689 fichiers de session stale dans le répertoire local-agent-mode-sessions sans jamais les nettoyer automatiquement
- Le journal Hyper-V affiche des erreurs JSON répétées ("The virtual machine or container JSON document is invalid") déclenchées à chaque démarrage
- La VM persiste même après suppression des fichiers de session et redémarrage de l'application, sauf si VirtualMachinePlatform est complètement désactivé
- L'utilisateur demande que l'infrastructure de VM ne s'initialise qu'à la demande (lors du démarrage d'une session Cowork), que les fichiers stale soient nettoyés automatiquement, et que le chat fonctionne sans VM

## Discussion sur Hacker News (202 commentaires)

**Avis positifs** :
- La VM est justifiée pour Cowork, qui nécessite un environnement sandboxé pour exécuter du code de manière sécurisée sans risquer la machine hôte.
- Le sandboxing au niveau VM offre une approche d'avenir pour les applications auto-modifiables et les agents IA, isolant complètement les risques.
- Certains utilisateurs trouvent Claude Desktop utile en environnement corporate pour les serveurs MCP préconfigurés et l'intégration SSO avec les services d'entreprise.

**Avis négatifs** :
- La VM de 10-13 GB se lance automatiquement au démarrage même pour les simples conversations, sans option de désactivation ou de démarrage à la demande.
- L'ingénierie chez Anthropic semble précipitée et peu soignée (« vibecoded »), avec une application écrite en React de 500k lignes et des interfaces brisées à plusieurs niveaux.
- L'absence de contrôle utilisateur sur une ressource substantielle (espace disque, RAM) est contraire à l'éthique de personnalisation, particulièrement problématique sur les machines avec faible stockage (<256 GB).
- Les utilisateurs ignorent souvent que la VM se lance à leur insu, créant une expérience confuse et sans transparence sur ce qui se passe réellement sur leur machine.
- Le CLI et les applications desktop d'Anthropic présentent des bugs criants et une qualité très inférieure à ce qu'on attendrait d'une entreprise avec accès à leurs meilleurs modèles.

**Top commentaires** :

- [z2](https://news.ycombinator.com/item?id=48480386) : This all feels like a race where the model companies try to solve doing work locally in a way that doesn't suck, before the major operating systems companies figure out AI integration into their OS that doesn't suck. It also makes me wonder why Google which has both Gemini and Android can't figure…
- [nathanyz](https://news.ycombinator.com/item?id=48480336) : The VM itself is for Claude Cowork which does all work within the VM sandbox. That doesn't help answer why they spin it up immediately and don't have a way to disable it though. Just the "why it exists" question.
- [literatepeople](https://news.ycombinator.com/item?id=48480786) : I didn’t get a screenshot of this, but I just found a really pointed example of Anthropics lack of craft / rush to build. If you open Claude on Windows, and click Dispatch \(under cowork\) to start that up, it will tell you that you need permissions windows doesn’t have. When you click the buttons fo…

---

[Article original](https://github.com/anthropics/claude-code/issues/29045) · [Discussion HN](https://news.ycombinator.com/item?id=48479452)
