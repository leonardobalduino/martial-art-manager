from http import HTTPStatus

from .schema.graduation_schema import (
    NewGraduationRequest,
    UpdateGraduationRequest,
    GraduationResponse,
    GraduationIdResponse
)
from ..businesses.graduation_bo import GraduationBo
from ..rest.base import Blueprint

api = Blueprint(
     name="Graduation",
     import_name="graduation_rest",
     url_prefix="/api/v1/graduations",
 )


@api.route("/", methods=["POST"])
@api.arguments(NewGraduationRequest, required=True,)
@api.response(
    status_code=HTTPStatus.CREATED,
    schema=GraduationIdResponse,
    description="""
    In case of success, the application informs the key that will identify
     only graduation in the system.""",
)
def save(new):
    """
    Create a new graduation.
    """
    graduation_bo = GraduationBo()
    return graduation_bo.save(new)


@api.route("/<graduation_id>", methods=["GET"])
@api.response(
    status_code=HTTPStatus.OK,
    schema=GraduationResponse,
    description="""
    In case of success, the application informs the key that will identify
     only graduation in the system.""",
)
def find_by_id(graduation_id):
    """
    Find by id of the graduation.
    """
    graduation_bo = GraduationBo()
    return graduation_bo.find_by_id(graduation_id)


@api.route("/", methods=["GET"])
@api.response(
    status_code=HTTPStatus.OK,
    schema=GraduationResponse(many=True),
    description="""
    In case of success, the application informs all graduations in the system.""",
)
def find_all():
    """
    Get all graduations.
    """
    graduation_bo = GraduationBo()
    return graduation_bo.find_all()


@api.route("/<graduation_id>", methods=["PATCH"])
@api.arguments(UpdateGraduationRequest, required=True,)
@api.response(
    status_code=HTTPStatus.NO_CONTENT,
    description="""
    Record updated.""",
)
def update_patch(graduation, graduation_id):
    """
    Update a graduation.
    """
    graduation_bo = GraduationBo()
    return graduation_bo.update(graduation_id, graduation)


@api.route("/<graduation_id>", methods=["DELETE"])
@api.response(
    status_code=HTTPStatus.NO_CONTENT,
    description="""
    Record deleted.""",
)
def delete(graduation_id):
    """
    Delete a graduation.
    """
    graduation_bo = GraduationBo()
    return graduation_bo.delete(graduation_id)