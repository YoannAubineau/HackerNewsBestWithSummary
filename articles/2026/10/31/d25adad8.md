---
article_fetched_at: '2026-10-31T14:05:07.497612Z'
attempts: 0
content_source: extracted
discussion_comment_count: 49
discussion_fetched_at: '2026-10-31T14:04:57.868105Z'
error: null
guid: https://news.ycombinator.com/item?id=50305637
hn_item_id: 50305637
hn_url: https://news.ycombinator.com/item?id=50305637
image_url: https://opengraph.githubassets.com/ad187d0f5f0784218e12b5da38c1f46ee6af6c01cc94238a9307bd9153dc60aa/kevinraymond/florilegium
is_ask_or_show_hn: false
llm_input_tokens: 8467
llm_latency_ms: 7987
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 877
our_published_at: '2026-10-31T13:43:49Z'
rewritten_title: 'Florilegium : des fleurs procédurales générées en Lua pour les marges
  LaTeX'
source_published_at: '2026-10-30T15:48:12Z'
status: summarized
summarized_at: '2026-10-31T14:06:21.201407Z'
title: 'Florilegium: Procedural Flowers in LaTeX'
url: https://github.com/kevinraymond/florilegium
---

## Résumé de l'article

Florilegium est un package LaTeX qui génère procéduralement des ornements floraux Delft-bleu dans les marges des documents. Chaque pétale, feuille et tige est une courbe paramétrée calculée en Lua durant la composition et écrite directement dans le PDF, sans images ni ressources externes.

- Le jardin s'adapte au texte : la composition croît en remplissant l'espace libre de manière déterministe selon le numéro de page, avec des motifs peints comme à l'aquarelle (fonds, contours, veines blanches).
- Deux thèmes alternatifs disponibles : un thème géométrique utilisant des formes plates, et un thème mathématique affichant des figures mathématiques (fractales, courbes, polyèdres) qui s'adaptent également à l'espace.
- Options de contrôle : densité (quantité d'ornements), intensité (opacité), saisons (évolution du printemps à l'automne), et visiteures (papillons, abeilles, escargots, oiseaux).
- Fonctionnalités intégrées : initiales décorées avec vigne entrelacée, fleurs aux sections, fleurs à la demande dans le texte, et marges miroir pour documents recto-verso.
- Version PostScript autonome incluse : le même code porté en PostScript pur fonctionne avec Ghostscript sans dépendre de TeX.

## Discussion sur Hacker News (49 commentaires)

**Avis positifs** :
- La beauté visuelle et technique du projet inspire les utilisateurs, avec de nombreux éloges sur l'esthétique des fleurs générées procéduralement
- L'utilisation créative de Lua dans LaTeX/PDF pour créer des animations ouvre de nouvelles possibilités insoupçonnées dans la typographie
- Le projet ravive l'esprit original de Knuth : utiliser les outils disponibles pour créer de la beauté documentaire, indépendamment de la méthode
- Le caractère procédural permet des variantes uniques à chaque compilation, enrichissant l'expérience du lecteur à travers différentes impressions
- Le nom 'florilegium' s'avère particulièrement pertinent, unissant l'allusion savante au concept littéraire et la métaphore florale du projet

**Avis négatifs** :
- La génération du README et une grande partie du code par IA est perçue comme manquant d'authenticité et de clarté pédagogique par rapport aux efforts artisanaux humains
- Le style d'écriture générée par IA est reconnaissable et gênant, avec un rythme saccadé caractéristique des LLM
- Le projet perd de son impact comparé à la version originale Reddit qui l'a inspiré, selon certains commentaires
- Utiliser l'IA pour ce projet contredit l'héritage de craftsmanship que représentait traditionnellement la typographie TeX, bien que cet argument soit contesté
- Préoccupations éthiques concernant l'appropriation d'une idée originale d'un utilisateur Reddit qui préférait garder son travail privé

**Top commentaires** :

- [lkm0](https://news.ycombinator.com/item?id=50308813) : In the same vein, a few years ago, somebody implemented procedural decorations for a recreation of Byrne's "Elements of Euclid" in LaTeX: https://github.com/jemmybutton/byrne-euclid \(bottom of the readme\)
- [kjraym](https://news.ycombinator.com/item?id=50314259) : I was recently made aware that my repo was mentioned here \(thanks nanna\). Thanks for posting your thoughts, either way you go - I respect your opinions. On the Reddit post \(https://www.reddit.com/r/LaTeX/comments/1xixznw/how\_do\_you\_m...\), I promised I would share the process I used to create the v1…
- [archermarks](https://news.ycombinator.com/item?id=50308704) : Gorgeous but the AI text is so grating.

---

[Article original](https://github.com/kevinraymond/florilegium) · [Discussion HN](https://news.ycombinator.com/item?id=50305637)
