---
article_fetched_at: '2026-05-18T13:11:14.164642Z'
attempts: 0
content_source: extracted
discussion_comment_count: 239
discussion_fetched_at: '2026-05-18T13:10:27.219721Z'
error: null
guid: https://news.ycombinator.com/item?id=48168856
hn_item_id: 48168856
hn_url: https://news.ycombinator.com/item?id=48168856
image_url: https://www.techspot.com/images2/news/bigimage/2026/05/2026-05-14-image-17.jpg
is_ask_or_show_hn: false
llm_input_tokens: 19708
llm_latency_ms: 13911
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1098
our_published_at: '2026-05-17T16:07:13Z'
rewritten_title: Un chercheur en sécurité affirme que Microsoft a intégré une porte
  dérobée à BitLocker et publie un exploit
source_published_at: '2026-05-17T13:42:30Z'
status: summarized
summarized_at: '2026-06-08T07:33:55.325621Z'
title: Security researcher says Microsoft built a Bitlocker backdoor, releases exploit
url: https://www.techspot.com/news/112410-security-researcher-microsoft-secretly-built-backdoor-bitlocker-releases.html
---

## Résumé de l'article

Un chercheur en sécurité connu sous le pseudonyme « Nightmare-Eclipse » a publié YellowKey, une vulnérabilité qui contournerait complètement le chiffrement intégral du volume de BitLocker (système de chiffrement de disque de Microsoft). Le chercheur soupçonne Microsoft d'avoir intentionnellement intégré une porte dérobée dans ce système de protection des données.

- La vulnérabilité YellowKey se déclenche en copiant un dossier « FsTx » sur une clé USB ou la partition EFI de Windows, puis en redémarrant la machine et en accédant à l'environnement de récupération Windows
- Une fois exploitée, la vulnérabilité accorde un accès sans restriction aux volumes protégés par BitLocker, sans nécessiter de mot de passe
- Le chercheur juge suspecte la présence du composant problématique exclusivement dans l'image WinRE officielle, suggérant qu'il s'agit d'une porte dérobée intentionnelle
- Seules les versions Windows 11 (et Server 2022/2025) seraient affectées, Windows 10 restant épargné
- Des chercheurs tiers ont confirmé le comportement décrit, et un second exploit nommé GreenPlasma permettrait une escalade de privilèges

## Discussion sur Hacker News (239 commentaires)

**Avis positifs** :
- Microsoft utilise des dark patterns pour forcer les comptes en ligne et activé BitLocker sans consentement explicite, transformant le chiffrement en rançon de facto qui empêche l'accès à l'ordinateur
- La vulnérabilité révèle un problème architectural réel : BitLocker en mode TPM seul n'offre aucune protection contre l'accès physique et ne justifie pas la fausse confiance qu'il inspire aux utilisateurs et aux organisations réglementées
- Si la vulnérabilité TPM+PIN est réelle comme affirmé, ce serait une différence suspecte avec Windows 11 que seule une malveillance organisée pourrait expliquer, notamment l'utilisation d'une version différente de fsTx.dll en WinRE
- Cette faille a des implications légales graves pour les organisations qui s'appuient sur BitLocker pour justifier de ne pas déclarer les appareils perdus/volés comme des violations de données (RGPD, HIPAA, etc.)
- Le shutdown mystérieux de TrueCrypt suivi de recommandations vers BitLocker ressemble à une coordination avec des agences gouvernementales pour compromettendre les alternatives ouvertes

**Avis négatifs** :
- L'exploit publié ne fonctionne qu'en mode TPM seul sans authentification préboot, ce qui n'est pas la configuration sécurisée recommandée ; BitLocker avec TPM+PIN reste sécurisé et aucune preuve n'existe pour l'exploit PIN claims
- Cet exploit est une faille du recovery environment (WinRE) et du secure boot, pas spécifiquement BitLocker ; Linux avec LUKS en TPM seul a la même architecture vulnérable par conception
- Toute implémentation d'accès physique sera compromised si on peut modifier le bootloader (EFI partition) ; ce n'est pas une backdoor mais une limitation inhérente au modèle de confiance
- Le chercheur n'a fourni aucune preuve pour ses affirmations d'exploit TPM+PIN et ses posts blog suggèrent une instabilité personnelle ; l'interprétation comme 'backdoor intentionnel' vs 'bug ordinaire' reste spéculative
- Microsoft comme tous les éditeurs fait des compromis entre sécurité et utilisabilité (récupération de compte, prix bas) ; WinRE décrypte automatiquement par design pour permettre la récupération, ce qui n'est pas une malveillance

**Top commentaires** :

- [embedding-shape](https://news.ycombinator.com/item?id=48169219) : Seems this traces back almost a week, from Nightmare-Eclipse who is the researcher who found this: Tuesday, 12 May 2026 - "Here are the links, yes, two vulnerabilities this time \[YellowKey\] \[GreenPlasma\] \[...\] Next patch tuesday will have a big surprise for you Microsoft" Wednesday, 13 May 2026 - "…
- [layer8](https://news.ycombinator.com/item?id=48170023) : Better writeup: https://infosec.exchange/@wdormann/116565129854382214 The published exploit doesn’t affect Bitlocker with a PIN, without which Bitlocker isn’t secure anyway. The original author claims they have an exploit that also works with a PIN, but hasn’t provided any proof of that.
- [kryogen1c](https://news.ycombinator.com/item?id=48170001) : From: https://infosec.exchange/@wdormann/116565129854382214 \>In a normal WinRE session, you have a X:\\Windows\\System32 directory that has a winpeshl.ini file in it \>However, with the YellowKey exploit, it looks like Transactional NTFS bits on a USB Drive are able to delete the winpeshl.ini file on…

---

[Article original](https://www.techspot.com/news/112410-security-researcher-microsoft-secretly-built-backdoor-bitlocker-releases.html) · [Discussion HN](https://news.ycombinator.com/item?id=48168856)
