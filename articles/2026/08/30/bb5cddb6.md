---
article_fetched_at: '2026-08-30T08:44:23.474320Z'
attempts: 0
content_source: extracted
discussion_comment_count: 81
discussion_fetched_at: '2026-08-30T08:44:21.753032Z'
error: null
guid: https://news.ycombinator.com/item?id=49495372
hn_item_id: 49495372
hn_url: https://news.ycombinator.com/item?id=49495372
image_url: https://cdn.mos.cms.futurecdn.net/G9dtD87HfBhVHzDmSHE2tE-1920-80.jpg
is_ask_or_show_hn: false
llm_input_tokens: 8285
llm_latency_ms: 11302
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 1027
our_published_at: '2026-08-30T08:40:06Z'
rewritten_title: Californie exempte les systèmes d'exploitation open source de la
  loi de vérification d'âge
source_published_at: '2026-08-30T03:15:36Z'
status: summarized
summarized_at: '2026-08-30T08:45:34.940846Z'
title: California lawmakers unanimously pass Linux exemption from age-verification
  law
url: https://www.tomshardware.com/software/linux/california-lawmakers-unanimously-pass-linux-exemption-from-age-verification-law-software-distributed-under-the-gpl-mit-bsd-and-apache-licenses-are-exempt
---

## Résumé de l'article

La Californie a adopté à l'unanimité le projet de loi AB 1856, qui exempte les systèmes d'exploitation open source de la loi numérique de vérification d'âge (Digital Age Assurance Act) qui entrera en vigueur le 1er janvier 2027. Cette exemption s'applique à toute personne ou entité distribuant un système d'exploitation ou une application sous des licences permettant la copie, la redistribution et la modification du code source (GPL, MIT, BSD, Apache).

- Les systèmes d'exploitation propriétaires (Windows, macOS, iOS, Android) restent soumis à l'obligation de collecter les données d'âge lors de la création de compte à partir du 1er janvier 2027
- L'exemption couvre les distributions Linux (Debian, Fedora, Ubuntu, Arch), les variantes BSD et les systèmes comme GrapheneOS, qui échappent ainsi aux exigences de vérification d'âge
- Les composants logiciels non distribués comme des applications exécutables autonomes (bibliothèques, dépendances via gestionnaires de paquets) et les extensions de navigateur sont également exclus du champ d'application
- L'amendement corrige une définition initiale absurde qui classait tout résident californien comme enfant, en supprimant les obstacles au signalement de l'âge adulte
- Une disposition interdit toute demande d'âge non requise par la loi, prévenant l'utilisation abusive de l'API de vérification comme canal de collecte de données généraliste

## Discussion sur Hacker News (81 commentaires)

**Avis positifs** :
- L'exemption pour les logiciels open source (GPL, MIT, BSD, Apache) est une victoire concrète contre une loi intrusive de vérification d'âge qui aurait menacé la liberté informatique et l'innovation collaborative
- La définition par critères fonctionnels (copie, redistribution, modification autorisées) plutôt que par une liste de licences spécifiques évite de favoriser certains projets et ne crée pas de gagnants/perdants artificiels
- L'exemption s'applique largement aux distributions Linux majeures, BSD, et aux gestionnaires de paquets, ce qui protège un écosystème vital pour les développeurs et les passionnés
- La disposition interdisant les demandes de signal d'âge à moins de l'exiger légalement ajoute une protection supplémentaire contre l'expansion future de la collecte de données personnelles

**Avis négatifs** :
- Ce n'est pas une victoire mais un emplâtre sur une mauvaise loi : les vérifications d'âge obligatoires demeurent pour Windows, macOS et Android, renforçant la surveillance de masse plutôt que de résoudre le problème
- L'exemption crée une inégalité arbitraire et soulève des questions d'égalité de traitement : pourquoi les enfants utilisant Linux seraient-ils exemptés de protection alors que ceux sur Windows ne le seraient pas ?
- La loi reste mal conçue et techniquement imprécise (distinction vague entre open source et propriétaire, flou autour de macOS qui contient des éléments sous APSL), créant des incohérences durables plutôt qu'une vraie solution
- L'exemption risque d'être temporaire ou contournée : une fois normalisée, la collecte de données PII pourrait être réintroduite, et les grandes entreprises trouveront des moyens de se conformer ou d'adapter leurs modèles
- Cette approche fragmentée (des exemptions au cas par cas) confirme l'incompétence législative et décourage une véritable réforme des lois de protection de la vie privée dont on aurait vraiment besoin

**Top commentaires** :

- [huimang](https://news.ycombinator.com/item?id=49496679) : So is anyone going to revert the commits that jumped the gun on this? E.g. systemd's birthdate field https://github.com/systemd/systemd/pull/40954
- [cm2187](https://news.ycombinator.com/item?id=49496239) : Excellent. From now on all kids will become linux natives. The decade of the linux desktop is coming!
- [red\_admiral](https://news.ycombinator.com/item?id=49496762) : We got into this mess because people wanted Facebook to have age verification, and MZ decided to push the responsibility on to OSes. The result looks to me like Facebook will ban access from non-approved OSes like Linux. Android will still be allowed, GrapheneOS probably not.

---

[Article original](https://www.tomshardware.com/software/linux/california-lawmakers-unanimously-pass-linux-exemption-from-age-verification-law-software-distributed-under-the-gpl-mit-bsd-and-apache-licenses-are-exempt) · [Discussion HN](https://news.ycombinator.com/item?id=49495372)
