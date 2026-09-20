---
article_fetched_at: '2026-09-20T20:02:16.759343Z'
attempts: 0
content_source: extracted
discussion_comment_count: 148
discussion_fetched_at: '2026-09-20T20:01:54.003774Z'
error: null
guid: https://news.ycombinator.com/item?id=49776729
hn_item_id: 49776729
hn_url: https://news.ycombinator.com/item?id=49776729
is_ask_or_show_hn: false
llm_input_tokens: 12104
llm_latency_ms: 12291
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 996
our_published_at: '2026-09-20T19:30:24Z'
rewritten_title: OpenAI collecte les activités des utilisateurs sur d'autres sites
  via son système de publicités
source_published_at: '2026-09-20T15:18:44Z'
status: summarized
summarized_at: '2026-09-20T20:03:32.028578Z'
title: ChatGPT now knows what you do on other websites via ad collector
url: https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/
---

## Résumé de l'article

OpenAI utilise un cookie appelé __obi pour suivre ce que les utilisateurs font sur des sites tiers ayant installé son code publicitaire. Ce cookie, créé lors de la connexion à ChatGPT, est transmis à OpenAI chaque fois qu'un utilisateur visite un site partenaire, permettant à OpenAI de relier l'activité hors ChatGPT au compte de l'utilisateur.

- Le mécanisme fonctionne en trois étapes : ChatGPT génère un identifiant signé, celui-ci devient un cookie sur le domaine OpenAI avec une durée de vie d'un an, et les sites publicitaires le renvoient à OpenAI avec des données de navigation (produits consultés, articles lus, comportements d'achat)
- Le cookie __obi est le seul cookie OpenAI configuré avec SameSite=None, permettant son envoi sur les requêtes cross-site, contrairement aux autres cookies OpenAI bloqués par le navigateur
- OpenAI collecte également l'identité des utilisateurs (email, téléphone, noms) à partir des formulaires et du gestionnaire de balises des sites, avec 685 événements de données extraites contre 255 fournis intentionnellement par les annonceurs
- OpenAI classe ce cookie comme un cookie "Analytics" dans sa politique, même s'il fonctionne comme un outil de suivi publicitaire ; le système fonctionne même pour les utilisateurs en session anonyme et sur les appareils Android
- Le mécanisme ne fonctionne pas sur iOS (Safari et Chrome) en raison de la protection contre le suivi tiers, et les annonceurs n'ont pas accès au cookie __obi malgré l'installation de leur code de conversion

## Discussion sur Hacker News (148 commentaires)

**Avis positifs** :
- Le suivi de tiers est une pratique standard en adtech depuis des décennies ; OpenAI suit simplement le modèle éprouvé de Facebook et Google en matière de monétisation
- L'attribution et la mesure de conversion sont techniquement nécessaires pour construire un système publicitaire fonctionnel et justifier les investissements massifs dans l'IA
- Avec consentement explicite et contrôle utilisateur, ce suivi pourrait potentiellement améliorer la qualité des réponses de ChatGPT en les personnalisant selon l'historique et les intérêts réels de l'utilisateur
- Cette pratique est cohérente avec le recrutement par OpenAI de nombreux anciens employés de Meta et Google, habitués à ces modèles de monétisation

**Avis négatifs** :
- C'est de la surveillance de masse déguisée : tracker les utilisateurs au-delà de ChatGPT sans consentement clair est moralement équivalent à du spyware, même si légal
- Le contexte de confiance est fondamentalement différent : contrairement à Facebook (gratuit), certains utilisateurs de ChatGPT payent pour le service et ne s'attendent pas à être tracés et profilés
- Les chromophores browser (Chrome/Edge) ne bloquent pas les cookies tiers par défaut, ce qui signifie que la majorité des utilisateurs ignorent complètement qu'ils sont traqués malgré des défenses raisonnables
- Cette pratique représente la monétisation inévitable par les annonces : OpenAI réduit progressivement ses subventions d'investisseurs et remplace la monétisation par la vente publicitaire basée sur la surveillance
- Les défenseurs confondent intentionnellement les publicités acceptables avec le suivi invasif des données personnelles ; le problème n'est pas l'existence d'annonces mais l'extraction de données comportementales

**Top commentaires** :

- [thih9](https://news.ycombinator.com/item?id=49778582) : I am once again happy that the EU is fighting practices like these via legislation. Some outcomes can be annoying, but the net result is still positive, for the consumers and their data privacy at least.
- [mavsman](https://news.ycombinator.com/item?id=49777671) : To me, this quote just about sums it up: \> The mechanism is standard adtech. What has no precedent is running it on an AI chat product. As someone who has been well aware of this mechanism for quite some time, I still feel icky anytime I re-read the details of it. What a time to be alive.
- [luke5441](https://news.ycombinator.com/item?id=49777947) : MDN lists how different browsers prevent this: https://developer.mozilla.org/en-US/docs/Web/Privacy/Guides/... Firefox, Brave and Safari do. Chrome and Edge do not.

---

[Article original](https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/) · [Discussion HN](https://news.ycombinator.com/item?id=49776729)
