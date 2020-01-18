# twitterro
    sosial media using django with postgreSQL

## start new project in django
    django-admin startproject twitterro

## run a server
    python manage.py runserver

## create a new app
    python manage.py startapp 'apps name'

## Make database prepare migration using orm
    python manage.py makemigrations

## Choose Migration
    python manage.py sqlmigrate 'model' 'migration file name'

## apply migration using orm
    python manage.py migrate

## add admin
    python manage.py createsuperuser
