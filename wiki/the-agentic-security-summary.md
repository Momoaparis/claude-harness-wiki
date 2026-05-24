# The Shorthand Guide to Everything Agentic Security — Résumé

**Summary** : Article de fond d'Affaan Mustafa (26 fév 2026) sur la sécurité des agents IA. Cadre les vulnérabilités récentes (CVEs Claude Code de février 2026, ToxicSkills, AI Recommendation Poisoning) et propose un standard minimal d'opsec pour 2026.

**Sources** : `raw/ingested/the-shorthand-guide-to-everything-agentic-security.md`

**Last updated** : 2026-05-23

---

## Thèse centrale

> *« Never let the convenience layer outrun the isolation layer. »*

Avec l'adoption massive des harnesses d'agents (Claude Code, Codex, OpenClaw, Cursor), la surface d'attaque s'étend rapidement. Le [[prompt-injection-sanitization|prompt injection]] n'est plus une curiosité — c'est devenu un vecteur de RCE, d'exfiltration de secrets, et de mouvement latéral. Le guide pose le standard minimum pour 2026.

## Constats déclencheurs

- [[claude-code-cves-2026]] : CVE-2025-59536 (CVSS 8.7) et CVE-2026-21852 démontrent que les fichiers de config (hooks, MCP, env vars) sont déjà du code exécutable, **avant même** l'acceptation du trust dialog.
- Étude Snyk **[[toxicskills-study]]** (fév 2026) : 36 % de 3984 skills publics scannés contenaient du prompt injection.
- Microsoft **[[agent-memory-hygiene|AI Recommendation Poisoning]]** (10 fév 2026) : la mémoire long terme devient un vecteur de persistance — le payload n'a plus besoin de gagner d'un coup.
- 17 470 instances OpenClaw exposées sur Internet selon Hunt.io (CVE-2026-25253).

## Cadre de défense

Le guide est organisé autour de 6 piliers, chacun a sa page dédiée :

1. **[[lethal-trifecta]]** — diagnostic : quand isoler ?
2. **[[agent-sandboxing]]** + **[[agent-identity-separation]]** — limiter le rayon d'explosion
3. **[[prompt-injection-sanitization]]** — frontière runtime sur tout texte entrant
4. **[[least-agency]]** — politique entre modèle et action (jamais le modèle comme autorité finale)
5. **[[agent-observability]]** — logger pour détecter
6. **[[agent-kill-switches]]** — pouvoir arrêter quand ça part en vrille
7. **[[agent-memory-hygiene]]** — mémoire narrow et jetable

Outils nommés : [[agentshield]] (scanner ECC), Snyk `agent-scan`, OWASP MCP Top 10.

## Lien avec le reste du wiki

Même auteur que [[the-longform-guide-summary]] et [[the-shorthand-guide-summary]]. Ces deux guides montrent *comment* tirer le maximum de Claude Code ; celui-ci montre *quels risques* cette puissance crée et comment les contenir.

## Related pages

- [[lethal-trifecta]]
- [[claude-code-cves-2026]]
- [[agent-sandboxing]]
- [[agent-identity-separation]]
- [[least-agency]]
- [[prompt-injection-sanitization]]
- [[agent-observability]]
- [[agent-kill-switches]]
- [[agent-memory-hygiene]]
- [[agentshield]]
- [[toxicskills-study]]
- [[ecc-overview]]
