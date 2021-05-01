from flask import jsonify

from ..models.user import User
from ..utils.cryptography import encrypt, decrypt
from ..utils.enuns import Roles
from ..utils.exceptions import UnAuthorizedException
from flask_jwt_extended import create_access_token

from ..utils.settings import get_admin_user


class UserBo:
    def save(self, new: dict) -> User:
        """
        @param new: Contains the attributes of the object
        """
        user = User(**new)
        user.active = False
        user.password = encrypt(user.password)
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

    def login(self, auth: dict, ) -> str:
        """
        @param auth: It is the dict that
         contains login and password of the object
        """
        login = auth.get("login")
        password = auth.get("password")
        user: User = User.objects.find_by_login(login)

        if user is None:
            raise UnAuthorizedException()

        dec_password = decrypt(user.password)
        if dec_password != password or user.active is False or user.active is None:
            raise UnAuthorizedException()

        additional_claims = {
            "id": str(user.id),
            "roles": user.roles,
            "name": user.name,
            "email": user.email,
        }

        access_token = create_access_token(
            identity=str(user.id),
            additional_claims=additional_claims,
        )

        return jsonify(access_token=access_token)

    def create_user_admin(self):
        try:
            admin = get_admin_user()

            user_admin = User.objects.find_by_login(admin.get("login"))
            if user_admin:
                return

            user = User()
            user.name = admin.get("name")
            user.login = admin.get("login")
            user.password = encrypt(admin.get("password"))
            user.email = admin.get("email")
            user.active = True
            user.roles = [Roles.ADMINISTRATOR.value]
            user.save()
            print("Created user admin")
        except Exception:
            pass
