## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Pipeline d'Intégration et de Déploiement Continu (CI/CD)

Ce projet utilise un pipeline CI/CD configuré avec CircleCI pour automatiser les tests et le déploiement. Le pipeline se compose des étapes suivantes :

#### 1. Build et Test
- Cette étape utilise l'image Docker `cimg/python:3.12.1` pour créer un environnement de test. Elle inclut les sous-étapes suivantes :
  - **Checkout** : Récupération du code source du repository GitHub.
  - **Installation des Dépendances** : Installation des dépendances du projet à partir de `requirements.txt`.
  - **Linting** : Exécution de `flake8` pour vérifier la conformité du code aux conventions de style PEP8.
  - **Tests et Couverture** : Exécution des tests unitaires avec `pytest` et mesure de la couverture du code. La build échoue si la couverture du code est inférieure à 80%.

#### 2. Build et Push Docker
- Cette étape construit une image Docker du projet et la pousse sur Docker Hub. Elle est exécutée après la réussite de l'étape "Build et Test". Les sous-étapes comprennent :
  - **Checkout** : Récupération du code source.
  - **Configuration de Docker** : Préparation de l'environnement Docker.
  - **Construction de l'Image Docker** : Création de l'image Docker en utilisant le `Dockerfile` du projet.
  - **Connexion à Docker Hub** : Connexion au Docker Hub en utilisant les identifiants fournis via les variables d'environnement.
  - **Push de l'Image Docker** : Envoi de l'image Docker sur Docker Hub avec un tag correspondant au SHA du commit dans Git.

#### Workflows
- Les workflows définissent l'ordre d'exécution des jobs et leurs dépendances :
  - **build-and-test-workflow** : Exécute d'abord le job `build-and-test`, suivi par `build-and-push-docker`. Le job `build-and-push-docker` nécessite que le job `build-and-test` s'exécute avec succès.