from http import HTTPStatus

from ..businesses.health_bo import HealthBo
from ..rest.base import Blueprint

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
    return "0.0.0"


@api.route("", methods=["GET"])
@api.response(
    HTTPStatus.OK,
    description="""
    In case of success, the application informs:
    
    - `alive`: Value bool in case of success. Always come `true`.
    - `version`: Version of API.
    """,
)
def ping():
    """
    "Health" of application.
    """
    health_bo = HealthBo()
    health_bo.ping_db()
    return {"alive": True, "version": "get_app_version()"}
