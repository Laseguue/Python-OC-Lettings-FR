.. _procedures_deploiement:

Procédures de Déploiement et de Gestion
========================================

Cette section décrit les processus de déploiement et de gestion de l'application Orange County Lettings, en utilisant CircleCI pour l'intégration et la livraison continues (CI/CD), Docker pour la conteneurisation, et Heroku pour le déploiement.

Déploiement
-----------

### Environnement de Production
- **Configuration de Django pour la Production** :
  - Assurez-vous que `DEBUG` est défini sur `False` et que les `SECRET_KEY` et autres variables sensibles sont définies en utilisant des variables d'environnement.
  - Configurez les fichiers statiques et les médias pour la production en utilisant un service de stockage comme Amazon S3, si nécessaire.

### CI/CD avec CircleCI
- **Configuration du Pipeline CI/CD** :
  - Le fichier `.circleci/config.yml` du projet contient la configuration du pipeline.
  - À chaque push sur le repository, CircleCI exécute les tests automatisés et vérifie que le code respecte les standards de qualité.

### Conteneurisation avec Docker
- **Création de l'Image Docker** :
  - Le `Dockerfile` à la racine du projet définit les étapes de création de l'image Docker de l'application.
  - Utilisez la commande `docker build` pour créer une image de l'application.

### Déploiement sur Heroku
- **Préparation pour Heroku** :
  - Assurez-vous que le `Procfile` est correctement configuré pour lancer l'application.
  - Configurez les variables d'environnement dans l'interface de gestion Heroku, y compris les informations de connexion à la base de données.
- **Déploiement** :
  - Utilisez le CLI de Heroku pour connecter votre repository à l'application Heroku.
  - Configurez CircleCI pour déployer automatiquement l'application sur Heroku après une build réussie.

Maintenance et Mises à Jour
---------------------------

### Maintenance Régulière
- Surveillez régulièrement les performances et les journaux d'erreurs sur Heroku pour identifier et résoudre les problèmes.
- Mettez à jour les dépendances régulièrement pour garantir la sécurité et l'efficacité de l'application.

### Processus de Mise à Jour
- Testez toutes les mises à jour en local ou dans un environnement de staging avant de les déployer en production.
- Utilisez les Pull Requests sur GitHub pour examiner les modifications de code et les faire valider par l'équipe avant de les fusionner dans la branche principale.
- Assurez-vous que CircleCI réussit à construire et tester les modifications avant de déployer sur Heroku.

Ce guide fournit un aperçu des étapes essentielles pour déployer et maintenir l'application Orange County Lettings. Ces procédures devraient être adaptées en fonction des spécificités de votre environnement de production et des besoins de votre équipe.
