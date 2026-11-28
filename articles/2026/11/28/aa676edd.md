---
article_fetched_at: '2026-11-28T02:24:44.770764Z'
attempts: 0
content_source: extracted
discussion_comment_count: 53
discussion_fetched_at: '2026-11-28T02:24:33.649839Z'
error: null
guid: https://news.ycombinator.com/item?id=50658191
hn_item_id: 50658191
hn_url: https://news.ycombinator.com/item?id=50658191
image_url: https://opengraph.githubassets.com/f996107bb81f45c946a11ccda774dbf04f566627a309eee9be1cedd9bf5432b5/gary23w/f-ck_data_brokers
is_ask_or_show_hn: false
llm_input_tokens: 7419
llm_latency_ms: 8262
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 937
our_published_at: '2026-11-28T01:57:46Z'
rewritten_title: 'Fuck_data_brokers.py : outil gratuit Python pour supprimer vos données
  chez plus de 600 courtiers'
source_published_at: '2026-11-26T18:37:21Z'
status: summarized
summarized_at: '2026-11-28T02:26:12.577522Z'
title: 'Show HN: Fuck_data_brokers.py'
url: https://github.com/gary23w/f-ck_data_brokers
---

## Résumé de l'article

Fuck_data_brokers.py est un script Python gratuit et open source qui automatise la suppression de vos données personnelles auprès des courtiers de données enregistrés. L'outil génère des lettres de suppression légales personnalisées basées sur votre juridiction, les envoie, suivi les réponses et escalade les refus auprès des régulateurs compétents.

- Accède à plus de 750 courtiers de données enregistrés auprès des régulateurs californiens, oregonais et texans, sans dépendances ni abonnement
- Génère et envoie des lettres de suppression légales au nom de l'utilisateur, envoyant uniquement le nom, l'adresse e-mail et la ville (zéro donné sensible)
- Analyse automatiquement les réponses des courtiers, identifie les prétextes (CAPTCHA, demande d'ID) et envoie des rappels aux entreprises qui ne répondent pas
- Fonctionne en tant que serveur MCP intégrable dans les assistants IA pour automatiser l'envoi et le suivi
- Stocke toutes les données localement sur l'ordinateur de l'utilisateur dans un dossier caché, sans téléchargement vers des serveurs externes

## Discussion sur Hacker News (53 commentaires)

**Avis positifs** :
- Automatise efficacement l'exercice des droits de suppression de données, rendant accessible ce qui était auparavant fastidieux et peu pratiqué par le public
- Le fichier brokers.json fourni est précieux en lui-même comme ressource, listant ~750 courtiers de données avec plus de détails que les services gratuits comme California DROP
- Offre une alternative gratuite et transparente aux services payants type Incogni ou Optery, avec code MIT-licensed et option payante optionnelle pour ceux qui ne peuvent pas l'exécuter eux-mêmes
- Répond à un problème réel : les données personnelles sont vendues même en dehors des États-Unis et aux citoyens de l'UE, avec des conséquences concrètes (appels de démarchage à minuit)
- Automatise à grande échelle ce qu'on peut légalement faire : envoyer des demandes de suppression aux régulateurs en cas de non-réponse dans les 7 jours pourrait effectivement incommoder les courtiers

**Avis négatifs** :
- Jouer selon les règles des courtiers (fournir données personnelles) peut les aider à enrichir leurs listes existantes plutôt que de les punir, le modèle économique reste inchangé
- Le script nécessite de fournir ses informations personnelles aux brokers eux-mêmes, créant un paradoxe : contribuer aux mêmes données qu'on cherche à supprimer
- Solutions insuffisantes sur le fond : les données réapparaissent après suppression, les courtiers ignorent les demandes, et aucune régulation U.S. n'existe réellement pour les contraindre
- Rédaction du README probablement générée par LLM et ton grandiloquent (« chaque star = une compliance department vaincue ») réduisant la crédibilité du projet
- Peu utile pour les personnes qui en ont le plus besoin : ceux sans compétences techniques ou sans accès à Python ne bénéficient que de l'option payante du créateur

**Top commentaires** :

- [arijun](https://news.ycombinator.com/item?id=50659725) : « If a form demands a photo of your ID, close the tab. They sell personal data. They are not getting more of it from you. » What happens then? Can’t they claim they don’t have to remove your data since you didn’t submit a form?
- [mzajc](https://news.ycombinator.com/item?id=50660048) : The incredibly sloppy prose and code, the call for stars, and the advertisement for a paid service in the README sour what is otherwise a nice idea IMHO.
- [joshmoody24](https://news.ycombinator.com/item?id=50659665) : Definitely going to use this. This is the kind of software I hope to see more of in this crazy new world we're heading into

---

[Article original](https://github.com/gary23w/f-ck_data_brokers) · [Discussion HN](https://news.ycombinator.com/item?id=50658191)
