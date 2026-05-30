---
article_fetched_at: '2026-05-30T14:31:02.551913Z'
attempts: 0
content_source: extracted
discussion_comment_count: 88
discussion_fetched_at: '2026-05-30T14:31:01.772983Z'
error: null
guid: https://news.ycombinator.com/item?id=48328175
hn_item_id: 48328175
hn_url: https://news.ycombinator.com/item?id=48328175
image_url: https://image.theregister.com/254471.jpg?imageId=254471&x=0&y=0&cropw=100&croph=100&panox=0&panoy=0&panow=100&panoh=100&width=1200&height=683
is_ask_or_show_hn: false
llm_input_tokens: 9754
llm_latency_ms: 13020
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1138
our_published_at: '2026-05-30T14:04:38Z'
rewritten_title: Microsoft affronte un chercheur en sécurité qui menace de publier
  six nouvelles failles zero-day
source_published_at: '2026-05-29T19:37:41Z'
status: summarized
summarized_at: '2026-05-30T14:31:21.890864Z'
title: Microsoft 0-day feud escalates as researcher threatens another exploit dump
url: https://www.theregister.com/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085
---

## Résumé de l'article

Nightmare Eclipse, un chasseur de bugs en désaccord avec Microsoft, a publié six failles zero-day Windows et menace une nouvelle divulgation le 14 juillet. Microsoft a répondu par un billet de blog affirmant que le chercheur n'a pas utilisé les canaux officiels de coordination et a menacé une action légale via sa Digital Crimes Unit.

- Six vulnérabilités Windows (RedSun, UnDefend, BlueHammer, YellowKey, GreenPlasma, MiniPlasma) ont été divulguées publiquement avec des preuves de concept exploitables; trois sont déjà activement exploitées en attaques
- Nightmare Eclipse affirme avoir été humilié par Microsoft, avoir eu son compte de signalement supprimé et n'avoir reçu aucune compensation, malgré le lancement de code d'exploitation sans attendre les correctifs
- Des experts en sécurité, dont ceux ayant travaillé chez Microsoft, critiquent la réponse de Redmond comme maladroite et menaçante, jugeant que l'entreprise aurait dû privilégier la désescalade
- Le fossé entre publication d'exploit et utilisation en attaque s'est réduit à quelques heures, multipliant les dégâts potentiels pour les entreprises
- Ce conflit illustre les tensions croissantes autour des processus de divulgation coordonnée entre chercheurs en sécurité et grands éditeurs

## Discussion sur Hacker News (88 commentaires)

**Avis positifs** :
- Microsoft a clairement mal géré cette situation : rejet du signalement, non-paiement des primes, révocation des comptes de communication, et déclarations publiques sans transparence sur la correspondance réelle.
- Le chercheur a tenté une divulgation responsable mais face à l'inaction et l'absence de compensation de Microsoft, la publication devient une forme légitime de responsabilisation pour une entreprise de 101 milliards de dollars de revenu net.
- L'« intentionnalité » soupçonnée du backdoor BitLocker (modification récente dans un sous-système inutilisé depuis longtemps, présent uniquement en mode recovery) paraît plausible et la réponse évasive de Microsoft renforce les soupçons.
- Microsoft a historiquement abusé du système de divulgation coordonnée : déclarant les vulnérabilités comme « intentionnelles », puis les corrigeant silencieusement sans CVE public, ce qui justifie la méfiance des chercheurs.
- La publication forcée révèle les failles réelles de Microsoft et met en lumière un problème systémique : une entreprise majeure qui livre du code défectueux avec impunité, tandis que les chercheurs en sécurité font le travail gratuitement.

**Avis négatifs** :
- Publier des exploits zero-day avec du code fonctionnel pour des vulnérabilités non corrigées expose les utilisateurs ordinaires et les ingénieurs innocents à des risques immédiats de malveillance, dépassant le cadre de la dispute avec Microsoft.
- La divulgation complète est justifiée mais Microsoft's management du bug bounty est complexe : les reviewers sont surchargés (spam IA, barrières linguistiques), souvent assignés après-heures sans récompense, et une mauvaise personne ou un mauvais jour peut tout gâcher.
- Il est possible que Microsoft tente simplement une communication maladroite plutôt que de dissimuler intentionnellement un backdoor : les motivations supposées d'« intention » manquent de preuves directes et reposent sur des inférences architecturales.
- La réputation de Microsoft n'a pas ralenti son succès auprès des suites de direction mondiale depuis des décennies, suggérant que les campagnes de divulgation publique risquent d'avoir peu d'impact et de causer surtout des dommages collatéraux.
- Certains commentaires reconnaissent que même les erreurs de gestion de bounty ne justifient pas de publier des exploits : blâmer le messager au lieu de la vulnérabilité sous-jacente peut encourager une culture où les chercheurs vendent directement aux agences plutôt que de signaler.

**Top commentaires** :

- [anonymousiam](https://news.ycombinator.com/item?id=48331127) : Attacking the messenger is an age-old trend in the bug reporting arena. Microsoft has the backing of many governments, and has access to the best legal teams possible, leaving this guy in a world of hurt. Microsoft seems to have brought this on themselves by creating a complex and user-hostile bug…
- [8cvor6j844qw\_d6](https://news.ycombinator.com/item?id=48328865) : « “CVD is a two-way street,” he said. “The vendor has some responsibility as well, so to go out publicly stating this person violated CVD without showing any of the correspondence seems bold.” “It confusingly claims their program ‘ensures researchers are compensated and publicly acknowledged’ in »…
- [rustyhancock](https://news.ycombinator.com/item?id=48329562) : I know this is a crazy take. But I go feel so down trodden by many many tech corps these days I find it hard not to have a smidge of satisfaction for this guy pointing out the colossal favour research developers do for them by responsible disclosure. That said, I feel bad for the inevitable victims…

---

[Article original](https://www.theregister.com/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085) · [Discussion HN](https://news.ycombinator.com/item?id=48328175)
