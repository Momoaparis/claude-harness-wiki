# Claude Code — Plugins

**Summary** : Les plugins dans Claude Code packagent des skills, MCPs et hooks en unités installables depuis un marketplace. Ils simplifient le setup mais consomment du context window — gérer les actifs avec soin.

**Sources** : `raw/ingested/the-shorthand-guide-to-everything-claude-code.md`, `raw/ingested/affaan-m-ecc-readme-part*.md`

**Last updated** : 2026-05-23

---

## Contenu

### Définition

Un plugin peut combiner :
- un ou plusieurs skills
- un MCP server
- des hooks préconfiguré

C'est une unité d'installation, pas un nouveau concept — c'est du packaging autour des primitives existantes.

### Installation

```bash
# Ajouter un marketplace
claude plugin marketplace add https://github.com/mixedbread-ai/mgrep

# Puis ouvrir Claude Code, lancer /plugins
# Naviguer jusqu'au nouveau marketplace, installer depuis là
```

### Navigation

- `/plugins` — liste les plugins installés, leur état (activé/désactivé), et les marketplaces
- `/mcp` — vue des MCP servers et leur statut

### Types de plugins notables

#### LSP Plugins

Language Server Protocol : donne à Claude des capacités d'IDE sans ouvrir un éditeur.

- **Type checking en temps réel** — erreurs TypeScript/Python au moment de l'édition
- **Go-to-definition** — navigation dans le code
- **Completions intelligentes**

Exemples :
```
typescript-lsp@claude-plugins-official  # TypeScript
pyright-lsp@claude-plugins-official    # Python
```

Utile surtout si Claude Code tourne hors d'un éditeur (terminal seul). Redondant si un éditeur est déjà ouvert avec LSP actif.

#### Hookify

Plugin officiel qui permet de créer des hooks **conversationnellement** plutôt qu'en éditant du JSON manuellement.

```
/hookify
> Je veux un hook qui lance Prettier après chaque édition de fichier .ts
```

Claude génère et configure le hook automatiquement.

#### mgrep

Plugin marketplace (Mixedbread) pour la recherche sémantique — voir [[mgrep-vs-grep]].

#### Chrome (navigateur intégré)

Plugin MCP built-in qui permet à Claude de contrôler le navigateur de façon autonome — cliquer, naviguer, observer le rendu.

### Gestion du context window

**Problème central** : chaque plugin actif (surtout les MCPs) consomme des tokens de context window. Avec trop d'outils activés, le window effectif de 200k peut tomber à ~70k.

**Règle de l'auteur** :
- Installer librement (20-30 MCPs en config)
- Garder **moins de 10 actifs** simultanément
- Maintenir **moins de 80 outils actifs** en tout

Détail des settings recommandés dans [[ecc-token-optimization]].

### Auto-loading des hooks de plugins (v2.1+)

Depuis Claude Code v2.1+, `hooks/hooks.json` des plugins installés est **automatiquement chargé**. Ne pas le redéclarer dans `plugin.json` ni le recopier dans `settings.json` — cela cause des doublons d'exécution. Cf. [[ecc-hooks-autoloading]] pour le détail.

⚠️ Cette auto-chargement est précisément la surface exploitée par [[claude-code-cves-2026|CVE-2025-59536]] : auditer les plugins tiers avant install via [[agentshield]].

**Désactivation par projet** dans `~/.claude.json` :
```json
{
  "projects": {
    "/chemin/projet": {
      "disabledMcpServers": ["playwright", "clickhouse", "AbletonMCP"]
    }
  }
}
```

La règle : activer uniquement ce qui est pertinent pour le projet courant.

**Voir aussi** : [[mcp-vs-cli-skills]] pour la stratégie CLI vs MCP.

### Marketplace officiel vs communauté

- `@claude-plugins-official` — plugins officiels Anthropic
- `@claude-code-plugins` — plugins communauté
- URLs GitHub directes — tout marketplace public

### Comparaison plugins vs skills manuels

| | Plugin | Skill manuel |
|---|---|---|
| Installation | `/plugins` marketplace | Fichier `.md` dans `~/.claude/skills/` |
| Scope | User-level par défaut | User ou project level |
| Contenu | Peut inclure MCP + hooks | Prompt / instructions uniquement |
| Contrôle | Via CLI | Direct sur le fichier |

Les deux coexistent — les plugins sont pratiques pour des outils établis, les skills manuels restent plus flexibles pour les patterns maison.

## Related pages

- [[claude-code-hooks]]
- [[mcp-vs-cli-skills]]
- [[mgrep-vs-grep]]
- [[ecc-hooks-autoloading]]
- [[ecc-token-optimization]]
- [[claude-code-cves-2026]]
- [[the-shorthand-guide-summary]]
