# Model Selection (Haiku / Sonnet / Opus)

**Summary** : Critères pour choisir entre les modèles Claude (Haiku, Sonnet, Opus) selon la nature de la tâche et le coût acceptable.

**Sources** : `raw/ingested/the-longform-guide-to-everything-claude-code.md`, `raw/ingested/affaan-m-ecc-readme-part*.md`, `raw/ingested/claude-opus-47-lovart-brand-design.md`

**Last updated** : 2026-05-23

---

## Contenu

### Règles par défaut

| Modèle | Quand l'utiliser |
|--------|------------------|
| **Sonnet** | Défaut pour ~90% des tâches de coding |
| **Opus** | Première tentative a échoué, tâche sur 5+ fichiers, décisions architecturales, code sécurité-critique |
| **Haiku** | Tâche répétitive, instructions très claires, rôle de "worker" dans un setup multi-agent |

### Pricing (Anthropic, fin 2025)

| Modèle | Input ($/M tokens) | Output ($/M tokens) |
|--------|--------------------|--------------------|
| Haiku | ~$1 | ~$5 |
| Sonnet 4.5 | $3 | $15 |
| Opus 4.5 | $15 | $75 |

### Analyse coût-rapport

- **Haiku vs Sonnet** : différence 3x — économie significative si Haiku suffit
- **Sonnet vs Opus** : différence 5x — économie majeure
- **Haiku vs Opus** : différence ~15x — combo le plus impactant

> "Sonnet 4.5 sits in a weird spot — relatively close en prix à Opus" → l'auteur recommande **Haiku + Opus** comme combo le plus impactant économiquement, en réservant Sonnet pour les cas où Haiku échoue.

### Mode dégradation / upgrade

Workflow recommandé :
1. Commencer par Haiku si la tâche semble simple
2. Si échec → Sonnet
3. Si échec persistant ou tâche très complexe → Opus

### Lien avec sub-agents

L'assignation du modèle se fait par sub-agent — voir [subagent-architecture](subagent-architecture.md).

### Settings ECC recommandés

[ECC](ecc-overview.md) cible **`model: sonnet`** comme défaut global (vs `opus`) pour ~60% de réduction de coût sur 80%+ des tâches. Et pour les subagents :

```json
{ "env": { "CLAUDE_CODE_SUBAGENT_MODEL": "haiku" } }
```

Détail complet dans [ecc-token-optimization](ecc-token-optimization.md).

### Opus 4.7 — capacités spécifiques

[claude-opus-47](claude-opus-47.md) introduit deux améliorations majeures qui influencent le choix du modèle :

- **Perception visuelle** : benchmark 54.5% → 98.5% — rend Opus 4.7 pertinent pour les tâches impliquant des images, screenshots, ou interfaces graphiques
- **Self-verification** : relance autonome si l'output est jugé insuffisant → moins d'allers-retours utilisateur sur les tâches longues
- **Computer Use** : pilotage de navigateur via [`--chrome`](claude-code-chrome-flag.md) MCP, fiable là où Opus 4.6 échouait

Ajouter Opus 4.7 aux cas d'usage : tâches visuelles, agents long-running, orchestration d'interfaces web.

## Related pages

- [subagent-architecture](subagent-architecture.md)
- [agent-abstraction-tierlist](agent-abstraction-tierlist.md)
- [modular-codebase-tokens](modular-codebase-tokens.md)
- [ecc-token-optimization](ecc-token-optimization.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
- [claude-opus-47](claude-opus-47.md)
