# ECC — Auto-loading des hooks (Claude Code v2.1+)

**Summary** : À partir de Claude Code v2.1, les `hooks/hooks.json` des plugins installés sont **chargés automatiquement par convention**. Les déclarer explicitement dans `.claude-plugin/plugin.json` ou les recopier dans `settings.json` cause des erreurs de duplication et des exécutions multiples.

**Sources** : `raw/ingested/affaan-m-ecc-readme-part*.md`

**Last updated** : 2026-05-23

---

## Le piège

À partir de Claude Code v2.1+, **Claude Code charge automatiquement** `hooks/hooks.json` de chaque plugin installé. C'est une convention silencieuse.

Si tu déclares explicitement le champ `"hooks"` dans `.claude-plugin/plugin.json`, tu obtiens :

```
Duplicate hooks file detected: ./hooks/hooks.json resolves to already-loaded file
```

Historique côté ECC : issues #29, #52, #103 — un cycle fix/revert répété, parce que le comportement a changé entre versions de Claude Code. Un test de régression empêche désormais la réintroduction.

## Pour les contributeurs au repo ECC

> **WARNING:** Do NOT add a `"hooks"` field to `.claude-plugin/plugin.json`.

Enforced par regression test.

## Pour les utilisateurs

### Installation via le script ECC

Si tu installes ECC via le script, **n'utilise pas** une copie brute de `hooks/hooks.json` dans `~/.claude/settings.json` ou `~/.claude/hooks/hooks.json` — les chemins ne seraient pas réécrits correctement.

Commande propre :

```bash
# macOS / Linux
bash ./install.sh --target claude --modules hooks-runtime

# Windows PowerShell
pwsh -File .\install.ps1 --target claude --modules hooks-runtime
```

Le script écrit des hooks résolus dans `~/.claude/hooks/hooks.json` et **ne touche pas** au `settings.json` existant.

### Installation via `/plugin install`

Si tu as installé ECC via `/plugin install`, **ne pas** copier les hooks dans `settings.json`. Claude Code v2.1+ les auto-load. Doublonner cause :

- Doublons d'exécution
- Conflits de hooks cross-platform

### Note Windows

Le répertoire de config Claude Code sur Windows est `%USERPROFILE%\.claude`, pas `~/claude`. Erreur fréquente.

## Lien sécurité

Cet auto-loading est précisément ce qui rend les [CVEs de février 2026](claude-code-cves-2026.md) graves : les hooks d'un repo poisoné sont chargés **avant** la fenêtre de trust. Conclusion :

- Ne jamais cloner un repo inconnu sans [sandbox](agent-sandboxing.md).
- Auditer les `hooks/hooks.json` des plugins avant install via [agentshield](agentshield.md).

## Configuration MCP — note adjacente

Les installs plugin de Claude intentionnellement **n'auto-enable pas** les MCP servers bundlés par ECC (pour éviter les noms trop longs sur les gateways tiers). Setup manuel via `/mcp` ou en copiant depuis `mcp-configs/mcp-servers.json` vers `.mcp.json`.

Si tu run déjà tes propres copies des MCPs bundlés :

```bash
export ECC_DISABLED_MCPS="github,context7,exa,playwright,sequential-thinking,memory"
```

C'est un filtre install/sync, **pas** un toggle Claude Code runtime.

## Related pages

- [claude-code-hooks](claude-code-hooks.md)
- [claude-code-cves-2026](claude-code-cves-2026.md)
- [agentshield](agentshield.md)
- [ecc-overview](ecc-overview.md)
- [claude-code-plugins](claude-code-plugins.md)
