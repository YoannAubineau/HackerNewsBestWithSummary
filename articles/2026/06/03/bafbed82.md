---
article_fetched_at: '2026-06-03T19:16:42.552450Z'
attempts: 0
content_source: extracted
discussion_comment_count: 145
discussion_fetched_at: '2026-06-03T19:16:39.451530Z'
error: null
guid: https://news.ycombinator.com/item?id=48385906
hn_item_id: 48385906
hn_url: https://news.ycombinator.com/item?id=48385906
image_url: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Social_Image_G4_12B.width-1300.png
is_ask_or_show_hn: false
llm_input_tokens: 12247
llm_latency_ms: 13934
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1054
our_published_at: '2026-06-03T18:49:25Z'
rewritten_title: 'Gemma 4 12B: un modèle multimodal unifié sans encodeur séparé'
source_published_at: '2026-06-03T16:04:42Z'
status: summarized
summarized_at: '2026-06-03T19:17:20.669700Z'
title: 'Gemma 4 12B: A unified, encoder-free multimodal model'
url: https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/
---

## Résumé de l'article

Google introduit Gemma 4 12B, un modèle de langage multimodal de 12 milliards de paramètres conçu pour fonctionner localement sur des ordinateurs portables. Il traite nativement les entrées visuelles et audio sans encodeurs séparés, réduisant ainsi la latence et l'empreinte mémoire.

- Architecture unifié sans encodeur : la vision et l'audio se projettent directement dans le réseau neural principal, éliminant les étapes de traitement intermédiaires coûteuses en ressources
- Performance compétitive : offre des résultats comparables au modèle 26B plus puissant tout en consommant moins de la moitié de la mémoire, avec support du multi-step reasoning et des workflows d'agents
- Exécution sur matériel standard : nécessite seulement 16 GB de VRAM pour tourner localement sur des ordinateurs portables grand public
- Licence ouverte et écosystème : distribué sous licence Apache 2.0 avec support sur LM Studio, Ollama, Hugging Face Transformers, llama.cpp et d'autres outils
- Optimisations de performance : inclut des drafters Multi-Token Prediction pour réduire la latence et un repository officiel de Skills pour développer des agents

## Discussion sur Hacker News (145 commentaires)

**Avis positifs** :
- L'architecture sans encodeur dédié simplifie véritablement le pipeline (simple projection matricielle + embeddings positionnels) et réduit les besoins mémoire comparé aux encodeurs traditionnels de 300-500M paramètres.
- Le modèle 12B peut fonctionner sur du matériel grand public en quantization int8 (12GB RAM), offrant une véritable alternative locale aux modèles cloud pour les utilisateurs avec 16GB+ de RAM unifiée ou VRAM.
- La capacité multimodale (vision + audio) dans un seul modèle dense et unifié ouvre des cas d'usage pratiques : transcription locale, classification d'images, traitement de documents, sans dépendre de services cloud.
- Google libère effectivement des modèles open-source robustes sous licence Apache 2.0, ce qui contraste positivement avec les concurrents et représente un vrai bénéfice pour la communauté des développeurs.
- La suppression du fichier .mmproj séparé et l'intégration directe aux outils comme llama.cpp simplifient le déploiement pratique, avec du support audio/vision qui arrive rapidement.

**Avis négatifs** :
- Le marketing '16GB RAM' est trompeur : bf16 natif demande ~24GB + overhead, et même à int8 sur MacBook Pro 18GB, Google Gallery refuse de charger le modèle pour cause de RAM insuffisante, suggérant des exigences mémoire réelles plus élevées.
- Les benchmarks de performance publiés sont en bf16, pas en quantization int8 que les utilisateurs réels emploieront, rendant les affirmations de performance potentiellement très optimistes pour les cas d'usage réels.
- Les performances visuelles observées sont décevantes : le modèle commet des erreurs basiques (ne reconnaît pas 'This is a test'), tandis que Qwen 3.5 0.8b (7% de la taille) le surpasse systématiquement en reconnaissance d'image.
- Les performances textuelles se dégradent : échoue sur des problèmes simples d'arithmétique (18+7 apples) que Gemma 3 12B réussit constamment, suggérant une régression en qualité texte brute.
- Le positionnement commercial reste opaque : Google ne permet pas l'usage payant sur Vertex et bloque les alternatives aux modèles Gemma, poussant les utilisateurs vers d'autres fournisseurs, contredisant le narratif d'open-source altruiste.

**Top commentaires** :

- [senko](https://news.ycombinator.com/item?id=48387695) : I ran the Q4 quant \(used with llama.cpp\) though my "minesweeper" vibe-coding benchmark: https://senko.net/vibecode-bench/2026/minesweeper-gamma-4-12... The result is decent, but it had a few bizzare/trivial syntax errors I had to fix manually: it would do an extra closing bracket or paren a few tim…
- [minimaxir](https://news.ycombinator.com/item?id=48386156) : The big story here is the encoder-free part, which I still don't fully understand. \> Vision: We replaced Gemma 4’s vision encoder with a lightweight embedding module consisting of a single matrix multiplication, positional embedding and normalizations. That's technically encoding, just without usin…
- [asim](https://news.ycombinator.com/item?id=48388066) : We are now entering the closed loop game. Google doesn't need anyone else to accelerate their models. This is their bread and butter. I'm both shocked but also not surprised that they continue to develop such efficiencies. Honestly it's like silicon and CPU architecture advancement. We kept shrinki…

---

[Article original](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) · [Discussion HN](https://news.ycombinator.com/item?id=48385906)
