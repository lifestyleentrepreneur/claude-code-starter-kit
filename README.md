# Claude Code Starter Kit

Un kit de démarrage pour découvrir **Claude Code** et **l'IA Agentique** en pratique. Tu télécharges le dossier, tu l'ouvres dans Claude Code, tu dis "Démarre le tour", et Claude Code te guide pendant 15-20 minutes à travers tous les concepts essentiels — sans jamais te perdre.

> **Important** : ce kit n'est pas un projet à installer au sens classique. C'est un environnement pédagogique conçu pour qu'un débutant puisse découvrir Claude Code en pratique, à son rythme.

## Ce que tu vas apprendre

En suivant le tour guidé, tu vas comprendre **en pratique** :

- **CLAUDE.md** — le fichier qui guide Claude Code en permanence
- **.env et .gitignore** — comment garder tes secrets en sécurité
- **.tmp** — l'espace de travail temporaire
- **Les 4 modes** — Default, Accept Edits, Plan, Auto-Accept
- **Bonne instruction** — la compétence n°1 pour bien utiliser Claude Code
- **Les skills** — compétences réutilisables que tu fabriques toi-même

À la fin du tour, tu auras lancé un vrai skill qui va chercher les dernières news sur Nvidia (ou n'importe quelle action que tu choisis) et génère un rapport PDF professionnel.

## Ce qu'il te faut avant de commencer

- **Claude Code installé** sur ton ordinateur → https://claude.com/claude-code
- **Python 3.9+** (déjà présent sur Mac, à télécharger sur Windows : python.org)

C'est tout. Aucune clé API à créer, aucun compte externe à ouvrir.

## Comment démarrer en 3 étapes

### 1. Télécharge ce kit

Clique sur le bouton vert **"Code"** en haut à droite de cette page GitHub, puis **"Download ZIP"**. Dézippe le fichier sur ton bureau ou dans tes Téléchargements.

### 2. Ouvre Claude Code dans le dossier

Ouvre ton terminal (sur Mac : Applications → Utilitaires → Terminal), puis tape :

```bash
cd ~/Downloads/claude-code-starter-kit-main
claude
```

(Adapte le chemin si tu as dézippé ailleurs.)

### 3. Lance le tour

Une fois Claude Code lancé, dis-lui simplement :

> Démarre le tour

Et c'est parti. Claude Code va lire le `CLAUDE.md` du kit et te guider clic par clic.

## À tester après le tour

Une fois que tu as fini le tour, tu peux t'amuser avec le skill `generate-finance-report` sur n'importe quelle action :

```
/generate-finance-report TSLA
/generate-finance-report AAPL
/generate-finance-report MSFT
```

Le PDF généré s'enregistre dans `.tmp/`.

## Tu veux aller plus loin ?

Je suis Farel Vignon Honvoh, consultant IA. Je construis des automatisations sur-mesure pour les entrepreneurs. Si tu veux qu'on travaille ensemble pour construire ton premier vrai système IA :

**→ https://cal.eu/honvoh/decouverte**

20 minutes, gratuit, on voit ensemble si on peut collaborer.

## Licence

Ce kit est fourni librement. Fais-en ce que tu veux : adapte-le, modifie-le, redistribue-le.
