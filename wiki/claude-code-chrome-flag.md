# Claude Code — Flag `--chrome`

**Summary** : Option de Claude Code qui connecte le modèle à une instance Chrome locale via MCP, lui permettant de piloter des interfaces web dans un navigateur déjà authentifié.

**Sources** : `raw/ingested/claude-opus-47-lovart-brand-design.md`

**Last updated** : 2026-05-23

---

## Contenu

### Principe

```bash
claude --chrome
```

Claude Code se connecte au Chrome local via MCP (Model Context Protocol). Le modèle peut alors :
- Lire le contenu de pages web
- Cliquer sur des éléments d'interface
- Remplir des formulaires
- Uploader des fichiers
- Télécharger des résultats

**Avantage clé** : Chrome est déjà authentifié. Claude hérite de toutes les sessions ouvertes (Lovart, Figma, GitHub, etc.) sans avoir besoin de gérer des tokens ou des credentials.

### Différence vs Computer Use

| Approche | Mécanisme | Fiabilité |
|----------|-----------|-----------|
| Computer Use (screenshot) | Vision + coordonnées pixels | Fragile, lent |
| Browser MCP (`--chrome`) | API DOM structurée | Plus robuste |
| Extension navigateur | Injection JS dans la page | Dépend du site |

Le flag `--chrome` utilise le MCP browser qui expose une API structurée du DOM, contrairement au Computer Use classique qui opère par screenshot + clic sur des coordonnées.

### Cas d'usage documenté

Voir [claude-opus-47-lovart-brand-design-summary](claude-opus-47-lovart-brand-design-summary.md).

[claude-opus-47](claude-opus-47.md) pilote Lovart de bout en bout :
1. Upload d'un PDF de 47 Mo dans Brand Kit
2. Création d'un projet depuis le Brand Kit
3. Génération de poster avec prompt custom
4. Utilisation du Font Generator
5. Sauvegarde du Create Skill
6. Export PSD
7. Génération vidéo Seedance

L'utilisateur n'interagit qu'à deux moments : description de la tâche + validation finale.

### Historique / fiabilité

Avant Opus 4.7 :
- Opus 4.6 + browser extension → résultats insuffisants
- Computer Use → résultats insuffisants
- Browser MCP avec Opus 4.6 → résultats insuffisants

Avec Opus 4.7 (benchmark visuel 98.5%) : pipeline complet fonctionnel.

La fiabilité du `--chrome` est donc fortement corrélée à la capacité de perception visuelle du modèle.

### Lien avec MCP vs CLI

Voir [mcp-vs-cli-skills](mcp-vs-cli-skills.md). Le `--chrome` MCP est un cas particulier : il ne peut pas être remplacé par une CLI, car l'interface web (Lovart, Figma) n'expose pas d'API CLI. C'est le cas où le MCP est irremplaçable — à condition que le modèle soit capable de l'utiliser efficacement.

## Related pages

- [claude-opus-47](claude-opus-47.md)
- [mcp-vs-cli-skills](mcp-vs-cli-skills.md)
- [subagent-architecture](subagent-architecture.md)
- [ai-design-agent](ai-design-agent.md)
- [claude-opus-47-lovart-brand-design-summary](claude-opus-47-lovart-brand-design-summary.md)
