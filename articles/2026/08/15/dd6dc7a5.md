---
article_fetched_at: '2026-08-15T03:31:27.590020Z'
attempts: 0
content_source: extracted
discussion_comment_count: 101
discussion_fetched_at: '2026-08-15T03:31:26.283248Z'
error: null
guid: https://news.ycombinator.com/item?id=49300759
hn_item_id: 49300759
hn_url: https://news.ycombinator.com/item?id=49300759
image_url: https://rustdesk.com/_astro/unattended-remote-access-wayland-og.BOcMxzVY_212cpk.webp
is_ask_or_show_hn: false
llm_input_tokens: 8308
llm_latency_ms: 9300
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 884
our_published_at: '2026-08-15T03:26:16Z'
rewritten_title: RustDesk ajoute l'accès distant sans surveillance sur Wayland avec
  support multi-moniteurs
source_published_at: '2026-08-14T16:12:52Z'
status: summarized
summarized_at: '2026-08-15T03:32:00.674573Z'
title: RustDesk now supports true unattended remote access on Wayland
url: https://rustdesk.com/blog/unattended-remote-access-wayland/
---

## Résumé de l'article

RustDesk, un logiciel libre d'accès distant, prend désormais en charge l'accès sans surveillance véritable sur le serveur d'affichage Wayland de Linux. Cela signifie qu'on peut se connecter à distance même quand personne n'est présente à la machine distante, y compris depuis l'écran de connexion après redémarrage, contrairement à ce qui était requis auparavant.

- RustDesk propose une version preview pour les systèmes x86_64 Debian/Ubuntu avec support Wayland et multi-moniteurs, tandis que ses concurrents (AnyDesk, TeamViewer) ne supportent que Xorg ou offrent un support Wayland expérimental
- L'accès sans surveillance fonctionne après la configuration initiale sans nécessiter d'approbation à chaque session
- Cette implémentation reste en testing avant de devenir la version par défaut, avec un déploiement futur planifié sur Fedora, Arch Linux et dans les versions standard de RustDesk
- Les utilisateurs de Wayland, particulièrement avec plusieurs écrans, sont invités à tester la preview et signaler les problèmes rencontrés

## Discussion sur Hacker News (101 commentaires)

**Avis positifs** :
- RustDesk offre de meilleures performances que VNC grâce aux codecs vidéo modernes et à la compression temporelle, rendant l'accès distant plus fluide et réactif
- Solution open source avec possibilité d'auto-hébergement du serveur, évitant la dépendance à des services tiers propriétaires et l'enshittification observée chez TeamViewer/AnyDesk
- Fonctionne sans besoin d'ouvrir de ports ni de VPN complexe, utilisant un système de relay peer-to-peer qui simplifie la configuration pour les utilisateurs
- Support de l'accès sans surveillance sur Wayland résout enfin un problème technique majeur, permettant un contrôle distant complet du système même au login
- Communauté active et amélioration continue du logiciel, avec des utilisateurs rapportant une utilisation satisfaisante depuis plusieurs années

**Avis négatifs** :
- Préoccupations de sécurité sérieuses : la base de code utilise SHA-256 au lieu de fonctions dérivation de clés (Argon2), comporte des commentaires alarmants sur les fallbacks non-sécurisés et repose sur un protocole personnalisé mal documenté
- Les connexions directes sur réseau local ne sont pas chiffrées par défaut, et les développeurs refusent d'implémenter le chiffrement pour ce cas d'usage courant
- Le projet souffre de problèmes de gouvernance et de dépendances à des sous-modules sans licence, ce qui place RustDesk dans une zone grise entre logiciel libre et propriétaire
- Problèmes de performance rapportés : consommation CPU excessive (800-1200%) et utilisation GPU (8-10%) sur certaines configurations, certains utilisateurs préférant TightVNC
- Fonctionnalités manquantes par rapport aux solutions propriétaires : pas de support pour la passthrough du microphone et absence de client web auto-hébergé

**Top commentaires** :

- [inktype](https://news.ycombinator.com/item?id=49302135) : RustDesk still does not support encrypted connections when self hosting: https://github.com/rustdesk/rustdesk/issues/3714
- [OsrsNeedsf2P](https://news.ycombinator.com/item?id=49305619) : Rustdesk is amazing. I was using it just 2 days ago and ran into this hiccup, so it's a pleasure to see it resolved
- [throwaway27448](https://news.ycombinator.com/item?id=49301811) : What is rustdesk and how is it distinct from vnc? Edit: i appreciate the explanations; thank you.

---

[Article original](https://rustdesk.com/blog/unattended-remote-access-wayland/) · [Discussion HN](https://news.ycombinator.com/item?id=49300759)
