from functools import wraps

from flask_jwt_extended import JWTManager, get_jwt

from src.utils.enuns import Roles
from src.utils.exceptions import UnAuthorizedException


def init_jwt(_app):
    _app.config['JWT_SECRET_KEY'] = 'DontSeeThis'
    return JWTManager(_app)


def check_role(role):
    def decorator(func):
        def wrapper():
            current_user = get_jwt()
            roles = current_user.get("roles")

            admin = Roles.ADMINISTRATOR.value in roles

            if admin is False:
                permission = role in roles
                if permission is None or permission is False:
                    raise UnAuthorizedException(message="You do not have permission")
            return func()

        return wrapper

    return decorator

# def check_role(role: str):
#     def wrapper():
#         def decorator():
#             current_user = get_jwt()
#             permission = role in current_user.get("roles")
#             if permission is None or permission is False:
#                 raise UnAuthorizedException(message="You do not have permission")
#         return decorator
#
#     return wrapper
