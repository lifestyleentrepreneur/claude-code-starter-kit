# Template — Bonne instruction à Claude Code

> La qualité de ton instruction décide de 80 % du résultat.
> Voici les 6 règles à appliquer (et le template à copier-coller).

---

## Les 6 règles

1. **Contexte** — la situation, le problème, ce qui existe déjà
2. **Résultat attendu** — ce que tu veux obtenir exactement (format, longueur, structure)
3. **Fichiers concernés** — utilise `@chemin/fichier.md` pour pointer directement
4. **Contraintes** — ce que Claude ne doit **pas** faire
5. **"Avant d'agir, dis-moi ton plan."** — active la phase Orchestration du DOE
6. **Think deeply / ultrathink** — mots-clés pour les tâches complexes

---

## Template à copier-coller

```
## Contexte
[Décris la situation. Qu'est-ce qui existe déjà ? Quel est le problème ?]

## Objectif
[Qu'est-ce que tu veux obtenir ? Sois précis.]

## Fichiers pertinents
- @chemin/vers/fichier1.md
- @chemin/vers/fichier2.md

## Résultat attendu
[Format, longueur, structure. Donne un exemple si possible.]

## Contraintes
- Ne fais pas [X]
- N'utilise pas [Y]
- Respecte [Z]

Avant d'agir, dis-moi ton plan. Think deeply.
```

---

## Exemple 1 — Trier mes emails

**Mauvaise instruction :**
> Crée un script pour trier mes emails.

**Bonne instruction :**
```
## Contexte
J'ai 200 emails non lus dans Gmail et je passe 30 minutes par jour à les trier à la main.
La plupart sont des newsletters, des notifications de paiement, et quelques vrais messages clients.

## Objectif
Script Python qui classe automatiquement les emails non lus en 5 catégories.

## Fichiers pertinents
- @.env (contient mes credentials Gmail API)
- @scripts/README.md

## Résultat attendu
- Script dans scripts/trier_emails.py
- 5 labels Gmail créés automatiquement : Urgent, Clients, Newsletters, Pubs, Autre
- Logs dans .tmp/tri_emails.log

## Contraintes
- Ne touche pas aux emails avec le label "Important" existant
- Ne supprime rien, toujours ajouter des labels
- Pas de dépendance externe au-delà de google-api-python-client

Avant d'agir, dis-moi ton plan.
```

---

## Exemple 2 — Rapport pour un client

**Mauvaise instruction :**
> Fais-moi un rapport sur l'entreprise X.

**Bonne instruction :**
```
## Contexte
Mon client (PME de 20 personnes, secteur textile) me demande une synthèse de l'état du marché
de la seconde main en France pour 2026. Il prépare un pivot stratégique.

## Objectif
Rapport markdown de 2-3 pages synthétisant l'opportunité, les risques et 3 scénarios d'entrée.

## Fichiers pertinents
- @research/sources_2026.md (les 12 articles que j'ai déjà collectés)
- @templates/rapport_client.md (la structure à suivre)

## Résultat attendu
- Sauvegardé dans reports/seconde_main_2026.md
- Structure : Résumé exécutif (1 para) → Marché → Risques → 3 scénarios → Reco
- Ton factuel, sources citées inline avec [numéro]

## Contraintes
- Utilise uniquement les sources listées dans sources_2026.md, pas d'hallucination
- Pas de jargon (cible : dirigeant non-spécialiste)
- Pas d'emojis

Avant d'agir, dis-moi ton plan. Ultrathink.
```

---

## Astuce pour démarrer

Si tu ne sais pas par où commencer, demande-toi :

> **Si je devais déléguer cette tâche à un humain qui ne connaît rien à mon business, de quoi aurait-il besoin pour la faire ?**

Tout ce qui te vient à l'esprit, c'est ça le contexte à donner à Claude.
