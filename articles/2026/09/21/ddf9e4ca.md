---
article_fetched_at: '2026-09-21T11:32:10.042738Z'
attempts: 0
content_source: extracted
discussion_comment_count: 20
discussion_fetched_at: '2026-09-21T11:32:07.107224Z'
error: null
guid: https://news.ycombinator.com/item?id=49761840
hn_item_id: 49761840
hn_url: https://news.ycombinator.com/item?id=49761840
image_url: https://cdn.i-scmp.com/sites/default/files/styles/og_image_scmp_generic/public/d8/images/canvas/2026/09/18/4d38a4b8-98a8-4462-acfa-eb718c19a85d_2bb080b5.jpg?itok=AeGmKIDY&v=1789736650
is_ask_or_show_hn: false
llm_input_tokens: 2958
llm_latency_ms: 7688
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 652
our_published_at: '2026-09-21T00:06:23Z'
rewritten_title: Alibaba met en open source un modèle IA capable de détecter le cancer
  et 150 autres pathologies
source_published_at: '2026-09-18T23:54:42Z'
status: summarized
summarized_at: '2026-09-21T11:33:28.155232Z'
title: Alibaba open-sources AI model that can detect cancer and nearly 150 conditions
url: https://www.scmp.com/tech/big-tech/article/3368055/alibaba-open-sources-medical-ai-model-can-detect-cancer-and-nearly-150-conditions
---

## Résumé de l'article

Alibaba Damo Academy a publié en open source « Damo Radar », un modèle de vision par langage qui analyse les scans CT pour identifier près de 150 pathologies abdominales, y compris les cancers. Testé sur environ 40 000 examens réels, le modèle a surpassé la plupart des radiologues avec une précision diagnostique moyenne (AUC) de 0,913 sur 146 découvertes cliniques.

- Le modèle a été entraîné sur des scans CT appairés à des rapports cliniques et couvre 18 organes abdominaux
- Il détecte une large gamme d'affections incluant les tumeurs malignes et autres anomalies
- L'approche d'entraînement pourrait être étendue à d'autres types d'imagerie médicale selon les chercheurs
- Alibaba le présente comme le premier modèle généraliste d'imagerie médicale au niveau expert mondial

## Discussion sur Hacker News (20 commentaires)

**Avis positifs** :
- Le modèle est efficace et léger (~131M paramètres, 5GB de poids) et peut s'exécuter sur du matériel standard comme un H100, rendant la technologie accessible
- Les résultats sont publiés dans des revues prestigieuses (Nature Medicine) avec des données multicentriques solides et le code/modèle sont open-sourcés sur GitHub et Hugging Face
- Les laboratoires chinois innovent réellement plutôt que simplement copier : contributions validées en architecture (GRPO, MLA, optimiseurs Muon) et publications bien documentées

**Avis négatifs** :
- Les métriques d'évaluation standard (ROC-AUC 0.9) masquent des performances réelles faibles : en cas de déséquilibre de classes sévère typique en diagnostic, cela peut signifier 80% de faux positifs
- L'utilisation persistante de ROC-AUC plutôt que Precision-Recall + mAP en 2026 suggère une communication marketing plutôt que de la rigueur scientifique
- Le succès des encodeurs CNN sur les vision transformers est contre-intuitif et mérite d'être expliqué, soulevant des questions sur la qualité de la validation des résultats

**Top commentaires** :

- [westurner](https://news.ycombinator.com/item?id=49763232) : From https://news.ycombinator.com/item?id=44693991 : \> EPS3.9 also had significant anti-tumor effects in the mice with liver cancer and activated anti-tumor immune responses “A Novel Exopolysaccharide, Highly Prevalent in Marine Spongiibacter, Triggers Pyroptosis to Exhibit Potent Anticancer Effect…
- [plaidfuji](https://news.ycombinator.com/item?id=49766868) : It is 2026. How are we still publishing articles on medical diagnostics data science and using area under the ROC curve as the primary metric of success. ROC-AUC of 0.9 under severe class imbalance \(almost always the case in diagnostics\) could still mean something like 4/5 predicted diagnoses are w…
- [Zaraif13](https://news.ycombinator.com/item?id=49767794) : I don't agree with the flak Chinese labs get. If it's really that easy to distill and compete with frontier models, why aren't other countries anywhere near this AI race?

---

[Article original](https://www.scmp.com/tech/big-tech/article/3368055/alibaba-open-sources-medical-ai-model-can-detect-cancer-and-nearly-150-conditions) · [Discussion HN](https://news.ycombinator.com/item?id=49761840)
