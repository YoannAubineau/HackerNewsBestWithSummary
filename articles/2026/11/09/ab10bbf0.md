---
article_fetched_at: '2026-11-09T00:21:29.056438Z'
attempts: 0
content_source: extracted
discussion_comment_count: 169
discussion_fetched_at: '2026-11-09T00:21:26.872367Z'
error: null
guid: https://news.ycombinator.com/item?id=50416158
hn_item_id: 50416158
hn_url: https://news.ycombinator.com/item?id=50416158
image_url: https://mailroute.net/og-default.png
is_ask_or_show_hn: false
llm_input_tokens: 15047
llm_latency_ms: 9173
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 995
our_published_at: '2026-11-09T00:18:40Z'
rewritten_title: Outlook.com rejette silencieusement les emails de domaines sans DMARC
  depuis novembre 2026
source_published_at: '2026-11-08T19:20:32Z'
status: summarized
summarized_at: '2026-11-09T00:22:14.758753Z'
title: Outlook.com Is Quietly Rejecting Email from Domains Without DMARC
url: https://mailroute.net/blog/outlook-rejecting-email-without-dmarc
---

## Résumé de l'article

Depuis le 5 novembre 2026, Microsoft rejette certains emails provenant de domaines qui ne publient pas d'enregistrement DMARC, sans l'avoir annoncé. Ce nouveau blocage affecte même les petits expéditeurs et crée des rejets partiels et imprévisibles qui passent souvent inaperçus, contrairement à la règle de mai 2025 qui visait les expéditeurs en masse.

- Le rejet cible tous les domaines sans DMARC, pas seulement les envoyeurs en masse (>5 000 messages/jour) de la politique précédente.
- Les bounces sont partiels : certains messages passent, d'autres sont rejetés, ce qui rend le problème difficile à détecter.
- Le message d'erreur « Message lacks SPF/DKIM/DMARC Auth Records » est trompeur : la plupart des domaines affectés ont SPF et DKIM, mais manquent l'enregistrement DMARC.
- Le correctif est simple : ajouter un enregistrement TXT `_dmarc` avec la valeur `v=DMARC1; p=none`, qui n'affecte pas le traitement par Gmail, Yahoo ou d'autres services.
- Cette tendance silencieuse reflète une stratégie des grands fournisseurs de courrier : imposer d'abord aux expéditeurs en masse, puis généraliser sans annonce.

## Discussion sur Hacker News (169 commentaires)

**Avis positifs** :
- DMARC est une protection légitime contre l'usurpation de domaine et le phishing, et son implémentation (SPF + DKIM + DMARC) est devenue un standard nécessaire pour tout envoyeur de mails professionnel
- L'application stricte de cette règle est efficace pour forcer l'adoption : sans pénalité tangible, les administrateurs repousse indéfiniment la configuration, alors qu'un rejet clair les pousse à corriger rapidement
- La configuration n'est pas complexe (15-30 minutes avec un guide) et représente un coût acceptable pour les envoyeurs légitimes, contrairement aux spammeurs motivés à contourner les obstacles
- Microsoft et d'autres fournisseurs ont annoncé cette évolution il y a plus d'un an via des canaux officiels et des articles de blog publics, donc pas vraiment en silence
- Cette mesure réduit significativement l'usurpation d'identité des domaines sans configuration, en particulier les domaines non-actifs utilisés uniquement pour le spoofing

**Avis négatifs** :
- L'absence d'annonce publique visible ou de communication directe avant le déploiement a pris de nombreux administrateurs par surprise le weekend, créant des perturbations opérationnelles
- DMARC seul (avec p=none) n'ajoute aucune sécurité supplémentaire quand SPF et DKIM sont déjà configurés correctement, c'est de la « sécurité théâtrale »
- Cette centralisation du contrôle email entre Microsoft et Google renforce les monopoles et érode l'accès ouvert : les petits envoyeurs légitimes ont peu de recours en cas de problème non documenté
- Outlook.com silencieuse rejette ou perd des emails valides depuis des années (même avec SPF/DKIM/DMARC corrects), sans explication ou recours public, rendant cette nouvelle règle suspecte
- Le standard DMARC a été conçu pour les grandes organisations complexes, pas pour les petits envoyeurs ou les domaines personnels, ce qui pénalise injustement ces derniers

**Top commentaires** :

- [Neikius](https://news.ycombinator.com/item?id=50416963) : Outlook.com is also rejecting mail based on blocklists that are not public and you essentialy cannot get yourself out. My VPS provider is pretty much entirely blocked and their regular blocklist process says we are golden so nothing to unblock. Outlook.com and similar are an anathema to email. This…
- [stephbook](https://news.ycombinator.com/item?id=50416581) : Sounds like something every mail sender should have done already. Good for Microsoft customers and I don't care one bit for the lazy people who have to late-patch now.
- [codethief](https://news.ycombinator.com/item?id=50418296) : Outlook.com has quietly dropped\[0\] emails from certain domains/IPs for years, even with SPF/DKIM/DMARC all properly set up and no history of spam. As someone who's administering their own mail server, Outlook has been the bane of my existence. \[0\]: As in: They accepted the email just fine \(accordin…

---

[Article original](https://mailroute.net/blog/outlook-rejecting-email-without-dmarc) · [Discussion HN](https://news.ycombinator.com/item?id=50416158)
