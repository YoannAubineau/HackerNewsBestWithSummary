---
article_fetched_at: '2026-07-04T23:54:22.912527Z'
attempts: 0
content_source: extracted
discussion_comment_count: 124
discussion_fetched_at: '2026-07-04T23:54:21.286969Z'
error: null
guid: https://news.ycombinator.com/item?id=48788283
hn_item_id: 48788283
hn_url: https://news.ycombinator.com/item?id=48788283
image_url: https://opengraph.githubassets.com/bec226760ddcd74e4c8c58935e3e24e751ed55c69df13eb3500db58575603556/ammaarreshi/Generals-Mac-iOS-iPad
is_ask_or_show_hn: false
llm_input_tokens: 9948
llm_latency_ms: 12977
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 994
our_published_at: '2026-07-04T23:11:57Z'
rewritten_title: Command and Conquer Generals porté nativement sur macOS, iPhone et
  iPad via Fable
source_published_at: '2026-07-04T19:41:10Z'
status: summarized
summarized_at: '2026-07-04T23:54:42.512503Z'
title: Command and Conquer Generals natively ported to macOS, iPhone, iPad using Fable
url: https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main
---

## Résumé de l'article

Command and Conquer Generals: Zero Hour a été porté nativement sur Apple Silicon Macs, iPhone et iPad sans émulation, en compilant le moteur 2003 original pour ARM64 et convertissant DirectX 8 en Metal via une chaîne Vulkan. Ce projet, basé sur la source GPL v3 d'EA et la fork GeneralsX existante, ajoute le support iOS/iPadOS avec des contrôles tactiles adaptés aux jeux de stratégie en temps réel.

- Le port compile le moteur 2003 réel (pas d'émulation) pour fonctionner nativement sur Apple Silicon, avec rendu DirectX 8 → DXVK → Vulkan → MoltenVK → Metal
- Les contrôles tactiles incluent sélection par tap, boîtes de sélection par glissement, désélection par long-press, défilement à deux doigts et zoom par pincement
- Les ressources du jeu ne sont pas incluses ; il faut posséder sa propre copie (Steam, ~5 $ en promotion)
- L'installation macOS nécessite Xcode, CMake, Ninja, Meson, vcpkg et le Vulkan SDK ; l'installation iOS nécessite en plus Xcode complet et une équipe Apple Developer
- Le projet est une collaboration ingénieur+IA : Claude Code (Anthropic) a assuré l'ingénierie sous la direction d'Ammaar Reshi, avec des notes détaillées dans docs/port/

## Discussion sur Hacker News (124 commentaires)

**Avis positifs** :
- Port technique impressionnante : conversion réussie d'une application DirectX 8 vers Metal via une chaîne de rendu complexe (DXVK → Vulkan → MoltenVK), sans émulation ni streaming
- Cas d'usage pertinent de l'IA : utilisation légitime d'agents de code pour adapter un projet existant à de nouveaux systèmes cibles, avec enjeux faibles et itération possible
- Implémentation tactile bien pensée : contrôles adaptés aux RTS mobiles (sélection par tap, drag-box, déselection long-press, zoom pinch, pan deux-doigts)
- Effort documenté transparemment : code open-source (GPL v3), log d'ingénierie détaillé des bugs et corrections, attribution claire des contributeurs précédents
- Potentiel de résurrection de jeux legacy : démontre qu'avec des outils modernes, des jeux abandonnés peuvent être ressuscités sur de nouvelles plateformes

**Avis négatifs** :
- Titre trompeur : le port a commencé en février, Fable n'a contribué que 19 commits sur 2000 ; l'attribution au modèle semble exagérée comparée au travail upstream
- Fable n'a probablement pas fait le travail : indices suggérant une dégradation à Opus plutôt qu'un vrai usage de Fable, mettant en question la crédibilité des affirmations sur l'IA
- Problèmes de maintenance à long terme : consommation batterie préoccupante sur iPad, crash lors de mise en arrière-plan documenté, stabilité sur longue durée incertaine
- Doute sur la supériorité de Fable : pas de preuve que Fable spécifiquement était nécessaire ; d'autres LLM modernes (GLM, GPT) auraient probablement pu accomplir la même tâche
- Questions légales non résolues : la reconstruction du code par décompilation du binaire, même si GPL v3, pourrait rester légalement contestable sans approche clean-room

**Top commentaires** :

- [Eufrat](https://news.ycombinator.com/item?id=48788939) : IMHO, this is an actual good use of what sounds like a person guiding a model to do a mass conversion. Although, I wish the porting docs were a little wordsmithed by a human, the AI generated text style is grating. The stakes are low, it’s mostly for fun and you can iterate on it. Compare this with…
- [xg15](https://news.ycombinator.com/item?id=48788648) : « \(tap-select, drag-box, long-press deselect, two-finger scroll, pinch zoom\) » This is another "AI-ism" I noticed, mostly in coding agents - they seem to be very fond of making up new "compound nouns" \(and occasionally verbs\) to sum up relatively complex and specific concepts into single noun phras…
- [namuol](https://news.ycombinator.com/item?id=48788381) : « Built on EA's GPL v3 source release via fbraz3/GeneralsX \(which did the heavy lifting of the macOS/Linux port — this fork adds the iOS/iPadOS port and a set of engine fixes\). »

---

[Article original](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main) · [Discussion HN](https://news.ycombinator.com/item?id=48788283)
