export $(grep -v '^#' .env.local | xargs -d '\n')
poetry run python ../../django_project/manage.py  runserver