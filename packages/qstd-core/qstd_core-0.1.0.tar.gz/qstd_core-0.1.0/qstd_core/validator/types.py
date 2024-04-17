import typing

from pydantic import BaseModel

from ..marshmallow import Schema

SchemaType = typing.Union[Schema, typing.Type[BaseModel]]
