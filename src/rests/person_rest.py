from http import HTTPStatus

from .schemas.person_schema import (
    NewPersonRequest,
    UpdatePersonRequest,
    PersonResponse,
    PersonIdResponse
)
from ..businesses.person_bo import PersonBo
from ..configs.jwt_config import check_role
from ..rests.base import Blueprint
from ..utils.enuns import Roles

api = Blueprint(
     name="Person",
     import_name="person_rest",
     url_prefix="/api/v1/persons",
 )


@api.route("/", methods=["POST"])
@check_role(role=Roles.MANAGE_REGISTER.value)
@api.arguments(NewPersonRequest, required=True,)
@api.response(
    status_code=HTTPStatus.CREATED,
    schema=PersonIdResponse,
    description="""
    In case of success, the application informs the key that will identify
     only person in the system.""",
)
def save(new):
    """
    Create a new person.
    """
    person_bo = PersonBo()
    return person_bo.save(new)


@api.route("/<person_id>", methods=["GET"])
@api.response(
    status_code=HTTPStatus.OK,
    schema=PersonResponse,
    description="""
    In case of success, the application informs the key that will identify
     only person in the system.""",
)
def find_by_id(person_id):
    """
    Find by id of the person.
    """
    person_bo = PersonBo()
    return person_bo.find_by_id(person_id)


@api.route("/", methods=["GET"])
@api.response(
    status_code=HTTPStatus.OK,
    schema=PersonResponse(many=True),
    description="""
    In case of success, the application informs all persons in the system.""",
)
def find_all():
    """
    Get all persons.
    """
    person_bo = PersonBo()
    return person_bo.find_all()


@api.route("/<person_id>", methods=["PATCH"])
@check_role(role=Roles.MANAGE_REGISTER.value)
@api.arguments(UpdatePersonRequest, required=True,)
@api.response(
    status_code=HTTPStatus.NO_CONTENT,
    description="""
    Record updated.""",
)
def update_patch(person, person_id):
    """
    Update a person.
    """
    person_bo = PersonBo()
    return person_bo.update(person_id, person)


@api.route("/<person_id>", methods=["DELETE"])
@check_role(role=Roles.ADMINISTRATOR.value)
@api.response(
    status_code=HTTPStatus.NO_CONTENT,
    description="""
    Record deleted.""",
)
def delete(person_id):
    """
    Delete a person.
    """
    person_bo = PersonBo()
    return person_bo.delete(person_id)
