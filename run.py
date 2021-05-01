from src import create_app
from src.businesses.user_bo import UserBo
from src.configs.jwt_config import init_jwt


def init_app():
    print("Martial Art Manager started!")
    return create_app()


app = init_app()
jwt = init_jwt(app)


@app.before_first_request
def create_user_admin():
    user_bo = UserBo()
    user_bo.create_user_admin()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

