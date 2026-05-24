# Principes ACID appliqués au state d'un agent

**Summary** : Les principes des transactions DB (Atomicity, Consistency, Isolation, Durability) s'appliquent au state d'un agent. Les violations sont la cause profonde de la divergence entre sessions et des "demi-commits" dangereux.

**Sources** : `raw/ingested/lecture-03-making-the-repository-the-single-source-of-truth.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le mapping

| Principe ACID | Application agent | Mécanisme concret |
|---------------|-------------------|-------------------|
| **A**tomicity | 1 commit = 1 opération logique complète | Pas de demi-commit, pas de "WIP unsaved" |
| **C**onsistency | Vérification après chaque opération | `make test` doit passer ; sinon rollback |
| **I**solation | Concurrence = branches/fichiers séparés | [[git-worktrees-parallel-claude|Git worktrees]], branches dédiées |
| **D**urability | Git = persistent ; session memory = temporaire | Tout state critique vit dans le repo, pas dans la conversation |

### Atomicity

Un commit doit représenter **une opération logique complète**. Pas "j'ai écrit du code mais les tests ne passent pas encore".

Antipattern :
```
commit abc123: "WIP: started auth module"
commit def456: "WIP: more auth stuff"  
commit ghi789: "fix tests"
```

Pattern correct :
```
commit abc123: "feat(auth): add password validation with tests passing"
```

Si on ne peut pas commit atomiquement → la tâche est trop grosse ([[atomic-task-decomposition|atomic task decomposition]]).

### Consistency

Après chaque opération atomique, l'état doit être **cohérent** :

- Tests passent
- Build passe
- Linter clean
- `feature_list.json` reflète la réalité

C'est exactement le sens du [[session-clean-handoff|clean state]] de la Lecture 12. Les 5 conditions = vérification de consistency.

### Isolation

Plusieurs agents en parallèle ne doivent **pas se marcher dessus**. Mécanismes :

- **Git worktrees** ([[git-worktrees-parallel-claude]]) : un dossier de travail par agent
- **Branches dédiées** : un agent = une branche
- **Fichiers séparés** : si possible, partitionner le travail par fichier/module

Voir aussi [[cascade-method]] pour l'organisation pratique de tabs parallèles.

### Durability

Le state qui doit survivre à la fin de session **doit être dans le repo** (commit), pas dans la conversation. La conversation est volatile.

Conséquence pratique :
- Décisions importantes → `DECISIONS.md` (voir [[decision-log-pattern]])
- État courant → `PROGRESS.md` ou `claude-progress.md` (voir [[progress-file-pattern]])
- Hypothèses ou contraintes découvertes → fichier dédié dans `docs/`

### Le risque du demi-commit

Sans atomicity stricte, on aboutit à des états "ni avant ni après" :

```
État repo: feature A à moitié codée
État repo: tests A à moitié écrits, certains échouent
État repo: doc A mentionne quelque chose qui n'existe pas encore
```

La session N+1 ne peut pas savoir si c'est volontaire (WIP) ou un accident. Elle va soit ignorer, soit "corriger" en cassant l'intention initiale.

> "No middle ground. Demi-commits dangereux." — Lecture 12

### Pourquoi ACID et pas un autre cadre

Le cours emprunte aux DBs parce que :

- Le repo agent **est** une DB (state + transactions)
- Les mêmes problèmes (race conditions, perte de durabilité, inconsistance) apparaissent
- Le vocabulaire est précis et déjà compris

### Pratiques concrètes

#### Pour Atomicity

- Avant de commit, run `make verify`
- 1 commit message = 1 phrase d'intention claire
- Si la tâche est trop grosse pour un commit → split

#### Pour Consistency

- Pre-commit hook qui run tests
- CI bloquante sur main
- [[template-clean-state-checklist|Clean state checklist]] en fin de session

#### Pour Isolation

- 1 agent = 1 worktree git
- Pas de hot reload partagé entre agents
- Locks explicites sur les fichiers de state si parallèle

#### Pour Durability

- Décisions clés → `DECISIONS.md` committé
- État → `PROGRESS.md` committé
- Pas de "j'ai expliqué à Claude dans la session" — il faut écrire

### À retenir

1. ACID s'applique : Atomicity, Consistency, Isolation, Durability.
2. **Demi-commit = poison**. La session suivante ne peut pas trier.
3. Tout state critique dans le **repo**, jamais dans la conversation.
4. Tests + lint + build verts = consistency check minimal.
5. Parallèle → [[git-worktrees-parallel-claude|worktrees]] obligatoires.

## Related pages

- [[repository-as-system-of-record]]
- [[progress-file-pattern]]
- [[decision-log-pattern]]
- [[session-clean-handoff]]
- [[git-worktrees-parallel-claude]]
- [[atomic-task-decomposition]]
- [[the-harness-engineering-curriculum-summary]]
