from flask_mongoengine import Document
from mongoengine import StringField, IntField

from ..repositories.graduation_repository import GraduationRepository


class Graduation(Document):
    name = StringField(required=True, unique=True)
    description = StringField(required=True)
    color = StringField()
    order = IntField()

    meta = {"queryset_class": GraduationRepository}

