from flask import Flask

from src.rest.health_rest import get_version


def openapi_config(app: Flask) -> None:
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["API_VERSION"] = get_version()

    app.config["OPENAPI_JSON_PATH"] = "/api/api-sec.json"
    app.config["OPENAPI_URL_PREFIX"] = "/api"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger/"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["OPENAPI_SWAGGER_UI_VERSION"] = "3.24.2"
    app.config["OPENAPI_REDOC_PATH"] = "/docs/"
    app.config["OPENAPI_REDOC_URL"] = "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"

    openapi_info = {
        "title": "Martial art manager",
        "description": "Martial art manager",
        "x-logo": {"url": "/static/logo.jpeg"},
    }
    app.config["API_TITLE"] = "Martial art manager"
    app.config["API_SPEC_OPTIONS"] = {
        "info": openapi_info,
    }


