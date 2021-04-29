from flask import Flask
from flask_cors import CORS

from .cache_config import cache_config
from .db_config import db_config
from .excpetion_config import error_handling_config
from .routes_config import routes_config
from ..configs.openapi_config import openapi_config


def api_config(app: Flask) -> None:
    CORS(app, resources={r"/*": {"origins": "*", "send_wildcard": "False"}})
    openapi_config(app)
    routes_config(app)
    cache_config(app)
    error_handling_config(app)
    db_config(app)
