import os

import dotenv

from src.utils.constants import VERSION


def load_settings():
    dotenv.load_dotenv()


def get_env(key, default=None) -> str:

    return os.getenv(key, default)


def get_version() -> str:
    return VERSION


def get_db_uri():
    return get_env("DB_URI", "mongodb://localhost:27017/db_mongo")
