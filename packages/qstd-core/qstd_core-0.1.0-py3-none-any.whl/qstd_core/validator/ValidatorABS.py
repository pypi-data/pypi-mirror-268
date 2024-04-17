import typing
from abc import ABC
from functools import wraps

from sanic.request import Request

from .. import openapi
from .types import SchemaType
from .enums import TargetNameEnum
from .exceptions import SchemaValidationException


def format_error_message(message: str, field: str) -> str:
    return message.format(field_name=field)


class ValidatorABS(ABC):
    schema: typing.Type[SchemaType]
    target_name: TargetNameEnum

    def __init__(
        self,
        schema: typing.Type[SchemaType],
        target_name: TargetNameEnum = TargetNameEnum.BODY,
        pass_data: bool = True,
        docs: bool = True
    ):
        self.schema = schema
        self.target_name = target_name
        self.schema_fields = list(self.schema.__fields__.keys()) if target_name == TargetNameEnum.PARAMS else []
        self.pass_data = pass_data
        self.docs = docs

    def get_target(self, request: Request, kwargs):
        if self.target_name == TargetNameEnum.BODY:
            return request.json or dict()
        elif self.target_name == TargetNameEnum.QUERY:
            return {k: v[0] for k, v in request.args.items()}
        elif self.target_name == TargetNameEnum.PARAMS:
            params = dict()
            for name in self.schema_fields:
                params[name] = kwargs[name]
            return params

    def __call__(self, func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            request = args[0] if isinstance(args[0], Request) else args[1]
            target = self.get_target(request, kwargs)
            validated = self.validate(target)
            if self.pass_data:
                kwargs[self.target_name.value] = validated
            return await func(*args, **kwargs)
        openapi.errors(SchemaValidationException)(func)
        if self.docs:
            getattr(openapi, self.target_name.value)(self.schema)(func)
        return wrapper

    def validate(self, payload: dict):
        raise NotImplementedError()
