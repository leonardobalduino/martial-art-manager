import os
from datetime import timedelta

import dotenv

from src.utils.constants import VERSION


def load_settings():
    dotenv.load_dotenv()


def get_env(key, default=None) -> str:
    return os.getenv(key, default)


def get_env_int(key, default=None) -> int:
    return int(os.getenv(key, default))


def get_version() -> str:
    return VERSION


def get_db_uri():
    return get_env("DB_URI", "mongodb://localhost:27017/db_mongo")


def get_jwt_secret_key():
    return get_env("JWT_SECRET_KEY", "DoNotSeeThis")


def get_jwt_access_token_expires():
    minutes = get_env_int("JWT_ACCESS_TOKEN_EXPIRES", 60)
    return timedelta(minutes=minutes)


def get_redis_host():
    return get_env("REDIS_HOST", "localhost")


def get_redis_port():
    return get_env_int("REDIS_PORT", 6379)


def get_admin_user():
    admin = {
        "name": get_env("USER_NAME", "Admin"),
        "login": get_env("USER_LOGIN", "admin"),
        "password": get_env("USER_PASSWORD", "admin"),
        "email": get_env("USER_EMAIL", "admin@admin.com "),
    }
    return admin


def get_cryptography_key():
    return get_env("CRYPTOGRAPHY_KEY", "lk78Ylnfw3AL44dlZvMhDv1KG_4EmSkYEXvFuFakugc=")


def get_upload_image_allowed_extensions():
    return get_env_str_list(
        "UPLOAD_IMAGE_ALLOWED_EXTENSIONS",
        "png, jpg, jpeg, svg",
        True
    )


def get_env_str_list(key, default=None, lower_case: bool = False) -> list:
    value = get_env(key, default)
    if lower_case:
        value = value.lower()
    if value is not None:
        value = value.replace(" ", "")
        value = [v for v in value.split(",")]
    else:
        value = []
    return value
