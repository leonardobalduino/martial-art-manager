from mongoengine import QuerySet, Q

from src.repositories.base import find_by_id


class UserRepository(QuerySet):
    def find_by_id(self, object_id: any):
        return find_by_id(self, object_id)

    def find_all(self):
        return list(self.all().order_by("name"))

    def find_by_login(self, login: str):
        return self.filter(Q(login=login)).first()
