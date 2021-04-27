from enum import Enum

from marshmallow import Schema
from marshmallow.fields import String, Integer


class GraduationDescriptionEnum(Enum):
    ID = "ID of graduation."
    NAME = "Name of graduation."
    DESCRIPTION = "Description of graduation."
    COLOR = "Color of graduation."
    ORDER = "Order of graduation."


class GraduationIdResponse(Schema):
    """
    Id of the graduation.
    """

    id = String(metadata={"description": GraduationDescriptionEnum.ID.value}, )


class NewGraduationRequest(Schema):
    """
    Data to create a new graduation.
    """

    name = String(
        required=True,
        metadata={"description": GraduationDescriptionEnum.NAME.value},
    )

    description = String(
        required=True,
        metadata={"description": GraduationDescriptionEnum.DESCRIPTION.value},
    )

    color = String(
        metadata={"description": GraduationDescriptionEnum.COLOR.value},
    )

    order = Integer(
        metadata={"description": GraduationDescriptionEnum.ORDER.value},
    )
