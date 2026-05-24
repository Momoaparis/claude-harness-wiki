# Patterns de design d'instructions

**Summary** : Trois patterns pour écrire des instructions agent qui survivent au temps : distinguer hard constraints des soft guidelines, documenter source/applicability/expiry sur chaque règle, et préférer les contraintes mécaniques aux énumérations textuelles.

**Sources** : `raw/ingested/lecture-04-split-instructions-across-files.md`

**Last updated** : 2026-05-24

---

## Contenu

### Pattern 1 : Hard vs soft

Toute règle dans une harness est de l'un des deux types :

| Type | Caractère | Format recommandé |
|------|-----------|-------------------|
| **Hard constraint** | MUST / MUST NOT — violation = bug | Bloc dédié "TOP CONSTRAINTS" en haut + check mécanique |
| **Soft guideline** | SHOULD / PREFER — violation = code review | Topic doc, exemples concrets |

Antipattern : mélanger les deux dans une même liste. L'agent n'a aucun signal sur ce qui est red-line vs suggestion.

Exemple correct :

```markdown
## TOP CONSTRAINTS (MUST)
1. Aucun `console.log` dans `src/` (use logger)
2. Aucun accès direct à la DB hors de `src/db/`
3. Toutes les routes API retournent `{success, data, error}`

## Guidelines (SHOULD, voir docs/style.md)
- Préférer la composition à l'héritage
- Limit fonctions à ~50 lignes
```

### Pattern 2 : Source / Applicability / Expiry

Chaque règle doit avoir trois métadonnées :

| Champ | But | Exemple |
|-------|-----|---------|
| **Source** | Pourquoi cette règle existe | "Bug XYZ-1234 : data corruption avec parsing inline" |
| **Applicability** | Quand elle s'applique | "Tous les endpoints qui acceptent du JSON utilisateur" |
| **Expiry** | À quoi elle disparaît | "Quand on migrera vers Zod en v3" |

Sans expiry, les règles s'accumulent indéfiniment. C'est l'origine du [[harness-rot-et-dette-technique|harness rot]].

Format pratique :

```markdown
## RULE: Parse JSON at boundary only
**Source**: Bug XYZ-1234 (mars 2026) — data corruption interne
**Applicability**: Tous les endpoints `POST /api/*`
**Expiry**: Migration vers Zod v3 (Q3 2026)

Detail: ...
```

### Pattern 3 : Constrain, don't micromanage

Mauvais : énumérer ce que l'agent doit faire.

```
- Utiliser la library X
- Mettre les imports dans cet ordre Y
- Nommer les variables comme Z
- ...
```

Bon : encoder l'invariant comme **check mécanique** (voir [[architectural-boundary-enforcement]]).

```bash
# Check: pas d'import direct de fs dans renderer
grep -r "require('fs')" src/renderer/ && exit 1
```

> "Enforce invariants; don't micromanage implementation." — Lecture 10

### Pattern bonus : Worker / checker separation

Dans les instructions, séparer ce qui s'adresse à l'agent qui **fait** du travail de ce qui s'adresse au **checker**.

- Worker instructions → `AGENTS.md` (ou topic docs)
- Checker rubric → `evaluator-rubric.md` (voir [[template-evaluator-rubric]])

Voir [[worker-checker-separation]].

### Comment auditer les instructions existantes

1. Pour chaque règle : peut-on identifier la source ? Sinon → la marquer "?" et investiguer.
2. Pour chaque règle : peut-on l'encoder en check ? Si oui, faire le check + supprimer le texte.
3. Pour chaque règle : encore valable aujourd'hui ? Si non → supprimer.
4. Compter le ratio MUST / SHOULD. Si toutes les règles sont MUST, l'agent ne peut plus prioriser.

### Le piège de l'accumulation

Une harness mal disciplinée suit ce cycle :

```
Agent fails → "ajoute une règle" → ajouté → 
même type d'échec re-prod → "ajoute une autre règle" →
600 lignes plus tard → l'agent ignore tout
```

Voir [[modular-instruction-architecture]] et [[lost-in-the-middle-effect]] pour les conséquences.

**Solution** : à chaque ajout de règle, demander :
1. Est-ce un cas isolé ou un pattern ?
2. Est-ce encodable en check mécanique ?
3. Y a-t-il déjà une règle qui le couvre (qu'on n'a pas appliquée) ?

### À retenir

1. **Hard vs soft** explicite. Pas de mélange.
2. **Source + applicability + expiry** sur chaque règle.
3. **Constrain via mécanique**, pas via énumération.
4. **Auditer périodiquement**. Supprimer ce qui est expiré.
5. Une règle de plus = un risque de [[lost-in-the-middle-effect|lost-in-the-middle]] de plus.

## Related pages

- [[modular-instruction-architecture]]
- [[lost-in-the-middle-effect]]
- [[architectural-boundary-enforcement]]
- [[worker-checker-separation]]
- [[harness-rot-et-dette-technique]]
- [[the-harness-engineering-curriculum-summary]]
