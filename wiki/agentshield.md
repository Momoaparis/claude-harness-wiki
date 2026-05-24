# AgentShield

**Summary** : Scanner de sécurité pour les configurations Claude Code, construit pendant le Claude Code Hackathon (Cerebral Valley × Anthropic, fév 2026). Détecte hooks malveillants, injection patterns, permissions trop larges, MCP risqués, exposition de secrets. Fait partie de l'écosystème [[ecc-overview|ECC]].

**Sources** : `raw/ingested/the-shorthand-guide-to-everything-agentic-security.md`, `raw/ingested/affaan-m-ecc-readme-part*.md`

**Last updated** : 2026-05-23

---

## Usage rapide

```bash
# Scan rapide (pas d'install)
npx ecc-agentshield scan

# Auto-fix des issues sûres
npx ecc-agentshield scan --fix

# Analyse profonde avec trois agents Opus 4.6
npx ecc-agentshield scan --opus --stream

# Génère une config sécurisée from scratch
npx ecc-agentshield init
```

Côté Claude Code, raccourci `/security-scan`. Côté CI, GitHub Action disponible.

## Ce qu'il scanne

5 catégories sur `CLAUDE.md`, `settings.json`, configs MCP, hooks, agent definitions, skills :

1. **Secrets detection** — 14 patterns.
2. **Permission auditing** — deny rules manquantes, write trop large.
3. **Hook injection analysis** — commandes shell dans hooks, sources non fiables.
4. **MCP server risk profiling** — over-privileged, source non vérifiée.
5. **Agent config review** — model overrides, prompts à risque.

Stats du repo : 1282 tests, 98 % coverage, 102 règles statiques.

## Le mode `--opus`

Pipeline à trois agents Opus 4.6 :

- **Attacker** (red team) — cherche les exploit chains.
- **Defender** (blue team) — évalue les protections existantes.
- **Auditor** — synthétise les deux en risk assessment priorisé.

Raisonnement adversarial, pas juste matching de patterns. Coûteux mais utile sur des configs critiques.

## Output

- Terminal : grade A-F coloré
- JSON : pipelines CI
- Markdown et HTML : rapports
- Exit code 2 sur findings critiques → utilisable comme build gate

## Lien avec les CVEs Claude Code

AgentShield est en grande partie une réaction aux [[claude-code-cves-2026|CVEs de février 2026]]. Les vecteurs qu'il cherche (hooks, MCP consent, env vars repo-controlled) sont exactement ceux qui ont été exploités. Voir aussi [[toxicskills-study]] pour le même angle sur les skills.

## Related pages

- [[claude-code-cves-2026]]
- [[ecc-overview]]
- [[toxicskills-study]]
- [[prompt-injection-sanitization]]
- [[the-agentic-security-summary]]
