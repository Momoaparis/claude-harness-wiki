# Atomic task decomposition

**Summary** : Décomposer un besoin large en unités atomiques (≥5 par feature majeure). Chaque unité = 1 comportement vérifiable + 1 commande exécutable + dépendances explicites. Sans ça, [[wip-limit-discipline|WIP=1]] échoue parce que les "tâches" sont trop grosses pour être finies en une session.

**Sources** : `raw/ingested/lecture-07-draw-clear-task-boundaries-for-agents.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le principe

Un besoin formulé à haut niveau ("Build user management") est **incomplétable** par un agent. Il doit être décomposé en unités où chacune :

1. A un **comportement unique** (pas "and also...")
2. A une **commande de vérification exécutable**
3. Déclare ses **dépendances** vers d'autres unités
4. Est **complétable en une session** (~30 min - 2h)

### Le test "Can I complete this in one session?"

Pour chaque tâche proposée, l'agent doit pouvoir répondre **oui** à :

- En partant d'un état clean state, puis-je faire cette tâche entièrement ?
- Puis-je écrire le code + les tests + run la verification + commit en une session ?

Si non → split.

### Exemple : "Build user management"

❌ Tâche atomique unique :
```
Task: Build user management system
```

✅ Décomposition :
```
Task 001: User registration endpoint (POST /api/register)
Task 002: Login endpoint (POST /api/login) — depends on 001
Task 003: Logout endpoint (POST /api/logout) — depends on 002
Task 004: Token refresh endpoint (POST /api/refresh) — depends on 002
Task 005: Get current user (GET /api/me) — depends on 002
Task 006: Update profile (PATCH /api/me) — depends on 005
Task 007: Password reset request (POST /api/reset-request) — depends on 001
Task 008: Password reset confirm (POST /api/reset-confirm) — depends on 007
```

8 atomic tasks. Chacune complétable en 1 session. Dépendances claires → DAG.

### Critères de chaque atomic task

#### 1. Single behavior

Pas de "and" dans le titre :

❌ `Add registration and email verification`
✅ `Add registration` + `Add email verification` (deux tasks séparées)

#### 2. Executable verification

Voir [[completion-evidence-executable]]. La commande doit être runnable et binaire.

#### 3. Explicit dependencies

Lister les tasks **prérequises** :

```json
{
  "id": "002",
  "dependencies": ["001"]
}
```

Si pas de dépendances : `[]`. Si dépendances cachées → tu vas découvrir au runtime que la tâche ne marche pas seule.

#### 4. Completable in one session

Estimation à la décomposition. Si dépasse 2h → split davantage.

### Combien d'atomic tasks ?

> "Break broad requirements into ≥5 atomic units." — Lecture 07

Minimum : 5 par feature majeure. Pour une vraie app, attendre 30-100 atomic tasks.

Si le nombre semble fou → c'est probablement le **vrai** scope qui était caché par la formulation initiale.

### L'effet sur la qualité

Sans atomic decomposition + WIP=1, l'agent va :

1. Démarrer "build auth"
2. Coder registration partiellement
3. Réaliser qu'il manque login → coder ça aussi
4. Réaliser qu'il manque token storage → coder ça aussi
5. Run out of context, half-done sur 5 things

Avec :

1. Pick task 001 (registration)
2. Code + test + verify → passing
3. Commit, end session ou continue à 002

VCR = 1.0 à chaque step.

### Le piège du "vague decomposition"

Tasks vagues :

❌ `Task 001: Set up authentication`

Le mot "set up" cache une infinité d'étapes. À reformuler :

✅ `Task 001: POST /api/register endpoint with email/password, validation, password hashing, DB write`

Si même cette formulation tient en une session, OK. Sinon, split encore.

### Comment décomposer

Méthode pratique (Lecture 07) :

1. **Décrire le besoin** en 1-2 phrases (le quoi)
2. **Lister les behaviors** observables (les endpoints, écrans, scripts)
3. **Pour chaque behavior**, écrire la verification command
4. **Ordonner par dépendances** (qui dépend de qui)
5. **Vérifier la taille** : chaque task ≤ 1 session
6. **Sanity check** : si on supprime une task, est-ce que le système marche encore (partiellement) ?

### Lien avec feature lists

L'atomic task decomposition produit le contenu de `task-breakdown.md` ou `feature_list.json` (voir [[feature-list-as-primitive]], [[template-feature-list-json]]).

### Cas réel : 8-feature API (Lecture 07)

| Approche | Granularité | VCR final |
|----------|-------------|-----------|
| "Build the API" (mono-task) | 1 task | 0.0 (rien fini) |
| Décomposition atomique 8 tasks | 8 atomic | 0.875 (7/8 passing) |

L'atomic decomposition **rend le projet complétable**.

### Pattern de l'agent autonome

Pour donner un agent travailler en autonomie :

1. Une atomic task est claire pour lui (pas d'ambiguïté)
2. Il peut self-verify (commande exécutable disponible)
3. Il sait quand s'arrêter (status `passing` est atteint)

Sans atomicity, l'agent autonome dérive.

### Antipatterns

- ❌ "Refactor everything to be more modular" → impossible à finir
- ❌ "Improve UX" → pas observable
- ❌ "Fix all the TODOs" → un TODO ≠ une atomic task
- ❌ Tasks trop petites ("rename variable") → bruit dans le breakdown
- ❌ Pas de dépendances déclarées → blocages cachés

### À retenir

1. Décomposer en **≥5 atomic units** par feature majeure.
2. Chaque unité = single behavior + verification + dependencies + completable in 1 session.
3. Le test : "puis-je commit en 1 session ?" Si non → split.
4. La décomposition est faite **en init phase**, pas pendant l'implémentation.
5. Sans atomicity, WIP=1 ne marche pas.

## Related pages

- [[wip-limit-discipline]]
- [[completion-evidence-executable]]
- [[task-breakdown-structure]]
- [[feature-list-as-primitive]]
- [[verified-completion-rate-metric]]
- [[the-harness-engineering-curriculum-summary]]
