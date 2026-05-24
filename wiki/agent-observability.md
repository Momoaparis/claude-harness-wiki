# Observabilité des agents

**Summary** : Sans visibilité sur ce que l'agent a lu, quels tools il a appelés, quels endpoints il a tenté de joindre, impossible de sécuriser. Les runs hijackés ont presque toujours des traces anormales avant d'être visiblement malveillants.

**Sources** : `raw/ingested/the-shorthand-guide-to-everything-agentic-security.md`

**Last updated** : 2026-05-23

---

## Pourquoi c'est non négociable

> Hijacked runs usually look weird in the trace before they look obviously malicious.

L'agent qui part en vrille produit des signaux faibles bien avant de causer des dégâts visibles : appel d'un outil rarement utilisé, accès à un fichier hors scope, tentative de connexion à un domaine jamais touché. Si tu ne logs pas, tu manques la fenêtre d'intervention.

## Le minimum à logger

- **tool name** — quel outil appelé
- **input summary** — paramètres principaux (sans dumper de secrets)
- **files touched** — chemins lus / écrits
- **approval decisions** — autorisé / bloqué / auto-approuvé
- **network attempts** — destination, méthode, blocage éventuel
- **session / task id** — pour corréler

## Format minimal

JSON structuré, suffisant pour démarrer :

```json
{
  "timestamp": "2026-03-15T06:40:00Z",
  "session_id": "abc123",
  "tool": "Bash",
  "command": "curl -X POST https://example.com",
  "approval": "blocked",
  "risk_score": 0.94
}
```

## À l'échelle

Pour les setups multi-agents ou les loops continus, brancher sur OpenTelemetry (ou équivalent). L'objectif n'est pas le vendor — c'est d'avoir une **baseline de session** sur laquelle les anomalies ressortent.

Cf. patterns plus généraux dans [[continuous-learning-skill]] et [[continuous-learning-v2]] : les bons logs nourrissent aussi la boucle d'apprentissage de l'agent.

## Le lien avec least agency

L'observabilité est l'autre moitié de [[least-agency]] : tu ne peux pas exiger des approvals si tu ne vois pas ce qui se passe entre deux approvals. Et tu ne peux pas activer un [[agent-kill-switches|kill switch]] sur la base d'un comportement anormal si tu n'as pas de signal pour détecter l'anomalie.

## Anti-pattern noté

`claude --dangerously-skip-permissions` sur un ralph loop. Sans approvals **et** sans logs détaillés, on revient à un état où l'agent peut bouger sans laisser de trace — on découvre les dégâts seulement après coup.

## Related pages

- [[least-agency]]
- [[agent-kill-switches]]
- [[continuous-learning-v2]]
- [[the-agentic-security-summary]]
