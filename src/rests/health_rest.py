from http import HTTPStatus

from flask import Blueprint

api = Blueprint(
    "Health",
    "health_rest",
    url_prefix="/api/health",
)


@api.route("/version", methods=["GET"])
def get_version():
    """
    Version of API.
    """
    return "0.0.0"
