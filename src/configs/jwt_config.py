import redis as redis
from flask_jwt_extended import JWTManager, get_jwt

from src.utils.enuns import Roles
from src.utils.exceptions import UnAuthorizedException
from src.utils.settings import (
    get_jwt_secret_key,
    get_jwt_access_token_expires,
    get_redis_host,
    get_redis_port
)

# Setup our redis connection for storing the blocklisted tokens. You will probably
# want your redis instance configured to persist data to disk, so that a restart
# does not cause your application to forget that a JWT was revoked.
jwt_redis_block_list = redis.StrictRedis(
    host=get_redis_host(), port=get_redis_port(), db=0, decode_responses=True
)


def init_jwt(_app):
    _app.config['JWT_SECRET_KEY'] = get_jwt_secret_key()
    _app.config["JWT_ACCESS_TOKEN_EXPIRES"] = get_jwt_access_token_expires()
    return JWTManager(_app)


def check_role(role):
    current_user = get_jwt()
    roles = current_user.get("roles")

    admin = Roles.ADMINISTRATOR.value in roles

    if admin is False:
        permission = role in roles
        if permission is None or permission is False:
            raise UnAuthorizedException(message="You do not have permission")
