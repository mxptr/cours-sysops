# Cours SysOps – Projet fil rouge

Projet fil rouge du cours **Technologies SysOps**.

L'objectif est de faire évoluer progressivement une application Flask, depuis son exécution locale jusqu'à son déploiement automatisé sur Kubernetes.

## Parcours

| TP | Thème | Technologies |
|---|---|---|
| TP1 | Prise en main et lancement de l'application | Git, Docker |
| TP2 | Optimiser, taguer et publier une image Docker | Docker, GHCR |
| TP3 | Premier déploiement Kubernetes | Kubernetes, Kind |
| TP4 | Déploiement complet avec Kubernetes | Kubernetes, ConfigMap, Secret |
| TP5 | Premier workflow GitHub Actions | GitHub Actions, GHCR |
| TP6 | Pipeline CI/CD complet | GitHub Actions, Kind, Kubernetes |

## Structure du projet

```text
cours-sysops/
├── app/
│   ├── app.py
│   └── requirements.txt
├── docs/
│   └── tps/
│       ├── README.md
│       ├── TP01.md
│       ├── TP02.md
│       ├── TP03.md
│       ├── TP04.md
│       ├── TP05.md
│       └── TP06.md
├── Dockerfile
├── .dockerignore
├── .gitignore
├── LICENSE
└── README.md
```

## Démarrage

Commencez par le [TP1 – Prise en main et lancement de l'application](docs/tps/TP01.md).

Les énoncés des six TPs sont disponibles dans [`docs/tps/`](docs/tps/).

## Projet pédagogique

Ce dépôt constitue le projet de départ du cours.

Vous êtes invités à **forker ce dépôt dans votre propre compte GitHub** puis à suivre progressivement les différents TPs en conservant votre historique Git.

Chaque TP vous amènera à faire évoluer progressivement le projet :

**Application Flask → Docker → GHCR → Kubernetes → GitHub Actions → CI/CD**
