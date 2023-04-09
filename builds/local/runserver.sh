export $(grep -v '^#' .env.local | xargs -d '\n')
poetry run python ../../src/django_project/manage.py  runserver