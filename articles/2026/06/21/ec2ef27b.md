---
article_fetched_at: '2026-06-21T07:35:09.934562Z'
attempts: 0
content_source: extracted
discussion_comment_count: 61
discussion_fetched_at: '2026-06-21T07:35:09.186492Z'
error: null
guid: https://news.ycombinator.com/item?id=48608645
hn_item_id: 48608645
hn_url: https://news.ycombinator.com/item?id=48608645
image_url: https://opengraph.githubassets.com/659584990e4b4099e536c90b17ea43757ff4a1bc50b37fd41ce3af4bb34f3dff/mysk-research/loupe
is_ask_or_show_hn: false
llm_input_tokens: 5182
llm_latency_ms: 11619
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 917
our_published_at: '2026-06-21T07:15:01Z'
rewritten_title: Loupe, une app iOS qui expose les données qu'une application native
  peut collecter
source_published_at: '2026-06-20T12:08:23Z'
status: summarized
summarized_at: '2026-06-21T07:35:47.394994Z'
title: Loupe – A iOS app that raises awareness about what native apps can see
url: https://github.com/mysk-research/loupe
---

## Résumé de l'article

Loupe est une application iOS et iPadOS open source créée par Mysk qui démontre concrètement ce que les apps natives peuvent accéder sur votre appareil. Elle lit les valeurs réelles des APIs iOS publiques auxquelles tout développeur tiers peut accéder, montrant comment les trackers forment un profil d'identification sans avoir besoin de vos données personnelles comme votre nom ou localisation.

- L'app classe les données accessibles en trois niveaux : passif (sans demande d'autorisation : langue, fuseau horaire, batterie), permission requise (contacts, photos, calendrier, localisation), et avancé (utilisation ingénieuse des APIs comme détection de schémas URL).
- Les données collectées restent entièrement sur l'appareil et ne sont jamais envoyées à moins que vous les exportiez explicitement.
- Loupe a été développée quasi entièrement avec des outils de codage assistés par l'IA et est distribuée gratuitement sous licence MIT.
- Les créateurs proposent également Psylo, un navigateur centré sur la confidentialité avec proxy et protections anti-fingerprinting.

## Discussion sur Hacker News (61 commentaires)

**Avis positifs** :
- Loupe expose des failles de confidentialité réelles et graves : accès au timestamp de création du volume, compteur pasteboard, liste des apps installées permettent un fingerprinting efficace sans permissions explicites
- L'app démontre que les protections d'Apple sont insuffisantes : les labels de confidentialité reposent sur l'honneur des développeurs, et même les apps sandboxées du MAS peuvent collecter massivement de données
- La corrélation de données entre apps (via SDKs tiers comme Facebook, IP, fuseau horaire, stockage) crée un profilage utilisateur systématique que la simple désactivation du suivi publicitaire ne bloque pas
- L'outil remplit un rôle éducatif crucial en rendant visible ce qui reste caché : beaucoup d'utilisateurs ignorent que des apps non autorisées peuvent accéder à cette information sensible
- Le problème suggère que l'internet devrait être opt-in plutôt qu'opt-out pour les apps, et qu'Apple devrait randomiser les identifiants de fingerprinting ou offrir des contrôles granulaires par catégorie

**Avis négatifs** :
- Loupe ne résout pas le problème fondamental : l'absence de véritable solution pratique hormis cesser d'installer des apps ou utiliser uniquement le web, ce qui limite l'utilité réelle de l'outil
- L'app a probablement été construite largement par IA (selon le README), ce qui soulève des questions sur sa fiabilité et sa complétude dans l'exposition des failles
- Le pasteboard changeCount et d'autres mécanismes ont des justifications légitimes (aider les apps à ne pas relancer des questions) et pourraient être modifiés plutôt que supprimés
- Sur le web aussi, la situation est aussi mauvaise sinon pire : les utilisateurs utilisent déjà des bloqueurs de publicités dans les navigateurs mais pas dans les apps, et de nombreux services web deviennent inutilisables sans installer l'app mobile
- Le problème décrit pourrait ressembler à une promotion voilée de Psylo avec achats in-app plutôt qu'une vraie solution d'empowerment utilisateur

**Top commentaires** :

- [throwaway27448](https://news.ycombinator.com/item?id=48616478) : I don't understand why internet access isn't opt-in for apps. Preventing exfiltration would prevent much of this harm, and most apps don't have any need to access the internet in the first place. Why am I creating a GE account to read my blood pressure? At least I know it's taking advantage of me.…
- [nomilk](https://news.ycombinator.com/item?id=48616439) : Why does a random app \(with no special permissions given to it\) get access to so much info, and why doesn't Apple tell users this \(important\) info? Why can't Apple make a long list of check boxes so users can dis/allow on a per-category and per-app basis? E.g. I had no idea a random app you install…
- [regecks](https://news.ycombinator.com/item?id=48614731) : Damn. The "iPhone last setup or erased on ..." is really nasty. What can a user really do about that? I feel like this should be fudged somehow by the OS.

---

[Article original](https://github.com/mysk-research/loupe) · [Discussion HN](https://news.ycombinator.com/item?id=48608645)
