from bson import ObjectId
from mongoengine import QuerySet, Document, Q


def _is_object_id(value: any):
    try:
        ObjectId(value)
        return True
    except Exception:
        return False


def _parse_to_object_id(value: any):
    if _is_object_id(value):
        return ObjectId(value)
    else:
        return str(ObjectId(b"111111111111"))


def find_by_id(qs: QuerySet, doc_id: str) -> Document:
    doc_id = _parse_to_object_id(doc_id)
    return qs.filter(Q(id=doc_id)).first()
