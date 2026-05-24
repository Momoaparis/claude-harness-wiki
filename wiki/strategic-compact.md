# Strategic Compact

**Summary** : Pratique de compactage manuel du contexte Claude Code à des points logiques choisis, en désactivant l'auto-compact qui survient à des moments arbitraires.

**Sources** : `raw/ingested/the-longform-guide-to-everything-claude-code.md`, `raw/ingested/affaan-m-ecc-readme-part*.md`

**Last updated** : 2026-05-23

---

## Contenu

L'**auto-compact** intégré dans Claude Code se déclenche à des points arbitraires, souvent en plein milieu d'une tâche. Le **strategic compact** est l'approche opposée : désactiver l'auto-compact et compacter manuellement à des moments logiques.

### Quand compacter manuellement

- Après une phase d'exploration, avant l'exécution
- Après avoir complété un jalon, avant le suivant
- Quand le contexte accumulé n'est plus pertinent pour la suite
- Après debugging, avant de continuer la feature
- Après une approche ratée, avant d'en essayer une autre

### Quand NE PAS compacter

- **En plein milieu d'une implémentation** — tu perdrais les noms de variables, chemins de fichiers, état partiel. C'est l'erreur la plus chère en pratique (ECC).

### Implémentation via hook

Un script bash hooké en `PreToolUse` peut compter les appels d'outils et suggérer le compactage après un seuil (par défaut 50) :

```bash
COUNTER_FILE="/tmp/claude-tool-count-$$"
THRESHOLD=${COMPACT_THRESHOLD:-50}
# ... incrémenter le compteur ...
if [ "$count" -eq "$THRESHOLD" ]; then
  echo "[StrategicCompact] $THRESHOLD tool calls reached - consider /compact if transitioning phases" >&2
fi
```

### Pourquoi c'est important

L'auto-compact peut résumer en perdant des informations cruciales au mauvais moment. Le strategic compact préserve les informations à travers les phases logiques du travail.

### Combinaison avec le mode Plan

Une fois le plan défini et le contexte nettoyé (option par défaut en plan mode désormais), le travail peut se faire à partir du plan, ce qui est particulièrement utile après une grosse phase d'exploration.

### Côté ECC

ECC recommande aussi de basculer `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` de 95 → **50** pour déclencher le compact plus tôt et préserver la qualité en sessions longues. Cf. [[ecc-token-optimization]].

## Related pages

- [[session-storage-pattern]]
- [[memory-persistence-hooks]]
- [[claude-code-hooks]]
- [[claude-code-commands]]
- [[ecc-token-optimization]]
- [[the-longform-guide-summary]]
