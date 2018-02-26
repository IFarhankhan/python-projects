# python-projects: https://docs.python.org/3/
Python open source projects: Includes APIs and web applications.


https://virtualenv.pypa.io/en/latest/installation/

For all project you should create seperate envs


"virtualenv -p python3 nameofyourenv"


Django: https://www.djangoproject.com/

1) Pacakges:  pip install django djangorestframework pyparsing six packaging appdirs
2) Directory: mkdir src  
3) cd src
4) Create: django-admin.py startproject api_users
5) cd api_users
5) Create api: python manage.py startapp user_api
6) Server: python manage.py runserver 0.0.0.0:8080
7) DBMake: python manage.py makemigrations
8) DBMigrate: python manage.py migrate
9) Create superuser: python manage.py createsuperuser

Flask: http://flask.pocoo.org/

1) Packages: pip install Flask Flask-JWT Flask-RESTful Flask-SQLAlchemy
