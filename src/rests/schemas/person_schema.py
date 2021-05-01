from enum import Enum

from marshmallow import Schema
from marshmallow.fields import (
    String,
    DateTime,
    Dict,
    Boolean,
)


class PersonDescriptionEnum(Enum):
    ID = "ID of person."
    NAME = "Name of person."
    START_DATE = "Start date of person."
    BIRTH_DATE = "Birth date of person."
    EMAIL = "Email of person."
    PHONES = "Phones of person."
    SOCIAL_NETWORK = "Social network of person."
    ADDRESS = "Address of person."
    ACTIVE = "Identify person active."


class PersonIdResponse(Schema):
    """
    Id of the person.
    """

    id = String(metadata={"description": PersonDescriptionEnum.ID.value}, )


class PersonResponse(Schema):
    """
    person.
    """

    id = String(metadata={"description": PersonDescriptionEnum.ID.value}, )

    name = String(
        metadata={"description": PersonDescriptionEnum.NAME.value},
    )

    start_date = DateTime(
        metadata={"description": PersonDescriptionEnum.START_DATE.value},
    )

    birth_date = DateTime(
        metadata={"description": PersonDescriptionEnum.BIRTH_DATE.value},
    )

    email = String(
        metadata={"description": PersonDescriptionEnum.EMAIL.value},
    )

    phones = Dict(
        metadata={"description": PersonDescriptionEnum.PHONES.value},
    )

    social_network = Dict(
        metadata={"description": PersonDescriptionEnum.SOCIAL_NETWORK.value},
    )

    address = Dict(
        metadata={"description": PersonDescriptionEnum.ADDRESS.value},
    )

    active = Dict(
        metadata={"description": PersonDescriptionEnum.ACTIVE.value},
    )


class NewPersonRequest(Schema):
    """
    Data to create a new person.
    """

    name = String(
        required=True,
        metadata={"description": PersonDescriptionEnum.NAME.value},
    )

    start_date = DateTime(
        metadata={"description": PersonDescriptionEnum.START_DATE.value},
    )

    birth_date = DateTime(
        metadata={"description": PersonDescriptionEnum.BIRTH_DATE.value},
    )

    email = String(
        metadata={"description": PersonDescriptionEnum.EMAIL.value},
    )

    phones = Dict(
        metadata={"description": PersonDescriptionEnum.PHONES.value},
    )

    social_network = Dict(
        metadata={"description": PersonDescriptionEnum.SOCIAL_NETWORK.value},
    )

    address = Dict(
        metadata={"description": PersonDescriptionEnum.ADDRESS.value},
    )

    active = Boolean(
        metadata={"description": PersonDescriptionEnum.ACTIVE.value},
    )


class UpdatePersonRequest(Schema):
    """
    Data to update a new person.
    """
    name = String(
        required=False,
        allow_none=True,
        metadata={"description": PersonDescriptionEnum.NAME.value},
    )

    start_date = DateTime(
        required=False,
        allow_none=True,
        metadata={"description": PersonDescriptionEnum.START_DATE.value},
    )

    birth_date = DateTime(
        required=False,
        allow_none=True,
        metadata={"description": PersonDescriptionEnum.BIRTH_DATE.value},
    )

    email = String(
        required=False,
        allow_none=True,
        metadata={"description": PersonDescriptionEnum.EMAIL.value},
    )

    phones = Dict(
        required=False,
        allow_none=True,
        metadata={"description": PersonDescriptionEnum.PHONES.value},
    )

    social_network = Dict(
        required=False,
        allow_none=True,
        metadata={"description": PersonDescriptionEnum.SOCIAL_NETWORK.value},
    )

    address = Dict(
        required=False,
        allow_none=True,
        metadata={"description": PersonDescriptionEnum.ADDRESS.value},
    )

    active = Dict(
        required=False,
        allow_none=True,
        metadata={"description": PersonDescriptionEnum.ACTIVE.value},
    )
