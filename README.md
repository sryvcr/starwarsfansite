# STARWARS FANSITE

### Requirements 
- python==3.8
- Django==3.0.8
- django-filter==2.1.0
- graphene-django==2.12.1

### How to run app

1. Clone repository
```sh
$ mkdir starwarsfansite
$ cd starwarsfansite
$ virtualenv . -p python3
$ mkdir src
$ cd src
$ git clone https://github.com/sryvcr/starwarsfansite.git
$ source ../bin/activate
$ (starwarsfansite) cd starwarsfansite
```

2. Apply requirements
```sh
$ (starwarsfansite) pip install -r requirements.txt
```

3. Run server
```sh
$ (starwarsfansite) python manage.py runserver
```

#### Note
In path starwarsfansite/test/ you will find many files that show how to make querys and mutations
