---
article_fetched_at: '2026-11-04T20:10:31.680232Z'
attempts: 0
content_source: ask_show_hn
discussion_comment_count: 138
discussion_fetched_at: '2026-11-04T20:10:26.347050Z'
error: null
guid: https://news.ycombinator.com/item?id=50363461
hn_item_id: 50363461
hn_url: https://news.ycombinator.com/item?id=50363461
is_ask_or_show_hn: true
llm_input_tokens: 10202
llm_latency_ms: 8158
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 961
our_published_at: '2026-11-04T19:27:49Z'
rewritten_title: Google Gemini utilise l'historique de chat des abonnés payants pour
  l'entraînement sans possibilité de désabonnement
source_published_at: '2026-11-04T10:10:27Z'
status: summarized
summarized_at: '2026-11-04T20:12:21.074458Z'
title: 'Tell HN: Gemini trains on chat history, even for subscribers (personal accounts)'
url: https://news.ycombinator.com/item?id=50363461
---

## Résumé de l'article

Gemini, le service de chatbot IA de Google, entraîne ses modèles sur l'historique de conversation des utilisateurs abonnés, y compris des comptes payants, avec la possibilité pour des examinateurs humains de lire ces transcriptions. Bien que Google affirme dissocier ces données de votre compte lors de l'examen humain, aucune opt-out n'existe sauf en désactivant l'historique ou en utilisant des sessions temporaires.

- Google utilise les activités Gemini pour l'entraînement des modèles d'IA si le paramètre « Conserver l'activité » est activé, même pour les comptes payants
- Un sous-ensemble de conversations est examiné par des examinateurs humains, et ces données sont conservées jusqu'à trois ans même après suppression de l'activité
- Google avertit explicitement les utilisateurs de ne pas entrer d'informations confidentielles car elles pourraient être vues par des examinateurs ou utilisées pour améliorer les services
- La seule façon de désactiver cet entraînement est de désactiver « Conserver l'activité », ce qui supprime automatiquement les sessions de chat après 72 heures
- L'abonnement payant n'exempte pas les utilisateurs de cette utilisation de leurs données pour l'entraînement

## Discussion sur Hacker News (138 commentaires)

**Avis positifs** :
- Les préoccupations sont justifiées : Google, entreprise de publicité, a historiquement toujours exploité les données utilisateur et n'a aucune incitation à s'arrêter
- Le manque de transparence et de choix réels est flagrant : désactiver l'entraînement force à perdre l'accès à l'historique de chat, ce qui est une pratique coercitive typique de Google
- Ce comportement s'inscrit dans un pattern bien établi chez Google : Maps cache la localisation si on refuse le tracking Wi-Fi/Bluetooth, YouTube supprime la page d'accueil sans historique, et Gemini sur téléphone Pixel devient inutile sans chat history
- La rétention légale (3 ans) pour des chats non supprimés dépasse largement les besoins réels de responsabilité juridique et semble justifier l'utilisation pour l'entraînement
- Même les utilisateurs payants sont traités comme du matériel à exploiter plutôt que comme des clients dont il faut respecter la vie privée

**Avis négatifs** :
- L'entraînement sur des sous-ensembles de chats avec examen humain peut être justifié pour des raisons de sécurité et de responsabilité légale, pas seulement pour améliorer les modèles
- Anthropic et OpenAI feraient probablement la même chose ; le problème n'est pas unique à Google mais systémique dans l'industrie des IA commerciales
- Les utilisateurs ont techniquement le choix : utiliser les chats temporaires sans historique, ou passer par des API avec clauses de confidentialité explicites, ou utiliser des modèles locaux
- D'autres options existent (Claude, ChatGPT, modèles hébergés comme DeepSeek) qui offrent de meilleurs termes ou des services en workspace avec davantage de protections
- La lire des termes de service et faire des choix conscients sur ce qu'on partage reste possible ; comparer les termes entre Gemini, Azure OpenAI et AWS montre des variations

**Top commentaires** :

- [fny](https://news.ycombinator.com/item?id=50366851) : "These chat transcripts may even be read by human reviewers." PSA: This is true of all the frontier model providers even if you disable activity tracking. They are all constantly monitoring your interactions for problematic behavior. \[0\]: https://www.nytimes.com/wirecutter/advice/ai-chat-privacy/ \[…
- [richrichardsson](https://news.ycombinator.com/item?id=50364314) : What's worse is if you have a Pixel phone then Gemini is completely useless without enabling this setting. I had it switched off: "Hey Google, remind me at 7pm \<something\>" "OK, your reminder is set for 7pm" Next day: "Hey Google, why didn't you remind me at 7pm" "I can't do anything with your phon…
- [devsda](https://news.ycombinator.com/item?id=50364867) : « Please don’t enter confidential information that you wouldn’t want a reviewer to see or Google » If Gemini has access to app data like gallery, mail etc that can also be subjected to human review? I imagine that will also be part of the context. They are vague when they say 'don't enter'. Is it o…

---

[Article original](https://news.ycombinator.com/item?id=50363461) · [Discussion HN](https://news.ycombinator.com/item?id=50363461)
