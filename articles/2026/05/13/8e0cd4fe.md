---
article_fetched_at: '2026-05-13T16:58:25.874756Z'
attempts: 0
content_source: extracted
discussion_comment_count: 190
discussion_fetched_at: '2026-05-13T16:58:25.115702Z'
error: null
guid: https://news.ycombinator.com/item?id=48121266
hn_item_id: 48121266
hn_url: https://news.ycombinator.com/item?id=48121266
image_url: https://jorijn.com/static/images/social-previews/9e36d69f81.png
is_ask_or_show_hn: false
llm_input_tokens: 20643
llm_latency_ms: 13217
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1157
our_published_at: '2026-05-13T16:13:06Z'
rewritten_title: Raisons techniques et légales du passage de GitHub vers l'auto-hébergement
  Forgejo
source_published_at: '2026-05-13T12:54:00Z'
status: summarized
summarized_at: '2026-05-13T16:58:45.382451Z'
title: Why I'm leaving GitHub for Forgejo
url: https://jorijn.com/en/blog/leaving-github-for-forgejo/
---

## Résumé de l'article

Un développeur détaille son migration de GitHub vers Forgejo v15 LTS auto-hébergé sur une machine locale, s'alignant avec la décision du gouvernement néerlandais d'utiliser Forgejo pour code.overheid.nl. L'auteur identifie trois problèmes structurels chez GitHub : sa subordination à la division CoreAI de Microsoft depuis août 2025, l'inversion en avril 2026 du consentement par défaut pour l'utilisation des données Copilot en entraînement d'IA, et les risques juridictionnels US (FISA Section 702, CLOUD Act) irrésolus.

- GitHub a connu 257 incidents en 12 mois (48 majeurs), avec une croissance de charge liée à l'IA nécessitant 30x la capacité actuelle selon son CTO
- La direction indépendante de GitHub a disparu quand Microsoft l'a intégré à sa division CoreAI, mettant fin à l'autonomie décisionnelle du produit
- Les données d'interaction Copilot (Free/Pro/Pro+) alimentent désormais l'entraînement par défaut, sans contrôle au niveau du dépôt ; seuls les clients payants (Business/Enterprise) en sont exempts
- Forgejo a été préféré à GitLab pour ses licences GPLv3+ (pas d'open-core), sa gouvernance démocratique via Codeberg e.V., et l'absence d'exposition commerciale future
- L'infrastructure de l'auteur utilise KVM isolé, gVisor, reconstructions VM hebdomadaires, filtrage nftables d'égoût, et tokens d'exécution limités pour contenir les risques de CI

## Discussion sur Hacker News (190 commentaires)

**Avis positifs** :
- Forgejo offre un excellent équilibre entre facilité d'utilisation et contrôle : code décentralisé, bien architecturé pour les personnalisations, et permet des fonctionnalités avancées (showcases privés, etc.) sans combattre l'architecture.
- L'infrastructure open source pour les outils de développement permet à la communauté d'avoir un contrôle réel et une protection contre les abus des géants technologiques, contrairement aux services centralisés qui imposent leurs conditions.
- GitHub a violé la confiance en entraînant Copilot sur les dépôts publics sans consentement explicite et en ignorant les obligations de licence d'attribution, poussant légitimement les développeurs à chercher des alternatives.
- Forgejo offre CI/CD natif, suivi des problèmes, registre de paquets et fonctionne bien pour les petits projets ; l'auto-hébergement est devenu accessible (NUC, Docker, Raspberry Pi) et les coûts sont gérables.
- La fédération envisagée de Forgejo via ForgeFed pourrait résoudre le problème de découverte tout en conservant la décentralisation, offrant un équilibre entre indépendance et communauté.

**Avis négatifs** :
- La fragmentation du marché : sans effet réseau massif, migrer vers Forgejo ou d'autres alternatives signifie perdre la découverte, les collaborateurs et l'audience établie sur GitHub, où se concentrent 99%+ des projets open source.
- Les alternatives promettent la décentralisation mais créent simplement de nouveaux centres de dépendance (Forgejo, GitLab, etc.) ; changer de fournisseur ne résout pas vraiment le problème de dépendance logicielle ou architecturale.
- Les défis pratiques persistent : migrer CI/CD, suivi des problèmes, historique de collaboration est complexe et coûteux ; GitHub Actions reste imbattable pour les matrices multi-OS gratuites (Windows, Linux, macOS avec plusieurs architectures).
- Le soi-disant départ massif de GitHub est largement exagéré : seule une petite minorité se migrate, créant une bulle de discussion sur HN/Twitter alors que l'immense majorité des développeurs reste sur GitHub par manque de meilleure option.
- L'aspect social et la découverte restent fondamentalement cassés : même avec Forgejo, sans plateforme centrale, les nouveaux projets disparaissent, les contributeurs ne se trouvent pas, et les mainteneurs perdent les avantages de la visibilité établie.

**Top commentaires** :

- [giancarlostoro](https://news.ycombinator.com/item?id=48121439) : Everyone seems to be leaving GitHub, and forgetting the entire spirit of what git is in my eyes. Git was always meant to be decentralized, the problem here is that all the tooling around git was centralized to GitHub because it was a cleaner experience, they scaled nicely, and were properly maintai…
- [zuzululu](https://news.ycombinator.com/item?id=48124099) : I'm kind of baffled why everybody is suddenly hating on github? I use it just fine. I'm actually impressed how well codex is able to interact with it. I virtually do not need to fret about git commands or managing github to respond to issues anymore. I don't see an alternative and its a bit of a st…
- [sc68cal](https://news.ycombinator.com/item?id=48121752) : I have also moved my git repositories to a self-hosted NUC. I have not yet bothered with a HTTP frontend to share it with the world, mostly because I don't want to provide AI scrapers with content and don't want to put the work in to block them. It's a shame that all these companies that benefited…

---

[Article original](https://jorijn.com/en/blog/leaving-github-for-forgejo/) · [Discussion HN](https://news.ycombinator.com/item?id=48121266)
