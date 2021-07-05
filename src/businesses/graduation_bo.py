from ..models.graduation import Graduation
from ..utils.exceptions import NotFoundException


class GraduationBo:
    def save(self, new: dict) -> Graduation:
        """
        @param new: Contains the attributes of the object
        """
        graduation = Graduation(**new)
        graduation.save()
        return graduation

    def update(
            self,
            graduation_id: any,
            graduation: dict,
            ignore_value_none=False
    ) -> Graduation:
        """
        @param graduation: It is a dictionary
        @param graduation_id: It is the key of the object
        @param ignore_value_none: If TRUE it will ignore the values equals none
        """
        base_graduation = self.find_by_id(graduation_id)

        for k, v in graduation.items():
            if hasattr(base_graduation, k):
                if ignore_value_none:
                    if v is not None:
                        base_graduation[k] = v
                else:
                    base_graduation[k] = v

        base_graduation.save()
        self._update_person_graduation(base_graduation)

    def _update_person_graduation(self, graduation: Graduation):
        graduation.reload()
        person_bo = self._get_instance_person_bo()
        person_bo.update_person_graduation_current(graduation)

    def find_by_id(self, graduation_id: any) -> Graduation:
        """
        @param graduation_id: It is the key of the object
        """
        graduation = Graduation.objects.find_by_id(graduation_id)
        return graduation

    def find_all(self):
        return Graduation.objects.find_all()

    def delete(self, graduation_id: any) -> Graduation:
        """
        @param graduation_id: It is the key of the object
        """
        graduation = Graduation.objects.find_by_id(graduation_id)

        person_bo = self._get_instance_person_bo()
        if person_bo.exists_by_graduation_current(graduation.id):
            raise NotFoundException(message="There is(are) people registered with this graduation")

        graduation.delete()

    def _get_instance_person_bo(self):
        from .person_bo import PersonBo
        person_bo = PersonBo()
        return person_bo
