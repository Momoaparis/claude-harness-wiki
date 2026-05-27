# Workflow d'évaluation de skill

**Summary** : Séquence structurée pour évaluer un skill : lancer les runs en parallèle (avec/sans skill), drafter les assertions pendant l'exécution, grader, agréger en benchmark, et présenter via l'eval viewer pour review humaine.

**Sources** :
- `raw/ingested/skills_skills_skill-creator-at-main.md`

**Last updated** : 2026-05-27

---

## Contenu

### Principe

L'évaluation compare deux configurations :
- **with_skill** : même prompt + skill chargé
- **without_skill** (ou **old_skill**) : même prompt sans skill (ou ancienne version)

Pour un skill nouveau : baseline = sans skill.
Pour l'amélioration d'un skill existant : baseline = snapshot de l'ancienne version.

### Étape 1 — Lancer tous les runs dans le même tour

Spawner tous les subagents en parallèle (with_skill ET without_skill) dans le même message. Ne pas faire les runs with_skill d'abord.

Instructions pour chaque subagent :
```
- Skill path: <path-to-skill>
- Task: <eval prompt>
- Input files: <fichiers si applicable, ou "none">
- Save outputs to: <workspace>/iteration-N/<eval-name>/with_skill/outputs/
```

Créer un `eval_metadata.json` pour chaque cas (assertions vides pour l'instant) :
```json
{
  "eval_id": 0,
  "eval_name": "nom-descriptif-du-cas",
  "prompt": "Le prompt de l'utilisateur",
  "assertions": []
}
```

### Étape 2 — Drafter les assertions pendant les runs

Utiliser le temps d'attente pour drafter les assertions quantitatives. Ne pas attendre passivement.

Bonnes assertions :
- Objectivement vérifiables
- Noms descriptifs (lisibles dans le benchmark viewer)
- Appropriées au type de skill (subjectif → évaluation qualitative, objectif → assertions)

Mauvaises assertions : celles qui passent toujours quelle que soit la version (non-discriminantes).

Mettre à jour `eval_metadata.json` et `evals/evals.json` avec les assertions rédigées.

### Étape 3 — Capturer les données de timing

Quand chaque subagent se termine, sauvegarder **immédiatement** dans `timing.json` :
```json
{
  "total_tokens": 84852,
  "duration_ms": 23332,
  "total_duration_seconds": 23.3
}
```
C'est la **seule** occasion de capturer ces données — elles arrivent dans la notification de fin de task et ne sont pas persistées ailleurs.

### Étape 4 — Grading, benchmark, eval viewer

1. **Grade chaque run** — subagent grader qui lit `agents/grader.md` → `grading.json` par run
   - Champs requis dans `grading.json` : `text`, `passed`, `evidence` (pas `name`/`met`/`details`)
   - Pour les assertions vérifiables programmatiquement : écrire et exécuter un script

2. **Agréger** :
   ```bash
   python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
   ```
   → `benchmark.json` + `benchmark.md` (pass_rate, time, tokens avec mean ± stddev et delta)

3. **Analyse** — rechercher les patterns cachés dans les stats :
   - Assertions qui passent toujours (non-discriminantes)
   - Evals à haute variance (potentiellement flaky)
   - Trade-offs temps/tokens

4. **Lancer l'eval viewer** (AVANT d'évaluer les outputs soi-même) :
   ```bash
   nohup python <skill-creator-path>/eval-viewer/generate_review.py \
     <workspace>/iteration-N \
     --skill-name "my-skill" \
     --benchmark <workspace>/iteration-N/benchmark.json \
     > /dev/null 2>&1 &
   ```
   Depuis iteration-2 : ajouter `--previous-workspace <workspace>/iteration-N-1`.
   Sans browser (Cowork, headless) : ajouter `--static <output_path>`.

### Ce que l'utilisateur voit dans le viewer

Onglet **Outputs** (un cas de test à la fois) :
- Prompt, output, output précédent (itération N-1), grades formels, textbox de feedback

Onglet **Benchmark** :
- Pass rates, timing, tokens par configuration avec breakdowns par eval

Navigation : boutons prev/next ou flèches. "Submit All Reviews" → `feedback.json`.

### Étape 5 — Lire le feedback

```json
{
  "reviews": [
    {"run_id": "eval-0-with_skill", "feedback": "le chart manque les labels d'axe", "timestamp": "..."},
    {"run_id": "eval-1-with_skill", "feedback": "", "timestamp": "..."}
  ],
  "status": "complete"
}
```

Feedback vide = satisfaisant. Concentrer les améliorations sur les cas avec feedback spécifique.

Arrêter le serveur viewer : `kill $VIEWER_PID 2>/dev/null`.

### Lien avec les concepts d'évaluation généraux

Ce workflow est une instanciation du [eval-roadmap](eval-roadmap.md) appliqué aux skills. Les [grader-types](grader-types.md) (code-based, model-based, human) correspondent ici aux assertions automatiques + review humaine. La métrique [pass-at-k-metric](pass-at-k-metric.md) s'applique aux runs parallèles.

## Related pages

- [skill-creator-meta-skill](skill-creator-meta-skill.md)
- [skill-creation-workflow](skill-creation-workflow.md)
- [skill-description-optimization](skill-description-optimization.md)
- [eval-roadmap](eval-roadmap.md)
- [grader-types](grader-types.md)
- [pass-at-k-metric](pass-at-k-metric.md)
- [checkpoint-vs-continuous-evals](checkpoint-vs-continuous-evals.md)
- [worker-checker-separation](worker-checker-separation.md)
