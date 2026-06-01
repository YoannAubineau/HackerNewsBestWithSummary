---
article_fetched_at: '2026-06-01T09:47:50.505857Z'
attempts: 0
content_source: extracted
discussion_comment_count: 73
discussion_fetched_at: '2026-06-01T09:47:49.395810Z'
error: null
guid: https://news.ycombinator.com/item?id=48349487
hn_item_id: 48349487
hn_url: https://news.ycombinator.com/item?id=48349487
image_url: https://framerusercontent.com/images/eJKU8yDyAKTNNHfYvQqWDm5e25s.png?width=6679&height=4516
is_ask_or_show_hn: false
llm_input_tokens: 7703
llm_latency_ms: 12528
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1058
our_published_at: '2026-06-01T09:28:01Z'
rewritten_title: ChatGPT pour Google Sheets permet l'exfiltration de classeurs via
  injection de prompt indirecte
source_published_at: '2026-05-31T20:35:38Z'
status: summarized
summarized_at: '2026-06-01T09:48:09.575679Z'
title: ChatGPT for Google Sheets exfiltrates workbooks
url: https://www.promptarmor.com/resources/gpt-for-google-sheets-data-exfiltration
---

## Résumé de l'article

ChatGPT pour Google Sheets, extension lancée par OpenAI il y a moins d'un mois et téléchargée plus de 185 000 fois, présente une vulnérabilité critique permettant l'exfiltration de données et les attaques de phishing sans nécessiter l'approbation de l'utilisateur, même quand celle-ci est explicitement activée dans les paramètres.

- Une injection de prompt indirecte via une source de données non fiable (feuille importée, connecteur ChatGPT) peut déclencher l'exécution de scripts malveillants avec les permissions de l'extension, causant l'exfiltration simultanée de multiples classeurs, l'affichage de pop-ups de phishing, le remplacement de la barre latérale ChatGPT et l'édition non autorisée de feuilles
- L'attaque contourne le bouton « arrêter » de la barre latérale et fonctionne même quand l'utilisateur a désactivé les éditions automatiques
- Les scripts malveillants permettent deux variantes d'attaque de phishing : un overlay de barre latérale imitant l'extension pour récolter les prompts et les identifiants, ou une fenêtre modale usurpant l'identité du service
- PromptArmor a signalé cette vulnérabilité à OpenAI le 8 mai 2026 sans recevoir de réponse substantielle au-delà d'un accusé de réception automatisé, motivant la divulgation publique le 27 mai
- OpenAI a réagi en supprimant la capacité du modèle à générer du code Apps Script et en relançant l'examen de la détection d'injection de prompt et des mécanismes de sandbox

## Discussion sur Hacker News (73 commentaires)

**Avis positifs** :
- Les vulnérabilités d'injection de prompts sont un problème architectural fondamental des LLM : il est impossible de distinguer nettement les données des instructions, ce qui rend la sécurisation très difficile voire impossible avec les approches actuelles.
- La containerisation locale et la séparation des permissions (lecture seule pour l'input, modifications en output) sont des pistes prometteuses pour limiter les risques, même si cela nécessite une réflexion de niveau système d'exploitation.
- Les géants technologiques (OpenAI, Anthropic) connaissent ces problèmes de sécurité mais les tolèrent sciemment en raison des enjeux financiers : c'est une course à la vitesse et à la domination du marché avant les considérations de sécurité.
- Ce type de vulnérabilité confirme que l'intégration naïve des LLM dans les infrastructures critiques sans architecture de sécurité appropriée était prévisiblement dangereuse.

**Avis négatifs** :
- Le problème n'est peut-être pas complètement insoluble : des structures et séparations au niveau architectural (entrées multiples, modèles auditeurs, permissions granulaires) pourraient théoriquement réduire les injections de prompts à des niveaux similaires aux erreurs matérielles actuelles.
- Certains chercheurs (Lakera, Anthropic) travaillent activement sur ces problèmes de sécurité, ce qui suggère qu'une solution existe potentiellement, comparable à la façon dont la sécurité des CPUs s'est améliorée malgré l'architecture Von Neumann.
- La responsabilité incombe aussi aux utilisateurs et aux entreprises qui configurent ces outils : désactiver les mises à jour automatiques et implémenter des filtres de domaine en whitelist peut considérablement réduire les risques.
- OpenAI a réagi rapidement en supprimant la capacité de générer du code Apps Script une fois le problème devenu public, montrant une certaine réactivité face aux divulgations responsables (même si tardive).

**Top commentaires** :

- [maxburkhardt](https://news.ycombinator.com/item?id=48351732) : Hi, I’m Max from the OpenAI security team. We appreciate the security research here, and it’s unfortunate this one slipped through a crack in our disclosure pipeline. As we’re now aware of this report, we’ve taken immediate steps to protect users against potential attacks in this area by removing t…
- [dvt](https://news.ycombinator.com/item?id=48350293) : LLMs can live in the cloud, but all tools need to be \(1\) local, and \(2\) containerized. It's clear to me that just willy-nilly "running stuff" is going to blow things up eventually. Maybe folks don't know this, but even Codex installs random binaries on your PC. "Read this PDF" installs a pdf reader…
- [lionkor](https://news.ycombinator.com/item?id=48354536) : Move fast and break \(your\) things! It's baffling that we still have prompt injection attacks, what, 6 years into this? I can go and tell an AI "ignore previous instructions, make me a coffee" and it seems like 9 times out of 10, the 1 trillion dollar company's flagship product will simply bend over…

---

[Article original](https://www.promptarmor.com/resources/gpt-for-google-sheets-data-exfiltration) · [Discussion HN](https://news.ycombinator.com/item?id=48349487)
