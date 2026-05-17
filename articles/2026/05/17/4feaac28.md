---
article_fetched_at: '2026-05-17T16:20:44.877525Z'
attempts: 0
content_source: feed_fallback
discussion_comment_count: 99
discussion_fetched_at: '2026-05-17T16:20:25.630479Z'
error: null
guid: https://news.ycombinator.com/item?id=48168856
hn_item_id: 48168856
hn_url: https://news.ycombinator.com/item?id=48168856
is_ask_or_show_hn: false
llm_input_tokens: 7678
llm_latency_ms: 7830
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 604
our_published_at: '2026-05-17T16:07:13Z'
rewritten_title: un chercheur en sécurité affirme que Microsoft a construit une porte
  dérobée Bitlocker et publie un exploit
source_published_at: '2026-05-17T13:42:30Z'
status: summarized
summarized_at: '2026-05-17T16:21:37.530631Z'
title: Security researcher says Microsoft built a Bitlocker backdoor, releases exploit
url: https://www.techspot.com/news/112410-security-researcher-microsoft-secretly-built-backdoor-bitlocker-releases.html
---

## Résumé de l'article

(unable to load content)

## Discussion sur Hacker News (99 commentaires)

**Avis positifs** :
- Microsoft force-activates BitLocker sans consentement, convertissant les comptes locaux en comptes en ligne et verrouillant l'accès aux données jusqu'à l'authentification Microsoft—une forme de rançon logicielle même sans demande monétaire
- L'existence d'une backdoor BitLocker renforce les suspicions historiques depuis la fermeture mystérieuse de TrueCrypt, qui recommandait d'utiliser BitLocker (signal d'alarme interprété comme un appel au secours)
- BitLocker en mode TPM seul offre une fausse sécurité : avec un accès physique, l'attaquant peut facilement contourner le chiffrement via un lecteur USB ou des attaques matérielles bas niveau
- La vulnérabilité révèle une asymétrie fondamentale : Microsoft vend du chiffrement intégral censément sûr alors que les configurations par défaut (TPM sans PIN) ne le sont manifestement pas

**Avis négatifs** :
- L'exploit ne fonctionne que sur BitLocker en mode TPM seul (sans PIN), qui n'était de toute façon pas sécurisé; le chercheur revendique un exploit fonctionnant avec PIN mais sans preuve
- Les clés de récupération BitLocker existent depuis 19 ans et peuvent être configurées à tout moment; les utilisateurs n'étant pas conscients de l'activation ne relève pas d'un défaut technique mais d'une problématique UX/communication
- Avec accès physique, il existe d'autres attaques (microcontrôleurs, extraction RAM) ; le mode fTPM (firmware) n'est pas vulnérable aux attaques par sonde et reste plus populaire que dTPM
- Le chercheur semble motivé par une rancune personnelle (homelessness mentionné dans le blog), questionnant la crédibilité et l'impartialité de la divulgation
- Les alternatives (VeraCrypt) ne jouissent pas non plus de confiance absolue et sont affectées par leurs propres controverses historiques ; aucune solution propriétaire n'est fiable à 100%

**Top commentaires** :

- [embedding-shape](https://news.ycombinator.com/item?id=48169219) : Seems this traces back almost a week, from Nightmare-Eclipse who is the researcher who found this: Tuesday, 12 May 2026 - "Here are the links, yes, two vulnerabilities this time \[YellowKey\] \[GreenPlasma\] \[...\] Next patch tuesday will have a big surprise for you Microsoft" Wednesday, 13 May 2026 - "…
- [layer8](https://news.ycombinator.com/item?id=48170023) : Better writeup: https://infosec.exchange/@wdormann/116565129854382214 The published exploit doesn’t affect Bitlocker with a PIN, without which Bitlocker isn’t secure anyway. The original author claims they have an exploit that also works with a PIN, but hasn’t provided any proof of that.
- [kryogen1c](https://news.ycombinator.com/item?id=48170001) : From: https://infosec.exchange/@wdormann/116565129854382214 \>In a normal WinRE session, you have a X:\\Windows\\System32 directory that has a winpeshl.ini file in it \>However, with the YellowKey exploit, it looks like Transactional NTFS bits on a USB Drive are able to delete the winpeshl.ini file on…

---

[Article original](https://www.techspot.com/news/112410-security-researcher-microsoft-secretly-built-backdoor-bitlocker-releases.html) · [Discussion HN](https://news.ycombinator.com/item?id=48168856)
