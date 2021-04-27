import os

import dotenv


def load_settings():
    dotenv.load_dotenv()


def get_env(key, default=None) -> str:

    return os.getenv(key, default)


def get_db_uri():
    return get_env("DB_URI", "mongodb://localhost:27017/db_mongo")
