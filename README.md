# Airline Passengers

Application web Django pour consulter des vols et les passagers qui y sont inscrits. Les données sont stockées dans une base SQLite locale.

## Fonctionnalités

- Affichage des vols avec leurs aéroports de départ et d’arrivée et leurs passagers.
- Liste des passagers et des vols associés.
- Interface d’administration Django disponible sur `/admin/`.

## Prérequis

- Python 3.12 ou version ultérieure compatible avec Django 6.1.
- `pip`.

## Installation et lancement

Dans PowerShell, depuis le dossier du projet :

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Ouvrez ensuite <http://127.0.0.1:8000/flights/>. La liste des passagers est accessible sur <http://127.0.0.1:8000/flights/passengers/>.

Pour créer un compte d’administration :

```powershell
python manage.py createsuperuser
```

Puis rendez-vous sur <http://127.0.0.1:8000/admin/>.

## Tests

```powershell
python manage.py test
```

## Structure

- `airline_passengers/` : configuration du projet Django.
- `flights/` : modèles, vues, routes et templates de l’application.
- `db.sqlite3` : base de données locale créée lors de l’utilisation du projet; elle n’est pas destinée à être partagée via Git.
