from src import create_app
from src.configs.jwt_config import init_jwt


def init_app():
    print("Martial Art Manager started!")
    return create_app()


app = init_app()
jwt = init_jwt(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

