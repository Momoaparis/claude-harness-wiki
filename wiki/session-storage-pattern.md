# Session Storage Pattern

**Summary** : Pattern de fichiers `.tmp` dans `.claude/` pour persister le contexte d'une session Claude Code à l'autre, évitant le "context rot".

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

Le pattern consiste à créer un fichier `.tmp` qui résume l'état actuel de la session — ce qui a fonctionné, ce qui n'a pas fonctionné, et ce qui reste à faire — puis à l'utiliser comme contexte de démarrage pour la session suivante.

### Structure recommandée du fichier

```
~/.claude/sessions/YYYY-MM-DD-topic.tmp
```

Un fichier par session, organisé par date et thème, pour éviter de polluer le contexte de nouveaux projets avec d'anciens travaux.

### Contenu d'un bon fichier de session

- **Approches qui ont marché** (avec preuves vérifiables)
- **Approches tentées qui n'ont pas marché** (pour ne pas les retenter)
- **Approches non tentées et tâches restantes**

### Workflow

1. En fin de session, Claude génère le résumé de l'état actuel
2. L'utilisateur révise, demande des éditions si besoin
3. Pour la session suivante, il suffit de fournir le chemin du fichier
4. Particulièrement utile quand on approche des limites de contexte

### Maintenance

Le dossier de sessions grandit avec le temps. Stratégies :
- Sauvegarder ailleurs (cloud, autre disque)
- Élaguer les sessions devenues inutiles
- Conserver uniquement les sessions "post-mortem" précieuses

## Related pages

- [[strategic-compact]]
- [[memory-persistence-hooks]]
- [[continuous-learning-skill]]
- [[the-longform-guide-summary]]
