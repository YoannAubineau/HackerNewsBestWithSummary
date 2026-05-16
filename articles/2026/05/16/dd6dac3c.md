---
article_fetched_at: '2026-05-16T06:45:24.327114Z'
attempts: 0
content_source: extracted
discussion_comment_count: 134
discussion_fetched_at: '2026-05-16T06:45:23.451199Z'
error: null
guid: https://news.ycombinator.com/item?id=48155690
hn_item_id: 48155690
hn_url: https://news.ycombinator.com/item?id=48155690
is_ask_or_show_hn: false
llm_input_tokens: 10815
llm_latency_ms: 11402
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1021
our_published_at: '2026-05-16T06:00:23Z'
rewritten_title: npm subit une attaque majeure de la chaîne d'approvisionnement, les
  développeurs jugent cela inévitable
source_published_at: '2026-05-16T00:36:02Z'
status: summarized
summarized_at: '2026-05-16T06:45:59.055295Z'
title: '''No way to prevent this,'' says only package manager where this regularly
  happens'
url: https://kevinpatel.xyz/posts/no-way-to-prevent-this/
---

## Résumé de l'article

Cet article, écrit sur le ton de la satire, critique la vulnérabilité chronique de l'écosystème JavaScript face aux attaques de chaîne d'approvisionnement. npm est un gestionnaire de paquets pour JavaScript qui centralise des millions de dépendances souvent maintenues par des contributeurs non vérifiés.

- L'article dénonce l'acceptation fataliste des développeurs face à des crises répétitives d'injection de malwares dans les paquets npm, notamment l'exécution par défaut de scripts arbitraires lors de l'installation.
- Les attaquants exploitent régulièrement des paquets abandonnés pour injecter des crypto-mineurs ou des malwares dans des millions d'applications en production.
- L'écosystème JavaScript crée une dépendance extrême envers des arbres profonds (40+ niveaux) de paquets tiers non vérifiés, contrairement à d'autres langages comme Go ou Rust qui disposent de bibliothèques standard robustes.
- La satire souligne l'absence de mesures de sécurité strictes (vérification cryptographique, bac à sable d'exécution) que npm pourrait mettre en place pour réduire les risques.
- D'autres écosystèmes ont signalé zéro incident du même type grâce à des standards de sécurité plus rigoureux intégrés à leurs chaînes d'outils.

## Discussion sur Hacker News (134 commentaires)

**Avis positifs** :
- npm est particulièrement vulnérable en raison de scripts post-installation qui exécutent du code arbitraire lors de l'installation, facilitant la création de vers auto-réplicants accédant aux tokens CI/CD
- D'autres écosystèmes (Maven Central, Go, Rust) ont des garde-fous supérieurs : vérification de domaine, versions exactes épinglées par défaut, absence de scripts d'installation automatiques
- Les cooldowns de publication (1-7 jours) et l'adoption d'outils comme pnpm/uv offrent des protections efficaces contre les attaques récentes, stoppant la propagation en heures plutôt qu'en secondes
- Le manque de financement des écosystèmes open source (npm, crates.io) empêche des mesures basiques de sécurité comme les namespaces vérifiés, contrairement à NuGet financé par Microsoft
- L'écosystème JavaScript favorise des micro-packages nombreux et interdépendants, créant une surface d'attaque massive comparée aux langages avec bibliothèques standard robustes

**Avis négatifs** :
- Les scripts post-installation ne sont qu'une distraction : le code malveillant s'exécute de toute façon lors de l'import des dépendances, avec ou sans postinstall scripts
- Tous les écosystèmes sont vulnérables aux attaques de chaîne d'approvisionnement (RubyGems, PyPI, XZ Tools) ; npm n'est pas unique, juste plus visible comme cible attrayante
- Les signatures PGP et namespaces ne préviennent pas les attaques si l'attaquant obtient les credentials du mainteneur lui-même, ce qui s'est produit récemment
- Les cooldowns ne font que repousser les attaques et créent des frictions pour les correctifs d'urgence ; la vraie solution est plus fondamentale (sandboxing, gestion des secrets)
- D'autres langages (Rust, Go) ont des mécanismes équivalents (build.rs, go:generate) permettant l'exécution de code arbitraire ; la maturité et la popularité de npm, pas uniquement sa conception, expliquent le nombre d'attaques

**Top commentaires** :

- [eranation](https://news.ycombinator.com/item?id=48156360) : I know people have opinions about cooldowns, but they would have saved you from axios, tanstack, and many other recent npm supply chain attacks. If you have Artifactory / Nexus, you probably already have cooldowns, but it's easy to set up if you don't. Why cooldowns? Most npm \(or pypi\) compromises…
- [aselimov3](https://news.ycombinator.com/item?id=48156010) : What are the actual guarantees that go/Rust make that Python/npm don’t? It seems like it might just be that Python/npm are juicier targets? I’m starting to try and avoid all third party packages
- [joeblubaugh](https://news.ycombinator.com/item?id=48156292) : There has been a lot of pain at my various jobs installing a safe global npm config on every developer machine, asking people not to disable it, checking it with mdm tools. A safer out-of-the-box configuration is long overdue.

---

[Article original](https://kevinpatel.xyz/posts/no-way-to-prevent-this/) · [Discussion HN](https://news.ycombinator.com/item?id=48155690)
