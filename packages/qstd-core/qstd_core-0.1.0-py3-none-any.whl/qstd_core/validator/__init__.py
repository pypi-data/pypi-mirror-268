import typing

from pydantic import BaseModel

from .enums import TargetNameEnum
from .ValidatorABS import ValidatorABS
from .ValidatorPydantic import ValidatorPydantic
from .ValidatorMarshmallow import ValidatorMarshmallow
from .types import SchemaType
from ..marshmallow import Schema


def _validator_factory(schema: SchemaType, target: TargetNameEnum) -> ValidatorABS:
    if isinstance(schema, Schema):
        return ValidatorMarshmallow(schema, target)
    elif issubclass(schema, BaseModel):
        return ValidatorPydantic(schema, target)
    else:
        raise NotImplementedError()


def body(schema: typing.Type[SchemaType]):
    return _validator_factory(schema, TargetNameEnum.BODY)


def query(schema: typing.Type[SchemaType]):
    return _validator_factory(schema, TargetNameEnum.QUERY)


def params(schema: typing.Type[SchemaType]):
    return _validator_factory(schema, TargetNameEnum.PARAMS)


def validate(schema: typing.Type[SchemaType], payload: dict):
    return _validator_factory(schema, TargetNameEnum.UNION).validate(payload)
