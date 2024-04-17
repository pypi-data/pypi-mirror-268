import typing

from sanic.request import Request

from .base import ApplicationException
from ..localization import localize
from ..sanic.request import get_languages


class LocalizedException(ApplicationException):
    status_code: int

    localization_key = None
    localization_params: dict = None
    message: str = None
    code: int = 0
    error: str

    def __init__(self, **params):
        super().__init__()
        if not self.localization_params:
            self.localization_params = params
        self.error = type(self).__name__

    def to_dict(self, request: typing.Optional[Request] = None):
        return dict(
            message=localize(
                self.localization_key,
                get_languages(request) if request is not None else None,
                self.localization_params
            ),
            code=self.code,
            error=self.error
        )


class BadRequestLocalizeException(LocalizedException):
    status_code = 400


class UnauthorizedLocalizeException(LocalizedException):
    status_code = 401


class ForbiddenLocalizeException(LocalizedException):
    status_code = 403


class NotFoundLocalizeException(LocalizedException):
    status_code = 404


class InternalServerLocalizeException(LocalizedException):
    status_code = 500


class TooManyRequestsLocalizeException(LocalizedException):
    status_code = 429
