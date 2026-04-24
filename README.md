# Claude Code Starter Kit

Un kit de démarrage pour découvrir **Claude Code** et **l'IA Agentique** en pratique. Tu télécharges le dossier, tu l'ouvres dans Claude Code, tu dis "Démarre le tour", et Claude Code te guide pendant 25-30 minutes à travers tous les concepts essentiels — sans jamais te perdre.

> **Important** : ce kit n'est pas un projet à installer au sens classique. C'est un environnement pédagogique conçu pour qu'un débutant puisse découvrir Claude Code en pratique, à son rythme.

## Ce que tu vas apprendre

En suivant le tour guidé, tu vas comprendre **en pratique** :

- **CLAUDE.md** — le fichier qui guide Claude Code en permanence
- **La méthodologie DOE** — Directive, Orchestration, Exécution : le mental model de l'IA Agentique
- **L'auto-réparation (self-healing)** — Claude Code diagnostique et corrige ses erreurs tout seul
- **.env et .gitignore** — comment garder tes secrets en sécurité
- **.tmp** — l'espace de travail temporaire
- **Les 4 modes** — Ask before edit, Edit automatically, Blend mode, Bypass permissions
- **Bonne instruction** — la compétence n°1 pour bien utiliser Claude Code
- **Les skills** — compétences réutilisables que tu fabriques toi-même
- **Les sub-agents** — comment déléguer des tâches spécialisées
- **L'agent navigateur web** — un agent qui navigue sur internet à ta place via Playwright

À la fin du tour, tu auras lancé un vrai skill qui va chercher les dernières news sur Nvidia (ou n'importe quelle action que tu choisis) et génère un rapport PDF professionnel de 5 pages incluant analyse technique avec graphique et analyse fondamentale.

## Ce qu'il te faut avant de commencer

- **Claude Code installé** sur ton ordinateur → https://claude.com/claude-code
- **Python 3.9+** (déjà présent sur Mac, à télécharger sur Windows : python.org)
- **3 dépendances Python** (Claude Code va t'aider à les installer si nécessaire) :
  - `yfinance` — pour récupérer les données boursières
  - `reportlab` — pour générer le PDF
  - `matplotlib` — pour le graphique technique
- **(Optionnel) MCP Playwright** — pour l'agent navigateur web. Deux modes :
  ```bash
  # Mode visible (tu vois le navigateur — recommandé pour débuter)
  claude mcp add playwright -- npx @playwright/mcp@latest --headed

  # Mode invisible (le navigateur tourne en arrière-plan)
  claude mcp add playwright -- npx @playwright/mcp@latest
  ```
  Pas obligatoire pour le tour de base. Tu peux l'ajouter après.

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

## 📄 Templates prêts à copier

Dans le dossier [`templates/`](./templates/) tu as trois fichiers réutilisables :

- [`claude_md_template.md`](./templates/claude_md_template.md) — Template de CLAUDE.md pour démarrer un nouveau projet
- [`bonne_instruction_template.md`](./templates/bonne_instruction_template.md) — Template pour écrire une instruction qui marche (les 6 règles + 2 exemples)
- [`directive_sop_template.md`](./templates/directive_sop_template.md) — Template de SOP pour la phase *Directive* de la méthodologie DOE

Copie-les dans tes projets, remplace les crochets, c'est tout.

Tous les autres liens mentionnés dans la vidéo (VS Code, Whisper Flow, communauté, appel gratuit) sont dans [`RESOURCES.md`](./RESOURCES.md).

---

## À tester après le tour

Une fois que tu as fini le tour, tu peux t'amuser avec le skill `generate-finance-report` sur n'importe quelle action :

```
/generate-finance-report TSLA
/generate-finance-report AAPL
/generate-finance-report MSFT
```

Le PDF généré (5 pages) s'enregistre dans `.tmp/`.

Tu peux aussi tester le sub-agent `code-explainer` qui prend n'importe quel fichier de code et l'explique en français simple :

> Utilise le code-explainer pour m'expliquer @scripts/generate_report.py

Tu peux aussi tester l'agent `web-browser` qui navigue sur internet à ta place :

> Utilise le web-browser pour chercher les dernières nouvelles sur l'intelligence artificielle

> Utilise le web-browser pour trouver le meilleur vol Paris -> New York pour le mois prochain

**Note :** l'agent web-browser nécessite le MCP Playwright. Installe-le avec :
```bash
# Mode visible (recommandé pour les démos)
claude mcp add playwright -- npx @playwright/mcp@latest --headed
```

## Tu veux aller plus loin ?

Je suis Farel Honvoh, consultant IA. Je construis des automatisations sur-mesure pour les entrepreneurs. Si tu veux qu'on travaille ensemble pour construire ton premier vrai système IA :

**→ https://cal.eu/honvoh/decouverte**

20 minutes, gratuit, on voit ensemble si on peut collaborer.

## Licence

Ce kit est fourni librement. Fais-en ce que tu veux : adapte-le, modifie-le, redistribue-le.
