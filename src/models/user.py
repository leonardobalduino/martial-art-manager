from mongoengine import Document, StringField, BooleanField, ListField

from src.repositories.user_repository import UserRepository


class User(Document):
    name = StringField(required=True, unique=True)
    login = StringField(required=True, unique=True)
    password = StringField()
    email = StringField(required=True, unique=True)
    active = BooleanField()
    roles = ListField(StringField())

    meta = {"queryset_class": UserRepository}
