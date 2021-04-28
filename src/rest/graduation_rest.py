from http import HTTPStatus

from .schema.graduation_schema import NewGraduationRequest, GraduationIdResponse, UpdateGraduationRequest
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
