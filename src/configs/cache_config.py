from flask import Flask
from flask_caching import Cache

cache = Cache(config={"CACHE_TYPE": "flask_caching.backends.simple"})


def cache_config(app: Flask):
    cache.init_app(app)
