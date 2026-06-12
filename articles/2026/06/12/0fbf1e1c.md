---
article_fetched_at: '2026-06-12T22:30:49.090073Z'
attempts: 0
content_source: tweet
discussion_comment_count: 158
discussion_fetched_at: '2026-06-12T22:30:47.780930Z'
error: null
guid: https://news.ycombinator.com/item?id=48495928
hn_item_id: 48495928
hn_url: https://news.ycombinator.com/item?id=48495928
image_url: https://pbs.twimg.com/media/HKclElRWMAATMuP.jpg?name=orig
is_ask_or_show_hn: false
llm_input_tokens: 13218
llm_latency_ms: 7333
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 540
our_published_at: '2026-06-12T21:48:39Z'
rewritten_title: Les développeurs de malware ont ajouté du texte sur les armes nucléaires
  et biologiques à leurs logiciels espions
source_published_at: '2026-06-11T20:24:18Z'
status: summarized
summarized_at: '2026-06-12T22:31:04.086529Z'
title: Malware developers added nuclear and biological weapons text to to their spyware
url: https://twitter.com/jsrailton/status/2064661778978533571
---

## Résumé de l'article

Tweet de @jsrailton :

> NEW: malware developers added nuclear & biological weapons text to to their spyware.
>
> Goal? To trigger LLM safety refusals... so that their spyware wouldn't be analyzed by an AI security scanner.
>
> Cleanest practical example I can think of for why over-indexing on first order safety alignment is risky.
>
> When closed (and open) models ship with aggressive refusals, they will be sprinkled with second-order blindspots that attackers will discover...and exploit.
>
> We are only in the earliest days of attackers leveraging these features, and it wouldn't surprise me if users systems that need to handle complex cybersecurity issues demand that models be less safety-blunted.
>
> In the weeds: @SocketSecurity's post also shows why intention matters in how you design a malware analysis pipeline to avoid prompt manipulation.
>
> H/T to colleagues that shared this with me https://socket.dev/blog/mini-shai-hulud-miasma-and-hades-worms-target-bioinformatics-and-mcp-developers-via-malicious

## Discussion sur Hacker News (158 commentaires)

**Avis positifs** :
- Les garde-fous contre les armes WMD dans les LLM sont justifiés comme mesures de conformité légale et de responsabilité des entreprises, comparables aux restrictions imposées dans les licences logicielles standard
- Même sans garantie d'efficacité totale, les garde-fous augmentent le coût/la friction pour les acteurs mal intentionnés et réduisent le bruit pour les agences de sécurité en diminuant les faux positifs
- Les barrières matérielles (enrichissement d'uranium, infrastructures de centrifugation) restent l'obstacle principal et les LLM ne changent pas fondamentalement cette réalité pour les États
- L'ajout de texte sur les armes WMD dans le malware pour tromper les analyseurs basés sur LLM est une tactique révélatrice montrant que les défenseurs doivent prendre la désobfuscation par IA plus au sérieux

**Avis négatifs** :
- Les garde-fous sont largement performatifs : l'information sur les armes nucléaires/biologiques est déjà publiquement disponible sur Internet et l'IA n'a pas d'informations secrètes que seuls les États possèdent
- Cette censure risque de concentrer le pouvoir des LLMs entre les mains de grandes organisations, créant une forme de gatekeeping comparable à l'Église catholique contrôlant la Bible
- La connaissance théorique ne suffit pas ; les obstacles réels (ressources massives, surveillance satellitaire, chaînes d'approvisionnement contrôlées) font que même les États-voyous échouent ou peinent
- Les garde-fous sont contournables et fragmentaires : les malwares peuvent simplement finetune des modèles locaux, et les restrictions inconsistentes (ex: instructions pour cuire une dinde vs. chimie) manquent de cohérence logique

**Top commentaires** :

- [elashri](https://news.ycombinator.com/item?id=48506927) : I still don't know why all these concern about nuclear weapons with LLMs. It is not that if an entity \(A country\) wants to develop a nuclear weapons that the resources they need for such a program and huge infrastructure and scientific enterprise would need an LLM to teach them anything. Knowing ho…
- [JadoJodo](https://news.ycombinator.com/item?id=48509288) : Even in the early 2000s, in the aftermath of 9/11, I can remember people in school passing around copies of The Anarchist’s Cookbook. Perhaps I’ve been naïve, but I’ve always assumed that should one actually want to look up instructions for nearly any sort of horrible thing one could imagine, it co…
- [gastonmorixe](https://news.ycombinator.com/item?id=48508697) : You can’t even ask about what’s in HN right now. It will switch to 4.8.

---

[Article original](https://twitter.com/jsrailton/status/2064661778978533571) · [Discussion HN](https://news.ycombinator.com/item?id=48495928)
