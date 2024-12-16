#!/bin/bash

sudo apt install python3.10-venv
python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic

python3 manage.py runserver 0.0.0.0:8000
