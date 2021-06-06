from mongoengine import QuerySet, Q

from src.repositories.base import find_by_id


class PersonRepository(QuerySet):
    def find_by_id(self, object_id: any):
        return find_by_id(self, object_id)

    def find_all(self, filters: dict):
        query = Q()
        if filters.get("active") is not None:
            query &= Q(active=filters.get("active"))

        if filters.get("council_member") is not None:
            query &= Q(council_member=filters.get("council_member"))

        return self.filter(query)
