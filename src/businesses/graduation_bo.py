from ..domains.graduation import Graduation


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
            if ignore_value_none:
                if v is not None:
                    base_graduation[k] = v
            else:
                base_graduation[k] = v

        base_graduation.save()

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
        graduation.delete()
