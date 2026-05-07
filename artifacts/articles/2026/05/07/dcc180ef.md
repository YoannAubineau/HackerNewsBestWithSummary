---
article_fetched_at: '2026-05-07T18:33:37.466916Z'
attempts: 0
content_source: extracted
discussion_comment_count: 66
discussion_fetched_at: '2026-05-07T18:33:36.463430Z'
error: null
feed_summary: '<p>Article URL: <a href="https://draxinar.github.io/articles/2026-05-01-uodemo-reverse-engineering.html">https://draxinar.github.io/articles/2026-05-01-uodemo-reverse-engineering.html</a></p>

  <p>Comments URL: <a href="https://news.ycombinator.com/item?id=48032976">https://news.ycombinator.com/item?id=48032976</a></p>

  <p>Points: 240</p>

  <p># Comments: 66</p>'
guid: https://news.ycombinator.com/item?id=48032976
hn_item_id: 48032976
hn_url: https://news.ycombinator.com/item?id=48032976
is_ask_or_show_hn: false
llm_input_tokens: 8704
llm_latency_ms: 12200
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 947
our_published_at: '2026-05-07T18:03:00Z'
rewritten_title: Reverse-engineering complet du serveur demo d'Ultima Online de 1998
  apres dix ans de travail
source_published_at: '2026-05-06T06:31:29Z'
status: summarized
summarized_at: '2026-05-07T18:34:12.703346Z'
title: Reverse-engineering the 1998 Ultima Online demo server
url: https://draxinar.github.io/articles/2026-05-01-uodemo-reverse-engineering.html
---

## Résumé de l'article

Un développeur a publié le reverse-engineering complet du serveur de démonstration d'Ultima Online de 1998, un MMORPG pionnier de 1997. Le projet représente environ 5 000 fonctions disassemblées depuis un binaire x86 MSVC et traduites en C99 portable, chacune comparée instruction par instruction avec l'original.

- Le serveur démo (UoDemo.exe, compilé avec Visual C++ 5.0) contenait le code serveur production complet de mi-1998 limité à l'île d'Ocllo, avec de nombreuses fonctionnalités intentionnellement désactivées pour la démo
- La reconstruction a utilisé radare2 pour la disassembly, des symboles dérivés d'un portage Linux du client UO, et une traduction manuelle en C99 avec vérification par re-disassembly et comparaison binaire
- Le projet corrige des problèmes de stabilité et de gameplay du binaire original, réactive des fonctionnalités cassées (spawning, système d'écologie prédateur/proie), et ajoute des compétences manquantes comme la méditation et la discrétion
- Le code supporte désormais 64-bit, tous les clients UO de 1998 à 2007, et inclut des implémentations modernisées du système de comptes et de cinq mécanismes de chiffrement différents
- Un serveur de test public (uo.serpent-isle.com) permet de tester cette reproduction fidèle du serveur UO de 1998, avec code source et données disponibles sur GitHub

## Discussion sur Hacker News (66 commentaires)

**Avis positifs** :
- L'archéologie protocolaire est une forme fascinante de préservation historique du jeu vidéo, combinant débogage logiciel et histoire informatique
- Les LLMs se sont révélés extraordinairement utiles pour accélérer les projets de décompilation longue durée, après une décennie de travail intermittent
- Ultima Online reste vivant avec une communauté active (2500+ joueurs sur UO Outlands), démontrant l'attrait durable du design sandbox original comparé aux MMORPGs actuels
- Le jeu a servi de tremplin d'apprentissage majeur pour plusieurs générations de programmeurs, particulièrement via les émulateurs de serveurs (Sphere, RunUO, POL)
- L'infrastructure réseau et la scalabilité distribuée (design VPN, Solaris vers Linux) d'UO était révolutionnaire et en avance sur son époque

**Avis négatifs** :
- Les LLMs et emulateurs modernes offrent une meilleure expérience qu'une reconstruction du code C des années 1990, jugé peu sûr pour la mise en ligne
- Le design sandbox original souffrait d'un déséquilibre : les griefers agressifs ont chassé les autres joueurs, détruisant l'équilibre écologique du jeu
- Le genre MMO ouvert n'a pas survécu à WoW, car la majorité des joueurs préfère des expériences « sur rails » avec quêtes guidées plutôt que sandbox
- L'utilisation d'une pile TCP pure pour tout (au lieu d'optimisations réseau) semble être une architecture « lente » pour un MMO des années 1990
- Au-delà de la curiosité technique, l'utilité pratique de cette reconstruction reste limitée par rapport aux emulateurs fonctionnels modernes

**Top commentaires** :

- [raymond\_goo](https://news.ycombinator.com/item?id=48035850) : Quote: If anyone out there has the dynamic0.mul or dynamic0.bkp \(server savegames\) or regions.txt \(spawn definitions\) or resbank.mul \(resources definitions\) files from the original Ultima Online servers, circa 1997-2003, I’d be very grateful if you could send them to me. It seems very unlikely that…
- [MacNCheese23](https://news.ycombinator.com/item?id=48040644) : As the final and last surviving dev of eqclassic I found this interesting, but expected more story meat on how tools were used and the overall process. Nevertheless, a nice read. I didn't have an LLM back then but also at least some debug symbols from a powerpc binary that was 3 years in the future…
- [helloplanets](https://news.ycombinator.com/item?id=48035030) : For anyone wanting to try UO out, it's still a game with an active player base. There are 3rd party servers like UO Outlands, which gets closer to the original gameplay. Meaning very harsh in comparison to what most people are used to in today's MMOs. Players can just come to gank you and you'll lo…

---

[Article original](https://draxinar.github.io/articles/2026-05-01-uodemo-reverse-engineering.html) · [Discussion HN](https://news.ycombinator.com/item?id=48032976)
