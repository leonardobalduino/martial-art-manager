from flask import Flask
from flask_mongoengine import MongoEngine

from ..utils import settings


def db_config(app: Flask):
    try:
        db = MongoEngine()
        db_uri = settings.get_db_uri()
        app.config["MONGODB_SETTINGS"] = {
            "host": db_uri,
            "connect": True,
            "tz_aware": True,
        }
        db.init_app(app)
    except Exception:
        pass
