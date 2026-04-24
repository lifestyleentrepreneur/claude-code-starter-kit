# Ressources — Claude Code pour débutants

> Tout ce qui a été mentionné ou promis dans la vidéo, centralisé ici.

---

## 🚀 Démarrer maintenant

### 1. Installer les outils de base

| Outil | Lien | Pourquoi |
|-------|------|----------|
| **VS Code** | https://code.visualstudio.com/ | L'IDE gratuit le plus utilisé au monde. Claude Code s'y intègre nativement. |
| **Claude Code** | https://docs.claude.com/en/docs/claude-code/overview | L'agent IA que tu vas piloter. Nécessite minimum le plan Claude Pro à 20$/mois. |
| **Python 3.9+** | https://www.python.org/downloads/ | Déjà installé sur Mac. Sur Windows, télécharge depuis le site officiel. |
| **Node.js** | https://nodejs.org/ | Nécessaire pour certains MCP (Playwright notamment). |

### 2. Télécharger ce starter kit

Clique sur le bouton vert **Code** en haut de cette page GitHub, puis **Download ZIP**. Dézippe sur ton bureau, ouvre le dossier dans VS Code, puis lance Claude Code.

### 3. Prompt de démarrage à copier-coller

Une fois le starter kit ouvert, colle ce message dans Claude Code :

```
Mets en place cet espace de travail en fonction de CLAUDE.md. Avant de
commencer, vérifie que Python et Node.js sont installés sur mon ordinateur.
Si quelque chose manque, installe-le pour moi. Ensuite, guide-moi étape par
étape à travers les concepts essentiels de Claude Code : CLAUDE.md, .env,
.tmp, les skills, les agents, et Playwright. Vas-y doucement, je suis débutant.
```

---

## 📄 Templates Claude Code (dans ce repo)

Dans le dossier [`templates/`](./templates/) tu trouveras trois fichiers prêts à l'emploi :

- **[`claude_md_template.md`](./templates/claude_md_template.md)** — Template de CLAUDE.md pour démarrer un nouveau projet
- **[`bonne_instruction_template.md`](./templates/bonne_instruction_template.md)** — Template pour écrire une instruction qui marche à tous les coups (les 6 règles + 2 exemples)
- **[`directive_sop_template.md`](./templates/directive_sop_template.md)** — Template de SOP (Standard Operating Procedure) pour la phase *Directive* de la méthodologie DOE

Copie-les, remplace les crochets, c'est tout.

---

## 📊 Bonus — Parler de votre nouvelle activité

Quand vous lancez une nouvelle activité (service, business, side project), la toute première étape c'est d'en parler à votre entourage. Voici deux outils pour le faire bien :

- **🗂️ Google Sheet — Suivi des contacts (Chaud / Tiède / Froid)**
  Un tableur avec les bonnes colonnes (relation, canal, catégorie, date, réponse, next step) + 3 exemples. Cliquez, faites "Faire une copie" → c'est à vous.
  👉 https://docs.google.com/spreadsheets/d/1cBLTfLkFnCKgzzMxEb62GwEaD3TVZG05-c2yEwYAHzA/copy

- **📝 Google Doc — Templates de messages**
  Ce qu'on dit au téléphone ou par message selon le profil de la personne (parent, ami proche, ancien collègue, connaissance éloignée). Avec templates d'appel, de vocal, de SMS, variations selon le profil, et relances.
  👉 https://docs.google.com/document/d/1R6thRO0jy6YkN7IZT55OyJxZJH_dvghGgaZgTralcFA/copy

---

## 🎁 Bonus mentionnés dans la vidéo

| Ressource | Lien | Quand l'utiliser |
|-----------|------|-----------------|
| **Whisper Flow** | https://wisprflow.ai/ | L'outil de dictée vocale que j'utilise pour écrire mes prompts en parlant. 10x plus rapide que taper. |
| **Communauté Skool (gratuite)** | https://skool.honvoh.com | La communauté où je partage mes ressources, mes vidéos longues, et où on discute automatisation IA. |

---

## 💬 Aller plus loin avec Farel

Envie qu'on construise une automatisation sur-mesure pour ton business ou ton usage perso ?

**→ Réserve un appel gratuit de 20 minutes : https://cal.eu/honvoh/decouverte**

On regarde ensemble ton cas, je te dis honnêtement si je peux t'aider, et si oui comment.

---

## 🗂️ Contenu du starter kit (rappel)

```
claude-code-starter-kit/
├── CLAUDE.md                      # Le tour guidé — Claude Code le lit automatiquement
├── README.md                      # Comment démarrer
├── RESOURCES.md                   # Ce fichier
├── .env.example                   # Template de fichier .env (à copier en .env)
├── .gitignore                     # La liste des fichiers à ne jamais commit
├── sample.txt                     # Fichier de démo
├── templates/                     # Templates réutilisables (nouveaux)
│   ├── claude_md_template.md
│   ├── bonne_instruction_template.md
│   └── directive_sop_template.md
├── .claude/
│   ├── skills/
│   │   └── generate-finance-report/   # Le skill qui génère un rapport PDF Nvidia
│   └── agents/
│       ├── code-explainer.md      # Sub-agent qui explique du code en français simple
│       └── web-browser.md         # Sub-agent qui navigue sur le web via Playwright
└── .tmp/                          # Espace temporaire (vidable sans risque)
```

---

## ❓ Questions

Poste une question sous la vidéo YouTube ou dans la communauté Skool. Je réponds à tout le monde.
