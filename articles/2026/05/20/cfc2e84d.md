---
article_fetched_at: '2026-05-20T21:33:36.183825Z'
attempts: 0
content_source: extracted
discussion_comment_count: 193
discussion_fetched_at: '2026-05-20T21:33:34.992572Z'
error: null
guid: https://news.ycombinator.com/item?id=48204770
hn_item_id: 48204770
hn_url: https://news.ycombinator.com/item?id=48204770
image_url: https://res.cloudinary.com/railway/image/upload/v1734405679/incident-hero_ri6qfy.png
is_ask_or_show_hn: false
llm_input_tokens: 14345
llm_latency_ms: 11784
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1015
our_published_at: '2026-05-20T21:30:40Z'
rewritten_title: Railway subit une panne de huit heures après suspension incorrecte
  de son compte Google Cloud
source_published_at: '2026-05-20T08:37:55Z'
status: summarized
summarized_at: '2026-05-20T21:34:01.298257Z'
title: 'Incident Report: May 19, 2026 – GCP Account Suspension'
url: https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage
---

## Résumé de l'article

Railway, plateforme de déploiement d'applications, a connu une interruption de service de huit heures le 19 mai 2026 après que Google Cloud ait suspendu par erreur son compte de production. Cette suspension a désactivé l'API, le tableau de bord et l'infrastructure réseau de Railway hébergée sur GCP, et la cascade d'effets s'est étendue aux workloads sur d'autres plateformes (AWS, Railway Metal) lorsque les caches de routage ont expiré.

- Google Cloud a placé le compte de production de Railway en suspension à 22:20 UTC le 19 mai, affectant le contrôle plane, l'API, le tableau de bord et les disques persistants.
- L'outage s'est propagé au-delà de GCP : les proxies edge de Railway dépendaient d'une API de contrôle plane hébergée sur GCP pour peupler les tables de routage ; à l'expiration du cache, tous les workloads, y compris ceux sur AWS et Railway Metal, ont commencé à retourner des erreurs 404.
- La récupération a duré plusieurs heures en raison de la nécessité de restaurer séparément les disques persistants (23:54 UTC), les instances de calcul et le réseau (01:30 UTC), suivi d'une limitation de débit involontaire de GitHub sur les webhooks de Railway.
- Railway reconnaît une dépendance architecturale critique : l'API de contrôle plane était un point de défaillance unique hébergé uniquement sur GCP, malgré un réseau maillé entre les trois plateformes.
- L'entreprise s'engage à éliminer cette dépendance en étendant les shards de base de données haute disponibilité à AWS et Metal, et en retirant les services GCP du chemin critique du plan de données.

## Discussion sur Hacker News (193 commentaires)

**Avis positifs** :
- Railway a pris ses responsabilités en reconnaissant que le choix d'architecture de dépendre de GCP était une erreur de leur part, au lieu de rejeter entièrement la faute sur Google
- Google a restauré l'accès au compte en 19 minutes, ce qui est une réaction relativement rapide pour une situation critique
- Le rapport d'incident de Railway est transparent et détaillé, montrant une approche professionnelle avec des mesures préventives concrètes pour éviter que cela se reproduise
- Les commentateurs reconnaissent que la conclusion de Railway de réduire la dépendance à GCP et de construire une architecture multi-cloud est une leçon architecturale importante
- DigitalOcean, Fly.io et d'autres alternatives émergeantes offrent des options viables pour les équipes cherchant à éviter les fournisseurs cloud hyperscale

**Avis négatifs** :
- Google a suspendu un compte client payant de plusieurs millions de dollars sans explication, confirmant un problème systémique de Google à bannir des comptes sans justification ou processus d'escalade humain
- Google n'a jamais expliqué publiquement pourquoi le compte a été suspendu, rendant impossible pour Railway de comprendre et prévenir une récurrence
- Le problème révèle la fragilité fondamentale de dépendre d'une plateforme cloud unique ; même Azure et AWS peuvent avoir des défaillances et des actions automatisées désastreuses
- Google a un historique décennal bien documenté de suspensions arbitraires sans recours, ce qui rend impossible de faire confiance à leurs services pour des opérations critiques
- Les ressources critiques de Railway restaient arrêtées pendant 4-6 heures après la restauration du compte, ce qui montre que le problème était bien plus profond qu'une simple restauration d'accès rapide

**Top commentaires** :

- [shwetanshu21](https://news.ycombinator.com/item?id=48211739) : This should be a warning to anyone running GCP. They suspend accounts left right and centre without even thinking about what they're doing. It seems like they use Gemini 3.1 Pro to run their production decisions. TK has a history of absolutely destroying the culture of the place like in OCI and has…
- [Animats](https://news.ycombinator.com/item?id=48211323) : "Finally, we are in planning to remove Google Cloud services from our data plane’s hot path, and keeping them only for secondary/failover." That's pretty clear. Google can no longer be trusted as a B2B service provider.
- [tcdent](https://news.ycombinator.com/item?id=48211589) : The interesting and yet-to-be-explained part is why google flagged the account? Put all the timestamps you want in the post mortem about what you observed, but you haven't addressed the root cause. The "this doesn't make sense" part of the story likely has a real explanation that nobody wants to re…

---

[Article original](https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage) · [Discussion HN](https://news.ycombinator.com/item?id=48204770)
