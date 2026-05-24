# ToxicSkills (étude Snyk, février 2026)

**Summary** : Étude Snyk publiée en février 2026 : 3984 skills publics scannés, **36 % (≈ 1434 skills) contenaient du prompt injection**, 1467 payloads malveillants identifiés (plusieurs payloads possibles par skill). Les skills tiers sont des artefacts de supply chain — à traiter comme tels.

**Sources** : `raw/ingested/the-shorthand-guide-to-everything-agentic-security.md`, Snyk *ToxicSkills: Malicious AI Agent Skills in the Wild*

**Last updated** : 2026-05-23

---

## Les chiffres

| Métrique | Valeur |
|----------|--------|
| Skills publics scannés | **3 984** |
| Skills contenant du prompt injection | **36 %** (≈ 1434) |
| Payloads malveillants identifiés | **1 467** |

Source : ClawHub (registre public de skills) au moment de l'étude.

## Pourquoi c'est un problème de supply chain

Un skill ressemble à un fichier markdown inoffensif. Mais une fois installé :

- Il est chargé en contexte automatiquement par certaines configs.
- Il peut contenir des instructions invisibles ([[prompt-injection-sanitization|Unicode caché]], commentaires HTML).
- Il peut référencer des liens externes qui changeront plus tard.
- Il peut déclencher des hooks via les patterns que [[agentshield]] détecte.

C'est la même classe de problème que les npm packages malveillants — mais sans la maturité d'outils de scan que l'écosystème npm a fini par développer.

## Conséquence pratique

> Treat skills like supply chain artifacts, because that is what they are.

Avant d'installer un skill :

1. Lire le contenu (vraiment, pas en diagonale).
2. Vérifier l'auteur, le repo source, la date de dernière modification.
3. Scanner avec [[agentshield]] ou `snyk agent-scan`.
4. Si possible, l'inliner dans le projet plutôt que de pointer vers un repo distant.
5. Préférer les skills d'écosystèmes maintenus ([[ecc-overview|ECC]]) aux skills isolés.

## Lien avec les autres surfaces

Une fois un skill malveillant chargé, il devient un vecteur pour les autres failles :

- [[prompt-injection-sanitization]] — si le skill contient du payload caché.
- [[claude-code-cves-2026]] — si le skill installe des hooks ou des MCP servers via la config.
- [[agent-memory-hygiene]] — si le skill modifie la mémoire persistée.

## Related pages

- [[agentshield]]
- [[prompt-injection-sanitization]]
- [[claude-code-cves-2026]]
- [[ecc-overview]]
- [[the-agentic-security-summary]]
