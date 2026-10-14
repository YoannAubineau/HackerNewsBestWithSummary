---
article_fetched_at: '2026-10-14T00:45:30.117694Z'
attempts: 0
content_source: extracted
discussion_comment_count: 310
discussion_fetched_at: '2026-10-14T00:45:23.585534Z'
error: null
guid: https://news.ycombinator.com/item?id=50054092
hn_item_id: 50054092
hn_url: https://news.ycombinator.com/item?id=50054092
image_url: https://www.bleepstatic.com/content/hl-images/2026/10/12/Ledger.jpg
is_ask_or_show_hn: false
llm_input_tokens: 25079
llm_latency_ms: 14712
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1212
our_published_at: '2026-10-14T00:37:18Z'
rewritten_title: Ledger confirme qu'un implant espion sur ses portefeuilles a causé
  des vols de cryptomonnaies
source_published_at: '2026-10-12T10:09:37Z'
status: summarized
summarized_at: '2026-10-14T00:47:02.654136Z'
title: Ledger confirms spy chip implant behind wallet crypto thefts
url: https://www.bleepingcomputer.com/news/security/ledger-confirms-hardware-wallet-spy-implant-behind-crypto-thefts/
---

## Résumé de l'article

Ledger, fabricant de portefeuilles matériels de cryptomonnaies, a confirmé que des appareils distribués par le revendeur malaisien CryptoBilis contenaient un implant matériel non autorisé permettant de voler les fonds des utilisateurs. Cet implant capturait l'affichage et les entrées de l'appareil pour extraire la phrase de récupération, puis la transmettait à l'attaquant via une connexion LTE.

- Des chercheurs ont identifié deux versions de l'implant intégré dans les Ledger Nano X, utilisant un microcontrôleur STM32G431KBU6 et une eSIM pour communiquer
- L'implant était dissimulé sous la batterie ou le coussin d'affichage OLED, avec une batterie de rechange pour alimenter le matériel malveillant
- Ledger recommande aux utilisateurs ayant acheté via CryptoBilis de ne pas initialiser leur appareil et de transférer leurs actifs vers un nouveau portefeuille
- Le volume d'appareils compromis est décrit comme « limité » et tous les rapports de vols proviendraient de cette chaîne d'approvisionnement
- Ledger conseille d'acheter uniquement auprès de revendeurs autorisés, tout en reconnaissant que sa vérification d'authenticité ne peut pas détecter les implants ajoutés

## Discussion sur Hacker News (310 commentaires)

**Avis positifs** :
- Les attaques supposément théoriques ou paranoïaques deviennent réelles : les implants matériels eSIM avec OCR sur les écrans d'affichage démontrent que les menaces longtemps jugées farfelues se concrétisent quand les enjeux financiers sont suffisants.
- Les schémas multisig avec portefeuilles de différents fabricants auraient dû être l'approche par défaut : plutôt qu'un seul portefeuille matériel, utiliser 2-of-2 ou 3-of-3 avec des vendeurs différents rend les attaques ciblées sur un seul fabricant inefficaces.
- Les portefeuilles matériels spécialisés sont des cibles juteuses et prévisibles : contrairement aux iPhone génériques, chaque Ledger est utilisé pour de la crypto, ce qui les rend beaucoup plus attractifs pour les attaques en chaîne d'approvisionnement.
- La prévention des attaques matérielles dès la conception était possible : des mesures anti-effraction, de la résine époxy, ou une meilleure isolation du bus d'affichage auraient considérablement compliqué cette attaque.
- Cet incident révèle pourquoi les systèmes financiers traditionnels imposent autant de réglementation : la réversibilité des transactions, les assurances et la responsabilité légale des institutions fournissent une protection que la crypto ne peut pas offrir.

**Avis négatifs** :
- Les attaques matérielles sophistiquées ne sont pas nouvelles : les gouvernements les pratiquent depuis des décennies (Cisco, pagers pour le Hamas). Ce qui change, c'est que les criminels ordinaires les utilisent maintenant, attirés par les profits massifs de la crypto, pas que la menace soit théorique.
- Un portefeuille matériel reste plus sûr qu'une application logicielle : malgré cet incident, les portefeuilles matériels ont subi moins de vols que les portefeuilles logiciels ou de garde, et cette attaque suppose un accès à la chaîne d'approvisionnement.
- La complexité du multisig dépasse la capacité de l'utilisateur moyen et crée d'autres risques : exiger 48 mots au lieu de 24, gérer trois portefeuilles différents et trois emplacements sécurisés augmente les erreurs utilisateur et la perte accidentelle de fonds.
- Les institutions financières traditionnelles présentent aussi des risques similaires : les données bancaires fuient régulièrement, les comptes se ferment sans recours valable, et les transferts internationaux échouent fréquemment sans compensation.
- Potentialiser le portefeuille en résine époxy ne résout pas fondamentalement le problème : avec suffisamment d'incitations financières, les attaquants peuvent contourner ou retirer l'époxy, et cela empêcherait les utilisateurs de vérifier l'intégrité du dispositif.

**Top commentaires** :

- [TacticalCoder](https://news.ycombinator.com/item?id=50046048) : No matter whether you like or hate or don't care about cryptocurrencies, this is incredible stuff... Now basically: every single attack that's been described as "theoretical" or "far-fetched" or "only existing in the mind of a paranoid person" did actually happen. We're talking here about a tiny eS…
- [cowlevel](https://news.ycombinator.com/item?id=50069828) : Not mentioned in article: MediaMarkt, the German equivalent of Best Buy, was selling these compromised devices on store shelves in every city in Germany.
- [megous](https://news.ycombinator.com/item?id=50069899) : The technique is so coool. I mean taping the screen output on the way to the display to get around having to hack the secure element. :\)

---

[Article original](https://www.bleepingcomputer.com/news/security/ledger-confirms-hardware-wallet-spy-implant-behind-crypto-thefts/) · [Discussion HN](https://news.ycombinator.com/item?id=50054092)
