# Architecture modulaire des instructions

**Summary** : Un giant `AGENTS.md` de 600 lignes est pire qu'inefficace — il gaspille le context window, dilue le signal, et enterre les contraintes critiques au milieu (où l'agent les ignore). Structure correcte : entry file court (50-200 lignes) + topic documents on-demand.

**Sources** : `raw/ingested/lecture-04-split-instructions-across-files.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le problème : instruction bloat

Quand toutes les instructions s'accumulent dans un seul `AGENTS.md` :

| Problème | Impact |
|----------|--------|
| **Context budget eaten** | 600 lignes ≈ 10-20K tokens ≈ 10-15% de la fenêtre |
| **[[lost-in-the-middle-effect|Lost in the middle]]** | Les règles au milieu sont ignorées par le modèle |
| **Cant-tell-what-matters** | Hard constraints et soft guidelines mélangées, l'agent ne sait pas |
| **Priority conflicts** | Règles ajoutées à différents moments se contredisent |
| **Maintenance decay** | Personne n'ose supprimer, donc le fichier grandit seul |

### Le cas réel : SaaS team (Lecture 04)

| État | Lignes AGENTS.md | Taux de succès | Compliance sécurité |
|------|------------------|----------------|---------------------|
| Avant split | 600 | **45%** | **60%** |
| Après split (entry 80 + topic docs) | 80 + 260 répartis | **72%** | **95%** |

L'agent ne lit plus 600 lignes pour chaque tâche — il lit 80 lignes + le(s) topic doc(s) pertinent(s).

### La structure recommandée

```
AGENTS.md (entry file, 50-200 lignes)
   │
   ├── Overview projet (5 lignes)
   ├── Stack tech (10 lignes)
   ├── Commandes (10 lignes)
   ├── Hard constraints (15 lignes max)
   └── Pointeurs vers docs/
         │
docs/
├── api-patterns.md (120 lignes)
├── database-rules.md (60 lignes)
├── testing-standards.md (80 lignes)
└── deployment.md (90 lignes)
```

L'agent lit `AGENTS.md` toujours. Il lit `docs/api-patterns.md` **seulement** quand il travaille sur l'API.

### Reveal on demand (progressive disclosure)

Métaphore du cours : "packing cubes". Pas tout dans un seul sac. Chaque cube contient un sujet. On ouvre le cube quand on en a besoin.

Principe d'UX de Jakob Nielsen appliqué à la doc agent : **progressive disclosure**. Ne pas dumper toutes les options à la fois.

### Critères pour chaque topic document

| Critère | Cible |
|---------|-------|
| Taille | 50-150 lignes |
| Cohérence thématique | Un seul sujet |
| Localisation | `docs/` au root **ou** à côté du module concerné |
| Référence depuis entry file | Lien explicite : "Pour la convention API, voir docs/api-patterns.md" |

### Le format entry file

```markdown
# Project XYZ

## Stack
Node 20, TypeScript, Postgres, Redis

## How to run
- `make setup` — install
- `make dev` — local server
- `make test` — full test suite

## Hard constraints (must follow)
1. Pas de `console.log` en prod (use logger)
2. Pas d'accès DB hors du module `src/db/`
3. Tous les endpoints retournent `{success, data, error}`

## Topic docs
- `docs/api-patterns.md` — conventions API
- `docs/database-rules.md` — schéma et migrations
- `docs/testing-standards.md` — tests
- `docs/deployment.md` — CI/CD

## Current state
Voir `PROGRESS.md`
```

Court. Routing-oriented. Pas de détail noyé.

### Les deux écoles convergent

- **OpenAI** : "Entry files must be short and routing-oriented."
- **Anthropic** : "Concise and high-priority."

Message identique : ne pas stuffer tout dans un fichier.

### Anti-pattern : "add a rule when bug" cycle

```
Agent fails → équipe ajoute une règle dans AGENTS.md → fix temporaire
→ même type de bug reproduit → ajout d'une autre règle → ...
→ AGENTS.md à 600 lignes → agent ignore les règles → tout casse
```

**Solution** : encoder les règles en checks mécaniques (voir [[architectural-boundary-enforcement]]), pas en accumulation textuelle.

### Le never-bury-middle principle

Pour ce qui reste dans l'entry file : les choses **critiques** vont **en haut ou en bas**, jamais au milieu. Le [[lost-in-the-middle-effect|lost-in-the-middle]] est un effet documenté du modèle.

Si une règle est trop importante pour être en bas et trop longue pour être en haut → la sortir dans un topic doc, pas la laisser au milieu.

### Documentation de chaque instruction

Chaque règle dans la harness doit avoir :

| Champ | Exemple |
|-------|---------|
| **Source** | "Décision après bug XYZ-1234 en mars 2026" |
| **Applicability** | "Quand on touche au module auth" |
| **Expiry condition** | "Quand on migre vers OAuth2" |

Sans expiry, les règles s'accumulent. Audit régulier : règle encore valable ? Sinon → supprimer.

### À retenir

1. **Entry file 50-200 lignes**. Topic docs 50-150 lignes.
2. **Progressive disclosure** : reveal on demand, pas tout d'un coup.
3. **Source + applicability + expiry** sur chaque règle.
4. **Hard constraints au top**. Soft guidelines dans topic docs.
5. Encoder en [[architectural-boundary-enforcement|checks mécaniques]] plutôt qu'accumuler du texte.

## Related pages

- [[lost-in-the-middle-effect]]
- [[instruction-design-patterns]]
- [[architectural-boundary-enforcement]]
- [[repository-as-system-of-record]]
- [[template-claude-md]]
- [[the-harness-engineering-curriculum-summary]]
