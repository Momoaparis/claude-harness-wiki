# Lost in the Middle effect

**Summary** : Les LLMs utilisent l'information située au milieu d'un long contexte significativement moins bien qu'aux extrémités. Une contrainte critique placée à la ligne 300 d'un `AGENTS.md` de 600 lignes a une forte probabilité d'être ignorée.

**Sources** : `raw/ingested/lecture-04-split-instructions-across-files.md` (citant Liu et al. 2023)

**Last updated** : 2026-05-24

---

## Contenu

### Le phénomène

**Liu et al. 2023** ("Lost in the Middle: How Language Models Use Long Contexts") ont montré expérimentalement que :

- Les LLMs ont une excellente recall sur l'info en **début** de contexte
- Les LLMs ont une bonne recall sur l'info en **fin** de contexte
- Les LLMs ont une recall **dégradée** sur l'info au **milieu**

Forme typique de la courbe : un U inversé, avec un creux marqué au milieu.

### Profil de recall

```
recall
 100% ┤█                                          █
      │██                                       ██
  75% ┤███                                  ████
      │ ████                            ████
  50% ┤   ████                       ████
      │      ████                ████
  25% ┤         █████        █████
      │              ██████ ██
   0% └─────────────────────────────────────
       début          milieu             fin
                  (position dans le contexte)
```

### Implications pour la harness

Si une règle critique est buried au milieu d'un long `AGENTS.md` :

> "the agent will almost certainly ignore it" — Lecture 04

Conséquence : pas seulement "moins bien", mais **systématiquement raté**. Si la règle est importante, sa position est non-négociable.

### Positions privilégiées

| Zone | Recall | Quoi y mettre |
|------|--------|---------------|
| **Top** | Haute | Overview, hard constraints, commandes |
| **Bottom** | Haute | Current state, next steps, pointeurs |
| **Milieu** | Basse | À éviter ; sortir en topic docs |

### Stratégies pratiques

#### 1. Limiter la longueur

Le moyen le plus simple : maintenir l'entry file à 50-200 lignes. À cette taille, il n'y a presque pas de "milieu" — tout est lu.

Voir [modular-instruction-architecture](modular-instruction-architecture.md).

#### 2. Sortir le contenu long en topic docs

Si une section devient longue (>30 lignes), la migrer vers `docs/topic.md` et garder un pointeur dans l'entry file.

#### 3. Encadrer les contraintes critiques

Si une règle doit absolument être respectée et qu'elle ne tient pas en haut, l'encadrer :

```markdown
## TOP CONSTRAINTS (NEVER VIOLATE)
1. Pas d'écriture directe à la DB hors src/db/
2. Pas de `console.log` en prod
3. ...

## Rest of doc
...

## CRITICAL REMINDER (BOTTOM)
Voir les TOP CONSTRAINTS ci-dessus avant de finir.
```

Répétition top + bottom = double recall.

#### 4. Encoder en mécanique

Plutôt que de risquer que l'agent ignore une règle textuelle, encoder en **check exécutable** (lint, pre-commit, CI). L'agent ne peut pas violer une règle qui fail la build.

Voir [architectural-boundary-enforcement](architectural-boundary-enforcement.md).

### Lien avec le context budget

Le lost-in-the-middle se combine avec le [context budget eaten](modular-instruction-architecture.md) :

- Long entry file → context bouffé + règles au milieu ignorées
- Court entry file + topic docs → context préservé + chaque doc tient en zones haute-recall

Double bénéfice.

### Mesurer chez soi

Test simple :
1. Prendre un `AGENTS.md` long avec une règle critique au milieu
2. Demander à l'agent de faire une tâche qui touche cette règle
3. Voir si la règle est respectée
4. Refaire en mettant la règle en haut → comparer

Si le comportement change → le lost-in-the-middle te touche.

### À retenir

1. Effet documenté (Liu et al. 2023) : recall en U inversé.
2. **Milieu = zone d'ignorance**. Ne rien y mettre de critique.
3. Top + Bottom = positions privilégiées.
4. Solution structurelle : entry file court + topic docs.
5. Solution radicale : encoder en check mécanique, pas en texte.

## Related pages

- [modular-instruction-architecture](modular-instruction-architecture.md)
- [instruction-design-patterns](instruction-design-patterns.md)
- [architectural-boundary-enforcement](architectural-boundary-enforcement.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
