from ..models.user import User


class UserBo:
    def save(self, new: dict) -> User:
        """
        @param new: Contains the attributes of the object
        """
        user = User(**new)
        user.active = False
        user.save()
        return user

    def update(
            self,
            user_id: any,
            user: dict,
            ignore_value_none=False
    ) -> User:
        """
        @param user: It is a dictionary
        @param user_id: It is the key of the object
        @param ignore_value_none: If TRUE it will ignore the values equals none
        """
        base_user = self.find_by_id(user_id)

        for k, v in user.items():
            if ignore_value_none:
                if v is not None:
                    base_user[k] = v
            else:
                base_user[k] = v

        base_user.save()

    def find_by_id(self, user_id: any) -> User:
        """
        @param user_id: It is the key of the object
        """
        graduation = User.objects.find_by_id(user_id)
        return graduation

    def find_all(self):
        return User.objects.find_all()

    def delete(self, user_id: any) -> User:
        """
        @param user_id: It is the key of the object
        """
        user = User.objects.find_by_id(user_id)
        user.delete()
