# Kill switches d'agent

**Summary** : Tu dois pouvoir arrêter un agent qui part en vrille. Connaître la différence SIGTERM/SIGKILL, tuer le **process group** (pas juste le parent), et armer un dead-man switch heartbeat-based pour les loops non supervisés.

**Sources** : `raw/ingested/the-shorthand-guide-to-everything-agentic-security.md`

**Last updated** : 2026-05-23

---

## SIGTERM vs SIGKILL

- `SIGTERM` — laisse au processus une chance de cleanup propre.
- `SIGKILL` — stoppe immédiatement, pas de cleanup.

Les deux comptent : SIGTERM en premier pour laisser flush les écritures, puis SIGKILL si rien n'arrive après quelques secondes.

## Tuer le process group, pas juste le parent

Si tu tues seulement le parent, les enfants continuent à tourner. C'est typiquement ce qui explique qu'on retrouve au matin 100 GB de RAM consommée par des processes orphelins.

Exemple Node :

```javascript
// Kill le process group entier
process.kill(-child.pid, "SIGKILL");
```

Le `-` devant le PID indique « process group ». Sans ça, on tue uniquement le PID indiqué.

## Dead-man switch heartbeat

Pour les loops non supervisés (ralph, continuous agents, cron jobs), ne pas compter sur l'agent compromis pour s'arrêter poliment.

Pattern minimal :

- Le supervisor démarre la tâche.
- La tâche écrit un **heartbeat toutes les 30 s**.
- Si le heartbeat stalle, le supervisor tue le process group.
- La tâche stallée est quarantaine pour review des logs.

## Pourquoi c'est devenu critique

Le guide cite l'incident OpenClaw où `/stop` et `/kill` ne fonctionnaient plus quand l'agent était en train de déraper. Les utilisateurs étaient bloqués face à un agent qui ignorait les commandes d'arrêt.

> If you do not have a real stop path, your "autonomous system" can ignore you at exactly the moment you need control back.

C'est pourquoi les kill switches doivent vivre **hors du processus** de l'agent — au niveau OS, container, ou supervisor — pas dans une commande que l'agent compromis peut intercepter.

## Lien avec le reste

- [[agent-observability]] fournit le signal — heartbeat, logs anormaux, tentative réseau bloquée.
- [[least-agency]] pose la politique — quand auto-approuver vs requérir humain.
- [[agent-sandboxing]] limite ce que l'agent peut faire **pendant** le délai entre la dérive et l'arrêt.

## Related pages

- [[agent-observability]]
- [[least-agency]]
- [[agent-sandboxing]]
- [[the-agentic-security-summary]]
