# Шаблон для проектов на Django

*Фронтенд: Django template + webpack*


Установить pre-commit при первом запуске:
```shell
bash start_pre-commit.sh
```

### Сруктура проекта:

```
builds/
├── local/
└── server/
local_pre-commit/
├── post-commit
└── static_version.py
src/
└── django_project/
    ├── django_project/
    │   ├── apps/
    │   │   ├── core/
    │   │   │   └── __init__.py
    │   │   └── __init__.py
    │   ├── settings/
    │   │   ├── __init__.py
    │   │   ├── _base.py
    │   │   ├── dev.py
    │   │   ├── local.py
    │   │   └── production.py
    │   ├── static/
    │   ├── templates/
    │   ├── webpack/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── externals/
    │   ├── apps/
    │   │   └── webpack_boilerplate
    │   └── libs/
    ├── __version__.py
    ├── last-update.txt
    └── manage.py
.gitignore
.pre-commit-config.yaml
CHANGELOG.md
delpyc.sh
poetry.lock
pyproject.toml
README.md
start_pre-commit.sh
```