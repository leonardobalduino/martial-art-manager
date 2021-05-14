from flask_mongoengine import Document
from marshmallow.fields import Nested
from mongoengine import (
    StringField,
    DictField,
    DateTimeField,
    BooleanField, ListField
)

from ..repositories.person_repository import PersonRepository


class GraduationHistory:
    graduation_id = StringField()
    name = StringField()
    description = StringField()
    color = StringField()
    graduation_date = DateTimeField()


class Person(Document):
    name = StringField(required=True, max_length=255)
    start_date = DateTimeField()
    birth_date = DateTimeField()
    email = StringField()
    phones = DictField()
    social_network = DictField()
    address = DictField()
    active = BooleanField()
    profile_image = StringField()
    biography = StringField()
    graduation_history = ListField(Nested(GraduationHistory))

    meta = {"queryset_class": PersonRepository}
