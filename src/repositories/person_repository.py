import re

from mongoengine import QuerySet, Q

from src.repositories.base import find_by_id, parse_to_object_id


class PersonRepository(QuerySet):
    def find_by_id(self, object_id: any):
        return find_by_id(self, object_id)

    def find_all(self, filters: dict):
        order_by = "name"
        order_2_by = ""
        query = Q()
        if name := filters.get("name"):
            query &= Q(name={
                    "$regex": re.escape(name),
                    "$options": "i",
                }
            )

        if filters.get("active") is not None:
            query &= Q(active=filters.get("active"))

        if filters.get("council_member") is not None:
            query &= Q(council_member=filters.get("council_member"))
            order_by = "-graduation_current__order"
            order_2_by = "name"

        if filters.get("graduation_id") is not None:
            graduation_id = parse_to_object_id(filters.get("graduation_id"))
            query &= Q(graduation_current__graduation_id=graduation_id)

        return self.filter(query).order_by(order_by, order_2_by)

    def find_by_graduation_current(self, graduation_current_id: any):
        pipeline = [
            {
                "$match": {
                    "graduation_current.graduation_id": parse_to_object_id(graduation_current_id)
                }
            }
        ]

        return self.aggregate(pipeline)

    def exists_by_graduation_current(self, graduation_current_id: any):
        query = Q(graduation_current__graduation_id=graduation_current_id)

        return self.filter(query).count()
