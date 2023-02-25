# Mashtaler Maksim, 02.2023
## ООО Ришат Тестовое задание


### Stack ###
- python3.11, Django - backend
- Postgres - database

## How to: ##

## Development local configuration ##
1) Create venv
2) Install dependencies
   - `pip install -r requirements.dev.txt`
3) Run docker container for postgres
   - `docker-compose  -f deploy/docker-compose.db.yaml up -d`
4) Make migrations
   - `cd todolist`
   - `manage.py makemigrations`
   - `manage.py migrate`
5) Run server 
   - `manage.py runserver`
6) Createsuperuser
   - `manage.py createsuperuser`
7) Connect to admin panel at http://127.0.0.1:8000/admin/
