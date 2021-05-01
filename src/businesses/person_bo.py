from ..models.person import Person


class PersonBo:
    def save(self, new: dict) -> Person:
        """
        @param new: Contains the attributes of the object
        """
        person = Person(**new)
        person.save()
        return person

    def update(
            self,
            person_id: any,
            person: dict,
            ignore_value_none=False
    ) -> Person:
        """
        @param person: It is a dictionary
        @param person_id: It is the key of the object
        @param ignore_value_none: If TRUE it will ignore the values equals none
        """
        base_person = self.find_by_id(person_id)

        for k, v in person.items():
            if ignore_value_none:
                if v is not None:
                    base_person[k] = v
            else:
                base_person[k] = v

        base_person.save()

    def find_by_id(self, person_id: any) -> Person:
        """
        @param person_id: It is the key of the object
        """
        person = Person.objects.find_by_id(person_id)
        return person

    def find_all(self):
        return Person.objects.find_all()

    def delete(self, person_id: any) -> Person:
        """
        @param person_id: It is the key of the object
        """
        person = Person.objects.find_by_id(person_id)
        person.delete()
