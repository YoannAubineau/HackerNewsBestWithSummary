---
article_fetched_at: '2026-05-03T22:12:56.311103Z'
attempts: 0
content_source: extracted
discussion_comment_count: 195
discussion_fetched_at: '2026-05-03T22:12:55.537243Z'
error: null
feed_summary: '<p>Article URL: <a href="https://wiki.alcidesfonseca.com/blog/why-tuis-are-back/">https://wiki.alcidesfonseca.com/blog/why-tuis-are-back/</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=48000028">https://news.ycombinator.com/item?id=48000028</a></p>

  <p>Points: 177</p>

  <p># Comments: 161</p>'
guid: https://news.ycombinator.com/item?id=48000028
hn_item_id: 48000028
hn_url: https://news.ycombinator.com/item?id=48000028
is_ask_or_show_hn: false
llm_input_tokens: 17130
llm_latency_ms: 11338
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 970
our_published_at: '2026-05-03T21:43:34Z'
rewritten_title: Les interfaces textuelles font leur retour face aux échecs des UI
  natives modernes
source_published_at: '2026-05-03T18:42:28Z'
status: summarized
summarized_at: '2026-05-03T22:13:30.603455Z'
title: Why TUIs Are Back
url: https://wiki.alcidesfonseca.com/blog/why-tuis-are-back/
---

## Résumé de l'article

Les interfaces textuelles (TUI) connaissent un regain d'intérêt après décennies d'obsolescence. Cet article analyse pourquoi les grandes plateformes (Windows, macOS, Linux) ont échoué à maintenir des frameworks graphiques cohérents et stables, poussant développeurs et utilisateurs vers des solutions alternatives.

- Windows a traversé une succession d'échecs : MFC, COM, ActiveX, Winforms, WPF, Silverlight, WinUi, MAUI, créant des lacunes et une complexité cognitive accablante à chaque itération
- macOS, autrefois modèle de cohérence, abandonne ses propres guidelines en rendant le redimensionnement de fenêtres quasi-impossible et en ignorant des principes comme la loi de Fitts
- Les applications Electron dominantes (Slack, Discord, VSCode) manquent de cohérence visuelle et de workflows clavier standards, fragmentant l'expérience utilisateur
- Linux souffre d'incohérence UI par design (GTK vs Qt), obligeant les entreprises à choisir entre Electron ou ignorer la plateforme
- Les TUI offrent vitesse, automabilité, portabilité et cohérence en se concentrant sur l'interaction plutôt que sur l'esthétique OS, remplissant le vide laissé par les plateformes majeures

## Discussion sur Hacker News (195 commentaires)

**Avis positifs** :
- Les TUI offrent des avantages techniques réels : latence faible, démarrage instantané, facilité de remoting via SSH, absence de bloat UI et meilleure densité d'information que les GUI
- Les TUI s'intègrent naturellement aux workflows existants (tmux, terminal multiplexers) et permettent une productivité accrue pour les utilisateurs du terminal grâce à la navigation au clavier
- Ils sont rapides à construire avec les outils modernes (Go + Bubble Tea, Ratatui en Rust, Rich en Python) et particulièrement bien adaptés aux agents IA qui opèrent sur du texte
- Les contraintes des TUI forcent une conception épurée sans bloat cosmétique, tandis que les GUI modernes accumulent padding excessif et animations inutiles
- Les TUI permettent des cas d'usage importants : déploiement sans installation locale (via SSH), monitoring, administration système, et fonctionnent mieux que les alternatives bloatées sur du matériel limité

**Avis négatifs** :
- Les TUI restent marginaux : la plupart des utilisateurs non-techniques les détestent, et la majorité des applications professionnelles (Salesforce, Workday, Bloomberg) restent basées GUI
- Le succès des TUI est largement superficiel et motivé par l'effet de mode : l'apparence 'cyberpunk' et l'association avec les hackers compétents prime sur l'utilité réelle, exacerbée par Claude Code
- Les limitations des TUI sont sévères : pas d'images, pas de graphiques véritables (simulations par caractères), impossible de créer des DAWs ou logiciels complexes, très dépendant de l'infrastructure Unix archaïque
- Les TUI modernes générés par IA (Claude Code, Gemini CLI) sont souvent lents, bugués et gonflés (Claude Code = 600 Kloc), contredisant les arguments d'efficacité
- Le vrai problème reste la fragmentation des GUI cross-platform natives : plutôt que de résoudre cela, les TUI offrent une fuite facile qui n'adresse pas les besoins des utilisateurs ordinaires et ralentit l'innovation en UI

**Top commentaires** :

- [zmmmmm](https://news.ycombinator.com/item?id=48002066) : I think it's the smoldering ruins of the OS vendor self interest collapsing in on itself. There's not a single good universal UI. The best is the browser and it is reasonably successful but the sandbox makes it specifically unsuitable / high friction for doing things that need local access to files…
- [schmorptron](https://news.ycombinator.com/item?id=48000364) : I think part of it is also that we're able to still LARP as full developers of complex systems while vibe coding by seeing an interface that makes us look like l33t h4xx0rs even though we're just pressing continue 15 times
- [qudat](https://news.ycombinator.com/item?id=48000929) : I think if you look purely at the numbers, the real reason TUIs are popular is claude code, everything else is background noise compared to it. What originally got me excited to build TUIs was the concept of delivering apps over the wire via SSH. SSH apps resemble a browser in that way: no local in…

---

[Article original](https://wiki.alcidesfonseca.com/blog/why-tuis-are-back/) · [Discussion HN](https://news.ycombinator.com/item?id=48000028)
