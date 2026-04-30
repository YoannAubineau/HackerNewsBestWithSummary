---
article_fetched_at: '2026-04-30T23:18:19.664680Z'
attempts: 0
content_source: extracted
discussion_comment_count: 97
discussion_fetched_at: '2026-04-30T23:18:19.004595Z'
error: null
feed_summary: '<p>Article URL: <a href="https://semgrep.dev/blog/2026/malicious-dependency-in-pytorch-lightning-used-for-ai-training/">https://semgrep.dev/blog/2026/malicious-dependency-in-pytorch-lightning-used-for-ai-training/</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=47964617">https://news.ycombinator.com/item?id=47964617</a></p>

  <p>Points: 294</p>

  <p># Comments: 92</p>'
guid: https://news.ycombinator.com/item?id=47964617
hn_item_id: 47964617
hn_url: https://news.ycombinator.com/item?id=47964617
image_url: https://semgrep.dev/assets/blog/semgrep-blog-pytorch-lightning-advisory.png
is_ask_or_show_hn: false
llm_input_tokens: 10531
llm_latency_ms: 10503
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 921
our_published_at: '2026-04-30T22:48:23Z'
rewritten_title: Attaque de compromission de la bibliothèque PyTorch Lightning avec
  vol de credentials et propagation cross-plateforme
source_published_at: '2026-04-30T16:09:26Z'
status: summarized
summarized_at: '2026-04-30T23:19:09.803816Z'
title: Shai-Hulud Themed Malware Found in the PyTorch Lightning AI Training Library
url: https://semgrep.dev/blog/2026/malicious-dependency-in-pytorch-lightning-used-for-ai-training/
---

## Résumé de l'article

PyTorch Lightning, une bibliothèque d'apprentissage profond populaire, a été compromise dans une attaque de la chaîne d'approvisionnement affectant les versions 2.6.2 et 2.6.3 publiées le 30 avril 2026. Le malware vole les credentials, tokens d'authentification, variables d'environnement et secrets cloud via plusieurs canaux de transmission (C2 HTTPS, API GitHub, dépôts publics, et branches de victimes), puis propage le code malveillant à d'autres packages npm.

- Les versions compromises (lightning 2.6.2 et 2.6.3) contiennent un répertoire _runtime caché avec un payload JavaScript obfusqué qui s'exécute automatiquement à l'importation du module
- Le malware cible les credentials locaux, les variables d'environnement, les pipelines CI/CD, et les services cloud majeurs (AWS, Azure, GCP), exfiltrant les données via quatre canaux parallèles pour contourner les blocages
- Une fois les tokens npm volés, le malware injecte son code dans tous les packages qu'il peut publier, créant une propagation par ver à travers l'écosystème npm
- Le malware établit la persistance en injectant des hooks dans Claude Code (.claude/settings.json) et VS Code (.vscode/tasks.json) qui réactivent le payload à chaque ouverture du projet
- L'attaque crée des dépôts publics GitHub avec des descriptions reconnaissables ("A Mini Shai-Hulud has Appeared") et utilise des commit messages avec le préfixe "EveryBoiWeBuildIsAWormyBoi" comme canaux de transmission de tokens codés en double base64

## Discussion sur Hacker News (97 commentaires)

**Avis positifs** :
- La compromission des identifiants PyPI des mainteneurs explique comment des versions malveillantes (2.6.2 et 2.6.3) ont pu être publiées directement, sans passage par le repository GitHub
- L'épinglage des dépendances (pinning) et les outils comme uv avec cooldowns sur les installations récentes offrent une protection efficace contre ces attaques
- Les attaques de chaîne d'approvisionnement se multiplient et gagnent en valeur avec la montée du cryptocurrency et des extorsions, confirmant l'urgence du problème
- L'écosystème Python ML est particulièrement vulnérable : maintainers non-informaticiens, nombreuses dépendances, pratiques de sécurité ad-hoc et utilisation de pickles exécutables sans restrictions

**Avis négatifs** :
- GitHub aurait pu bloquer automatiquement les repos créés avec des noms Dune et des README suspects via regex, mais n'a pas appris de précédentes attaques similaires
- La détection est restée compliquée avant la publication : la détection avant release nécessite des outils commerciaux sophistiqués peu accessibles aux petits projets
- PyPI n'impose pas l'authentification à deux facteurs pour la publication, seulement pour la connexion, ce qui a permis la compromise des credentials
- Les développeurs modernes, notamment ceux utilisant les LLM (Claude Code) pour suggérer des dépendances, installent du code sans vérification manuelle, créant un filtre de sécurité inefficace

**Top commentaires** :

- [wlkr](https://news.ycombinator.com/item?id=47966396) : This might just be the frequency illusion at play, but there seem to have been a number of high-profile supply chain attacks of late in major packages. There are several articles on the first few pages of HN right now with different cases. Looking back ten years to \`left-pad\`, are there more succes…
- [jackdoe](https://news.ycombinator.com/item?id=47966126) : I cant wait to have no dependencies. An extreme example is now when I make interactive educational apps for my daughter, I just make Opus use plain js and html; from double pendulums to fluid simulations, works one shot. Before I had hundreds of dependencies. Luckily with MIT licensed code I can ju…
- [mkeeter](https://news.ycombinator.com/item?id=47965646) : A repository search shows 2.2K repos with the text "A Mini Shai-Hulud has Appeared", all created within the past day: https://github.com/search?q=A%20Mini%20Shai-Hulud%20has%20Ap...

---

[Article original](https://semgrep.dev/blog/2026/malicious-dependency-in-pytorch-lightning-used-for-ai-training/) · [Discussion HN](https://news.ycombinator.com/item?id=47964617)
