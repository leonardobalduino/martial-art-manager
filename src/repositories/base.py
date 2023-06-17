from bson import ObjectId
from mongoengine import QuerySet, Document, Q

from src.utils.exceptions import NotFoundException


def _is_object_id(value: any):
    try:
        ObjectId(value)
        return True
    except Exception:
        return False


def parse_to_object_id(value: any):
    if _is_object_id(value):
        return ObjectId(value)
    else:
        return str(ObjectId(b"111111111111"))


def find_by_id(qs: QuerySet, doc_id: str, throw_exception: bool = True) -> Document:
    obj = qs.filter(Q(id=doc_id)).first()
    if obj is None and throw_exception:
        raise NotFoundException(message="Record not found", errors=str(qs))

    return obj
