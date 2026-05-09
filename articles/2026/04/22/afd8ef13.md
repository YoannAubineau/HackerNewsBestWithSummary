---
article_fetched_at: '2026-04-23T00:13:01.758086Z'
attempts: 0
content_source: extracted
discussion_comment_count: 29
discussion_fetched_at: '2026-04-23T00:13:02.094315Z'
error: null
feed_summary: '<p>Article URL: <a href="https://techcrunch.com/2026/04/22/apple-fixes-bug-that-cops-used-to-extract-deleted-chat-messages-from-iphones/">https://techcrunch.com/2026/04/22/apple-fixes-bug-that-cops-used-to-extract-deleted-chat-messages-from-iphones/</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=47868867">https://news.ycombinator.com/item?id=47868867</a></p>

  <p>Points: 258</p>

  <p># Comments: 73</p>'
guid: https://news.ycombinator.com/item?id=47868867
hn_item_id: 47868867
hn_url: https://news.ycombinator.com/item?id=47868867
image_url: https://techcrunch.com/wp-content/uploads/2026/04/iphone-pop-up-notifications.jpg?resize=1200,900
is_ask_or_show_hn: false
model: anthropic/claude-haiku-4.5
our_published_at: '2026-04-22T23:54:38Z'
rewritten_title: Apple corrige un bug permettant aux forces de l'ordre d'extraire
  les messages supprimés des iPhones
source_published_at: '2026-04-22T20:27:31Z'
status: summarized
summarized_at: '2026-04-23T00:13:24.531320Z'
title: Apple fixes bug that cops used to extract deleted chat messages from iPhones
url: https://techcrunch.com/2026/04/22/apple-fixes-bug-that-cops-used-to-extract-deleted-chat-messages-from-iphones/
---

## Résumé de l'article

Apple a publié une mise à jour de sécurité corrigeant une faille qui permettait aux autorités d'accéder aux messages supprimés ou auto-effacés sur les iPhones. Le bug conservait les notifications contenant ces messages en cache pendant jusqu'à un mois, permettant aux outils judiciaires d'extraire les données même après leur suppression dans l'application de messagerie.

- Les notifications des messages effacés restaient stockées dans la base de données système d'Apple, contrairement au contenu des messages eux-mêmes qui était supprimé
- Le FBI avait exploité cette faille pour extraire des messages Signal supprimés lors d'investigations, révélation qui a alerté Signal et les défenseurs de la vie privée
- Apple a déployé le correctif sur iOS 18 et les versions antérieures, sans expliquer pourquoi les notifications étaient conservées initialement
- Cette vulnérabilité compromettait la fonction d'auto-suppression des messages, essentielle pour les utilisateurs à risque confrontés à des saisies de téléphone

## Discussion sur Hacker News (29 commentaires analysés)

**Confirmations** :
- Le bug révèle une faille systémique : les notifications déchiffrées et affichées par l'OS sont stockées localement en clair dans une base de données, indépendamment du chiffrement de bout en bout utilisé par l'application messager.
- Apple a correctement backporté le correctif vers iOS 18, ce qui démontre la gravité de la vulnérabilité et l'engagement nécessaire pour la corriger.
- Les utilisateurs soucieux de confidentialité doivent configurer leurs notifications pour n'afficher que l'existence d'un message, sans contenu ni expéditeur – une protection que Signal et autres apps offrent.
- Le problème révèle une tension fondamentale : une fois que le texte atteint la couche de rendu du système, l'OS peut en faire ce qu'il souhaite, indépendamment des garanties cryptographiques de l'application.

**Réfutations** :
- La culpabilité d'Apple/Google concernant le stockage de notifications n'est pas liée à leurs serveurs de notifications (comme parfois présenté), mais exclusivement à la gestion locale des données sur l'appareil après déchiffrement.
- Le correctif est classé comme un problème de « logging » (redaction de données), suggérant que les notifications n'étaient pas directement dans la base de données principale mais dans des fichiers journaux – nuance importante sur la portée réelle de la vulnérabilité.
- La tactique supposée d'Apple forçant iOS 26 via les mises à jour iOS 18 est contestée : les utilisateurs gardent le contrôle des mises à jour automatiques, et ce comportement existait déjà dans les versions antérieures.

---

[Article original](https://techcrunch.com/2026/04/22/apple-fixes-bug-that-cops-used-to-extract-deleted-chat-messages-from-iphones/) · [Discussion HN](https://news.ycombinator.com/item?id=47868867)
