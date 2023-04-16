# Шаблон для проектов на Django

*Фронтенд: Django template + webpack*


Установить pre-commit при старте проекта:
```shell
bash start_pre-commit.sh
```

### Сруктура проекта:

```
scripts/                                   # Различные скрипты
├── local_pre-commit/                      # Локальный pre-commit
│   ├── post-commit                        # 🩼 для сохраннения измененённого файла пре-коммитом static_version.py
│   └── static_version.py                  # При коммите меняет timestamp в файле src/django_project/last-update.txt (Необходим, чтобы браузером не  кэшировалась статика)
└── delpyc.sh                              # Чистит кэш Python
src/                                       # Содержит директории для бэка, фронта, devops
├── builds/
│   ├── ...
│   └── README.md                           
└── django_project/
    ├── ...
    └── README.md                          # Описание и структура Django проекта 
.gitignore
.pre-commit-config.yaml
CHANGELOG.md
delpyc.sh
poetry.lock
pyproject.toml
README.md
start_pre-commit.sh
```