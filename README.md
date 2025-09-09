# Système de Gestion des Employés

Une application web Django pour gérer les informations des employés d'une entreprise.

## Fonctionnalités

- Liste complète des employés
- Ajout de nouveaux employés
- Modification des informations des employés
- Suppression d'employés
- Interface utilisateur intuitive

## Structure du Projet

Le projet est composé des éléments suivants :
- Une application Django `employe` pour la gestion des employés
- Un modèle `Employe` avec les champs :
  - Nom
  - Email
  - Poste
  - Salaire
- Interface utilisateur avec des templates Django
- Formulaires pour la saisie et la modification des données

## Technologies Utilisées

- Python 3.13
- Django 5.2.6
- SQLite (base de données par défaut)
- Tailwind CSS (via CDN) pour le style
- DaisyUI (via CDN) comme bibliothèque de composants UI
- HTML pour les templates

### Intégration Frontend
Le projet utilise Tailwind CSS et DaisyUI via CDN, ce qui signifie qu'aucune installation locale n'est nécessaire. Les CDN sont déjà configurés dans le template de base :
```html
<link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
<link href="https://cdn.jsdelivr.net/npm/daisyui@5/themes.css" rel="stylesheet" type="text/css" />
```

## Installation

1. Clonez le dépôt
```bash
git clone [URL_DU_DEPOT]
cd django
```

2. Créez un environnement virtuel et activez-le
```bash
python -m venv env
# Sur Windows
env\Scripts\activate
```

3. Installez les dépendances Python
```bash
pip install -r requirements.txt
```

4. Effectuez les migrations
```bash
python manage.py migrate
```

5. Lancez le serveur de développement
```bash
python manage.py runserver
```

L'application sera accessible à l'adresse http://127.0.0.1:8000/

## Utilisation

- Accédez à la liste des employés via la page d'accueil
- Utilisez le bouton "Ajouter un employé" pour créer un nouvel enregistrement
- Cliquez sur "Modifier" pour mettre à jour les informations d'un employé
- Utilisez "Supprimer" pour retirer un employé de la base de données

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
