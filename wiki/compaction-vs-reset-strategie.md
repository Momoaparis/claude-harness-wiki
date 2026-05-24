# Compaction vs reset — stratégie

**Summary** : Deux façons de gérer la fin de contexte : compacter (résumer dans la même session) ou reset (nouvelle session). Compaction préserve la "psychologie" de l'agent mais perd les "pourquoi". Reset démarre propre mais dépend d'artefacts complets. Le choix dépend du modèle et de la tâche.

**Sources** : `raw/ingested/lecture-05-keeping-context-alive-across-sessions.md`

**Last updated** : 2026-05-24

---

## Contenu

### Les deux approches

#### Compaction

Demander à l'agent (ou au système) de **résumer** la conversation pour libérer du contexte tout en restant dans la même session.

Voir [[strategic-compact]] pour le pattern `/compact` de Claude Code.

**Avantages** :
- Continuité de session : l'agent garde sa "psychologie" (style, contexte implicite)
- Pas de rebuild cost
- Plus rapide

**Inconvénients** :
- Le résumé **perd des détails**, surtout les "pourquoi" derrière les décisions
- Risque que le résumé soit biaisé (l'agent garde ce qu'il pense important — pas forcément ce qui l'est)
- Compaction multiple → dérive

#### Reset

Terminer la session actuelle après avoir produit les artefacts ([[progress-file-pattern]], [[decision-log-pattern]]), puis démarrer une nouvelle session.

**Avantages** :
- Contexte propre, pas de bias accumulé
- Forcer l'écriture des artefacts (utile à long terme)
- Pas de risque de "rushed finish" lié à la [[context-anxiety-modeles|context anxiety]]

**Inconvénients** :
- Rebuild cost (3-15 min selon qualité des artefacts)
- L'agent perd les détails informels (intuitions non écrites)
- Demande de la discipline (artefacts complets)

### Matrice de décision

| Situation | Stratégie |
|-----------|-----------|
| Modèle Sonnet 4.5 + tâche longue | **Reset** (anxiety trop forte) |
| Modèle Opus 4.6/4.7 + tâche moyenne | Compaction OK |
| Tâche en cours qui n'est pas un bon stopping point | Compaction si on est encore loin de la limite |
| Tâche complétée + tests verts | **Reset** (c'est un stopping point propre) |
| Beaucoup de "pourquoi" implicites en jeu | **Reset** (force à les écrire) |
| Session debug avec hypothèses qui s'enchaînent | Compaction (préserver le fil) |

### Le critère "stopping point"

Reset à un mauvais moment = perte. Un bon stopping point :

1. Build vert + tests verts
2. Commit propre (pas de WIP)
3. `PROGRESS.md` mis à jour
4. `Next best step` clair

Voir [[session-clean-handoff|clean state checklist]] pour les 5 conditions.

### Compaction : ce qui se perd typiquement

Liste des choses qui disparaissent à la compaction (à compenser via artefacts si nécessaire) :

- Le raisonnement détaillé derrière une décision
- Les hypothèses testées et rejetées
- Les avertissements lus mais ignorés ("ce sera traité après")
- Les questions de l'humain et les réponses nuancées de l'agent
- Les pourquoi implicites ("j'utilise X parce que Y, mais on devrait migrer un jour")

**Avant de compacter** : écrire dans `DECISIONS.md` ou `PROGRESS.md` ce qui doit survivre.

### Pattern "compact then commit"

Idéal pour les sessions très longues :

```
[work] → 70% context →
  1. Update PROGRESS.md
  2. Update DECISIONS.md si besoin
  3. Commit tout
  4. /compact
[continue work in same session]
```

Le commit est crucial : il transforme l'état conversationnel en état git **durable**.

### Pattern "stop and reset"

Quand l'agent commence à montrer des signes de [[context-anxiety-modeles|context anxiety]] :

```
[symptoms: rushed answers, skipping tests, "I'll finish later"]
  ↓
  1. Force checklist [[template-clean-state-checklist|clean state]]
  2. Update PROGRESS.md + DECISIONS.md
  3. Commit
  4. End session
[new session starts fresh]
```

### Lien avec Claude Code

Claude Code propose :

- `/compact` — compaction manuelle (voir [[strategic-compact]])
- `/clear` — reset partiel (clear conversation but keep CLAUDE.md context)
- Nouvelle session (terminal restart) — reset complet

[[memory-persistence-hooks|Les hooks]] peuvent automatiser : PreCompact pour sauvegarder l'état, SessionStart pour relire les artefacts.

### Antipatterns

- **Compaction multiple sans commit** → dérive incrémentale, état git désynchronisé
- **Reset sans avoir écrit `PROGRESS.md`** → la nouvelle session redécouvre tout (rebuild cost max)
- **Garder une session ouverte plusieurs jours** → contexte accumulé devient illisible
- **Compacter sur Sonnet 4.5** quand l'anxiety est déjà visible → on amplifie

### Métriques pour décider

Quelques signaux à surveiller :

| Signal | Action recommandée |
|--------|---------------------|
| Context window > 70% | Préparer le clock-out |
| L'agent saute des étapes | Reset immédiat |
| L'agent répète une question | Compaction défaillante, prefer reset |
| Tâche bloquée >30 min sans progrès | Reset (et logger la cause dans DECISIONS) |

### À retenir

1. **Compaction** = même session, perd les "pourquoi", rapide.
2. **Reset** = nouvelle session, perd l'informel, propre.
3. Le choix dépend du **modèle** (Sonnet 4.5 → reset ; Opus → soit) et du **stopping point**.
4. **Toujours commit + update artefacts** avant compaction ou reset.
5. La context anxiety est un signal pour passer au reset.

## Related pages

- [[cross-session-context-loss]]
- [[context-anxiety-modeles]]
- [[progress-file-pattern]]
- [[decision-log-pattern]]
- [[session-clean-handoff]]
- [[strategic-compact]]
- [[memory-persistence-hooks]]
- [[the-harness-engineering-curriculum-summary]]
