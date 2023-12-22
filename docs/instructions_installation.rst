.. _instructions_installation:

Instructions d'Installation
==========================

Cette section fournit un guide étape par étape pour installer et configurer l'application Orange County Lettings sur votre système. Suivez ces instructions pour mettre en place l'environnement de développement nécessaire.

Prérequis
---------

Avant de commencer, assurez-vous que les éléments suivants sont installés sur votre machine :

- **Python 3.8+** : Langage de programmation principal utilisé pour le développement de l'application.
- **Django 3.1+** : Framework web utilisé pour construire l'application.
- **PostgreSQL** : Système de gestion de base de données pour stocker toutes les données de l'application.

Étapes d'Installation
----------------------

1. **Cloner le Repository** :
   - Utilisez la commande `git clone [URL]` pour cloner le repository du projet sur votre machine locale. Remplacez `[URL]` par l'URL du repository Git.

2. **Créer un Environnement Virtuel** :
   - Exécutez `python -m venv venv` pour créer un nouvel environnement virtuel.
   - Activez l'environnement virtuel avec `source venv/bin/activate` sur Unix/Linux ou `venv\Scripts\activate` sur Windows.

3. **Installer les Dépendances** :
   - Installez toutes les dépendances requises en exécutant `pip install -r requirements.txt` dans le dossier racine du projet.

4. **Configurer la Base de Données PostgreSQL** :
   - Assurez-vous que PostgreSQL est installé et fonctionne sur votre machine.
   - Créez une nouvelle base de données pour l'application.
   - Configurez les paramètres de la base de données dans le fichier `settings.py` du projet pour correspondre à votre configuration PostgreSQL.

5. **Appliquer les Migrations** :
   - Lancez `python manage.py migrate` pour créer les tables nécessaires dans la base de données.

6. **Créer un Superutilisateur** :
   - Créez un superutilisateur pour accéder à l'interface d'administration Django en exécutant `python manage.py createsuperuser` et suivez les instructions.

7. **Lancer le Serveur de Développement** :
   - Démarrez le serveur de développement en exécutant `python manage.py runserver`.
   - Accédez à `http://localhost:8000` dans votre navigateur pour voir l'application en action.

Après avoir suivi ces étapes, l'application Orange County Lettings devrait être opérationnelle sur votre système de développement local. Pour toute question ou problème lors de l'installation, veuillez consulter la FAQ ou contacter l'assistance technique.
