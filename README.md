# Anis's PROJECT – Série de TP n°1

## Contexte

Ce projet fait partie de la **Série de TP n°1 – Pratiques et outils du développement logiciel collaboratif**.[file:1]  
L’objectif est de développer un module Python `StudentStats` permettant de calculer des statistiques simples sur des notes d’étudiants (moyenne, minimum, maximum) en respectant une charte de codage commune et un workflow Git/Trello collaboratif.[file:1]

## Équipe du projet

| Rôle               | Nom de l’étudiant    |
|--------------------|----------------------|
| Chef de Projet     | Izri Anis            |
| Architecte Logiciel| Yacine Beldjoudi     |
| Développeur Backend| Zaki Benacef         |
| Responsable Qualité| Bouchayeb Adel       |

Le Chef de Projet est responsable de l’organisation, du Trello et de la livraison finale (tests, liens GitHub/Trello).[file:1][file:2]  
L’Architecte définit la structure du code.[file:1][file:2]  
Le Développeur implémente les fonctions de calcul.[file:1]  
Le Responsable Qualité vérifie le respect de la charte et la documentation.[file:2]

## Fonctionnalités prévues

Le module `StudentStats` doit fournir au minimum :[file:1]

- Une fonction pour calculer la moyenne d’une liste de notes.  
- Une fonction pour trouver la note minimale.  
- Une fonction pour trouver la note maximale.  

Toutes les fonctions doivent respecter :[file:1]  
- Le nommage en `snake_case`.  
- Une docstring complète (description, paramètres, retour).  
- Un style de code propre (pas de code mort, espaces autour des opérateurs).

## Organisation du code

Le projet est structuré de la façon suivante :[file:1]

- `main.py` : point d’entrée du programme, utilise les fonctions de `utils.py`.  
- `utils.py` : contient les fonctions de calcul (moyenne, min, max) et leur documentation.  

L’Architecte crée la structure initiale (`main.py` et `utils.py`) et effectue le premier commit sur la branche `main`.[file:1][file:2]

## Workflow Git

Nous utilisons GitHub avec les règles suivantes :[file:1][file:2]

- Ne jamais coder directement sur la branche `main`.  
- Pour chaque fonctionnalité, créer une branche dédiée (ex : `feat-moyenne`).  
- Faire des commits avec un préfixe obligatoire : `ADD`, `FIX`, `DOC`, ou `MOD` (ex : `ADD fonction moyenne`).  
- Ouvrir une Pull Request de la branche de fonctionnalité vers `main`.  
- Un autre membre (souvent le Responsable Qualité) fait la revue de code avant le merge.

## Gestion de projet (Trello)

Un tableau Trello public est utilisé pour suivre les tâches.[file:1][file:2]

Colonnes utilisées :  
- Backlog  
- À faire  
- En cours  
- En revue  
- Terminé  

Exemples de cartes :[file:1]  
- Config – Créer repo GitHub + .gitignore.  
- Arch – Créer structure `main.py` et `utils.py`.  
- Dev – Fonction moyenne.  
- Dev – Fonction min.  
- Dev – Fonction max.  

Chaque membre s’assigne une carte et déplace la carte selon l’avancement (En cours → En revue → Terminé).[file:1][file:2]

## Livraison

En fin de TP, le Chef de Projet :[file:1][file:2]

- Fait un `git pull` sur `main`.  
- Exécute `main.py` pour vérifier que tout fonctionne.  
- S’assure que le Trello est à jour.  
- Envoie à l’enseignant :  
  - L’URL du dépôt GitHub.  
  - L’URL du tableau Trello.
