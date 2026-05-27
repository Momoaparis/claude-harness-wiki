# skill-creator (meta-skill)

**Summary** : Meta-skill officiel Anthropic pour créer de nouveaux skills ou améliorer des skills existants, via un cycle draft → test → évaluation humaine + quantitative → itération.

**Sources** :
- `raw/ingested/skills_skills_skill-creator-at-main.md`

**Last updated** : 2026-05-27

---

## Contenu

### Rôle

`skill-creator` est le skill qui permet de créer d'autres skills. Il fournit un workflow structuré pour :

- partir d'une idée et rédiger un `SKILL.md`
- créer des cas de test réalistes
- lancer des runs (avec skill vs sans skill) en parallèle
- évaluer quantitativement et qualitativement les résultats
- itérer jusqu'à satisfaction
- optimiser la description pour le triggering

C'est l'application directe du principe [[prompt-as-asset]] : capturer un workflow efficace comme skill réutilisable.

### Processus de création

#### 1. Capture d'intention

Extraire de la conversation courante :
- Que doit faire ce skill ?
- Quand doit-il se déclencher ? (phrases/contextes utilisateur)
- Quel est le format de sortie attendu ?
- Faut-il des cas de test vérifiables ?

#### 2. Interview & recherche

Clarifier les edge cases, formats d'entrée/sortie, critères de succès, dépendances. Chercher les MCPs disponibles et les patterns existants.

#### 3. Rédaction du SKILL.md

Frontmatter obligatoire :
- `name` — identifiant du skill
- `description` — **mécanisme de déclenchement principal** (quand utiliser + ce que ça fait). Doit être "légèrement pushy" pour éviter l'undertriggering.

Corps : instructions en mode impératif, exemples, formats de sortie.

→ Voir [[skill-anatomy]] pour la structure complète.

#### 4. Test

2-3 prompts réalistes (ce qu'un vrai utilisateur écrirait). Sauvegarder dans `evals/evals.json`. Lancer en parallèle : run "avec skill" + run "sans skill" (baseline).

→ Voir [[skill-eval-workflow]] pour le détail.

#### 5. Évaluation

- Assertions quantitatives + grading automatique
- Eval viewer pour review humaine
- Analyse des patterns dans les transcripts

#### 6. Itération

Améliorer le skill en généralisant depuis le feedback (ne pas overfitter sur les exemples). Supprimer ce qui ne sert pas. Expliquer le *pourquoi* plutôt qu'empiler des MUST. Reboucler jusqu'à satisfaction ou stagnation.

#### 7. Optimisation du triggering

→ Voir [[skill-description-optimization]].

### Principes d'amélioration

- **Généraliser, pas overfitter** : les exemples de test ne représentent pas tous les usages futurs.
- **Garder le prompt lean** : supprimer ce qui n'apporte pas de valeur, lire les transcripts (pas juste les outputs).
- **Expliquer le pourquoi** : les LLMs modernes comprennent les raisons. Préférer l'explication à l'interdiction rigide.
- **Factoriser les scripts répétés** : si tous les runs écrivent `create_docx.py`, bundler ce script dans `scripts/`.

### Adaptation par environnement

| Env | Spécificités |
|---|---|
| Claude Code | Workflow complet avec subagents parallèles |
| Claude.ai | Pas de subagents → runs séquentiels, pas de baseline, pas d'optimisation description |
| Cowork | Subagents OK, pas de browser → `--static` pour l'eval viewer |

## Related pages

- [[harness-creator-et-skill-creator-summary]]
- [[skill-anatomy]]
- [[skill-creation-workflow]]
- [[skill-eval-workflow]]
- [[skill-description-optimization]]
- [[prompt-as-asset]]
- [[eval-roadmap]]
- [[grader-types]]
