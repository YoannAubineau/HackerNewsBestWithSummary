---
article_fetched_at: '2026-10-06T20:41:10.784190Z'
attempts: 0
content_source: extracted
discussion_comment_count: 239
discussion_fetched_at: '2026-10-06T20:41:09.013586Z'
error: null
guid: https://news.ycombinator.com/item?id=49977588
hn_item_id: 49977588
hn_url: https://news.ycombinator.com/item?id=49977588
image_url: https://www.techdirt.com/wp-content/themes/techdirt/assets/images/td-rect-logo-white.png
is_ask_or_show_hn: false
llm_input_tokens: 22244
llm_latency_ms: 14180
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1023
our_published_at: '2026-10-06T20:29:59Z'
rewritten_title: Meta's Muse révèle de graves failles de sécurité et d'accès aux données
  personnelles
source_published_at: '2026-10-06T12:45:49Z'
status: summarized
summarized_at: '2026-10-06T20:42:29.553981Z'
title: Meta’s Muse is an adorable privacy and security dumpster fire
url: https://www.techdirt.com/2026/10/06/metas-muse-is-an-adorable-privacy-and-security-dumpster-fire/
---

## Résumé de l'article

Muse est un agent IA généraliste de Meta, lancé récemment avec un avatar animé nommé Jolly, censé automatiser des tâches comme les réservations de restaurant ou les paiements. Malgré les promesses de Meta sur la sécurité et la confidentialité, le produit a connu plusieurs semaines tumultueuses marquées par des failles critiques.

- Un zéro-day permettait d'espionner les utilisateurs Mac ; l'application accède aux messages privés sans permission et les télécharge sur le cloud, même quand l'utilisateur refuse explicitement.
- Un chercheur a découvert comment donner accès root en usurpant l'identité de l'agent Muse lui-même.
- Une démonstration YouTube a montré que Muse vendait des articles bien en dessous de leur valeur et divulguait l'adresse personnelle de l'utilisateur.
- Muse crée des profils détaillés de tous les contacts de l'utilisateur (amis, famille, collègues) et collecte massivement des données depuis les emails, calendriers et comptes financiers.
- Des sources internes révèlent que Meta a bâclé les correctifs de sécurité pour respecter le calendrier de lancement, avec des ingénieurs craignant une fuite massive de données.

## Discussion sur Hacker News (239 commentaires)

**Avis positifs** :
- Muse offre certaines capacités techniques intéressantes (modèle performant, interface soignée, prix compétitif) et des cas d'usage légitimes existent si l'utilisateur garde le contrôle strict (comparaison de prix, planification sans transactions réelles, gestion de tâches locales).
- L'architecture de Muse est relativement transparente comparée à d'autres agents : elle révèle son système de prompts, permet l'inspection des fichiers de mémoire, et fonctionne dans une VM isolée où l'utilisateur a techniquement un contrôle théorique.
- Les agents IA pourraient avoir des usages positifs légitimes (récupération de souvenirs oubliés, assistance sur des tâches complexes, automatisation de tâches administratives pénibles) s'ils étaient conçus et régulés correctement.

**Avis négatifs** :
- Meta a un antécédent documenté de violations de confidentialité répétées, d'exploitation de données à grande échelle, et de manque de respect pour les limites utilisateur, rendant l'idée de lui confier accès complet à ses données et transactions personnelles intrinsèquement dangereuse.
- Même avec des garde-fous techniques, les LLM restent imprévisibles et commetent erreurs graves (vente d'articles à prix rikdicules, envoi d'argent par erreur, divulgation accidentelle d'informations sensibles) sans recours ni responsabilité légale claire de Meta.
- Le modèle économique des grandes tech (Meta, Google, OpenAI) repose fondamentalement sur l'extraction et la monétisation de données personnelles ; confier un agent autonome à une telle entreprise revient à automatiser l'espionnage consentement et à amplifier les manipulations comportementales.
- L'absence de véritable consentement éclairé : les utilisateurs moyens ne comprennent pas les permissions qu'ils accordent, Meta encourage activement le partage complet de données sans explication claire, et les contacts d'un utilisateur qui installent Muse compromettent la confidentialité de l'utilisateur sans son accord.
- La solution évidente (sandbox strictes, permissions limitées, garanties financières, régulation) ne sera jamais implémentée volontairement par Meta car elle réduirait la valeur d'extraction des données ; seule la régulation gouvernementale contraignante pourrait forcer un vrai changement.

**Top commentaires** :

- [piazz](https://news.ycombinator.com/item?id=49979930) : I’m pretty frustrated with Muse and the last thing I want to be doing with my free time is defending Meta, but this is such clickbait. Point by point: \> “OMG you can jailbreak it and get it to spill its VM” This is the whole point; any content on the VM is yours. It runs in an isolated sandboxed VM…
- [jagermo](https://news.ycombinator.com/item?id=49978280) : I get the appeal of agents, I do. This is the future stuff we always wanted. But I cannot get myself to give one of these things access to my bank account or allow it to do price comparsion and shopping without oversight. Or access to my email or chat history. I just do not trust any of them, not w…
- [chadd](https://news.ycombinator.com/item?id=49979245) : It's very simple. There is ZERO chance the worlds biggest advertising companies will refrain, long-term, from using your most intimate secrets, gathered through your many conversations with their AI personal assistants, to sell you things.

---

[Article original](https://www.techdirt.com/2026/10/06/metas-muse-is-an-adorable-privacy-and-security-dumpster-fire/) · [Discussion HN](https://news.ycombinator.com/item?id=49977588)
