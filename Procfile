web: gunicorn auth_system.wsgi:application --log-file -
python manage.py collectstatic --noinput
manage.py migrate