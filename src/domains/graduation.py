from flask_mongoengine import Document
from mongoengine import StringField, IntField


class Graduation(Document):
    name = StringField(required=True, unique=True)
    description = StringField(required=True)
    color = StringField()
    order = IntField()

