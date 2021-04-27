from ..rests.base import Blueprint

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
