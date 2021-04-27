from ..domains.graduation import Graduation


class GraduationBo:
    def save(self, new: dict) -> Graduation:
        """
        @param new: Contains the attributes of the object
        """
        graduation = Graduation(**new)
        graduation.save()
        return graduation
