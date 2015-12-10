web:python manage.py makemigrations
web:python manage.py migrate
web:python manage.py runserver
web: gunicorn practiceplacementpapers.wsgi
heroku ps:scale web=1
worker:celeryd --loglevel=INFO
