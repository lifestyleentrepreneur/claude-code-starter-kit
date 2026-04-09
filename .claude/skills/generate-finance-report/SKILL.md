---
name: generate-finance-report
description: Génère un rapport PDF d'analyse financière pour une action cotée en bourse. Récupère les dernières news via Yahoo Finance, analyse le sentiment et les thèmes, compose un rapport PDF professionnel. Use when the user wants to analyze a stock or generate a financial report.
argument-hint: "TICKER (e.g. NVDA, AAPL, TSLA, MSFT, GOOGL)"
allowed-tools: Bash, Read
---

# Generate Finance Report

Génère un rapport PDF d'analyse financière complet pour une action cotée en bourse, en utilisant Yahoo Finance comme source de données.

## Ce que ce skill fait

1. Récupère les informations de base de la compagnie (nom, secteur, cap boursière, prix actuel)
2. Récupère les 10 dernières news publiées sur cette compagnie
3. Analyse le sentiment global (positif, neutre, négatif)
4. Identifie les thèmes principaux qui ressortent des news
5. Génère un rapport PDF professionnel avec :
   - Cover avec ticker, nom, prix, variation
   - Section "Vue d'ensemble" avec les chiffres clés
   - Section "News récentes" avec les 10 dernières news résumées
   - Section "Analyse" avec le sentiment et les thèmes
   - Section "Recommandation" (à interpréter avec prudence)

## Comment lancer

```bash
cd .claude/skills/generate-finance-report/scripts
python3 generate_report.py NVDA
```

Remplace `NVDA` par n'importe quel ticker valide :
- **NVDA** — Nvidia
- **AAPL** — Apple
- **TSLA** — Tesla
- **MSFT** — Microsoft
- **GOOGL** — Google
- Ou n'importe quel autre ticker que tu connais (ex: META, AMZN, NFLX...)

## Output

Le PDF est enregistré dans `.tmp/finance_report_{TICKER}.pdf` à la racine du starter kit.

Le script ouvre automatiquement le PDF à la fin (sur macOS).

## Dépendances

```bash
pip3 install yfinance reportlab --break-system-packages
```

(Sur les Mac récents, le `--break-system-packages` peut être nécessaire. Sinon, utiliser un venv.)

## Aucune clé API requise

Yahoo Finance via la librairie `yfinance` est public et ne nécessite aucune authentification. Tu peux lancer ce skill autant de fois que tu veux, sur n'importe quel ticker, sans rien payer.

## Limitations

- Les données viennent de Yahoo Finance, qui peut avoir des délais de quelques minutes sur les news
- L'analyse de sentiment est basique (mots-clés) — pas un vrai modèle ML
- Ce rapport est **éducatif** et ne doit JAMAIS être utilisé comme conseil d'investissement
- Si Yahoo Finance bloque temporairement les requêtes (rate limit), réessaie après quelques minutes
