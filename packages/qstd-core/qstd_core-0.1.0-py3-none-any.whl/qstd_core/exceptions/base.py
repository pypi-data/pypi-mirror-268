
class ApplicationException(Exception):
    pass


class BaseApplicationException(ApplicationException):
    status_code: int

    message: str
    code: int
    error: str

    def __init__(self):
        self.error = type(self).__name__
        super().__init__()

    def to_dict(self):
        return dict(message=self.message, code=self.code, error=self.error)


class BadRequestException(BaseApplicationException):
    status_code = 400


class UnauthorizedException(BaseApplicationException):
    status_code = 401


class ForbiddenException(BaseApplicationException):
    status_code = 403


class NotFoundException(BaseApplicationException):
    status_code = 404


class TooManyAttemptsException(BaseApplicationException):
    status_code = 429


class InternalException(BaseApplicationException):
    status_code = 500
