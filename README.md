# Documentation du projet FizzBuzz

## Contexte du projet

Ce projet implémente une version basique du jeu FizzBuzz en Python. L'objectif est de mettre en place un processus de développement structuré avec des tests unitaires, une intégration continue via GitHub Actions, ainsi que la conteneurisation avec Docker.

## Étapes réalisées

### 1. Implémentation de FizzBuzz

Création du fichier main.py contenant la logique du programme FizzBuzz.
L'affichage des 100 premières lignes de sortie attendues.

### 2. Mise en place des tests unitaires

Création des fichiers de test test_main.py et test_fizzbuzz.py.
Utilisation de unittest et pytest pour couvrir différents scénarios.
en plus j'ai voulu créer de deux branches distinctes (test_unitest et test_pytest) sur github pour tester ces deux approches et voire leur différences.

### 3. Configuration de la couverture de code

Intégration de coverage.py pour mesurer la couverture des tests.
Exécution de coverage report pour obtenir un pourcentage de couverture.

Résultats obtenus pour pytest:
```bash
coverage report
Name               Stmts   Miss  Cover
--------------------------------------
main.py               16      3    81%
test_fizzbuzz.py      17      0   100%
test_main.py          21      1    95%
--------------------------------------
TOTAL                 54      4    93%
```

Résultats obtenus pour unittest:
```bash
coverage report
Name               Stmts   Miss  Cover
--------------------------------------
main.py               16      3    81%
test_fizzbuzz.py      17     12    29%
test_main.py          21      1    95%
--------------------------------------
TOTAL                 54     16    70%
```
### 4. Intégration continue avec GitHub Actions

Création d’un workflow dans .github/workflows/ci.yml.
Configuration du pipeline pour tester le code sur plusieurs OS et versions de Python.
Blocage des push directs sur main, obligeant l'utilisation des PULL REQUEST.
Ajout d'une validation qui empêche la fusion d’une PULL REQUEST si les tests échouent.

### configuration du git action :
GitHub Actions est un outil d'automatisation intégré à GitHub qui permet d'exécuter des tâches automatiquement lorsque des événements se produisent (ex: push, pull request), souvent utilisé pour la CI/CD.
j'ai créé une matrice de test qui va exécuter le workflow pour toutes les combinaisons possibles des valeurs définies par exremple : 

Le système d'exploitation testé (os)
Le workflow sera exécuté sur :
Ubuntu (Linux) (ubuntu-latest)
Windows (windows-latest)
MacOS (macOS-latest)

La version de Python (python-version)
Le workflow sera exécuté avec :
Python 3.10
Python 3.11
Python 3.12

### 5. Gestion des branches et des PRs
ceci a etait fait sur github
Blocage des push directs sur main pour imposer un workflow de type feature branch.
Une PR ne peut être fusionnée que si tous les tests passent.
Création de PRs pour valider le processus, avec une PR correcte et une PR volontairement invalide.

### 6. Conteneurisation avec Docker

Création d'une image docker.
```bash
docker build -t fizzbuzz-test .
```

creation d'une image
```bash
docker run -d fizzbuzz-test
```
et lancer/relancer le conteneur 
```bash
docker start be01ae840da63eb7ddf2080af18a50bcb0e3c94ddd21b6104719d8eb8ddbdebc
```
Écriture d'un Dockerfile pour conteneuriser l’application.

Un Dockerfile est un fichier de configuration qui décrit comment créer une image Docker. 

### 7. Adaptation du workflow GitHub Actions pour Docker

Le workflow utilise désormais une image Docker tierce pour exécuter les tests.

Ajout d’une étape de build de l’image Docker dans un répertoire temporaire.



Résumé

L'ensemble de ces actions permet de garantir :

Un code testé et fiable.

Un processus de développement structuré avec CI/CD.

Une gestion rigoureuse des contributions via PRs.

Une portabilité et une reproductibilité avec Docker.
