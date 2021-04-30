from enum import Enum

from marshmallow import Schema
from marshmallow.fields import String, Integer, List, Boolean


class UserDescriptionEnum(Enum):
    ID = "ID of user."
    NAME = "Name of user."
    LOGIN = "Login of user."
    PASSWORD = "Password of user."
    EMAIL = "Order of user."
    ACTIVE = "Identify user active"
    ROLES = "Roles of user."
    ACCESS_TOKEN = "Access token"


class UserIdResponse(Schema):
    """
    Id of the user.
    """

    id = String(metadata={"description": UserDescriptionEnum.ID.value}, )


class UserResponse(Schema):
    """
    user.
    """

    id = String(metadata={"description": UserDescriptionEnum.ID.value}, )

    name = String(
        metadata={"description": UserDescriptionEnum.NAME.value},
    )

    active = Boolean(
        metadata={"description": UserDescriptionEnum.ACTIVE.value},
    )


class NewUserRequest(Schema):
    """
    Data to create a new user.
    """

    name = String(
        required=True,
        metadata={"description": UserDescriptionEnum.NAME.value},
    )

    login = String(
        required=True,
        metadata={"description": UserDescriptionEnum.LOGIN.value},
    )

    email = String(
        required=True,
        metadata={"description": UserDescriptionEnum.EMAIL.value},
    )

    roles = List(
        String,
        metadata={"description": UserDescriptionEnum.ROLES.value},
        required=False,
        allow_none=True,
    )


class UpdateUserRequest(Schema):
    """
    Data to update a new user.
    """
    name = String(
        required=False,
        allow_none=True,
        metadata={"description": UserDescriptionEnum.NAME.value},
    )

    login = String(
        required=False,
        allow_none=True,
        metadata={"description": UserDescriptionEnum.LOGIN.value},
    )

    password = String(
        required=False,
        allow_none=True,
        metadata={"description": UserDescriptionEnum.PASSWORD.value},
    )

    email = String(
        required=False,
        allow_none=True,
        metadata={"description": UserDescriptionEnum.EMAIL.value},
    )

    roles = List(
        String,
        metadata={"description": UserDescriptionEnum.ROLES.value},
        required=False,
        allow_none=True,
    )

    active = Boolean(
        required=False,
        allow_none=True,
        metadata={"description": UserDescriptionEnum.ACTIVE.value},
    )


class AuthenticationRequest(Schema):
    """
    Data to authentication of the user.
    """

    login = String(
        required=True,
        metadata={"description": UserDescriptionEnum.LOGIN.value},
    )

    password = String(
        required=True,
        metadata={"description": UserDescriptionEnum.PASSWORD.value},
    )


class AccessTokenResponse(Schema):
    """
    Access token of the user.
    """

    access_token = String(
        metadata={"description": UserDescriptionEnum.LOGIN.value},
    )
