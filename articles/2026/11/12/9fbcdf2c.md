---
article_fetched_at: '2026-11-12T17:27:23.813773Z'
attempts: 0
content_source: extracted
discussion_comment_count: 200
discussion_fetched_at: '2026-11-12T17:27:16.500310Z'
error: null
guid: https://news.ycombinator.com/item?id=50463899
hn_item_id: 50463899
hn_url: https://news.ycombinator.com/item?id=50463899
image_url: https://forums.spacebattles.com/data/svg/12/1/1794175159/sb_2022_favicon_192x192.png
is_ask_or_show_hn: false
llm_input_tokens: 13617
llm_latency_ms: 7521
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 866
our_published_at: '2026-11-12T17:16:10Z'
rewritten_title: Humble Bundle désactive la plupart de ses mesures de sécurité dans
  sa nouvelle version
source_published_at: '2026-11-12T06:52:48Z'
status: summarized
summarized_at: '2026-11-12T17:29:11.225713Z'
title: Humble Bundle just killed most of their security through vibecoding
url: https://forums.spacebattles.com/threads/humble-bundle-just-completely-killed-most-of-their-security-through-vibecoding.1346295/
---

## Résumé de l'article

Humble Bundle, plateforme de vente de jeux vidéo et de contenus numériques, a lancé une nouvelle version de son site qui supprime ou désactive de nombreuses protections de sécurité essentielles. L'authentification à deux facteurs a été supprimée, les changements de mot de passe et d'adresse e-mail ne nécessitent plus de confirmation, et la société a confié la sécurité à une entreprise spécialisée en IA.

- L'authentification à deux facteurs (2FA) n'existe plus ; le mot de passe reste la seule protection d'accès au compte
- Les utilisateurs peuvent modifier leur mot de passe sans entrer l'ancien mot de passe ni confirmer le nouveau, et changer d'adresse e-mail sans vérification de mot de passe
- En cas de compromission de compte, les utilisateurs ne reçoivent qu'une notification passive après la modification de l'e-mail
- La gestion de la sécurité a été confiée à une entreprise spécialisée en IA
- Des signalements indiquent que les paiements en un clic (illegal) seraient activés, bien que la confirmation reste à vérifier

## Discussion sur Hacker News (200 commentaires)

**Avis positifs** :
- Le problème révèle des failles de processus management : les décisions d'optimisation de coûts et les restructurations ont dépassé les considérations de sécurité et de qualité
- L'incident illustre l'importance cruciale du testing avant déploiement : les failles de sécurité basiques (absence de 2FA, confirmation de paiement) auraient été détectées avec un minimum de vérification
- Les modèles IA performants auraient probablement refusé ou flagué ces implémentations dangereuses ; le choix de modèles bon marché reflète une décision métier plutôt qu'une limitation technique
- Ce cas démontre pourquoi les architectures legacy bien documentées et testées restent préférables à des rewrites complètes sans préparation

**Avis négatifs** :
- L'attribution systématique aux LLM manque de preuves directes ; les mauvaises pratiques de sécurité existaient bien avant l'IA et peuvent simplement refléter l'incompétence humaine ou l'externalisation bon marché
- Blâmer le 'vibe coding' plutôt que la responsabilité managériale et humaine risque d'être une excuse commode : les décideurs gardent le contrôle final du déploiement
- Les LLMs sont des multiplicateurs (bons ou mauvais) mais pas des agents autonomes : la véritable cause est la décision humaine de ne pas revoir/tester avant de déployer, avec ou sans IA
- La critique des rewrites complètes serait valable même avec du code traditionnel ; c'est un problème d'ingénierie bien connu, pas une spécificité de l'IA
- Certains utilisateurs ont remarqué que la suppression de la 2FA par email répond à une demande réelle : elle était contraignante et certains services offrent des alternatives comme les magic links

**Top commentaires** :

- [oliwarner](https://news.ycombinator.com/item?id=50464874) : Weird that they lay all this at the feet of vibecoding. I've asked for authentication systems several times and they've tended to come with pretty good feature-sets. Perhaps it's because I know what I'm asking for. Edit: I've just tried to log in and it's failed through both Google and email. Whate…
- [trvz](https://news.ycombinator.com/item?id=50464542) : This is not AI's fault. In fact, they had to probably fight the LLM to get it this simple. I'm a subscriber to Humble Bundle Choice \(their monthly offering\), and it has been a pain to receive a code via email at every login.
- [1313ed01](https://news.ycombinator.com/item?id=50464574) : Can someone there please just click the rollback button now and we can all forget this ever happened. I don't think that new site can be saved. The old site was fine. Just leave it like it was. I bought a bundle as recently as last month. Three bundles I think. If they just focus on finding more fu…

---

[Article original](https://forums.spacebattles.com/threads/humble-bundle-just-completely-killed-most-of-their-security-through-vibecoding.1346295/) · [Discussion HN](https://news.ycombinator.com/item?id=50463899)
