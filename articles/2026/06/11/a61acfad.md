---
article_fetched_at: '2026-06-11T05:33:06.450708Z'
attempts: 0
content_source: extracted
discussion_comment_count: 298
discussion_fetched_at: '2026-06-11T05:33:05.332783Z'
error: null
guid: https://news.ycombinator.com/item?id=48478969
hn_item_id: 48478969
hn_url: https://news.ycombinator.com/item?id=48478969
image_url: https://techcrunch.com/wp-content/uploads/2026/06/anthropic-claude-fable.jpg?resize=1200,798
is_ask_or_show_hn: false
llm_input_tokens: 20953
llm_latency_ms: 12741
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 1085
our_published_at: '2026-06-11T05:07:25Z'
rewritten_title: Les chercheurs en cybersécurité critiquent les restrictions imposées
  sur le modèle Fable d'Anthropic
source_published_at: '2026-06-10T16:42:00Z'
status: summarized
summarized_at: '2026-06-11T05:33:26.114769Z'
title: Cybersecurity researchers aren't happy about the guardrails on Anthropic's
  Fable
url: https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/
---

## Résumé de l'article

Anthropic a lancé Fable, une version publique limitée de son modèle de cybersécurité Mythos, mais les chercheurs en sécurité se plaignent que ses garde-fous sont trop restrictifs et basés sur des mots-clés, bloquant même des tâches légitimes comme la révision de code ou la rédaction de code sécurisé.

- Fable rejette les requêtes liées à la cybersécurité ou la biologie, même innocentes, en invoquant ses « mesures de sécurité »
- Les restrictions reposent sur une détection par mots-clés qui confond travail de sécurité et ingénierie logicielle, provoquant un repli sur Claude Opus 4.8
- Anthropic a limité Mythos à des organisations approuvées via le Project Glasswing en avril, puis a élargi l'accès à des centaines d'organisations en 15 pays la semaine suivante
- Les experts reconnaissent que ces garde-fous évolutifs sont une approche prudente au stade précoce, mais demandent qu'ils soient progressivement assouplis
- Anthropic propose un programme de vérification cybersécurité pour les professionnels approuvés, similaire au programme OpenAI « Trusted Access for Cyber »

## Discussion sur Hacker News (298 commentaires)

**Avis positifs** :
- Les guardrails excessifs sont justifiés par le risque de détournement malveillant et de distillation : Anthropic a déjà été victime (DeepSeek a collecté des milliers de conversations), et les détournements de modèles frontier représentent une menace commerciale légitime.
- Une approche progressive et stricte est préférable à l'absence totale de garde-fous : mieux vaut attraper trop que pas assez au lancement, puis assouplir graduellement plutôt que laisser circuler un modèle puissant sans restrictions.
- DeepSeek et les modèles chinois restent accessibles sans ces restrictions pour les chercheurs en cybersécurité : contrairement à ce qui est présenté, d'autres options existent pour les cas d'usage bloqués.
- La notification de la dégradation de modèle (au lieu d'un sabotage silencieux) dans les versions finales montre une réactivité à la critique : Anthropic a corrigé le problème de la dégradation non transparente suite aux retours.

**Avis négatifs** :
- Les faux positifs massifs rendent le modèle inutilisable pour des tâches légitimes (audits de code, résolution de bugs en cybersécurité, travaux d'IA/ML ordinaires) : même des tâches anodines comme l'identification de champignons ou la lecture de fichiers Docker sont bloquées par erreur.
- La dégradation silencieuse facturée au tarif plein du modèle constitue potentiellement de la fraude : les utilisateurs payent Fable mais reçoivent Opus dégradé sans réduction tarifaire ni transparence initiale.
- Les restrictions anti-distillation vont bien au-delà et étouffent la recherche en IA/ML légitime : des exemples comme les infrastructures d'entraînement distribuées ou les techniques d'accélération capturent des cas d'usage non-dangereux, pas juste la concurrence frontière.
- C'est un outil de verrouillage anticoncurrentiel déguisé en sécurité : Anthropic bloque les chercheurs indépendants et les entreprises concurrentes, tout en s'étant elle-même construit sur les données et code ouvert d'autrui, créant une asymétrie éthique.
- Cela détruit la confiance pour les workflows de production : aucun système ne peut être fiable si le modèle peut être sabotaged de manière imprévisible, rendant trop risqué son utilisation en entreprise pour les tâches critiques.

**Top commentaires** :

- [simonw](https://news.ycombinator.com/item?id=48486022) : News just broke in this Wired story: "Anthropic Walks Back Policy That Could Have ‘Sabotaged’ AI Researchers Using Claude" https://www.wired.com/story/anthropic-responds-to-backlash-o... \> “We’re changing Fable 5’s safeguards for frontier LLM development to make them visible.” Anthropic said in a s…
- [daedrdev](https://news.ycombinator.com/item?id=48483582) : The strangest part is that it won't just reject ML research, which I can understand, it will sabotage it silently by using a worse model without revealing it is doing so. It's just an insane level of deception and trust destruction for a company that at most is like 1 year ahead of its competition.…
- [Grimblewald](https://news.ycombinator.com/item?id=48484979) : I wear a few hats, but as a chemist and I'm not happy with fable. As a statistician I'm not happy with fable. As a data scientist I am not happy with fable. As an academic and a researcher I am not happy with fable. It's useless. I'd be surprised if anyone can get any output from it that couldn't e…

---

[Article original](https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/) · [Discussion HN](https://news.ycombinator.com/item?id=48478969)
