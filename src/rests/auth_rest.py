from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt

from .schemas.user_schema import (
    AuthenticationRequest,
    AccessTokenResponse
)
from ..businesses.user_bo import UserBo
from ..configs.jwt_config import jwt_redis_block_list
from ..rests.base import Blueprint
from ..utils.settings import get_jwt_access_token_expires

api = Blueprint(
     name="Authentication",
     import_name="login_rest",
     url_prefix="/api/v1/auth",
 )


@api.route("/login", methods=["POST"])
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


@api.route("/logout", methods=["DELETE"])
@jwt_required()
@api.response(
    status_code=HTTPStatus.OK,
    description="""
    It will revoke the token.""",
)
def login():
    """
    Authentication Logout.
    """
    jti = get_jwt()["jti"]
    jwt_redis_block_list.set(jti, "", ex=get_jwt_access_token_expires())
    return jsonify(msg="Access token revoked")


@api.route("/renew", methods=["GET"])
@jwt_required()
@api.response(
    status_code=HTTPStatus.OK,
    schema=AccessTokenResponse,
    description="""
    In case of success, the application informs the key that will identify
     only user in the system.""",
)
def renew():
    """
    Authentication Renew.
    """
    user_bo = UserBo()
    return user_bo.renew()
