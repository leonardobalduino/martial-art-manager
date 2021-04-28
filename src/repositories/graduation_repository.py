from mongoengine import QuerySet

from src.repositories.base import find_by_id


class GraduationRepository(QuerySet):
    def find_by_id(self, object_id: any):
        return find_by_id(self, object_id)
