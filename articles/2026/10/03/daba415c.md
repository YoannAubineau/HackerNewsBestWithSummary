---
article_fetched_at: '2026-10-03T18:27:34.635122Z'
attempts: 0
content_source: extracted
discussion_comment_count: 191
discussion_fetched_at: '2026-10-03T18:27:31.196381Z'
error: null
guid: https://news.ycombinator.com/item?id=49937631
hn_item_id: 49937631
hn_url: https://news.ycombinator.com/item?id=49937631
image_url: https://developer.apple.com/news/images/og/full-disk-access-og.png
is_ask_or_show_hn: false
llm_input_tokens: 15518
llm_latency_ms: 9681
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 813
our_published_at: '2026-10-03T17:35:13Z'
rewritten_title: Apple renforce les contrôles d'accès disque complet sur macOS pour
  limiter les abus
source_published_at: '2026-10-02T19:37:01Z'
status: summarized
summarized_at: '2026-10-03T18:28:46.325751Z'
title: Updates to Full Disk Access in macOS
url: https://developer.apple.com/news/?id=p6zjojqw
---

## Résumé de l'article

Apple annonce des changements aux règles d'accès disque complet sur macOS, une permission qui permet aux applications d'accéder à tous les fichiers du système. Certains développeurs exploitent cette permission de manière dangereuse, exposant les données sensibles des utilisateurs sans leur consentement explicite.

- Apple introduira des contrôles renforcés exigeant une action utilisateur très explicite avant d'accorder l'accès disque complet à une application
- Des développeurs utilisent actuellement cette permission pour accéder sans restriction aux fichiers, emails, messages et historique de navigation
- Pour les applications de communication, cet accès non contrôlé compromet également la confidentialité des contacts de l'utilisateur
- Apple justifie cette restriction par les risques croissants liés aux agents IA de plus en plus autonomes et capables

## Discussion sur Hacker News (191 commentaires)

**Avis positifs** :
- Les contrôles d'accès granulaires et les permissions spécifiques par dossier sont nécessaires à l'ère des agents IA et des logiciels de renseignement commercial, contrairement au modèle de confiance des années 1990
- Les utilisateurs non-techniques ont besoin de protection contre les applications malveillantes ou les demandes de permissions trompeuses, même si cela implique des restrictions pour les utilisateurs avertis
- La granularité accrue des permissions (Documents, Téléchargements, Historique de navigation séparé) est un progrès par rapport au binaire tout-ou-rien du Full Disk Access actuel
- Les restrictions existent déjà et les utilisateurs conservent la liberté de les contourner s'ils le souhaitent vraiment ; c'est une question de consentement éclairé et de transparence

**Avis négatifs** :
- Apple crée une pente glissante vers un modèle verrouillé style iPad où seules les applications approuvées peuvent accéder aux données sensibles, perdant progressivement la liberté des utilisateurs propriétaires
- Les dialogues de permission actuels sont déjà accablants et les utilisateurs finissent par les ignorer ; ajouter plus de contrôles rendra macOS encore moins utilisable sans vraiment améliorer la sécurité
- Les modifications fragmentent l'écosystème des développeurs (Terminal, outils CLI, agents) en rendant impossible une granularité vraiment utile sans déclencher des dizaines de prompts ou exiger des VM Linux
- Le système des permissions crée une fausse sécurité tout en handicapant les utilisateurs avertis ; il manque les API modernes (fine-grained ACLs, contrôle par-processus) que les systèmes comme SELinux ou OpenBSD possèdent
- Apple réagit à un incident unique (Muse/Meta) en imposant des restrictions globales au lieu de corriger les véritables failles ; les restrictions de sandbox sur les conteneurs d'app brisent déjà les workflows existants

**Top commentaires** :

- [ghusto](https://news.ycombinator.com/item?id=49945435) : I have to have my machine further crippled in order protect people who don't know what they're doing on a computer. I don't think there's anything wrong with people not knowing how to use a computer properly. In fact, I wouldn't expect a normal person to, why should they? So what I would love to se…
- [eviks](https://news.ycombinator.com/item?id=49941360) : « We give developers powerful APIs to build incredible capabilities Full Disk Access largely sidesteps these controls » That's because you don't really. Just like you don't give users "powerfulf" controls, so instead they have to resort to dumb ones like "Full disk" For example, if you care about "…
- [drnick1](https://news.ycombinator.com/item?id=49946515) : I don't understand why this is a problem at all. AFAIK macOS is UNIX, so you can create user accounts and run programs as separate users. This is what I routinely do on Linux to run coding tools or other programs that should not have "full disk access," in particular to the files and mounts of my m…

---

[Article original](https://developer.apple.com/news/?id=p6zjojqw) · [Discussion HN](https://news.ycombinator.com/item?id=49937631)
