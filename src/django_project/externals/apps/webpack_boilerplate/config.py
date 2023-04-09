import re

__all__ = ("load_config", "get_setting_value")


def load_from_django():
    from django.conf import settings

    DEFAULT_CONFIG = {
        "CACHE": not settings.DEBUG,
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
        "LOADER_CLASS": "externals.apps.webpack_boilerplate.loader.WebpackLoader",
    }

    user_config = dict(DEFAULT_CONFIG, **getattr(settings, "WEBPACK_LOADER", {}))

    user_config["ignores"] = [re.compile(i) for i in user_config["IGNORE"]]
    user_config["web_framework"] = "django"
    return user_config


def load_config(name):
    try:
        pass

        return load_from_django()
    except ImportError:
        pass

    raise Exception("can not load config from this project")


def get_setting_value(key):
    try:
        from django.conf import settings

        return settings.get(key, None)
    except ImportError:
        pass

    try:
        from flask import current_app

        map = {"STATIC_URL": "STATIC_URL"}
        return current_app.config.get(map[key], None)
    except ImportError:
        pass


def setup_jinja2_ext(app):
    """
    Run by flask app
    """
    from .contrib.jinja2ext import WebpackExtension

    app.jinja_env.add_extension(WebpackExtension)
