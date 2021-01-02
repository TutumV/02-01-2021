from flask import jsonify
from enum import Enum


class WebStatus:
    OK = 'ok'
    ERROR = 'error'


class ErrorCode(Enum):
    SUCCESS = 0
    VALIDATION_ERROR = 1
    UNEXPECTED_ERROR = 2
    CREDENTIALS_ERROR = 3
    NOT_FOUND = 4


class Response:
    def __call__(self, status: WebStatus, code: ErrorCode, data=None):
        self.status = status
        self.data = data if data else dict()
        self.code = code
        return jsonify(dict(status=self.status, data=self.data,
                            errors=dict(code=code.value, message=code.name)))


CustomResponse = Response()
