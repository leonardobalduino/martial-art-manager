from flask_cors import CORS


def cors_config(app):
    configs = (
        {
            "resources": r"/api/health/*",
            "methods": ("GET", "HEAD", "OPTIONS"),
        },
        {
            "resources": r"/api/v1/*",
            "origins": "*",
            "send_wildcard": "False",
        },
    )

    for config in configs:
        CORS(app, **config)
