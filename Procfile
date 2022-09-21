release: sh -c 'python manage.py makemigrations && python manage.py migrate && python manage.py loaddata movie_catalog_data.json'
web: gunicorn project_django.wsgi --log-file -