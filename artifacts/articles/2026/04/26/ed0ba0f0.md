---
article_fetched_at: '2026-04-26T15:14:42.446271Z'
attempts: 0
content_source: extracted
discussion_comment_count: 99
discussion_fetched_at: '2026-04-26T15:14:42.227756Z'
error: null
feed_summary: '<p>Article URL: <a href="https://asahilinux.org/2026/04/progress-report-7-0/">https://asahilinux.org/2026/04/progress-report-7-0/</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=47909226">https://news.ycombinator.com/item?id=47909226</a></p>

  <p>Points: 242</p>

  <p># Comments: 71</p>'
guid: https://news.ycombinator.com/item?id=47909226
hn_item_id: 47909226
hn_url: https://news.ycombinator.com/item?id=47909226
image_url: https://asahilinux.org/img/AsahiLinux_logomark_256px.png
is_ask_or_show_hn: false
llm_input_tokens: 13165
llm_latency_ms: 11667
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 941
our_published_at: '2026-04-26T14:37:29Z'
rewritten_title: Asahi Linux progress with kernel 7.0 release and major driver improvements
source_published_at: '2026-04-26T10:50:32Z'
status: summarized
summarized_at: '2026-04-26T15:15:00.330652Z'
title: Asahi Linux Progress Linux 7.0
url: https://asahilinux.org/2026/04/progress-report-7-0/
---

## Résumé de l'article

Asahi Linux has released a progress report coinciding with Linux 7.0 kernel. Key improvements include automated installer deployment, ambient light sensor support for display calibration, significant idle power consumption reductions, Bluetooth audio reliability fixes, and Variable Refresh Rate display support.

- Installer automation now enables automatic builds and deployments via GitHub workflows, solving previous synchronization issues between installer bundles and kernel changes
- Ambient Light Sensor (ALS) support added for True Tone-like display color calibration, requiring firmware updates retrievable through the Asahi Installer
- Power Management Processor (PMP) support implementation reduces idle power consumption by approximately 20% on M1 Pro MacBook Pro devices
- Broadcom Bluetooth coexistence support prevents audio dropouts caused by WiFi-Bluetooth interference by prioritizing audio streams
- Variable Refresh Rate (VRR) discovered and implemented for external displays and MacBook Pro ProMotion screens, though currently available only as a kernel module parameter due to specification limitations
- Hardware support expanded for M3 machines with PCIe, keyboards, trackpads, and NVMe controller drivers; additional sample rates (44.1, 88.2, 176.4, 192 kHz) enabled for headphone jack audio

## Discussion sur Hacker News (99 commentaires)

**Avis positifs** :
- L'équipe Asahi démontre une expertise remarquable avec des avancées constantes et une compréhension profonde des besoins des utilisateurs, notamment en reverse engineering (exemple : support des taux d'échantillonnage audio via analyse comparative de datasheets).
- Le matériel Apple avec Linux offre une excellente combinaison : Apple Silicon est très efficace énergétiquement et performant, et Linux sur du matériel Mac unifié est plus stable que sur du matériel PC hétérogène.
- Les marges bénéficiaires saines du matériel Apple signifient que les ventes à des utilisateurs Linux représentent du profit pur sans besoin de verrouillage écosystème, ce qui pourrait justifier une aide officielle.
- Le projet progresse régulièrement (M3 en version alpha, M4 en développement) et offre un vrai bénéfice aux utilisateurs qui apprécient Linux mais veulent du matériel de qualité, avec potentiellement des dizaines de milliers d'utilisateurs.

**Avis négatifs** :
- Asahi reste un projet parallèle non intégré au kernel mainline ou aux distributions majeures (Ubuntu, Debian, Fedora), et atteindre le 95% de polissage nécessaire à l'expérience publique générale demande autant d'effort que les premiers 80%.
- Apple n'aide pas officiellement car cela créerait des obligations de support documentaire et de compatibilité, transformant la 'non-responsabilité plausible' actuelle en charge réelle pour chaque bug rapporté.
- Les Mac Apple sont une cible mouvante : sans engagement à la stabilité de l'interface matériel-logiciel, les futures modifications d'Apple rendront les choses difficiles pour Asahi sans que cela ne préoccupe Apple.
- La majorité des acheteurs de Mac pour l'écosystème ne basculeraient jamais vers Linux ; seul un segment minuscule (développeurs déjà familiers avec Linux) en bénéficierait réellement, insuffisant pour justifier l'effort d'Apple.
- macOS reste un choix populaire et fonctionnel pour la majorité des utilisateurs, et le contrôle total de la pile logicielle est fondamental à la philosophie Apple, rendant peu probable toute coopération formelle avec un effort tiers.

**Top commentaires** :

- [kakwa\_](https://news.ycombinator.com/item?id=47910679) : While I absolutely love the technical write-up from the Asahi team, and being absolutely impressed by their accomplishment, to the risk of being an overly negative contrarian, I remain a bit skeptical. I'm concerned that after all these years, it's still a separate project and not an effort sustain…
- [brynet](https://news.ycombinator.com/item?id=47910068) : « .. macOS only ever programs CS42L84 to operate at either 48 or 96 kHz, we could only add support for those two sample rates to the Linux driver .. However, CS42L42 supports all the other common sample rates, and while the register layout and programming sequence is different, the actual values »…
- [georgeburdell](https://news.ycombinator.com/item?id=47910342) : I really hope this project continues to gain momentum. Apple Hardware + Linux is the least fscked OS running on the best hardware. MacOS continues to be a tire fire with endless bugs and churn between versions.

---

[Article original](https://asahilinux.org/2026/04/progress-report-7-0/) · [Discussion HN](https://news.ycombinator.com/item?id=47909226)
