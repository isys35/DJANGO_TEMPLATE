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
    │   │   └── webpack_boilerplate/
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

##### `builds/`
- `builds/` - Тут хранятся контейнеры для развёртывания.
- `builds/local/` - Для локальной разработки
- `builds/server/` - Для дева и продакшена

##### `local_pre-commit/`
- `local_pre-commit/` - Локальный pre-commit.
- `local_pre-commit/post-commit` - 🩼 для сохраннения измененённого файла пре-коммитом static_version.py
- `local_pre-commit/static_version.py` - При коммите меняет timestamp в файле src/django_project/last-update.txt (Необходим, чтобы браузером не  кэшировалась статика)

##### `src/`
Содержит дериктории для бэкенда и фронтенда. В этом случае фронт в templates, поэтому директория одна.