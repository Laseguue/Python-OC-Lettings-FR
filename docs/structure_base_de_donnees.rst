.. _structure_base_de_donnees:

Structure de la Base de Données et Modèles de Données
=====================================================

Cette section fournit un aperçu de la structure de la base de données et des modèles de données du projet.

Schéma de la Base de Données
-----------------------------

Modèle Profile: Étend le modèle User de Django, ajoute un champ favorite_city. Relations: OneToOne avec User.
Modèle Letting: Représente les locations, lié au modèle Address par une relation OneToOne.
Modèle Address: Stocke les détails de l'adresse, utilisé par le modèle Letting.

.. code-block:: text

    +------------------+     +------------------+     +------------------+
    |                  |     |                  |     |                  |
    |      User        |     |     Profile      |     |     Letting      |
    |                  |     |                  |     |                  |
    | - id             |<----| - user_id (FK)   |     | - id             |
    | - username       |     | - favorite_city  |     | - title          |
    | - password       |     +------------------+     | - address_id (FK)|
    | - email          |                                 |                  |
    | - first_name     |     +------------------+     +------------------+
    | - last_name      |     |                  |
    | ...              |     |     Address      |
    +------------------+     |                  |
                             | - id             |
                             | - number         |
                             | - street         |
                             | - city           |
                             | - state          |
                             | - zip_code       |
                             | - country_iso_code|
                             +------------------+

                             
Description des Modèles
------------------------

Les modèles incluent Address, Letting, et Profile, 
chacun avec des relations et des rôles définis pour 
gérer efficacement les données de location et d'utilisateur.


