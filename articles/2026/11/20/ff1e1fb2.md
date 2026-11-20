---
article_fetched_at: '2026-11-20T01:33:44.612474Z'
attempts: 0
content_source: extracted
discussion_comment_count: 192
discussion_fetched_at: '2026-11-20T01:33:40.513766Z'
error: null
guid: https://news.ycombinator.com/item?id=50562262
hn_item_id: 50562262
hn_url: https://news.ycombinator.com/item?id=50562262
image_url: https://ounapuu.ee/posts/2026/11/19/unsafeguards/media/cover_hu_5a6285e4518135fc.jpg
is_ask_or_show_hn: false
llm_input_tokens: 17866
llm_latency_ms: 10057
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1105
our_published_at: '2026-11-20T00:40:44Z'
rewritten_title: Un développeur critique les garde-fous d'IA qui l'empêchent de sécuriser
  son service
source_published_at: '2026-11-19T16:30:18Z'
status: summarized
summarized_at: '2026-11-20T01:36:02.961131Z'
title: Fuck Your AI Safeguards
url: https://ounapuu.ee/posts/2026/11/19/unsafeguards/
---

## Résumé de l'article

Un ingénieur produit senior dénonce les restrictions imposées par Claude AI (assistant IA d'Anthropic) lors de tentatives de correction de failles de sécurité dans son propre service. Il argumente que ces mesures de protection ralentissent les efforts de sécurisation légitime tout en restant inefficaces face aux acteurs malveillants utilisant des modèles sans garde-fous.

- L'auteur s'est heurté à des refus d'assistance de Claude pour appliquer des correctifs de sécurité, malgré son contrôle avéré du service et la nécessité de se conformer aux réglementations locales
- Le processus d'exemption proposé par Anthropic exige plusieurs jours d'attente, l'abandon de protections de propriété intellectuelle, et la soumission de documents d'identité
- L'auteur souligne que les criminels et les laboratoires d'IA majeurs contournent facilement ces restrictions en utilisant des modèles déchaînés ou non filtrés disponibles en open source
- Il a finalement résolu le problème en recourant à des modèles open source hébergés en UE (GLM 5.3) qui ont permis d'identifier et corriger la faille
- Il critique Anthropic pour créer un paysage de sécurité moins robuste tout en potentiellement renforçant sa position concurrentielle avant une IPO

## Discussion sur Hacker News (192 commentaires)

**Avis positifs** :
- Les garde-fous sont inefficaces et contre-productifs : ils bloquent les utilisateurs légitimes (développeurs, chercheurs en sécurité) tout en laissant les acteurs malveillants contourner les restrictions via des modèles alternatifs non censurés
- Les entreprises d'IA appliquent une double norme : elles utilisent internement des modèles sans restrictions pour leurs propres recherches en sécurité, puis refusent les mêmes capacités aux utilisateurs payants
- Les safeguards créent une protection racket : seules les entreprises de pointe peuvent accéder aux outils puissants sans restrictions, les obligeant à payer pour les services spécialisés (CVP, etc.) avec des processus opaques et lents
- Les modèles ouverts (chinois notamment) démontrent l'efficacité réelle : GLM-5.3 a aidé HuggingFace lors d'une attaque quand les modèles fermés ont refusé; ils offrent une alternative viable face à ce contrôle monopolistique
- Blocages contre-productifs même pour les tâches légitimes : refus d'aider à sécuriser ses propres systèmes, à faire du reverse-engineering de contenus libres de droits, ou à charger des cartes sur ses propres appareils

**Avis négatifs** :
- Les safeguards sont nécessaires car les modèles d'IA posent des risques réels : prolifération incontrôlée, autonomie excessive des systèmes (HuggingFace l'a prouvé), nécessité de séparation entre usages bénins et malveillants
- Il est impossible pour les entreprises de distinguer parfaitement les intentions légitimes des abus : comparer aux restrictions de sécurité humaines (ex. numéros de téléphone professionnels) qui utilisent aussi des safeguards génériques par défaut
- Les modèles ouverts posent leurs propres risques : prolifération irréversible, pas de limite au contrôle sur les capacités dangereuses, contrairement aux modèles fermés avec responsabilité éditoriale
- La critique ignore les véritables dangers : concentration de la puissance IA, dépendance accrue des utilisateurs, perte de compétences humaines, création de contenus générés en masse, plutôt que des refus ciblés sur la sécurité
- Les programmes d'accès spécialisé (CVP) existent et ne sont pas impossibles à obtenir; critiquer les safeguards sans proposer d'alternative cohérente revient à demander zéro contrôle

**Top commentaires** :

- [SkyeCA](https://news.ycombinator.com/item?id=50565247) : The safeguards are the future of closed AI and the increasing number of tasks Claude refuses to help with has been a big wake-up call to me. The closed models can only get more restricted as time goes on and they're going to be a dead end if you want to do anything outside the norm. Claude already…
- [nathanfig](https://news.ycombinator.com/item?id=50562645) : This had real consequences during the HuggingFace attack- closed models refused to help, GLM-5 is what HuggingFace used to thwart the swarm. More importantly, it showcases how little teeth the Claude constitution has. Claude will reassure users that its constitution means it prioritizes user autono…
- [espeed](https://news.ycombinator.com/item?id=50565937) : No one should use Fable 5.2 going forward. Anthropic officially added silent degradation back, "Fable 5.2 and Claude Mythos 5.2 perform at about the level of Opus 5.5": "Thus, in relevant areas, including accelerator kernel optimization and improving large language model architectures, Fable 5.2 an…

---

[Article original](https://ounapuu.ee/posts/2026/11/19/unsafeguards/) · [Discussion HN](https://news.ycombinator.com/item?id=50562262)
