# Grader Types (Code, Model, Human)

**Summary** : Trois types de "graders" pour évaluer la sortie d'un agent — code-based (rapide, brittle), model-based (flexible, non-déterministe), human (gold standard, coûteux).

**Sources** : The Longform Guide to Everything Claude Code.md (citant Anthropic engineering blog)

**Last updated** : 2026-05-22

---

## Contenu

### 1. Code-Based Graders

Évaluation programmatique automatisée.

**Méthodes** :
- String match
- Binary tests
- Static analysis
- Outcome verification

**Avantages** : rapide, peu coûteux, objectif, déterministe.

**Limite** : *brittle* — sensible aux variations valides (ex : même résultat mais formatage différent fait échouer le match).

**Quand l'utiliser** : la vérité-terrain est unique et bien définie.

### 2. Model-Based Graders

Un autre modèle LLM juge la sortie.

**Méthodes** :
- Rubric scoring
- Natural language assertions
- Pairwise comparison

**Avantages** : flexible, gère la nuance, accepte les variations sémantiquement équivalentes.

**Limite** : non-déterministe, plus coûteux en tokens, le grader peut hallucial.

**Quand l'utiliser** : sorties créatives ou multiples réponses valides possibles.

### 3. Human Graders

Évaluation par expert humain.

**Méthodes** :
- SME (Subject Matter Expert) review
- Crowdsourced judgment
- Spot-check sampling

**Avantages** : qualité gold standard, capture les subtilités.

**Limite** : coûteux, lent, non-scalable.

**Quand l'utiliser** : décisions à fort enjeu, calibration des autres graders.

### Stratégie en pratique

Combiner les trois selon le besoin :
1. **Code-based** pour la majorité (rapide et fréquent)
2. **Model-based** pour les cas où code-based est trop brittle
3. **Human** pour le spot-check et la calibration

### Source

Article Anthropic : "Demystifying Evals for AI Agents" (Jan 2026)
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

## Related pages

- [[checkpoint-vs-continuous-evals]]
- [[pass-at-k-metric]]
- [[eval-roadmap]]
- [[the-longform-guide-summary]]
