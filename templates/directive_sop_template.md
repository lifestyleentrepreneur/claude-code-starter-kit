# Template — SOP / Directive

> **Qu'est-ce qu'une SOP ?**
> Standard Operating Procedure : un document en markdown qui décrit **quoi faire** en langage naturel, pas **comment coder**.
> C'est l'étape *Directive* de la méthodologie DOE (Directive → Orchestration → Exécution).
>
> Tu écris une fois la procédure, Claude Code la relit à chaque fois qu'il doit accomplir la tâche.

---

## 1. Objectif

*Une phrase. Qu'est-ce qu'on essaie d'accomplir avec cette procédure ?*

> Exemple : "Rédiger un email de suivi après un appel client à partir du transcript Zoom."

---

## 2. Quand l'utiliser

*Les déclencheurs — mots-clés ou situations qui indiquent à Claude qu'il doit suivre cette SOP.*

> Exemple : "Quand l'utilisateur demande 'envoie un follow-up à [client]' ou 'rédige un email de suivi'."

---

## 3. Inputs (entrées)

*Les informations que Claude doit avoir pour commencer. Liste-les toutes.*

- Transcript de la conversation (fichier `.txt` ou `.md`)
- Nom du client
- Base de données CRM (pour récupérer l'email)

---

## 4. Outils autorisés

*Quels outils Claude peut utiliser pour cette tâche. Limiter la panoplie évite les dérives.*

- `Read` — lire le transcript et la base CRM
- `Write` — créer le draft
- MCP Gmail — poser le draft dans les brouillons

---

## 5. Étapes

*Le processus. Numérote les étapes. Reste en langage naturel.*

1. Lire le transcript et extraire les informations capitales (décisions, next steps, deadlines)
2. Rechercher l'email du client dans le CRM
3. Rédiger l'email en appliquant la structure : salutation → récap → next steps → CTA
4. Sauvegarder en draft dans Gmail (ne **jamais** envoyer directement)
5. Prévenir l'utilisateur que le draft est prêt

---

## 6. Output attendu

*À quoi ressemble le résultat final. Plus c'est précis, plus c'est reproductible.*

- Un draft Gmail dans la boîte "Brouillons"
- Sujet : `Suite à notre échange — [sujet principal]`
- Corps en français, vouvoiement, 150-250 mots
- Ton chaleureux, pas marketing

---

## 7. Contraintes (à ne PAS faire)

*Les garde-fous. Aussi important que les étapes.*

- Ne jamais envoyer l'email directement — toujours laisser en draft
- Ne pas utiliser les tirets du milieu (—) dans le corps
- Ne pas inventer d'information qui ne serait pas dans le transcript
- Ne pas utiliser d'emojis dans le corps (max 1 dans la salutation si pertinent)

---

## 8. Cas extrêmes

*Que faire quand le scénario de base ne s'applique pas ?*

- **Pas d'email dans le CRM** → prévenir l'utilisateur et demander l'adresse
- **Transcript vide ou trop court** → demander plus de contexte avant de rédiger
- **Plusieurs décisions contradictoires** → lister les ambiguïtés et demander clarification

---

## 9. Exemple de rendu

*Un vrai exemple de ce à quoi l'output doit ressembler. Claude apprend mieux par l'exemple.*

```
Sujet : Suite à notre échange — prochaines étapes

Bonjour [prénom],

Merci pour notre appel de ce matin. Voici un récap rapide :

- Objectif validé : [...]
- Prochaine livraison : [...] d'ici le [date]
- Point en suspens : [...]

Je vous envoie le brief détaillé d'ici mercredi. D'ici là, n'hésitez pas si une question vous vient.

Belle journée,
Farel
```
