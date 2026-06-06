---
article_fetched_at: '2026-06-06T17:25:55.280235Z'
attempts: 0
content_source: extracted
discussion_comment_count: 146
discussion_fetched_at: '2026-06-06T17:25:54.621160Z'
error: null
guid: https://news.ycombinator.com/item?id=48407499
hn_item_id: 48407499
hn_url: https://news.ycombinator.com/item?id=48407499
image_url: https://www.boxofcables.dev/content/images/2026/06/Screenshot-2026-06-03-072838.png
is_ask_or_show_hn: false
llm_input_tokens: 11769
llm_latency_ms: 11452
llm_models_used:
- anthropic/claude-4.5-haiku-20251001
llm_output_tokens: 901
our_published_at: '2026-06-06T17:04:41Z'
rewritten_title: Azure Linux 4.0 devient la première distribution généraliste de Microsoft
source_published_at: '2026-06-05T03:14:28Z'
status: summarized
summarized_at: '2026-06-06T17:26:13.203644Z'
title: Azure Linux 4.0 is Microsoft's first general-purpose Linux
url: https://www.boxofcables.dev/azure-linux-4-0-is-microsofts-first-general-purpose-linux/
---

## Résumé de l'article

Azure Linux 4.0, la distribution Linux développée en interne par Microsoft, accède à la préversion publique et peut désormais s'exécuter sur n'importe quelle machine virtuelle Azure, marquant son passage d'un système d'exploitation spécialisé à une distribution généraliste.

- Azure Linux 4.0 est dérivée de Fedora 43 et abandonne l'assemblage manuel des paquets pour un modèle de suivi de Fedora avec des overlays déclaratifs documentant chaque modification.
- La pile de composants s'est modernisée : kernel 6.18 LTS, dnf5 à la place de tdnf, glibc 2.42, systemd 258, OpenSSL 3.5 et Python 3.14, avec certification FIPS 140-3 prévue.
- La distribution s'exécute sur tous les services Azure : machines virtuelles, conteneurs, AKS, et WSL, avec base distroless capable et images de conteneurs disponibles sur Microsoft Container Registry.
- Des entreprises majeures ont migré : Databricks a déplacé plus de 100 000 VMs et un million de CPU cores, LinkedIn son infrastructure entière vers Azure Linux.
- Azure Linux se distingue par une chaîne d'approvisionnement vérifiable par design, une minimalité intentionnelle (pas de bureau ni GUI) et le positionnement de Microsoft comme mainteneur majeur de distribution Linux en amont de Fedora.

## Discussion sur Hacker News (146 commentaires)

**Avis positifs** :
- Azure Linux offre une chaîne d'approvisionnement auditable et une conformité SBOM, utile pour les audits de sécurité en entreprise
- Microsoft contribue réellement à l'écosystème Linux depuis des années (kernel, WSL, Mono) et ce choix reflète une stratégie cloud légitime, similaire à celle d'Amazon et Google avec leurs propres distributions
- Basé sur Fedora/RPM, ce qui donne accès à un large écosystème de paquets et facilite l'intégration avec les services Azure
- La stratégie Microsoft de diversifier au-delà de Windows est pragmatique : Azure et Microsoft 365 sont devenus bien plus lucratifs que Windows lui-même

**Avis négatifs** :
- Le titre est trompeur : Microsoft elle-même décrit cette distribution comme « Purpose-Built for Azure », pas comme « general-purpose » ; elle manque de desktop, GUI et ne supporte que les workloads cloud/serveur
- Simplement un fork/snapshot de Fedora 43 sans amélioration claire – les différences mineures pourraient être remontées en amont ; à quoi bon au lieu d'utiliser Fedora directement ?
- Inquiétudes légitimes sur le verrouillage propriétaire : historiquement Microsoft a pratiqué l'« Embrace, Extend, Extinguish » (bien que Google soit un cas plus contemporain avec Chrome, YouTube et Gmail)
- Pigeonnage du travail de Red Hat sans compensation ; Fedora bleeding-edge n'est pas adapté aux workloads de production généraux, contrairement à RHEL, ce qui crée une fausse impression
- Manque de certification matérielle multi-cloud et de support en dehors de l'écosystème Microsoft, limitant la véritable polyvalence par rapport aux distributions traditionnelles

**Top commentaires** :

- [rswail](https://news.ycombinator.com/item?id=48411710) : OK, so this is important not because it comes from Microsoft. 1. It's general purpose in that it is designed to be used to deliver any application software, whether containerized, on a VM or on \(specific\) bare hardware. 2. It has an SBOM that allows all elements of the distribution when run as a co…
- [codycharris](https://news.ycombinator.com/item?id=48407901) : No it's not. It's for tuned for Azure. Nobody is running this outside of their compute environment.
- [froh](https://news.ycombinator.com/item?id=48407847) : call me old fashioned isn't a general purpose OS one that runs on any hardware and set up? and is certified with hardware vendors for full backing and support? all this says is: "MS now provides a unified Linux from WSL to the MS cloud. just like what you got w/ SUSE RH canonical up to now. but wit…

---

[Article original](https://www.boxofcables.dev/azure-linux-4-0-is-microsofts-first-general-purpose-linux/) · [Discussion HN](https://news.ycombinator.com/item?id=48407499)
