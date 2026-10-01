# Cours SysOps – Projet fil rouge

Projet pédagogique utilisé dans le cadre du cours **Technologies SysOps**.

## Application

Application web Python basée sur Flask.

L'application écoute sur le port `5000`.

## Objectifs pédagogiques

Au cours des travaux pratiques, vous allez progressivement :

1. Prendre en main l'application.
2. La conteneuriser avec Docker.
3. Optimiser l'image Docker.
4. Publier l'image sur GitHub Container Registry (GHCR).
5. Déployer l'application sur Kubernetes avec Kind.
6. Utiliser ConfigMap et Secret.
7. Mettre en place un workflow GitHub Actions.
8. Construire une chaîne CI/CD complète.

## Technologies

- Python
- Flask
- Docker
- GitHub Container Registry (GHCR)
- Kubernetes
- Kind
- GitHub Actions

## Structure du projet

```text
cours-sysops/
├── app/
│   ├── app.py
│   └── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## Démarrage local

Construire l'image :

```bash
docker build -t cours-sysops:tp1 .
```

Lancer le conteneur :

```bash
docker run -d --name cours-sysops-tp1 -p 5000:5000 cours-sysops:tp1
```

Tester :

```bash
curl http://localhost:5000
```

Ou ouvrir http://localhost:5000 dans un navigateur.

## Travaux pratiques

Les énoncés et corrections sont fournis séparément par le formateur.

Le dépôt représente volontairement **l'état initial du projet avant le TP1**. Les étudiants feront évoluer le projet au fil des TPs.
