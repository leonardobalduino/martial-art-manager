from http import HTTPStatus

from .schemas.user_schema import (
    NewUserRequest,
    UpdateUserRequest,
    UserResponse,
    UserIdResponse
)
from ..businesses.user_bo import UserBo
from ..rests.base import Blueprint

api = Blueprint(
     name="User",
     import_name="user_rest",
     url_prefix="/api/v1/users",
 )


@api.route("/", methods=["POST"])
@api.arguments(NewUserRequest, required=True,)
@api.response(
    status_code=HTTPStatus.CREATED,
    schema=UserIdResponse,
    description="""
    In case of success, the application informs the key that will identify
     only user in the system.""",
)
def save(new):
    """
    Create a new user.
    """
    user_bo = UserBo()
    return user_bo.save(new)


@api.route("/<user_id>", methods=["GET"])
@api.response(
    status_code=HTTPStatus.OK,
    schema=UserResponse,
    description="""
    In case of success, the application informs the key that will identify
     only user in the system.""",
)
def find_by_id(user_id):
    """
    Find by id of the user.
    """
    user_bo = UserBo()
    return user_bo.find_by_id(user_id)


@api.route("/", methods=["GET"])
@api.response(
    status_code=HTTPStatus.OK,
    schema=UserResponse(many=True),
    description="""
    In case of success, the application informs all users in the system.""",
)
def find_all():
    """
    Get all users.
    """
    user_bo = UserBo()
    return user_bo.find_all()


@api.route("/<user_id>", methods=["PATCH"])
@api.arguments(UpdateUserRequest, required=True,)
@api.response(
    status_code=HTTPStatus.NO_CONTENT,
    description="""
    Record updated.""",
)
def update_patch(user, user_id):
    """
    Update a user.
    """
    user_bo = UserBo()
    return user_bo.update(user_id, user)


@api.route("/<user_id>", methods=["DELETE"])
@api.response(
    status_code=HTTPStatus.NO_CONTENT,
    description="""
    Record deleted.""",
)
def delete(user_id):
    """
    Delete a user.
    """
    user_bo = UserBo()
    return user_bo.delete(user_id)
