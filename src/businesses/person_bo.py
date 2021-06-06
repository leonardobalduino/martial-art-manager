from werkzeug.datastructures import FileStorage

from .upload_bo import UploadBo
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

    def find_all(self, filters):
        return Person.objects.find_all(filters)

    def delete(self, person_id: any) -> Person:
        """
        @param person_id: It is the key of the object
        """
        person = Person.objects.find_by_id(person_id)
        person.delete()

    def update_profile_image(
            self,
            person_id: any,
            file: FileStorage
    ) -> str:
        person = Person.objects.find_by_id(person_id)

        upload_bo = UploadBo()
        image_base64 = upload_bo.get_image_base64(file)

        person.profile_image = image_base64
        person.save()

        return image_base64
