---
article_fetched_at: '2026-06-17T15:03:51.096095Z'
attempts: 0
content_source: extracted
discussion_comment_count: 78
discussion_fetched_at: '2026-06-17T15:03:50.276330Z'
error: null
guid: https://news.ycombinator.com/item?id=48563394
hn_item_id: 48563394
hn_url: https://news.ycombinator.com/item?id=48563394
is_ask_or_show_hn: false
llm_input_tokens: 9997
llm_latency_ms: 12871
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1030
our_published_at: '2026-06-17T14:40:57Z'
rewritten_title: Techniques pour identifier et exploiter les vulnérabilités des serveurs
  IIS en bug bounty
source_published_at: '2026-06-16T22:53:34Z'
status: summarized
summarized_at: '2026-06-17T15:04:44.556536Z'
title: Humiliating IIS servers for fun and jail time
url: https://mll.sh/humiliating-iis-servers-for-fun-and-jail-time/
---

## Résumé de l'article

Cet article détaille les méthodes de reconnaissance et d'exploitation des serveurs Internet Information Services (IIS), le serveur web Microsoft souvent mal configuré. L'auteur guide les testeurs de sécurité à travers les étapes de découverte, d'énumération et d'accès non autorisé aux ressources sensibles.

- **Découverte des serveurs IIS** : utiliser Shodan, Google Dorks (recherche de fichiers typiques IIS comme aspnet_client ou _vti_bin) et l'analyse active des en-têtes HTTP (Server: Microsoft-IIS, X-Powered-By: ASP.NET)
- **Énumération des hôtes virtuels** : exploiter les certificats SSL et brute-forcer les noms d'hôte lorsque le serveur retourne une erreur HTTPAPI 2.0 générique
- **Énumération des noms courts (tilde)** : exploiter l'héritage du format DOS 8.3 avec des outils comme shortscan pour découvrir des fichiers et répertoires cachés, puis résoudre les noms complets via GitHub ou BigQuery
- **Accès aux fichiers critiques** : localiser web.config (contenant les clés de chiffrement pour RCE via ViewState), exploiter les traversées de répertoires, utiliser les sessions sans cookie pour accéder aux DLL du répertoire bin
- **Contournement des protections** : exploiter les différences de normalisation de chemins entre proxies et IIS, contourner les filtres d'upload avec des variantes d'extensions (.cer, .svg, .xsl) et des points finaux (.aspx.), utiliser la pollution de paramètres HTTP (HPP) pour contourner les WAF

## Discussion sur Hacker News (78 commentaires)

**Avis positifs** :
- Les honeypots avec IIS sont une tactique légitime pour gaspiller le temps des attaquants et collecter de l'intelligence en sécurité
- L'obscurité est une couche de sécurité valide en complément d'autres mesures, pas en remplacement, suivant une stratégie en profondeur (masquage + prévention + préparation)
- IIS reste massivement utilisé dans les environnements d'entreprise, administrations et secteur public pour l'intranet et applications métier legacy, particulièrement avec Active Directory et domaines Windows
- L'article offre un excellent contenu de reconnaissance et pentesting sur IIS avec des références d'outils pertinentes et peu de filler, malgré sa présentation discutable
- Ces techniques de reconnaissance/exploitation sur IIS restent pertinentes aujourd'hui car les vulnerabilités DOS 8.3, traversal directory et serveurs mal configurés demeurent courants

**Avis négatifs** :
- Sans être en plage IP d'une organisation établie, les honeypots IIS ne reçoivent que du trafic bot générique ; les vrais attaquants ciblent les gros acteurs ou cherchent des 0-days, pas des cibles aléatoires
- Ces techniques de reconnaissance sont vieilles de 20+ ans (début 2000s) et relèvent du script kiddie plutôt que d'une contribution innovante à la sécurité
- L'article semble généré ou très fortement édité par IA (style Claude), ce qui dilue la valeur d'une vraie expertise humaine et crée une fatigue communautaire autour du flagging LLM
- Le ton léger du titre sur 'humilier pour le plaisir et la prison' est trompeur : l'auteur prétend faire du bug bounty légal, mais cela normalise des comportements abusifs gratuits sans justification
- La mise en page a des problèmes d'affichage sérieux sur plusieurs navigateurs (sidebar chevauchant le contenu principal)

**Top commentaires** :

- [naturalmovement](https://news.ycombinator.com/item?id=48563989) : I front all my honeypots with the IIS landing page precisely because it attracts black hat jagoffs. Nothing makes me happier than knowing I've wasted hours of their time chasing their own tails.
- [Lammy](https://news.ycombinator.com/item?id=48564622) : « IIS has a legacy behavior inherited from the old DOS 8.3 filename convention. » Is this exposing the underlying OS's behavior coupled with the fact that the IIS document root is \`C:\\Inetpub\` by default? Eight-dot-three filenames are enabled by default on the C drive but disabled by default on all…
- [xmcp123](https://news.ycombinator.com/item?id=48568858) : Oh man this takes me back. Once upon a time, all server logs were basically unusable because of the amount of IIS scanners out there. There was a directory traversal that was literally just url encoding “../“ that absolutely lit the internet on fire for many months.

---

[Article original](https://mll.sh/humiliating-iis-servers-for-fun-and-jail-time/) · [Discussion HN](https://news.ycombinator.com/item?id=48563394)
