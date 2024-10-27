# README - Application de Gestion des Tâches

## Objectif du projet
Cette application web de gestion des tâches permet aux utilisateurs de s'inscrire, de se connecter et de gérer leurs tâches de manière efficace. Les utilisateurs peuvent créer, modifier, annuler, supprimer et marquer des tâches comme terminées.

## Technologies Utilisées
- **Backend**: Django avec Django Rest Framework (DRF)
- **Frontend**: React.js
- **Base de données**: PostgreSQL
- **Authentification**: Djoser et JSON Web Tokens (JWT)
- **Design**: Figma pour la conception des interfaces utilisateur

## Détails Techniques

### Backend
Lors de la création de l'application, j'ai utilisé Django Rest Framework (DRF) pour le backend, et grâce à mon expérience avec cet outil, j'ai pu le mettre en œuvre sans trop de difficultés. L'intégration de Djoser pour la gestion de l'authentification a été une tâche relativement simple, car il fournit une API prête à l'emploi pour l'inscription et la connexion des utilisateurs. J'ai également intégré JSON Web Tokens (JWT) pour la gestion des sessions.

Un défi spécifique que j'ai rencontré était la nécessité de créer des serializers personnalisés pour l'enregistrement des utilisateurs. Cela m'a permis d'ajouter les tokens d'accès et de rafraîchissement dans la réponse de l'API, facilitant ainsi l'authentification et l'autorisation des utilisateurs dans l'application.

Concernant les modèles, j'ai défini deux modèles principaux : `AppUser`, qui hérite de `AbstractUser`, et le modèle `Task` pour gérer les tâches. Pour simplifier la création des vues, j'ai utilisé des classes génériques de DRF telles que `ListAPIView`, `CreateAPIView`, `UpdateAPIView`, et `DestroyAPIView`. Cela m'a permis de respecter les meilleures pratiques de DRF tout en minimisant le code nécessaire pour gérer les opérations CRUD.

### Compromis
Un compromis que j'ai dû faire concerne le choix entre l'utilisation de `ModelViewSet` pour gérer toutes les opérations CRUD d'un coup, ou de conserver des vues génériques pour chaque opération. J'ai choisi d'utiliser des vues génériques pour plusieurs raisons : cela offre plus de flexibilité pour personnaliser le comportement de chaque vue à l'avenir, surtout si des exigences supplémentaires devaient être ajoutées. Même si cela a entraîné un code légèrement plus long, cela garantit que chaque vue est spécifiquement adaptée à ses fonctionnalités, facilitant ainsi les ajustements futurs.

### Autres Défis Techniques
D'autres défis techniques ont émergé, notamment la gestion de la compatibilité entre navigateurs lors du développement du frontend avec React. J'ai veillé à ce que l'application soit compatible avec les navigateurs modernes, mais cela a nécessité des tests supplémentaires pour garantir que les fonctionnalités d'interaction soient cohérentes sur toutes les plateformes.

Enfin, un autre défi a été d'assurer une intégration fluide entre le frontend et le backend. Cela incluait la configuration des appels API pour récupérer et envoyer des données correctement. Bien que j'aie utilisé des outils comme Axios pour faciliter les requêtes HTTP, il a fallu du temps pour gérer les erreurs et assurer une bonne communication entre les deux couches de l'application.

### Côté Client
Sur le côté client, j'ai principalement utilisé React pour créer une expérience utilisateur interactive. J'ai commencé par créer un fichier `api.jsx` dans lequel j'ai centralisé toutes les requêtes API pour chaque endpoint. Cela a simplifié la gestion des appels API, car tous les points d'accès sont maintenant regroupés au même endroit, rendant le code plus propre et plus facile à maintenir.

Ensuite, j'ai développé des composants pour les pages de login, registration, et dashboard. Pour la gestion des formulaires, j'ai intégré `react-hook-form` pour simplifier la validation et la gestion de l'état des formulaires. J'ai également utilisé Zod pour la validation des données, ce qui m'a permis de m'assurer que les utilisateurs fournissent des informations correctes et conformes avant d'envoyer des requêtes au backend.

Un défi particulier dans cette partie a été d'assurer que la validation soit à la fois intuitive et utile pour l'utilisateur. L'utilisation de `react-hook-form` et Zod a facilité cette tâche, bien que la configuration initiale ait pris un certain temps. En conséquence, les formulaires offrent une expérience fluide et réactive, avec des messages d'erreur clairs qui améliorent l'expérience utilisateur.

## Instructions pour Exécuter l'Application

###  backend 
1. Installez Pipenv si ce n'est pas déjà fait :
   ```bash
   pip install pipenv
2. Installez les dépendances avec Pipenv :
   ```bash
   pipenv install  
3. Effectuez les migrations :
   ```bash
   python manage.py migrate
1. Démarrez le serveur :
   ```bash
   python manage.py runserver




###  backend 
1. Installez les dépendances :
   ```bash
   npm install
2. Démarrez l'application :
   ```bash
   npm start  
