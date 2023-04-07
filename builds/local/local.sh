#!/usr/bin/env bash
docker-compose --env-file .env.local up --detach --force-recreate --build
export $(grep -v '^#' .env.local | xargs -d '\n')
poetry run python ../../src/django_project/manage.py  runserver