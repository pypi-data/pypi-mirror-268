import copy
import typing

import jsonref

from pydantic import BaseModel


def schema_to_openapi(schema: typing.Union[typing.Type[BaseModel], dict]) -> dict:
    return copy.deepcopy(jsonref.loads(schema.schema_json(), jsonschema=True))
