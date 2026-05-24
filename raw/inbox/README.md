# raw/inbox — Boîte de réception permanente

Stockage **local et permanent** sur E:, pour les fichiers en attente d'ingestion.

## Architecture

OneDrive sert uniquement de **relais transitoire** entre le téléphone et le PC.
Les données réelles vivent ici, sur E:.

```
[Téléphone] → [OneDrive cloud]
                    ↓ sync auto Windows
        [C:\Users\DELL\OneDrive\llm-wiki-inbox\]   ← buffer temporaire
                    ↓ déplacement par Claude
        [E:\llm-wiki\raw\inbox\]   ← TU ES ICI (permanent, sur E:)
                    ↓ ingestion Claude
        [E:\llm-wiki\raw\ingested\]
```

## Workflow

1. **Téléphone** : partager un article vers OneDrive → dossier `llm-wiki-inbox`.
2. **PC allumé** : OneDrive synchronise automatiquement.
3. **Session Claude** : demander *"ingère les nouveaux fichiers"*.
   - Phase 0 : Claude relève le buffer OneDrive vers `raw/inbox/` (libère OneDrive)
   - Phase 1-3 : ingestion + archivage vers `raw/ingested/`
4. **Résultat** : OneDrive redevient vide, données capitalisées sur E:.

Voir [CLAUDE.md](../../CLAUDE.md#workflow-mobile-capture-quotidienne) pour le protocole détaillé.

## Dépôt direct au PC

Si tu veux ajouter un fichier directement depuis le PC (sans passer par le
téléphone), tu peux le déposer directement ici dans `raw/inbox/`. Claude le
traitera comme un fichier mobile à l'ingestion suivante.

## Formats acceptés

- `.md` (Markdown — idéal, capture propre via extension Markdownload)
- `.txt`
- `.pdf`
- `.html`
- Liens YouTube / web : créer un fichier `.md` contenant juste l'URL et un titre.
