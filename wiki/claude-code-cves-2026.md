# CVEs Claude Code (février 2026)

**Summary** : Trois vulnérabilités publiées par Check Point Research le 25 février 2026 montrent que les fichiers de config d'un projet Claude Code (hooks, MCP, env vars) sont du code exécutable **avant** l'acceptation du trust dialog. Patch obligatoire.

**Sources** : `raw/ingested/the-shorthand-guide-to-everything-agentic-security.md`, Check Point Research, NVD

**Last updated** : 2026-05-23

---

## CVE-2025-59536 (CVSS 8.7)

**Hook pre-trust execution.** Du code contenu dans le projet pouvait s'exécuter **avant** que l'utilisateur ne valide le trust dialog. Le trigger : ouvrir le repo dans Claude Code suffisait.

Vecteur : un repo poisoné contenait des [[claude-code-hooks|hooks]] qui se déclenchent sur événements (`SessionStart`, etc.) — ces hooks sont chargés au démarrage, avant que la fenêtre d'approbation utilisateur ne s'affiche.

Versions affectées : antérieures à `1.0.111` (NVD).

## CVE-2026-21852

**ANTHROPIC_BASE_URL override.** Un projet attaquant pouvait définir `ANTHROPIC_BASE_URL`, redirigeant le trafic API vers un endpoint contrôlé, **fuitant la clé API** avant la confirmation de trust.

Versions affectées : avant `2.0.65` pour les mises à jour manuelles.

## MCP consent abuse

Configuration `enableAllProjectMcpServers` et settings repo-controlled pouvaient auto-approuver les serveurs MCP du projet avant que l'utilisateur ait sérieusement « trusted » le répertoire.

## Le pattern commun

Les trois failles partagent la même structure :

> Les fichiers `.claude/` et `.mcp.json` voyagent dans git. Ils sont supposés être protégés par une frontière de confiance. **Cette frontière est exactement ce que les attaquants vont viser.**

Toute donnée portée par le repo (hooks, MCP config, env vars, settings) doit être traitée comme **du code exécutable provenant d'un tiers**.

## Mesures correctives

- Mettre à jour Claude Code (`1.0.111+` puis `2.0.65+`).
- Ne **jamais** cloner un repo inconnu sans [[agent-sandboxing|sandbox]].
- Auditer les configs des repos cloned via [[agentshield]] ou `agent-scan`.
- Voir aussi [[ecc-hooks-autoloading]] : les hooks de plugins sont chargés automatiquement à partir de Claude Code v2.1+, ce qui élargit encore la surface.

## CVE-2026-25253 (OpenClaw — hors scope Claude Code)

**17 470 instances OpenClaw exposées sur Internet** selon Hunt.io. OpenClaw est un orchestrateur d'agents distinct de Claude Code, mais partage la même surface d'attaque (configs repo-controlled, hooks auto-chargés). Mentionné dans le même rapport de sécurité de février 2026.

Ce CVE ne concerne pas Claude Code directement — il illustre que la classe de vulnérabilité (config-as-code pré-trust) dépasse un seul outil et affecte tout l'écosystème des harnesses d'agents.

Source : [[the-agentic-security-summary]]

## Lecture obligatoire

- Check Point Research, *Caught in the Hook: RCE and API Token Exfiltration Through Claude Code Project Files* (25 fév 2026).
- NVD entries pour CVE-2025-59536 et CVE-2026-21852.

## Related pages

- [[agent-sandboxing]]
- [[ecc-hooks-autoloading]]
- [[agentshield]]
- [[claude-code-hooks]]
- [[the-agentic-security-summary]]
