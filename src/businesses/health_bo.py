from ..repositories.db_query import get_db_version


class HealthBo:
    def ping_db(self):
        try:
            db_version = get_db_version()
            return f"Conected on data base MongoDB (version={db_version})"
        except Exception as ex:
            raise ex

