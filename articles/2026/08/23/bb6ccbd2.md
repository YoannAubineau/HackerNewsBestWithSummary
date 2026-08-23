---
article_fetched_at: '2026-08-23T16:14:22.285108Z'
attempts: 0
content_source: extracted
discussion_comment_count: 57
discussion_fetched_at: '2026-08-23T16:14:19.915410Z'
error: null
guid: https://news.ycombinator.com/item?id=49406333
hn_item_id: 49406333
hn_url: https://news.ycombinator.com/item?id=49406333
is_ask_or_show_hn: false
llm_input_tokens: 6603
llm_latency_ms: 10827
llm_models_used:
- anthropic/claude-haiku-4.5
llm_output_tokens: 968
our_published_at: '2026-08-23T15:43:50Z'
rewritten_title: Comment un processeur Athlon XP s'est cassé lors du retrait du radiateur
source_published_at: '2026-08-23T05:51:01Z'
status: summarized
summarized_at: '2026-08-23T16:15:19.150463Z'
title: The End of an Athlon
url: http://www.os2museum.com/wp/the-end-of-an-athlon/
---

## Résumé de l'article

Un chercheur a découvert qu'un processeur Athlon XP s'était fragmenté lors du retrait de son radiateur, révélant les fragilités du design flip-chip PGA utilisé par Intel et AMD vers 2000. Ces processeurs avaient du silicium exposé pour améliorer le refroidissement, mais cette conception s'est avérée très fragile mécaniquement.

- Le silicium exposé contenait une micro-fissure qui n'affectait pas le fonctionnement jusqu'à ce que le retrait du radiateur ne provoque l'effondrement d'une grande portion du die
- Les deux fabricants ont rapidement abandonné le flip-chip PGA au profit de processeurs encapsulés (lidded), qui offraient une meilleure durabilité tout en conservant de bonnes propriétés de refroidissement
- Intel et AMD ont constaté que le refroidissement était difficile quand la puissance des processeurs dépassait 50W, d'où l'exploration du flip-chip
- Les CPUs flip-chip étaient très sensibles à une installation inégale du radiateur et montraient souvent des coins endommagés, bien que cela n'impacte généralement pas l'opération
- Les conceptions ultérieures comme les processeurs LGA sans broches d'Intel se sont avérées beaucoup plus robustes, le point faible s'étant déplacé vers le socket de la carte mère

## Discussion sur Hacker News (57 commentaires)

**Avis positifs** :
- Le démontage des processeurs Athlon (« delidding ») était une pratique courante chez les overclockeurs, mais très risquée en raison de la fragilité extrême de la puce silicium nue exposée.
- Les Athlon XP sans capot étaient particulièrement fragiles lors de l'installation du dissipateur thermique, nécessitant une grande prudence et une application de force précise pour éviter la fissuration du silicium.
- Cette fragilité était un problème bien connu de la communauté des passionnés au début des années 2000, incitant certains à développer des solutions comme des espaceurs en cuivre pour protéger le die.
- Les conditions de refroidissement étaient précaires à l'époque, avec des ventilateurs extrêmement bruyants et des solutions bricolées (ventilateurs de table) souvent nécessaires pour éviter la surchauffe et les crashes.
- L'assemblage des PC était globalement plus délicat et dangereux dans les années 2000, avec des risques nombreux lors du montage des dissipateurs, des barrettes RAM et du démontage des connecteurs.

**Avis négatifs** :
- Contrairement aux idées reçues, réparer ou restaurer un chip complètement endommagé est techniquement et économiquement impossible, même avec des ressources illimitées.
- Les Athlon XP n'étaient pas les seuls processeurs fragiles : les Pentium 4 avaient également des capots, et les packagings flip-chip restent courants et présentent toujours des risques lors du remplacement des pâtes thermiques.
- La construction des processeurs modernes avec throttling automatique et meilleure gestion thermique rend ces processeurs beaucoup plus robustes qu'à l'époque, contredisant l'idée que « c'était mieux avant ».
- L'assemblage de PC moderne, malgré quelques complications supplémentaires (câbles d'alimentation, supports GPU), est globalement plus tolérant aux erreurs et mieux conçu pour éviter les dégâts accidentels.

**Top commentaires** :

- [c0l0](https://news.ycombinator.com/item?id=49408098) : Ouch, that poor die :\( I remember it well, back in the very early 2000s, when my own Athlon XP 1800+ \(an AGOIA stepping, I do know that for sure :D\) met its untimely end at the hands of a device that was designed to prevent the exact misfortune that killed its sister CPU as seen in this submission!…
- [Aurornis](https://news.ycombinator.com/item?id=49406694) : Hardcore builders will remove the lid of their CPU to get the best possible thermal contact. The performance improvement is very small and not worth it but the bragging rights are fun. Unless you destroy the chip while delidding it, that is.
- [Waterluvian](https://news.ycombinator.com/item?id=49408797) : I've been assembling my own desktop PCs since I was about 15, but I have never gotten comfortable with just how much pressure it takes to affix some heat sinks. I think it was my Thunderbird 1200 where you had to press a slotted-head screwdriver on the lever to force it down and under the clasp.

---

[Article original](http://www.os2museum.com/wp/the-end-of-an-athlon/) · [Discussion HN](https://news.ycombinator.com/item?id=49406333)
