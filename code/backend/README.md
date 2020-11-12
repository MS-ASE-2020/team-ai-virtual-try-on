# Backend Readme

## Installation

```bash
$ python3 -m pip install django djangorestframework coreapi django-cors-headers django-revproxy
```

## Run Backend

```bash
$ python3 manage.py makemigrations BackendManagement
$ python3 manage.py migrate
$ python3 manage.py runserver
```