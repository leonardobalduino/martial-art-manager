from bson import ObjectId
from werkzeug.datastructures import FileStorage

from .graduation_bo import GraduationBo
from .upload_bo import UploadBo
from ..models.graduation import Graduation
from ..models.person import Person


class PersonBo:
    def save(self, new: dict) -> Person:
        """
        @param new: Contains the attributes of the object
        """
        self._validate_graduation(new)
        person = Person(**new)
        person.save()
        return person

    def update(
            self,
            person_id: any,
            person: dict,
            ignore_value_none=True
    ) -> Person:
        """
        @param person: It is a dictionary
        @param person_id: It is the key of the object
        @param ignore_value_none: If TRUE it will ignore the values equals none
        """
        base_person = self.find_by_id(person_id)
        self._validate_graduation(person)
        for k, v in person.items():
            if hasattr(base_person, k):
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

    def update_person_graduation_current(self, graduation_current: Graduation):
        persons = self.find_by_graduation_current(graduation_current.id)

        dict_graduation = self._parse_gradution_to_dict(graduation_current)
        for p in persons:
            p["id"] = ObjectId(p["_id"])
            del p["_id"]

            person = Person(**p)
            person.graduation_current = dict_graduation.copy()
            person.save()

    def find_all(self, filters):
        return Person.objects.find_all(filters)

    def find_by_graduation_current(self, graduation_current_id: any):
        return Person.objects.find_by_graduation_current(graduation_current_id)

    def exists_by_graduation_current(self, graduation_current_id: any) -> bool:
        return Person.objects.exists_by_graduation_current(graduation_current_id) > 0

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

    def _parse_gradution_to_dict(self, graduation: Graduation):
        graduation_dict = {
            "name": graduation.name,
            "graduation_id": graduation.id,
            "description": graduation.description,
            "color": graduation.color,
        }

        return graduation_dict

    def _validate_graduation(self, person: dict):
        if "graduation_current_id" in person:
            graduation_bo = GraduationBo()
            graduation_id = person["graduation_current_id"]
            graduation = graduation_bo.find_by_id(graduation_id)

            del person["graduation_current_id"]

            person["graduation_current"] = self._parse_gradution_to_dict(graduation)
