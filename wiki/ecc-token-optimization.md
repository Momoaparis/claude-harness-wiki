# ECC — Optimisation tokens

**Summary** : Settings `~/.claude/settings.json` recommandés par ECC pour réduire ~60% le coût Claude Code sans sacrifier la qualité. Cible : modèle par défaut, budget de thinking, seuil d'autocompact, et modèle des subagents.

**Sources** : `raw/ingested/affaan-m-ecc-readme-part*.md`

**Last updated** : 2026-05-23

---

## Config recommandée

Dans `~/.claude/settings.json` :

```json
{
  "model": "sonnet",
  "env": {
    "MAX_THINKING_TOKENS": "10000",
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50",
    "CLAUDE_CODE_SUBAGENT_MODEL": "haiku"
  }
}
```

## Impact détaillé

| Setting | Default | Recommandé | Impact |
|---------|---------|------------|--------|
| `model` | opus | **sonnet** | ~60 % de réduction de coût ; couvre 80-90 % des tâches de coding |
| `MAX_THINKING_TOKENS` | 31 999 | **10 000** | ~70 % de réduction du thinking caché par requête |
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | 95 | **50** | Compacte plus tôt → meilleure qualité en session longue |
| `CLAUDE_CODE_SUBAGENT_MODEL` | (inherits) | **haiku** | Subagents en Haiku — voir [subagent-architecture](subagent-architecture.md) |
| `ECC_CONTEXT_MONITOR_COST_WARNINGS` | on | **off** (subs) | Coupe les warnings API-rate inutiles si tu es en subscription |

## Quand basculer en Opus

```
/model opus
```

Réservé aux moments qui le justifient : architecture profonde, debug épineux, raisonnement complexe. Cf. [model-selection-claude](model-selection-claude.md).

## Daily workflow commands

| Commande | Usage |
|----------|-------|
| `/model sonnet` | Default pour la majorité des tâches |
| `/model opus` | Architecture, debug profond |
| `/clear` | Entre tâches sans rapport (gratuit, instantané) |
| `/compact` | Aux breakpoints logiques — cf. [strategic-compact](strategic-compact.md) |
| `/cost` | Monitor le spending en session |

## Plafond MCP / tools

> **Critical:** Don't enable all MCPs at once.

Chaque description de tool MCP consomme des tokens de la fenêtre 200k — potentiellement jusqu'à la réduire à ~70k.

Règles ECC :

- **Moins de 10 MCPs** enabled par projet.
- **Moins de 80 tools** actifs.
- `/mcp` pour disabler les MCPs Claude Code (persisté dans `~/.claude.json`).
- `ECC_DISABLED_MCPS` n'est qu'un filtre install/sync ECC — pas un toggle runtime.

Cf. [mcp-vs-cli-skills](mcp-vs-cli-skills.md) pour la stratégie de remplacement.

## Agent Teams — alerte coût

Agent Teams spawn plusieurs context windows. Chaque teammate consomme des tokens indépendamment. À réserver aux tâches où la parallélisation a une valeur claire (multi-module, reviews parallèles). Pour les tâches séquentielles simples, les subagents sont plus économes — voir [subagent-architecture](subagent-architecture.md).

## Lien avec strategic compact

Le skill `strategic-compact` (bundlé dans ECC) suggère `/compact` aux breakpoints logiques plutôt que d'attendre l'auto-compact à 95 % du contexte. Cf. [strategic-compact](strategic-compact.md) pour le détail.

## Related pages

- [model-selection-claude](model-selection-claude.md)
- [strategic-compact](strategic-compact.md)
- [subagent-architecture](subagent-architecture.md)
- [mcp-vs-cli-skills](mcp-vs-cli-skills.md)
- [modular-codebase-tokens](modular-codebase-tokens.md)
- [ecc-overview](ecc-overview.md)
