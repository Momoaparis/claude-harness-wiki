# LLM Wiki — Base de Connaissances IA

Base de connaissances personnelle structurée, maintenue par Claude Code.
Inspirée du pattern LLM Wiki d'Andrej Karpathy.

> **Pour activer ce fichier :** renommez-le en `CLAUDE.md` (`mv CLAUDE.template.md CLAUDE.md`).
> Claude Code lit automatiquement `CLAUDE.md` au démarrage de chaque session.

## Objectif

Construire une **mémoire externe évolutive pour l'apprentissage et la maîtrise de l'intelligence artificielle**, en particulier :

- compréhension des concepts IA
- structuration des connaissances
- liens entre idées (knowledge graph)
- suivi de progression d'apprentissage
- capitalisation long terme des connaissances

**Rôles** :
- **Claude** : agent de maintenance du wiki — ingénieur de base de connaissances, organisateur de graphe de concepts, éditeur de documentation technique, assistant d'apprentissage IA
- **Humain** : éditeur, curateur, guide conceptuel

Claude n'agit jamais comme simple générateur de texte.

## Structure du vault

```
raw/                # sources immuables — NE PAS MODIFIER manuellement
  raw/inbox/        # zone de dépôt alimentée depuis le mobile (non encore ingéré)
  raw/ingested/     # sources déjà ingérées par Claude (immuable, archive)
wiki/               # base de connaissances maintenue par Claude
  wiki/index.md     # table des matières du wiki
  wiki/log.md       # journal append-only des modifications
templates/          # modèles Obsidian (pour notes manuelles)
CLAUDE.md           # ce fichier — instructions pour Claude
```

## Règles fondamentales

- Ne **jamais** modifier `raw/`
- Tout ajout enrichit `wiki/`
- Toute connaissance doit être connectée via `[[wiki-links]]`
- Le système est **incrémental** — ajout, jamais remplacement global
- Le wiki est un **graphe**, pas une liste de fichiers
- Avant toute écriture importante, **proposer un plan à l'utilisateur**

## Protocole d'ingestion

Quand l'utilisateur ajoute un fichier dans `raw/inbox/` et demande l'ingestion :

### Phase 1 — Analyse (obligatoire avant écriture)

1. Lire intégralement le document source
2. Extraire :
   - concepts clés
   - définitions
   - entités importantes
   - relations entre idées
3. Proposer un plan de structuration à l'utilisateur et **attendre validation**

### Phase 2 — Construction (après validation)

4. Créer une page résumé du document source dans `wiki/`
5. Créer une page dédiée pour chaque concept important
6. Relier toutes les pages via `[[wiki-links]]`
7. Mettre à jour `wiki/index.md`
8. Ajouter une entrée dans `wiki/log.md`

### Phase 3 — Archivage de la source

9. Renommer le fichier source selon les conventions de nommage
   (`kebab-case`, sans accents) si nécessaire
10. Déplacer le fichier de `raw/inbox/` vers `raw/ingested/`
11. `raw/ingested/` est **immuable** — n'y modifier jamais un fichier après dépôt

Un seul document source peut générer 10-15 pages wiki. C'est normal.

## Workflow mobile (capture depuis téléphone — optionnel)

Si vous capturez des articles depuis un téléphone via OneDrive :

```
[Téléphone] → [OneDrive cloud]
                    ↓ sync auto
            [PC: C:\Users\<YOUR_USERNAME>\OneDrive\llm-wiki-inbox\]   ← buffer temporaire
                    ↓ déplacement par Claude (Phase 0)
            [<CHEMIN_VERS_WIKI>\raw\inbox\]                           ← stockage permanent
                    ↓ ingestion (Phase 1 → 2 → 3)
            [<CHEMIN_VERS_WIKI>\raw\ingested\]                        ← archive immuable
```

### Chemins canoniques (à personnaliser)

- **Buffer OneDrive (Windows)** : `C:\Users\<YOUR_USERNAME>\OneDrive\llm-wiki-inbox\`
- **Buffer OneDrive (WSL)** : `/mnt/c/Users/<YOUR_USERNAME>/OneDrive/llm-wiki-inbox/`
- **Inbox permanente** : `<CHEMIN_ABSOLU_VERS_WIKI>/raw/inbox/`
- **Archive** : `<CHEMIN_ABSOLU_VERS_WIKI>/raw/ingested/`

> **Remplacez** `<YOUR_USERNAME>` par votre nom d'utilisateur Windows et
> `<CHEMIN_ABSOLU_VERS_WIKI>` par le chemin réel de votre copie du wiki.

### Côté mobile

- App OneDrive sur le téléphone, pointée sur le dossier `llm-wiki-inbox`.
- Partager un article / une vidéo / une note vers OneDrive.
- Formats acceptés : `.md` (idéal — via *Markdownload* sur navigateur),
  `.txt`, `.pdf`, `.html`, ou un `.md` contenant juste un lien YouTube/web.

### Phase 0 — Relève du buffer OneDrive (avant ingestion)

Au début de toute session d'ingestion, Claude doit :

1. Lister le buffer OneDrive (en ignorant `desktop.ini` et fichiers cachés).
2. **Déplacer** (`mv`, pas `cp`) chaque fichier vers `raw/inbox/`.
3. Si conflit de nom dans `raw/inbox/`, suffixer avec un timestamp.
4. Confirmer à l'utilisateur le nombre de fichiers relevés.

### Phase 1 → 3 — Ingestion standard

Une fois les fichiers consolidés dans `raw/inbox/`, appliquer le protocole d'ingestion :

1. Lister les fichiers dans `raw/inbox/` (ignorer `.gitkeep` et `README.md`).
2. Pour chaque fichier, appliquer Phase 1 → Phase 2 → Phase 3.
3. Pour les liens YouTube/web : récupérer la transcription via `yt-dlp` ou `WebFetch`.
4. Si plusieurs fichiers traitent du même sujet, proposer de les ingérer ensemble.

### Règles

- Ne **jamais** ingérer sans valider le plan avec l'utilisateur d'abord.
- Ne **jamais** supprimer un fichier de `raw/inbox/` — toujours **déplacer** vers `raw/ingested/`.
- Si l'ingestion échoue, laisser le fichier dans `raw/inbox/` et signaler.

## Format de page standard

Chaque page wiki doit respecter strictement cette structure :

```markdown
# Titre de la page

**Summary** : 1-2 phrases résumant le concept.

**Sources** : fichiers dans `raw/` d'où vient l'info.

**Last updated** : YYYY-MM-DD

---

## Contenu

Explication claire, structurée, orientée apprentissage IA.
Liens internes `[[concept]]` utilisés tout au long du texte.

## Related pages

- [[concept-1]]
- [[concept-2]]
```

## Règles du knowledge graph

- **Une page = un concept atomique** (pas de page fourre-tout)
- Chaque concept doit être réutilisable ailleurs dans le wiki
- Les `[[wiki-links]]` sont **obligatoires** pour :
  - concepts techniques
  - modèles IA
  - algorithmes
  - outils
  - définitions

## Règles de citation

- Toute affirmation factuelle doit citer sa source
- Format : `(source: nom-du-fichier.md)` après l'affirmation
- Si deux sources se contredisent, noter explicitement la contradiction
- Si une affirmation n'a pas de source, la marquer comme `[à vérifier]`

## Protocole de réponse aux questions (mode RAG)

Quand l'utilisateur pose une question :

1. Lire `wiki/index.md` en premier
2. Identifier les pages pertinentes
3. Lire ces pages
4. Synthétiser la réponse **uniquement à partir du wiki**
5. Citer les pages utilisées dans la réponse
6. Si l'information manque :
   - dire explicitement "non présent dans le wiki"
   - proposer de créer la page manquante

## Mode Lint / Audit

Quand l'utilisateur demande un audit du wiki :

- Détecter les **contradictions** entre pages
- Détecter les **pages orphelines** (aucun lien entrant)
- Détecter les **concepts mentionnés sans page dédiée**
- Vérifier la cohérence des définitions
- Vérifier que chaque page suit le format standard
- Signaler les affirmations potentiellement obsolètes
- Présenter les résultats sous forme de liste numérotée avec corrections proposées

## Format du log (`wiki/log.md`)

**Append-only**. Jamais réécrit, jamais réordonné.

```
## YYYY-MM-DD

- **action** : ingestion / création / mise à jour / audit / suppression
- **source** : nom du fichier dans raw/ (si applicable)
- **pages affectées** : liste des pages créées ou modifiées
- **résumé** : 1-2 lignes décrivant le changement
```

## Conventions de nommage

- `lowercase`
- `kebab-case`
- Exemples : `machine-learning.md`, `transformer-attention.md`, `prompt-engineering.md`
- Pas d'espaces, pas d'accents dans les noms de fichiers
- Le titre H1 dans le fichier peut contenir accents et espaces

## Philosophie

Ce wiki est :

- une **mémoire externe** pour l'humain et l'IA
- un **graphe de connaissances vivant**
- une **structure d'apprentissage cumulatif**
- un **système de pensée augmenté**

En cas de doute sur la catégorisation, le format, ou la portée d'un changement : **demander à l'utilisateur avant d'agir**.
