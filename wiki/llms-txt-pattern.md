# llms.txt Pattern

**Summary** : Convention émergente où les sites de documentation exposent une version `llms.txt` optimisée pour les LLMs, à consommer directement par Claude.

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

### La convention

De plus en plus de plateformes exposent une route `/llms.txt` sur leur site de documentation. Ce fichier est une version :
- **Plate** (markdown ou texte brut)
- **Concise** (pas de boilerplate UI)
- **Structurée** pour la consommation par LLM

### Exemple

Helius (blockchain) : https://www.helius.dev/docs/llms.txt

### Comment l'utiliser

Quand Claude se plante sur une API ou un SDK :
1. Aller sur le site de docs
2. Tester `/llms.txt` au bout de l'URL
3. Si présent, le feeder directement à Claude

```bash
curl https://www.helius.dev/docs/llms.txt | claude
```

ou inline dans une session :
```
"Voici la doc à jour : <coller le contenu de llms.txt>"
```

### Pourquoi c'est mieux

| Méthode | Coût | Qualité |
|---------|------|---------|
| Context7 MCP | Tokens à chaque call | Bonne |
| Firecrawl du site | Tokens élevés (HTML/JS) | Variable selon le site |
| `llms.txt` | Minimal | Optimisée pour LLM |

### Quand utiliser quoi

- **`llms.txt` disponible** → premier choix, le plus économique
- **Sinon Context7** → si la lib y est indexée
- **Sinon Firecrawl** → en dernier recours, pour scraper le site

### Phase de découverte

Au démarrage d'un projet, **vérifier la présence d'un `llms.txt`** sur tous les services qu'on va utiliser. Le sauvegarder localement permet une référence offline rapide.

### Lien avec le kickoff

S'intègre naturellement dans le [[two-instance-kickoff]] : l'instance "deep research" collecte les `llms.txt` disponibles et les met dans le projet.

## Related pages

- [[two-instance-kickoff]]
- [[mcp-vs-cli-skills]]
- [[the-longform-guide-summary]]
