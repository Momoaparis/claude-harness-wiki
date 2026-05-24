# Eval Roadmap (8 Steps)

**Summary** : Roadmap en 8 étapes pour construire un système d'évaluation robuste pour un agent IA, depuis les premiers tests jusqu'à la maintenance.

**Sources** : The Longform Guide to Everything Claude Code.md (citant Anthropic engineering)

**Last updated** : 2026-05-22

---

## Contenu

Méthodologie issue de l'article Anthropic "Demystifying Evals for AI Agents".

### Les 8 étapes

#### 1. Start early
Commencer par 20-50 tâches simples issues d'échecs réels rencontrés.

#### 2. Convert real failures
Transformer les échecs reportés par les utilisateurs en cas de test. C'est gratuit et 100% pertinent.

#### 3. Write unambiguous tasks
Écrire des tâches non-ambiguës. Critère : deux experts indépendants doivent arriver au même verdict.

#### 4. Build balanced problem sets
Tester quand le comportement **devrait** se produire ET quand il **ne devrait pas**. Sans cela, l'éval favorise le sur-déclenchement.

#### 5. Build robust harness
Chaque trial démarre dans un environnement propre — pas de pollution entre tests.

#### 6. Grade what agent produced, not the path it took
Le critère est l'output final, pas la trajectoire. Évite les contraintes implicites sur "comment" l'agent doit s'y prendre.

#### 7. Read transcripts
Lire les transcripts d'un grand nombre de trials. Les patterns d'échec ne se voient qu'en lisant.

#### 8. Monitor for saturation
100% pass rate signifie que le test set est trop facile → ajouter des cas plus difficiles.

### Application pratique

Pour un workflow Claude Code :

1. Logger les sessions où on a dû corriger Claude
2. Extraire les patterns d'échec
3. Créer des skills/tests qui détectent ce pattern
4. Mesurer après modifications si le pattern recule

### Lien avec continuous learning

Ce processus alimente [[continuous-learning-skill]] : les échecs deviennent des skills, les skills deviennent des évals.

### Avertissement saturation

Un eval set à 100% ne prouve pas que le système est parfait — il prouve que les évals sont trop simples.

## Related pages

- [[grader-types]]
- [[pass-at-k-metric]]
- [[checkpoint-vs-continuous-evals]]
- [[continuous-learning-skill]]
- [[the-longform-guide-summary]]
