from flask import Flask
from flask_smorest import Api
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, map, *args):
        super().__init__(map)
        self.map = map
        self.regex = args[0]


def register_routes(app: Flask, routes: list):
    api = Api(app)
    for blp in routes:
        api.register_blueprint(blp)


def routes_config(app: Flask):
    app.url_map.converters["regex"] = RegexConverter

    from ..rests.health_rest import api as health_api
    from ..rests.graduation_rest import api as graduation_api
    from ..rests.user_rest import api as user_api

    routes = [
            health_api,
            user_api,
            graduation_api,
        ]
    register_routes(app, routes)
