---
article_fetched_at: '2026-09-09T21:24:20.037739Z'
attempts: 0
content_source: extracted
discussion_comment_count: 196
discussion_fetched_at: '2026-09-09T21:24:15.704178Z'
error: null
guid: https://news.ycombinator.com/item?id=49624856
hn_item_id: 49624856
hn_url: https://news.ycombinator.com/item?id=49624856
is_ask_or_show_hn: false
llm_input_tokens: 17985
llm_latency_ms: 10849
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 859
our_published_at: '2026-09-09T21:21:07Z'
rewritten_title: Développeur de logiciel macOS face à la suspension injustifiée de
  son compte Google Ads
source_published_at: '2026-09-09T11:43:21Z'
status: summarized
summarized_at: '2026-09-09T21:24:59.644424Z'
title: How I advertise malicious software on Google Ads
url: https://xlii.space/eng/malicious-software-on-google-ads/
---

## Résumé de l'article

Un développeur a vu son compte Google Ads suspendu après avoir dépensé 500 dollars pour promouvoir RACE, un multiplexeur de terminal macOS open source écrit en Rust. Google a allégué que le logiciel était malveillant et que le site était compromis, mais sans fournir de détails ni d'explications.

- Le développeur a mené un audit de sécurité complet : Google Safe Browsing, VirusTotal, vérification des signatures, analyse du code JavaScript et logs Cloudflare ne révèlent aucune menace
- Google Search Console ne signale aucun problème de sécurité sur les domaines race-term.com et downloads.race-term.com
- L'application RACE gère légalement des processus terminaux en arrière-plan (fonction essentielle du multiplexeur), documentée et configurableconfigurations alternatives disponibles
- Le développeur a soumis quatre appels successifs avec preuves détaillées, tous rejetés sans explication supplémentaire et sans clarification des critères utilisés par Google Ads
- La situation crée un paradoxe insoluble : impossibilité de corriger un problème non expliqué et absence de voie de recours transparente autres que des actions légales en Europe

## Discussion sur Hacker News (196 commentaires)

**Avis positifs** :
- Google traite les utilisateurs et annonceurs de manière monopoliste, cachée derrière des systèmes automatisés sans recours humain ni transparence
- Les décisions de modération de Google sont opaques et impossibles à contester : comptes suspendus sans explications, appels rejetés automatiquement, pas d'accès aux véritables raisons
- Les grandes entreprises tech délibérément contournent la responsabilité en automatisant les rejets et en rendant tout contact humain inaccessible, une stratégie systématique observée chez RyanAir, Amazon, Meta et autres
- Google permet massivement les annonces frauduleuses et les escroqueries (faux sites gouvernementaux, jeux AI slop, etc.) tout en suspendant les utilisateurs légitimes, montrant que la plateforme privilégie les revenus publicitaires sur la sécurité

**Avis négatifs** :
- À l'échelle de Google, il est techniquement infaisable de tout réviser manuellement : les scammeurs génèrent du contenu plus vite que les modérateurs humains ne peuvent l'examiner
- Les filtres automatiques trop agressifs (nouveaux domaines, certains mots-clés) sont une heuristique nécessaire contre les malwares, même s'ils créent faux positifs
- Google a effectivement réactivé le compte après la publicité sur HackerNews, démontrant que le système peut fonctionner et que la visibilité publique résout les problèmes
- Certaines entreprises tierces (passports, TSA PreCheck) ne sont pas des arnaqueurs mais des services légitimes autorisés, rendant difficile de distinguer les vrais des faux
- Les utilisateurs techniques auraient pu utiliser OpenStreetMap ou d'autres alternatives plutôt que de compter sur Google

**Top commentaires** :

- [1970-01-01](https://news.ycombinator.com/item?id=49625427) : Google has forgotten the plot. A quick tangent story follows: I attempted to add a Tesla Supercharger as it went live to Google Maps. I was the very first to pay to recharge at the new location. The process went something like this: 1st time: Uploaded 4 photos, local business info, current charger…
- [OptionX](https://news.ycombinator.com/item?id=49625360) : Google is the worst offender, but a lot of companies are increasingly hiding themselves behind a wall of automated systems to completely neuter users ability to challenge any decision unilaterally taken by the them. The LLM-age has worsen the situation but it started well before it. At some point i…
- [Toutouxc](https://news.ycombinator.com/item?id=49625650) : That’s surprising, because in my opinion Google doesn’t care about malicious anything. The other day I had to look for something on YouTube on my dad’s computer with a disabled ad-blocker. I saw like 30 ads in 15 minutes, every single one of them was a scam, literally not a single non-fraudulent ad…

---

[Article original](https://xlii.space/eng/malicious-software-on-google-ads/) · [Discussion HN](https://news.ycombinator.com/item?id=49624856)
