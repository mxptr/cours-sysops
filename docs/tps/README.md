# Travaux pratiques

## Projet fil rouge

Les six travaux pratiques font évoluer progressivement l'application Flask,
depuis son exécution locale jusqu'à une chaîne CI/CD avec Kubernetes.

## Parcours

### TP1 – Prise en main et lancement de l'application

Préparer l'environnement, cloner le projet, construire et lancer l'application
avec Docker.

[Voir l'énoncé du TP1](TP01.md)

### TP2 – Optimiser, taguer et publier une image Docker

Optimiser le Dockerfile, utiliser un utilisateur non-root et publier l'image
sur GitHub Container Registry.

[Voir l'énoncé du TP2](TP02.md)

### TP3 – Premier déploiement Kubernetes

Créer un cluster Kind local, déployer l'application avec un Deployment et
l'exposer avec un Service.

[Voir l'énoncé du TP3](TP03.md)

### TP4 – Déploiement complet avec Kubernetes

Utiliser ConfigMap et Secret, mettre à jour le Deployment et manipuler le
scaling et le remplacement automatique des Pods.

[Voir l'énoncé du TP4](TP04.md)

### TP5 – Premier workflow GitHub Actions

Automatiser la construction et la publication de l'image Docker sur GHCR.

[Voir l'énoncé du TP5](TP05.md)

### TP6 – Pipeline CI/CD complet

Créer un cluster Kind éphémère dans GitHub Actions, construire et publier
l'image, la charger dans Kind, déployer l'application et vérifier son bon
fonctionnement.

[Voir l'énoncé du TP6](TP06.md)
