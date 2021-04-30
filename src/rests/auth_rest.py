from http import HTTPStatus

from .schemas.user_schema import (
    NewUserRequest,
    UpdateUserRequest,
    UserResponse,
    UserIdResponse, AuthenticationRequest, AccessTokenResponse
)
from ..businesses.user_bo import UserBo
from ..rests.base import Blueprint

api = Blueprint(
     name="Authentication",
     import_name="login_rest",
     url_prefix="/api/v1/auth",
 )


@api.route("/", methods=["POST"])
@api.arguments(AuthenticationRequest, required=True,)
@api.response(
    status_code=HTTPStatus.OK,
    schema=AccessTokenResponse,
    description="""
    In case of success, the application informs the key that will identify
     only user in the system.""",
)
def login(auth):
    """
    Authentication Login.
    """
    user_bo = UserBo()
    return user_bo.login(auth)
