---
article_fetched_at: '2026-05-17T18:20:41.806405Z'
attempts: 0
content_source: extracted
discussion_comment_count: 188
discussion_fetched_at: '2026-05-17T18:20:41.271202Z'
error: null
guid: https://news.ycombinator.com/item?id=48168198
hn_item_id: 48168198
hn_url: https://news.ycombinator.com/item?id=48168198
image_url: https://www.williamangel.net/blog/2026/05/17/2026-05-17-offline-llm-energy-use.png.
is_ask_or_show_hn: false
llm_input_tokens: 18476
llm_latency_ms: 12938
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1092
our_published_at: '2026-05-17T17:58:01Z'
rewritten_title: Apple Silicon pour l'inférence locale coûte trois fois plus cher
  que OpenRouter
source_published_at: '2026-05-17T12:09:23Z'
status: summarized
summarized_at: '2026-05-17T18:21:01.079839Z'
title: Apple Silicon costs more than OpenRouter
url: https://www.williamangel.net/blog/2026/05/17/offline-llm-energy-use.html
---

## Résumé de l'article

Une analyse comparative montre que faire tourner des modèles d'IA localement sur un MacBook Pro M5 coûte significativement plus cher que d'utiliser des services cloud comme OpenRouter, malgré l'absence de frais d'électricité apparents.

- Le coût amorti d'un MacBook Pro 14" M5 Max ($4299) sur 5 ans représente environ $0.10/heure en amortissement matériel, plus $0.02/heure en électricité, soit ~$1.50-$4.80 par million de tokens selon la vitesse d'inférence (10-40 tokens/sec)
- OpenRouter propose des modèles comparables (Gemma 4 31b) à ~$0.50 par million de tokens, soit un tiers du coût et environ 2x plus rapide (60-70 tokens/sec vs 10-20 tokens/sec localement)
- Le coût du matériel domine le calcul économique : l'amortissement sur 3 ans vs 10 ans change le coût par million de tokens d'un facteur 10
- Pour un employé utilisant l'inférence locale, le coût des tokens générés reste négligeable comparé au salaire (~1000x moins cher que les tokens)
- Malgré ces désavantages économiques, les modèles locaux comme Gemma 4 31b offrent des performances proches de Claude Sonnet sur du matériel grand public

## Discussion sur Hacker News (188 commentaires)

**Avis positifs** :
- Les fournisseurs cloud bénéficient d'économies d'échelle massives (tarifs électriques industriels, utilisation multi-locataire 24/7, matériel optimisé) qui rendent structurellement impossible de rivaliser avec l'inférence locale sur le coût par token.
- L'analyse omet que le MacBook reste une machine polyvalente avec valeur résiduelle décente, tandis que les tokens sont consommés ; il faut comparer seulement la différence de coût d'upgrade, pas l'intégralité du prix.
- Pour les charges agentic typiques, les tokens d'entrée dominent les coûts (10x+ les tokens de sortie), et le cache local est quasi-gratuit comparé au cache cloud compliqué et cher d'OpenRouter.
- Les entreprises de frontière vendent probablement à perte via VC pour capturer le marché ; les prix actuels ne sont pas stables et augmenteront quand les subsides cesseront.
- L'analyse favorise excessivement le cloud en arrondissant les paramètres défavorables au MacBook (électricité +10%, puissance haute-gamme, utilisation 24/7) et ignore les optimisations locales (spéculative decoding, quantification).

**Avis négatifs** :
- La confidentialité des données et le contrôle sur les paramètres d'inférence, LoRA et vecteurs de direction ne sont PAS des questions de coût monétaire mais de valeur personnelle ; comparer seulement le prix par token rate manque l'essentiel.
- Les modèles ouverts locaux (Gemma, Qwen) sont nettement plus lents et moins capables que les modèles frontier (Claude Opus, ChatGPT) ; la vitesse cloud 3-7x meilleure maintient le flow et productivité en développement itératif.
- Les coûts d'input dominent l'inférence agentique, où le cache local gratuit ou presque renverse entièrement le calcul ; analyser seulement les tokens output invalide la conclusion.
- Même en optimisant, un MacBook M5 Max à 4300$ reste 2600$ plus cher qu'un MacBook 14" base à 1700$ ; le différentiel de coût matériel pour l'IA ne se justifie pas économiquement pour la plupart.
- Les modèles ouverts bon marché (Qwen, DeepSeek) offrent bien meilleur rapport qualité/coût que Gemma pour le benchmark, rendant l'analyse techniquement obsolète et mal choisie.

**Top commentaires** :

- [bastawhiz](https://news.ycombinator.com/item?id=48168433) : This isn't a good analysis, and it's because it keeps rounding everything up. He rounds up the cost of electricity by 10%. He has a range of power use, takes the high end \(which is 2x the low end\) and multiplies it by the inflated electricity cost. But then they talk about using a newly purchased M…
- [applfanboysbgon](https://news.ycombinator.com/item?id=48168387) : Unless I'm misunderstanding, this is counting the entire laptop in the cost of generating tokens. The calculation seems to omit that, in addition to receiving LLM output, you have also received a laptop in exchange for your money. If you intend to put this machine in a dark corner and run it solely…
- [dijit](https://news.ycombinator.com/item?id=48169040) : Frontier AI companies are selling at a loss. Excusing everything else that u/bastawhiz said\[0\]; the obvious fact here is that Claude, OpenAI, Gemini et al. are quite literally burning through 100's of billions of dollars and selling it back to you for pennies on the dollar in the hopes that they ge…

---

[Article original](https://www.williamangel.net/blog/2026/05/17/offline-llm-energy-use.html) · [Discussion HN](https://news.ycombinator.com/item?id=48168198)
