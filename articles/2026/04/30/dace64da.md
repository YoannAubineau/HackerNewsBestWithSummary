---
article_fetched_at: '2026-04-30T22:18:09.911482Z'
attempts: 0
content_source: extracted
discussion_comment_count: 214
discussion_fetched_at: '2026-04-30T22:18:09.126620Z'
error: null
feed_summary: '<p>Recent: <i>Copy Fail</i> - <a href="https://news.ycombinator.com/item?id=47952181">https://news.ycombinator.com/item?id=47952181</a>
  - April 2026 (466 comments)</p>

  <hr />

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=47965108">https://news.ycombinator.com/item?id=47965108</a></p>

  <p>Points: 279</p>

  <p># Comments: 197</p>'
guid: https://news.ycombinator.com/item?id=47965108
hn_item_id: 47965108
hn_url: https://news.ycombinator.com/item?id=47965108
is_ask_or_show_hn: false
llm_input_tokens: 17159
llm_latency_ms: 11501
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 949
our_published_at: '2026-04-30T21:53:06Z'
rewritten_title: La vulnérabilité CopyFail du noyau Linux n'a pas été divulguée aux
  développeurs Gentoo
source_published_at: '2026-04-30T16:43:47Z'
status: summarized
summarized_at: '2026-04-30T22:18:27.668457Z'
title: CopyFail was not disclosed to Gentoo developer
url: https://www.openwall.com/lists/oss-security/2026/04/30/10
---

## Résumé de l'article

CopyFail est une vulnérabilité critique d'escalade de privilèges locale dans le noyau Linux (CVE-2026-31431), introduite en 2017 et corrigée dans les versions 6.18.22, 6.19.12 et 7.0. Les distributions n'ont pas reçu d'avertissement préalable car le rapport n'a pas été envoyé à la liste de diffusion linux-distros, contrairement aux pratiques habituelles de divulgation responsable.

- La vulnérabilité affecte toutes les versions du noyau depuis 4.14 (2017) jusqu'aux corrections en avril 2026
- Les versions long-term 6.12, 6.6, 6.1, 5.15 et 5.10 n'ont pas encore reçu de correctif, le portage étant complexe
- Gentoo et autres distributions ont dû mettre en place des contournements (comme la désactivation du module authencesn) faute d'avertissement en amont
- L'absence de notification préalable aux distributions est attribuée au fait que le rapport n'a pas transité par le canal standard linux-distros ML
- Cet incident soulève des questions sur les procédures de divulgation responsable pour les vulnérabilités du noyau

## Discussion sur Hacker News (214 commentaires)

**Avis positifs** :
- La divulgation responsable exige une notification préalable des distributions majeures avant la publication publique d'une exploitation fonctionnelle, permettant aux distributions de préparer et tester des correctifs
- Le processus standard de divulgation (90 jours après signalement ou 30 jours après patch) s'applique ici, mais l'équipe de sécurité du kernel n'a pas assuré la communication en aval auprès des distributions, créant un vide de responsabilité
- La vulnérabilité est critique pour les systèmes hébergés en partage (HPC, académie) et les conteneurs non-VM, rendant l'absence de notification aux distributions d'autant plus grave
- Une simple notification préalable aux équipes de sécurité d'Ubuntu, RHEL et SUSE (explicitement mentionnées sur le site de divulgation) aurait probablement suffi à éviter la débâcle
- L'équipe du kernel refuse délibérément de traiter les vulnérabilités comme telles et se refuse à notifier les distributions, transférant la responsabilité au reporter

**Avis négatifs** :
- Le reporter a suivi la politique de divulgation standard du kernel (30 jours après patch en amont) utilisée par Google Project Zero et d'autres majeurs ; c'est un problème d'organisation du kernel, pas du reporter
- Le kernel est un projet libre avec des limitations de ressources ; les reporters ne devraient pas être responsables de contacter individuellement chaque distribution en aval
- Les vulnérabilités Linux LPE sont monnaie courante et tout hébergeur sérieux devrait utiliser des VMs ou d'autres isolations au lieu de compter sur le kernel comme limite de sécurité
- La divulgation immédiate au public permet aux administrateurs de mitiger rapidement leurs systèmes et d'auditer les compromissions potentielles, plutôt que de rester vulnérables en silence
- Le patche était disponible depuis un mois et les distributions auraient dû le récupérer plus activement ; c'est une défaillance organisationnelle du kernel et des distributions, pas du reporter

**Top commentaires** :

- [xeeeeeeeeeeenu](https://news.ycombinator.com/item?id=47966060) : For context, the author of the linked post, Sam James, is a Gentoo developer. Anyway, this is a disaster. It was extremely irresponsible to share the exploit with the world before the distributions shipped the fix. Who knows how many shared hosting providers were hacked with this. It's also worryin…
- [semiquaver](https://news.ycombinator.com/item?id=47966172) : \> Note that for Linux kernel vulnerabilities, unless the reporter chooses to bring it to the linux-distros ML, there is no heads-up to distributions. Why would they imply it is incumbent on the reporter to liaise with distributions? That seems to assume a high level of familiarity with the linux pr…
- [whatevaa](https://news.ycombinator.com/item?id=47968013) : Stop blaming the reporter. Start asking kernel to fix their process. Linux kernel is no longer a toy project, it has full time employees employed by various companies. They should have handled notifying distributions. Not some rando.

---

[Article original](https://www.openwall.com/lists/oss-security/2026/04/30/10) · [Discussion HN](https://news.ycombinator.com/item?id=47965108)
