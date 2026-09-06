---
article_fetched_at: '2026-09-06T20:58:03.256246Z'
attempts: 0
content_source: extracted
discussion_comment_count: 144
discussion_fetched_at: '2026-09-06T20:58:01.648740Z'
error: null
guid: https://news.ycombinator.com/item?id=49586698
hn_item_id: 49586698
hn_url: https://news.ycombinator.com/item?id=49586698
image_url: https://www.phoronix.net/image.php?id=2026&image=m3_macs
is_ask_or_show_hn: false
llm_input_tokens: 9989
llm_latency_ms: 9138
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 766
our_published_at: '2026-09-06T20:18:10Z'
rewritten_title: Asahi Linux officialise le support des Mac Apple M3 avec des limitations
source_published_at: '2026-09-06T14:08:59Z'
status: summarized
summarized_at: '2026-09-06T20:58:36.668215Z'
title: Asahi Linux Now Officially Supports Apple M3 Macs – With Caveats
url: https://www.phoronix.com/news/Asahi-Linux-Official-M3
---

## Résumé de l'article

Asahi Linux, une distribution Linux pour les Mac à processeur Apple Silicon, annonce le support officiel des Macs M3 avec des fonctionnalités comparables aux générations M1 et M2, mais avec des restrictions significatives.

- Le support GPU reste incomplet : pas d'accélération 3D performante ni efficace énergétiquement pour le moment
- La veille système et les ports HDMI ne fonctionnent pas faute de support DCP (Display Coprocessor)
- Le support couvre tous les appareils Apple M3 sauf le Mac Studio M3 Ultra
- L'intégration upstream dans Linux kernel est en cours avec support de base présent, mais l'équivalent fonctionnel complet n'est attendu qu'à partir de Linux 7.4+

## Discussion sur Hacker News (144 commentaires)

**Avis positifs** :
- L'équipe Asahi accomplit un travail remarquable et impressionnant en rétro-ingéniérant le silicium personnalisé d'Apple sans documentation officielle, comparable à réparer une fusée en vol.
- Le matériel Apple Silicon offre des performances et une efficacité énergétique supérieures, justifiant l'intérêt de le supporter sous Linux pour ceux qui veulent exploiter ce potentiel.
- Apple laisse techniquement la porte ouverte pour installer d'autres OS (contrairement à ce qui serait trivial à bloquer), et a même apporté des modifications pour rendre Asahi plus robuste selon certains contributeurs.
- Le projet répond à un besoin réel : certains utilisateurs veulent utiliser du matériel haute performance sans être limités à macOS, et Asahi fonctionne déjà raisonnablement bien sur M1/M2 pour des cas d'usage comme les jeux via Steam.

**Avis négatifs** :
- Apple ne fournit pas de documentation technique contrairement aux concurrents Intel et AMD qui contribuent activement aux drivers Linux, ce qui force Asahi à faire du travail de rétro-ingénierie chronophage et inefficace.
- Le support reste incomplet et fragile : pas de Thunderbolt, DisplayPort instable, gestion du sommeil dysfonctionnelle, et chaque nouvelle génération de puce M requiert un reverse-engineering complet car les spécifications changent constamment.
- Le marché cible d'Asahi est minuscule comparé à l'effort d'ingénierie requis, et la plupart des utilisateurs pourraient simplement utiliser UTM (virtualisation native) pour exécuter Linux sans ces complications.
- Apple ne partage probablement pas les specs par intérêt commercial : maintenir l'écosystème fermé force les utilisateurs à rester dans macOS et renforce l'adoption de l'écosystème Apple global (services, iCloud, etc.).

**Top commentaires** :

- [JLO64](https://news.ycombinator.com/item?id=49587272) : Here's the blog post from the Asahi devs announcing this: https://asahilinux.org/2026/09/m2-episode-1/
- [Krish1577](https://news.ycombinator.com/item?id=49586741) : Reverse-engineering Apple's custom silicon is basically the modern equivalent of repairing a spaceship while it's actively launching. Incredible work by the Asahi team!
- [sansah](https://news.ycombinator.com/item?id=49587112) : Lack of sleep and HDMI support is real roadblock for adoption. Hope they gets past soon.

---

[Article original](https://www.phoronix.com/news/Asahi-Linux-Official-M3) · [Discussion HN](https://news.ycombinator.com/item?id=49586698)
