---
article_fetched_at: '2026-11-02T21:08:56.100768Z'
attempts: 0
content_source: extracted
discussion_comment_count: 528
discussion_fetched_at: '2026-11-02T21:08:53.331060Z'
error: null
guid: https://news.ycombinator.com/item?id=50337608
hn_item_id: 50337608
hn_url: https://news.ycombinator.com/item?id=50337608
is_ask_or_show_hn: false
llm_input_tokens: 40769
llm_latency_ms: 8263
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 821
our_published_at: '2026-11-02T20:20:17Z'
rewritten_title: Ubuntu n'a pas corrigé une faille critique du noyau Linux deux semaines
  après Debian
source_published_at: '2026-11-02T14:52:00Z'
status: summarized
summarized_at: '2026-11-02T21:10:56.886157Z'
title: WTF Ubuntu?
url: https://chalmovsky.com/posts/wtf-ubuntu
---

## Résumé de l'article

Ubuntu, distribution Linux commercialisée par Canonical, n'a pas publié de correctif pour CVE-2026-98432, une faille critique (score CVSS 9.8) du noyau Linux découverte depuis 2016 et exploitable à distance pour obtenir les droits root. Debian a publié un correctif le 16 octobre, mais toutes les versions supportées d'Ubuntu restent listées comme vulnérables plus de deux semaines après, malgré les promesses de l'éditeur concernant des correctifs rapides pour les vulnérabilités critiques.

- Debian et d'autres distributions maintenues par des bénévoles (Arch, Alpine) ont déjà livré le correctif, contrairement à Ubuntu qui vend des abonnements de sécurité
- La faille existe depuis 2016 et affecte virtuellement chaque serveur Linux de la planète, avec un exploit fonctionnel permettant une compromission totale
- L'auteur a dû mettre ses serveurs Ubuntu hors ligne en attendant une correction et annonce son migration vers une autre distribution
- Le délai de neuf jours après l'évaluation CVSS 9.8 contredit la promesse d'Ubuntu de fournir des correctifs rapides pour les vulnérabilités critiques

## Discussion sur Hacker News (528 commentaires)

**Avis positifs** :
- Debian et autres distros communautaires ont publié le correctif rapidement, démontrant une meilleure réactivité que Ubuntu malgré des ressources limitées
- Le délai de deux semaines est inacceptable pour une vulnérabilité critique (CVSS 9.8) affectant même les clients payants d'Ubuntu Pro, contrastant avec les promesses de support de sécurité
- Ubuntu a perdu de la crédibilité par son manque de communication : aucune explication du retard, contradictions entre la notation de priorité et la sévérité, absence de mitigations documentées
- Cette incident révèle un problème systémique chez Canonical : priorité au marketing (Ubuntu Pro) sans livrer la sécurité promise, comparé à des alternatives plus fiables comme Rocky/Alma Linux

**Avis négatifs** :
- Les critiques ignorent que Ubuntu teste des dizaines de kernel pour plusieurs architectures sur 10 ans, ce qui prend du temps, contrairement aux distros avec cycles plus rapides
- Anthropic seul affirme obtenir une RCE ; les autres sources (AWS, Red Hat) décrivent plutôt un déni de service, et l'EPSS indique <1% de probabilité d'exploitation réelle
- Les utilisateurs non-payants se plaignent d'une distro gratuite ; les vraies critiques devraient venir des clients Ubuntu Pro, qui eux ont droit aux mitigations firewall en attendant
- Ubuntu a sorti les kernels patché en « proposed » depuis le 28 octobre, accessibles via apt avec l'option `-t` ; le retard concerne seulement la promotion vers les dépôts « security » standard

**Top commentaires** :

- [BoppreH](https://news.ycombinator.com/item?id=50338289) : Worse yet, the Ubuntu security incident page\[0\] lists "Ubuntu Priority: High" \(as opposed to Critical, which would trigger an out-of-schedule patch\). There's a "Why this priority?" link that simply says: \> Why is this CVE high priority? \> See ubuntu cvss score That's it, we don't even get a period…
- [throw0101c](https://news.ycombinator.com/item?id=50338468) : For the record, the kernels with the fixes are in the "proposed" repos for each LTS release: \* https://launchpad.net/ubuntu/+source/linux You can pull them down with a "-t" added to your apt-get \(but will not appear by default\). 26LTS had the new kernel go to the updates/security repos on October 2…
- [alentred](https://news.ycombinator.com/item?id=50343162) : To be fair: while critical \(9.8\) it has an EPSS score of \<1% \(probability of it being actually used\). According to \[1\], \[2\], and others, at worst the issue results in a kernel crash or a denial of service. I read the post by Anthropic too, but something just doesn't reconcile there between everyone…

---

[Article original](https://chalmovsky.com/posts/wtf-ubuntu) · [Discussion HN](https://news.ycombinator.com/item?id=50337608)
