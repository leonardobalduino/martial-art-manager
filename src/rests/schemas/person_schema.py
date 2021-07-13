from enum import Enum

from flask_smorest.fields import Upload
from marshmallow import Schema
from marshmallow.fields import (
    String,
    DateTime,
    Dict,
    Boolean,
    Nested,
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
    COUNCIL_MEMBER = "Identify person council member."
    PROFILE_IMAGE = "Image of profile."
    BIOGRAPHY = "Biography of person."
    GRADUATION_CURRENT = "Current graduation."
    GRADUATION_ID = "ID of graduation."
    GRADUATION_NAME = "Name of graduation."
    GRADUATION_DESCRIPTION = "Description of graduation."
    GRADUATION_COLOR = "Color of graduation."
    GRADUATION_DATE = "Date of graduation."


class Graduation(Schema):
    graduation_id = String(
        metadata={"description": PersonDescriptionEnum.GRADUATION_ID.value},
        default="",
    )

    name = String(
        metadata={"description": PersonDescriptionEnum.GRADUATION_NAME.value},
        default="",
    )

    description = String(
        metadata={"description": PersonDescriptionEnum.GRADUATION_DESCRIPTION.value},
        default="",
    )

    color = String(
        metadata={"description": PersonDescriptionEnum.GRADUATION_COLOR.value},
        default="",
    )

    graduation_date = DateTime(
        metadata={"description": PersonDescriptionEnum.GRADUATION_DATE.value},
        default=None,
    )


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

    active = Boolean(
        metadata={"description": PersonDescriptionEnum.ACTIVE.value},
    )

    graduation_current = Nested(
        Graduation,
        metadata={"description": PersonDescriptionEnum.GRADUATION_CURRENT.value},
    )

    council_member = Boolean(
        metadata={"description": PersonDescriptionEnum.COUNCIL_MEMBER.value},
    )

    profile_image = String(metadata={"description": PersonDescriptionEnum.PROFILE_IMAGE.value}, )

    biography = String(metadata={"description": PersonDescriptionEnum.BIOGRAPHY.value}, )


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

    council_member = Boolean(
        metadata={"description": PersonDescriptionEnum.COUNCIL_MEMBER.value},
    )

    biography = String(
        metadata={"description": PersonDescriptionEnum.BIOGRAPHY.value},
        required=False,
        allow_none=True,
    )

    graduation_current_id = String(
        metadata={"description": PersonDescriptionEnum.GRADUATION_CURRENT.value},
        required=False,
        allow_none=True,
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

    active = Boolean(
        required=False,
        allow_none=True,
        metadata={"description": PersonDescriptionEnum.ACTIVE.value},
    )

    council_member = Boolean(
        required=False,
        allow_none=True,
        metadata={"description": PersonDescriptionEnum.COUNCIL_MEMBER.value},
    )

    graduation_current_id = String(
        metadata={"description": PersonDescriptionEnum.GRADUATION_CURRENT.value},
        required=False,
        allow_none=True,
    )


class ProfileImagePersonRequest(Schema):
    file = Upload(description="File to be sent")


class ProfileImagePersonResponse(Schema):
    """
    File base64.
    """
    file_base64 = String()


class GetAllPersonRequest(Schema):
    active = Boolean(
        required=False,
        allow_none=True,
        metadata={"description": PersonDescriptionEnum.ACTIVE.value},
    )

    council_member = Boolean(
        required=False,
        allow_none=True,
        metadata={"description": PersonDescriptionEnum.COUNCIL_MEMBER.value},
    )

    graduation_id = String(
        required=False,
        allow_none=True,
        metadata={"description": PersonDescriptionEnum.GRADUATION_CURRENT.value},
    )
