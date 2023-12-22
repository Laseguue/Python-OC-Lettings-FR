.. _guide_demarrage_rapide:

Guide de Démarrage Rapide
=========================

Ce guide fournit des instructions claires pour démarrer rapidement avec l'application Orange County Lettings. Suivez ces étapes pour lancer l'application et naviguer dans ses fonctionnalités clés.

Comment Démarrer l'Application
------------------------------

1. **Lancer le Serveur** :
   - Dans votre terminal, naviguez vers le dossier racine du projet.
   - Exécutez la commande `python manage.py runserver` pour démarrer le serveur de développement.
   - Le serveur démarre, généralement sur le port 8000.

2. **Accéder à l'Application** :
   - Ouvrez votre navigateur web.
   - Allez à `http://localhost:8000` pour visualiser la page d'accueil de l'application.
   - Explorez les différentes sections disponibles : Accueil, Lettings, et Profils.

3. **Utiliser l'Interface Administrateur** :
   - Pour accéder à l'interface administrateur, allez à `http://localhost:8000/admin`.
   - Connectez-vous avec le superutilisateur. Si vous n'avez pas encore de superutilisateur, créez-en un en utilisant `python manage.py createsuperuser` dans le terminal.
   - Une fois connecté, vous pouvez gérer les utilisateurs, les profils, et les lettings.

Commandes de Base
------------------

- **Démarrer le Serveur** : 
   - Exécutez `python manage.py runserver` pour lancer le serveur de développement. Il s'exécutera par défaut à l'adresse `http://localhost:8000`.

- **Arrêter le Serveur** : 
   - Pour arrêter le serveur, utilisez `Ctrl + C` dans votre terminal.

- **Accès à l'Interface Administrateur** : 
   - Naviguez vers `http://localhost:8000/admin` pour accéder à l'interface administrateur.
   - Utilisez les identifiants du superutilisateur pour vous connecter.

Conseils Utiles
---------------

- Assurez-vous que toutes les dépendances sont installées avant de lancer le serveur.
- Pour les modifications importantes, testez votre application localement avant de déployer les changements en production.
- Consultez la documentation technique pour des informations détaillées sur la structure et les fonctionnalités de l'application.

Ce guide rapide est conçu pour vous aider à démarrer avec l'application Orange County Lettings. Pour une utilisation plus approfondie, veuillez vous référer aux autres sections de cette documentation.
