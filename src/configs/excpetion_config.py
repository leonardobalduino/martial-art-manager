from dataclasses import asdict, dataclass

import mongoengine
from flask import jsonify, Flask
from werkzeug.exceptions import UnprocessableEntity, HTTPException


@dataclass
class Error:
    message: str = None
    code: int = None
    status: str = None
    errors: any = None

    def as_dict(self):
        return asdict(self)


def _serialize_error(
    http_code: int,
    code: int,
    message: str,
    errors: any = None,
) -> tuple:
    error_message = Error()
    error_message.code = code
    error_message.message = message
    error_message.errors = errors
    return jsonify(error_message), http_code


def _get_attr_exception(e: BaseException, attr: str, default: any) -> any:
    value = getattr(e, attr, repr(e))
    value = value if value is not None else default
    return value


def error_handling_config(app: Flask):
    @app.errorhandler(mongoengine.NotUniqueError)
    def handle_not_unique_error(e):
        return _serialize_error(
            400, 400, message=getattr(e, 'message', repr(e)), errors=str(e),
        )

    @app.errorhandler(UnprocessableEntity)
    def handle_un_processable_entity(e):
        return _serialize_error(
            422, 422, message=getattr(e, 'message', repr(e)), errors=str(e),
        )

    @app.errorhandler(HTTPException)
    def handle_application_http_error(e):
        code = _get_attr_exception(e, "code", 500)
        error_code = _get_attr_exception(e, "error_code", 500)
        message = _get_attr_exception(e, "message", getattr(e, "description", repr(e)))
        errors = _get_attr_exception(e, "errors", str(e))

        return _serialize_error(
            error_code, code, message=message, errors=errors,
        )

    @app.errorhandler(Exception)
    def handle_unknown_exception(e):
        return _serialize_error(
            500, 500, message=getattr(e, "message", repr(e)), errors=str(e),
        )
