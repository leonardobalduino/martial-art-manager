from http import HTTPStatus

from ..businesses.health_bo import HealthBo
from ..configs.cache_config import cache
from ..rests.base import Blueprint
from ..utils import settings

api = Blueprint(
     name="Health",
     import_name="health_rest",
     url_prefix="/api/health",
 )


@api.route("/version", methods=["GET"])
def get_version():
    """
    Version of API.
    """
    return settings.get_version()


@api.route("", methods=["GET"])
@api.response(
    HTTPStatus.OK,
    description="""
    In case of success, the application informs:
    
    - `alive`: Value bool in case of success. Always come `true`.
    - `version`: Version of API.
    """,
)
@cache.cached(timeout=60)
def ping():
    """
    "Health" of application.
    """
    health_bo = HealthBo()
    health_bo.ping_db()
    return {"alive": True, "version": settings.get_version()}
