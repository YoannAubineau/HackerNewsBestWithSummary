---
article_fetched_at: '2026-08-03T15:38:37.276908Z'
attempts: 0
content_source: extracted
discussion_comment_count: 153
discussion_fetched_at: '2026-08-03T15:38:35.081239Z'
error: null
guid: https://news.ycombinator.com/item?id=49154332
hn_item_id: 49154332
hn_url: https://news.ycombinator.com/item?id=49154332
is_ask_or_show_hn: false
llm_input_tokens: 14896
llm_latency_ms: 11986
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1038
our_published_at: '2026-08-03T15:00:00Z'
rewritten_title: Des chercheurs découvrent que des CVE SQLite critiques sont générées
  par IA et ne contiennent aucune vulnérabilité réelle
source_published_at: '2026-08-03T11:28:54Z'
status: summarized
summarized_at: '2026-08-03T15:38:57.752250Z'
title: Critical CVE issued for hallucinated SQLite vulnerability
url: https://research.jfrog.com/post/sqlite-critical-cves-or-llm-slops/
---

## Résumé de l'article

JFrog Security a enquêté sur une série de CVE SQLite présentées comme critiques et découvert qu'elles sont entièrement fabriquées par des outils IA (« LLM slop »). En examinant le code source réel de SQLite, en compilant les versions officielles et en testant les preuves de concept, les chercheurs ont confirmé que les vulnérabilités n'existent pas : les fonctions citées n'existaient pas dans les versions mentionnées, les numéros de ligne dépassaient la fin des fichiers, et aucune des failles ne figurait sur la page officielle des CVE de SQLite.

- 54 des 55 CVE publiés par le même compte GitHub sont entièrement fictifs, l'un contenant un vrai bug mais avec des métadonnées CVE non vérifiées
- Les tests avec AddressSanitizer sur des versions officielles compilées en environnement isolé n'ont provoqué aucun crash ni fuite mémoire
- La détection d'IA (GPTZero) confirme que tous les avis semblent générés automatiquement
- Le système de publication CVE (MITRE/NVD) n'exige pas de vérification d'identité ni de preuve de concept, permettant aux fausses soumissions de traverser le pipeline jusqu'aux bases de données publiques et aux scanners d'entreprise
- Ces CVE fictives peuvent détourner les équipes de sécurité vers des corrections inutiles et polluer les priorités d'automatisation basée sur l'IA

## Discussion sur Hacker News (153 commentaires)

**Avis positifs** :
- Les CVE générés par IA illégitimes exposent un problème systémique grave : les organisations soumises à des politiques strictes de correction doivent désormais gérer des vulnérabilités fictives, ce qui paralyse les processus de sécurité réels
- Les LLM modernes trouvent effectivement de vraies vulnérabilités dans du code établi depuis longtemps, ce qui accélère la découverte et pourrait améliorer la sécurité globale malgré le bruit actuel
- Cette crise devrait forcer une refonte du système CVE/CVSS qui était déjà cassé avant les IA, avec trop de faux positifs et des scores de sévérité peu fiables
- Le manque de vérification humaine et de validation par les CNAs (Numbering Authorities) avant attribution de CVE est indefensable et doit être corrigé
- Plusieurs projets majeurs (Curl, Linux kernel) deviennent CNA pour reprendre le contrôle et éviter que des tiers attribuent des CVE non vérifiés

**Avis négatifs** :
- Le système CVE était déjà dysfonctionnel avant les IA avec une majorité de vulnérabilités non exploitables ; le blâmer entièrement sur les LLM minimise des problèmes structurels préexistants
- L'article lui-même semble généré par IA selon les détecteurs ; débunker du slop avec du slop fragilise la crédibilité de l'analyse
- Les faux positifs IA renforcent paradoxalement les incitations des attaquants à exploiter les vraies vulnérabilités plutôt que de les signaler, puisque crédibilité du système s'effondre
- Il n'existe aucune solution facile : automatiser la vérification des CVE avec des IA crée une boucle infinie où l'IA ment sur la reproduction des bugs
- Le coût réel sera énorme : maintainers submergés, organisations bloquées par des outils de scan (Snyk, Veracode), et les vrais bugs correctifs continueront à être ignorés dans le chaos

**Top commentaires** :

- [gortok](https://news.ycombinator.com/item?id=49155075) : We can chalk this up as another example of over-exhuberance by what folks believe LLMs can accomplish vs. what they actually are. LLM-based “AI” is able to use its vast corpus of inputs and calculate the most statistically likely output in a given situation. It is probabilistic, and when you are de…
- [ChrisMarshallNY](https://news.ycombinator.com/item?id=49154534) : The problem with this kind of thing, is that it reduces the S/N \(Signal-to-Noise\) ratio, so weeding out the legit CVEs becomes a lot more difficult. But, on the other hand, I do know that LLMs have been discovering a lot of legit CVEs, and I will lay odds that the blackhats are leveraging them to t…
- [Ekaros](https://news.ycombinator.com/item?id=49154645) : Not validating submissions seems like avenue for massive attack. Flood the whole system with endless false reports. Thus making it significantly less reliable.

---

[Article original](https://research.jfrog.com/post/sqlite-critical-cves-or-llm-slops/) · [Discussion HN](https://news.ycombinator.com/item?id=49154332)
