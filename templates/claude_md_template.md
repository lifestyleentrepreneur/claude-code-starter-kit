# Template — CLAUDE.md pour un nouveau projet

> **Comment utiliser ce template :**
> 1. Copie ce fichier à la racine de ton nouveau projet et renomme-le `CLAUDE.md`
> 2. Remplace les `[crochets]` par tes informations
> 3. Supprime les sections qui ne s'appliquent pas
> 4. Ouvre le dossier dans Claude Code — il lira ce fichier automatiquement

---

# [NOM DE TON PROJET] — Instructions pour Claude Code

> Fichier lu automatiquement à chaque session par Claude Code.

---

## Qui je suis

- **Nom :** [Ton prénom]
- **Métier :** [Ce que tu fais dans la vie, en une phrase]
- **Langue préférée :** français
- **Tu me [tutoies / vouvoies] :** [choisir]

---

## Objectif de ce workspace

*En 1-2 phrases : à quoi sert ce dossier ?*

> Exemple : "Ce workspace contient tous mes scripts d'automatisation pour gérer mon CRM Airtable et mon calendrier Google."

---

## Structure du projet

*Liste les dossiers importants et leur rôle. Claude s'en sert pour savoir où chercher quoi.*

```
.
├── scripts/           # Scripts Python
├── data/              # Données brutes (jamais modifier à la main)
├── reports/           # Rapports générés
├── .tmp/              # Fichiers temporaires (vidables)
├── .env               # Clés API (jamais commit)
└── templates/         # Templates réutilisables
```

---

## Règles non-négociables

*Les choses que Claude doit toujours faire, ou ne jamais faire. Aussi précises que possible.*

- Toujours demander confirmation avant de supprimer un fichier
- Toujours créer un backup avant de modifier un fichier dans `data/`
- Ne jamais commit les fichiers `.env` ou `.tmp/*`
- Ne jamais utiliser les tirets du milieu (—) dans les textes générés
- Ne jamais inventer d'information qui n'est pas dans les sources

---

## Conventions

*Comment tu travailles. Style, format, outils préférés.*

- **Python** : 3.11+, imports classés PEP8, docstrings sur toutes les fonctions publiques
- **Markdown** : titres en français, tableaux plutôt que listes imbriquées
- **Commits Git** : messages en français, format `type: description` (feat, fix, docs, refactor)
- **Variables sensibles** : toujours dans `.env`, jamais en clair dans les scripts

---

## Auto-amélioration (self-healing)

> Si tu rencontres une erreur pendant une exécution, ne t'arrête pas au premier obstacle.
>
> 1. Lis le message d'erreur, identifie la cause
> 2. Tente au moins une solution (installer la dépendance, corriger le chemin, réessayer avec une approche alternative)
> 3. Si tu corriges quelque chose de récurrent, ajoute une ligne dans ce CLAUDE.md pour que tu n'aies pas à le redécouvrir la prochaine fois
> 4. Ne me dérange que si tu as déjà essayé au moins une solution

---

## Outils et accès disponibles

*APIs, MCP, bases de données auxquels Claude a accès dans ce workspace.*

- `AIRTABLE_TOKEN` dans `.env` — accès CRM Airtable
- MCP Playwright — navigation web (mode headed)
- Scripts custom dans `scripts/` — réutilise-les au lieu d'en créer de nouveaux quand possible

---

## Ce que je veux éviter

*Les patterns ou comportements que tu as déjà vus et qui ne marchent pas pour toi.*

- Les scripts de 500 lignes "au cas où" — préfère des scripts focalisés de 50 lignes
- Les rapports avec emojis et langage marketing — reste factuel
- Les solutions qui demandent d'installer 10 dépendances — minimise les deps externes

---

## Contact

- **Email :** [ton@email.com]
- **Calendrier :** [lien calendly si partagé]

---

*Dernière mise à jour : [date]*
