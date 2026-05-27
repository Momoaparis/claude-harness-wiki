# Fresh session readability test

**Summary** : Test empirique pour vérifier si le repo est auto-suffisant. Une nouvelle session avec zéro contexte humain doit pouvoir répondre à 5 questions fondamentales depuis le repo seul. Chaque non-réponse = gap dans la carte du projet.

**Sources** : `raw/ingested/lecture-03-making-the-repository-the-single-source-of-truth.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le test

Démarrer une nouvelle session Claude Code (ou Codex) **sans aucun contexte conversationnel**. L'agent doit pouvoir répondre à ces 5 questions **uniquement depuis le repo** :

| # | Question | Fichier qui doit répondre |
|---|----------|--------------------------|
| 1 | **What is this project?** | `AGENTS.md` / `CLAUDE.md` (root) |
| 2 | **How is it organized?** | `ARCHITECTURE.md` ou structure de dossiers évidente |
| 3 | **How do I run it?** | `Makefile`, scripts, ou section "How to run" dans AGENTS.md |
| 4 | **How do I verify a change?** | Commandes de test/lint explicites (`make test`, `pytest`, etc.) |
| 5 | **Where are we right now?** | `PROGRESS.md` / `claude-progress.md` |

### Critère de succès

> "Ready to start work without asking human." — Lecture 03

Si l'agent doit poser une question à l'humain après avoir lu le repo, le test a échoué. L'humain devient un goulet d'étranglement et la connaissance reste "in heads" — invisible pour les futures sessions.

### Pourquoi 5 questions précises

Chaque question correspond à un **moment** du cycle de travail :

```
1. What        → orientation initiale
2. How org     → naviguer le code
3. How run     → exécuter en local
4. How verify  → tester un changement
5. Where now   → reprendre le fil
```

Manquer 1 = l'agent ne sait pas dans quoi il est.  
Manquer 5 = l'agent recommence le travail déjà fait.

### Procédure concrète

1. **Setup** : crée une session Claude Code dans un répertoire de travail isolé (worktree par exemple — voir [git-worktrees-parallel-claude](git-worktrees-parallel-claude.md))
2. **Prompt minimal** : "Read the repo and tell me how to add a new feature called X"
3. **Observer** :
   - L'agent lit-il les bons fichiers ?
   - Pose-t-il des questions ? Lesquelles ?
   - Quelles décisions invente-t-il (drift) ?
4. **Cartographier les gaps** : pour chaque question non-répondue, identifier le fichier manquant
5. **Combler** : ajouter le fichier au bon endroit (knowledge next to code, voir [repository-as-system-of-record](repository-as-system-of-record.md))
6. **Re-tester**

### Cas réel (cours)

> "Good progress records reduce session startup diagnostic time by 60-80%." — Lecture 08

Sans `claude-progress.md` : 20 minutes de diagnostic au démarrage.  
Avec : 3 minutes pour atteindre l'état exécutable.

Voir [rebuild cost](rebuild-cost-metric.md).

### Antipatterns détectés par le test

- Agent demande "what's the tech stack?" → `AGENTS.md` ne le dit pas
- Agent fait `npm install` puis échec → `package.json` deps manquantes, pas de `.nvmrc`
- Agent invente une convention de naming → pas de `CONTRIBUTING.md` ni de section conventions
- Agent ne sait pas si une feature est faite ou pas → pas de `feature_list.json` (voir [feature-list-as-primitive](feature-list-as-primitive.md))

### Lien avec l'initialisation

[La phase d'init](initialization-phase-separation.md) (Lecture 06) doit produire un repo qui passe le fresh session test. C'est son critère de sortie.

### Quand re-tester

- Après chaque refactor structurel majeur
- Avant chaque release
- Si un nouvel humain rejoint l'équipe et a du mal à onboarder (signal indirect)

### Différence avec l'ablation testing

[L'ablation testing](ablation-study-methodology.md) mesure la valeur **marginale** d'un composant de harness (remove + mesurer drop). Le fresh session test mesure la **complétude** de la carte (peut-on naviguer sans guide humain ?).

Les deux sont complémentaires :
- Ablation = "ce composant sert-il à quelque chose ?"
- Fresh session = "manque-t-il quelque chose ?"

### À retenir

1. **5 questions** : What / How org / How run / How verify / Where now.
2. Test = démarrer une session sans contexte et observer ce qui manque.
3. Échec = drift de l'agent ou questions à l'humain.
4. Re-tester après chaque évolution majeure.
5. Complémentaire de [l'ablation](ablation-study-methodology.md).

## Related pages

- [repository-as-system-of-record](repository-as-system-of-record.md)
- [ablation-study-methodology](ablation-study-methodology.md)
- [initialization-phase-separation](initialization-phase-separation.md)
- [rebuild-cost-metric](rebuild-cost-metric.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
