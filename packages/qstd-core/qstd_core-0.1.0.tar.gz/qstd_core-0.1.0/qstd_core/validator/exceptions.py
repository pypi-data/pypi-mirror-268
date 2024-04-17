import typing

from ..exceptions import BadRequestException, BaseApplicationException
from .enums import TargetNameEnum


class SchemaValidationException(BadRequestException):
    class SchemaValidationItemException(BaseApplicationException):
        message: str
        code: int = 2
        location: typing.List[str]

        def __init__(self, message: str, location: typing.Any):
            super().__init__()
            self.message = message
            self.location = location

        def to_dict(self):
            return dict(**super().to_dict(), location=self.location)

    target: str
    code: int = 1
    message = 'Validation errors'
    errors: typing.List[SchemaValidationItemException]

    def __init__(self, target: TargetNameEnum, errors):
        super().__init__()
        self.errors = errors
        self.target = str(target.value)

    def to_dict(self):
        return dict(
            **super().to_dict(),
            target=self.target,
            errors=[error.to_dict() for error in self.errors]
        )


class NotRequestProvidedException(BadRequestException):
    code = 3
    target: str

    def __init__(self, target: TargetNameEnum):
        super().__init__()
        self.message = f'No request {target.name} provided'
        self.target = str(target.value)

    def to_dict(self):
        return dict(
            **super().to_dict(),
            target=self.target
        )

