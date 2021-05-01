from datetime import datetime
from datetime import timedelta
from datetime import timezone

from flask_jwt_extended import get_jwt, create_access_token, get_jwt_identity, set_access_cookies

from src import create_app
from src.businesses.user_bo import UserBo
from src.configs.jwt_config import init_jwt, jwt_redis_block_list
from src.utils.settings import get_jwt_access_token_expires


def init_app():
    print("Martial Art Manager started!")
    return create_app()


app = init_app()
jwt = init_jwt(app)


@app.before_first_request
def create_user_admin():
    user_bo = UserBo()
    user_bo.create_user_admin()


# Using an `after_request` callback, we refresh any token that is within 30
# minutes of expiring. Change the timedeltas to match the needs of your application.
@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(
            now + get_jwt_access_token_expires()
        )

        if target_timestamp > exp_timestamp:
            current_user = get_jwt()
            additional_claims = {
                "id": current_user.get("id"),
                "roles": current_user.get("roles"),
                "name": current_user.get("name"),
                "email": current_user.get("email"),
            }
            access_token = create_access_token(
                identity=get_jwt_identity(),
                additional_claims=additional_claims
            )
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response


# Callback function to check if a JWT exists in the redis blocklist
@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token_in_redis = jwt_redis_block_list.get(jti)
    return token_in_redis is not None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

