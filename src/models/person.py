from flask_mongoengine import Document
from mongoengine import (
    StringField,
    DictField,
    DateTimeField,
    BooleanField
)

from ..repositories.person_repository import PersonRepository


class Person(Document):
    name = StringField(required=True, max_length=255)
    start_date = DateTimeField()
    birth_date = DateTimeField()
    email = StringField()
    phones = DictField()
    social_network = DictField()
    address = DictField()
    active = BooleanField()

    meta = {"queryset_class": PersonRepository}

