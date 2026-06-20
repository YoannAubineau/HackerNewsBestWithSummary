---
article_fetched_at: '2026-06-20T14:44:57.279757Z'
attempts: 0
content_source: extracted
discussion_comment_count: 79
discussion_fetched_at: '2026-06-20T14:44:55.837383Z'
error: null
guid: https://news.ycombinator.com/item?id=48606619
hn_item_id: 48606619
hn_url: https://news.ycombinator.com/item?id=48606619
is_ask_or_show_hn: false
llm_input_tokens: 6786
llm_latency_ms: 11429
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1011
our_published_at: '2026-06-20T14:37:50Z'
rewritten_title: Comment stocker un site web entier dans un favicon d'une page
source_published_at: '2026-06-20T05:33:59Z'
status: summarized
summarized_at: '2026-06-20T14:45:47.269694Z'
title: I Stored a Website in a Favicon
url: https://www.timwehrle.de/blog/i-stored-a-website-in-a-favicon/
---

## Résumé de l'article

Tim Wehrle a créé une preuve de concept où un favicon (petite icône d'onglet) contient le code HTML complet d'un site web, encodé directement dans les pixels de l'image PNG. Le favicon de 9×9 pixels (81 pixels, soit 243 octets de capacité) stocke 208 octets de contenu HTML avec un en-tête de 4 octets, et un script JavaScript bootstrap décode et affiche le contenu en lisant les canaux RGB de l'image via l'API Canvas.

- Chaque pixel PNG stocke trois octets (canaux rouge, vert, bleu) ; le texte UTF-8 du HTML y est écrit directement, créant une image visuelle de bruit aléatoire
- Le processus comporte deux étapes : l'encodage prépend quatre octets indiquant la longueur du contenu, puis remplissent les pixels ; le décodage inverse lit les pixels via Canvas et reconstruit le HTML original
- Le favicon n'occupe que 9×9 pixels (87 % d'utilisation), bien plus petit qu'une icône de favicon standard, mais nécessite un chargeur JavaScript pour fonctionner
- Bien que techniquement fonctionnel, cette approche n'a aucune utilité pratique comparée aux méthodes ordinaires de distribution d'HTML, mais illustre comment repousser les limites des formats standards
- Des alternatives existent : SVG en favicon, blocs de commentaires PNG (tEXt, zTXt, iTXt) ou format ICO multi-résolution

## Discussion sur Hacker News (79 commentaires)

**Avis positifs** :
- Concept créatif et exploratoire : démonstration ingénieuse de ce qu'il est possible de faire avec les contraintes techniques du web, explorant les limites de manière ludique et curieuse.
- Alternatives techniques intéressantes : plusieurs approches (SVG avec données encodées, fichiers PNG avec chunks de commentaires, polyglots HTML/PNG, QR codes avec WebAssembly) offrent des voies d'exploration encore plus pratiques ou efficaces.
- Potentiel de contournement et de détournement : possibilité d'utiliser le cache favicon pour contourner les blocages, les restrictions de vie privée ou créer de nouveaux vecteurs de stockage inattendus.
- Respecte le temps du lecteur : style d'écriture direct et concis qui va à l'essentiel, apprécié par certains lecteurs pour son efficacité communicationnelle.
- Inspiration pour d'autres projets : exemples concrets de jeux en favicons (Snake, Doom, Pong) montrant que le concept peut être poussé plus loin.

**Avis négatifs** :
- Préoccupations de sécurité et de vie privée : le cache favicon persistent peut être exploité pour le suivi transfrontalier, le fingerprinting et la contournement du mode incognito, des risques importants insuffisamment adressés.
- Aucune utilité pratique réelle : manque de cas d'usage concrets justifiant cette approche par rapport aux solutions standards existantes (URL, stockage normal, etc.).
- Style d'écriture saccadé difficile à lire : phrases très courtes, structure hachurée et hachée qui ressemble à du contenu généré par IA, réduisant l'accessibilité malgré les bonnes intentions.
- Complexité injustifiée : ajouter une couche de décodage pour seulement 208 bytes alors que des solutions plus simples existent (servir directement le HTML comme favicon, utiliser des chunks PNG standard).
- Charge de travail du navigateur : nécessité d'un script de bootstrap pour décoder, sans gains évidents par rapport aux approches plus directes ou aux formats de fichiers existants.

**Top commentaires** :

- [Tepix](https://news.ycombinator.com/item?id=48606876) : Instead of going via pixels, why not use a SVG favicon and directly store markup inside it and extract it? Use this favicon.svg: \<svg xmlns="http://www.w3.org/2000/svg"\> \<circle cx="50%" cy="50%" r="50%" fill="orange"/\> \<p\>hello HN!\</p\> \</svg\> use this in your \<head\> to use a svg favicon: \<link id=…
- [divvsaxena](https://news.ycombinator.com/item?id=48609552) : This is one of those projects that's completely impractical but makes the web more interesting. I love seeing people explore weird constraints just to see what's possible.
- [Retr0id](https://news.ycombinator.com/item?id=48608772) : « You still need a tiny bootstrap loader to decode the image. » Nope, you can do it all in a single file with an html/png polyglot \(and nowadays you can get better compression ratios with newer formats like webp\). https://web.archive.org/web/20120801001616/http://daeken.com...

---

[Article original](https://www.timwehrle.de/blog/i-stored-a-website-in-a-favicon/) · [Discussion HN](https://news.ycombinator.com/item?id=48606619)
