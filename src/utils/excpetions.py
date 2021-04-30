from werkzeug.exceptions import HTTPException


class SystemException(HTTPException):
    def __init__(
        self,
        code: any,
        message: str = None,
        errors: any = None,
        http_code: int = None,
    ):
        self.error_code = code
        self.message = message
        self.errors = errors
        self.code = http_code if http_code is not None else 500


class NotFoundException(SystemException):
    def __init__(
        self, message: str = None, errors: any = None,
    ):
        super(NotFoundException, self).__init__(
            code=404, message=message, errors=errors, http_code=404
        )


class UnAuthorizedException(SystemException):
    def __init__(
        self, message: str = "Unauthorized", errors: any = None,
    ):
        super(UnAuthorizedException, self).__init__(
            code=401, message=message, errors=errors, http_code=401
        )
