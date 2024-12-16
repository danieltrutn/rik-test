#!/bin/sh


python3 manage.py makemigrations --noinput --merge
python3 manage.py migrate

[ -d ./staticfiles/static ] || mkdir -p ./staticfiles/static
python3 manage.py collectstatic --no-input

exec python3 manage.py runserver 0.0.0.0:8000

exec "$@"