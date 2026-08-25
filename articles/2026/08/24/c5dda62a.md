---
article_fetched_at: '2026-08-25T06:30:54.964807Z'
attempts: 0
content_source: extracted
discussion_comment_count: 20
discussion_fetched_at: '2026-08-25T06:30:54.414460Z'
error: null
guid: https://news.ycombinator.com/item?id=49411395
hn_item_id: 49411395
hn_url: https://news.ycombinator.com/item?id=49411395
image_url: https://compote.slate.com/images/6ee722e0-9927-467f-b919-0c0a9217bae5.jpeg?crop=1560%2C1040%2Cx0%2Cy0&width=1560
is_ask_or_show_hn: false
llm_input_tokens: 4663
llm_latency_ms: 11569
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 991
our_published_at: '2026-08-24T19:24:38Z'
rewritten_title: Microsoft supprime les données de 170 000 associations faute de communication
  sur fin de programme
source_published_at: '2026-08-23T18:55:54Z'
status: summarized
summarized_at: '2026-08-25T06:31:13.047366Z'
title: Over 170k Nonprofits Lost All Their Data. Is Microsoft to Blame?
url: https://slate.com/technology/2026/08/microsoft-software-nonprofit-data-delete.html
---

## Résumé de l'article

Microsoft a cessé unilatéralement ses programmes de licences gratuites pour les petites organisations à but non lucratif en juin 2025, entraînant la perte de données pour environ 171 000 associations. Le géant technologique avait annoncé la fin du programme en 2024, mais sa communication insuffisante sur cette transition a laissé de nombreuses ONG sans préavis avant la suppression définitive de leurs fichiers stockés sur OneDrive et l'accès aux applications premium.

- Microsoft a cité un objectif de « simplification » de son offre de subventions pour justifier l'arrêt du programme, affirmant avoir notifié les clients à partir du printemps 2025, mais plusieurs sources rapportent n'avoir reçu aucun avertissement ou des messages confus.
- Les notifications de Microsoft étaient principalement envoyées aux adresses administrateur rarement consultées, souvent noyées dans le spam, tandis que les renouvellements de licences n'incluaient pas d'informations supplémentaires sur le calendrier de fermeture.
- Les petites associations, qui dépendaient de ces outils gratuits pour environ 30 % de leurs dépenses informatiques, se retrouvent incapables de migrer rapidement vers des alternatives, les versions en ligne des applications Microsoft étant moins performantes que les versions payantes.
- Le contexte politique et commercial explique probablement cette décision : Microsoft donne la priorité à l'IA et à la réduction des coûts, tout en cherchant à éviter les scrutins du gouvernement Trump concernant les organisations soutenues par ses donations.
- Les organisations affectées font face à des pertes de données substantielles (500 Go ou plus) et à des centaines d'heures de travail pour recréer les documents et processus perdus.

## Discussion sur Hacker News (20 commentaires)

**Avis positifs** :
- Microsoft a violé ses propres engagements contractuels en supprimant les données avant le délai de 90 jours stipulé, ce qui constitue une rupture fondamentale de confiance
- La culture d'entreprise actuelle chez Microsoft privilégie la réduction des coûts et les revenus d'abonnement au détriment de la qualité, notamment après la suppression des équipes QA
- Les nonprofits ont été victimes d'une gestion irresponsable : absence de notification claire, suppression immédiate au lieu d'une période de transition progressive, et refus d'assumer la responsabilité
- Le problème systémique des alertes excessives provoque une fatigue d'alarme chez les administrateurs IT, les rendant incapables de détecter les vrais risques
- Une approche plus responsable aurait été une période de lecture seule de deux mois pour alerter les utilisateurs, plutôt qu'une suppression définitive et irréversible

**Avis négatifs** :
- Ces organisations utilisaient un service cloud gratuit ou subventionné sans avoir mis en place de sauvegarde indépendante ou de stratégie de rétention de données
- La dépendance à des services cloud sans contrat commercial clair ni infrastructure de secours est une mauvaise pratique IT fondamentale
- Selon la documentation officielle Microsoft, les données devraient être conservées 90 jours après expiration, suggérant une possible confusion ou non-respect de la politique plutôt qu'une malveillance délibérée
- D'autres services cloud (comme Flickr) maintiennent les données bien plus longtemps malgré des avertissements répétés, ce qui n'excuse pas mais contextualise le problème
- L'industrie technologique générale souffre d'un manque de sérieux chronique dans la continuité et la fiabilité des services

**Top commentaires** :

- [12\_throw\_away](https://news.ycombinator.com/item?id=49411696) : Yep, this is the sort of thing happens when you've deeply internalized that trustworthiness and continuity is not important. Microsoft today is not a serious company, it is not run by serious people, and it is at the forefront of a deeply unserious industry.
- [iamniels](https://news.ycombinator.com/item?id=49416147) : This is wrong on so many levels. First of all, IT admins receive weekly e-mails from AWS, Google and MS that a certain service will shut down and that it will affect operations. In 90% of the cases, these e-mails are sent to all customers instead of only the affected customers, so admins get alarm…
- [valicord](https://news.ycombinator.com/item?id=49413706) : According to https://learn.microsoft.com/en-us/microsoft-365/commerce/sub... the data should not be deleted for 90 days after license expiration - what am I missing?

---

[Article original](https://slate.com/technology/2026/08/microsoft-software-nonprofit-data-delete.html) · [Discussion HN](https://news.ycombinator.com/item?id=49411395)
