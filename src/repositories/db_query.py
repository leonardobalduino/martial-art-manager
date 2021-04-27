from mongoengine import get_db


def get_build_info():
    db = get_db()
    build_info = db.command("buildinfo")
    return build_info


def get_db_version():
    build_info = get_build_info()
    db_version = build_info.get("version", "?")
    return db_version
