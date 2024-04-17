import typing

from .spec import OpenapiRouteContent, OpenapiRouteParameterEnum
from .utils import (
    upsert,
    override_handlers,
    exception_schema_to_response,
    schema_mapper_factory,
    object_schema_to_parameters,
    path_schema_from_raw_parameters
)
from .enum import STATUS_TO_DESCRIPTION
from ..validator.types import SchemaType


def response_file(content_type='*/*', status=200, description=None):
    if description is None:
        description = STATUS_TO_DESCRIPTION.get(status, None)

    def inner(func):
        upsert(func).add_response_schema(
            status,
            {
                'description': 'File',
                'type': 'string',
                'format': 'binary'
            },
            content_type,
            description
        )
        return func
    return inner


def body_form_data_file(name='file', description: str = None, required=True):
    schema = {
        'type': 'object',
        'properties': {
            name: {
                'description': 'File',
                'type': 'string',
                'format': 'binary'
            }
        },
        'required': [name] if required else []
    }
    if description is not None:
        schema['description'] = description

    def inner(func):
        upsert(func).add_body_schema(
            'multipart/form-data',
            schema
        )
        return func
    return inner


def body_form_data_files(name='files', required=True, max_items=1):
    schema = {
        'type': 'object',
        'properties': {
            name: {
                'type': 'array',
                'items': {
                    'description': 'File',
                    'type': 'string',
                    'format': 'binary'
                }
            }
        },
        'required': [name] if required else []
    }
    if max_items is not None:
        schema['properties'][name]['maxItems'] = max_items

    def inner(func):
        upsert(func).add_body_schema(
            'multipart/form-data',
            schema
        )
        return func
    return inner


def body_binary(content_type='*/*'):
    def inner(func):
        upsert(func).add_body_schema(
            content_type,
            {
                'description': 'File',
                'type': 'string',
                'format': 'binary'
            }
        )
        return func
    return inner


def tag(tag_name: str, includes=None, excludes=None):
    def inner(func):
        upsert(func).add_tag_fabric(tag_name, includes, excludes)
        return func
    return inner


def exclude():
    def inner(func):
        upsert(func).exclude = True
        return func
    return inner


def handler(method: str, url: str):
    def inner(func):
        override_handlers[method + url] = func
        return func
    return inner


def no_content(status=204):
    def inner(func):
        upsert(func).add_response_content(
            status,
            OpenapiRouteContent(description='No content')
        )
        return func
    return inner


def deprecated():
    def inner(func):
        upsert(func).deprecated = True
        return func
    return inner


def errors(*exceptions, content_type='application/json'):
    def inner(func):
        spec = upsert(func)
        for exception in exceptions:
            spec.add_response_schema(
                status=exception.status_code,
                schema=exception_schema_to_response(exception=exception),
                content_type=content_type,
                description=STATUS_TO_DESCRIPTION.get(exception.status_code, None)
            )
        return func
    return inner


def body(schema: SchemaType, content_type='application/json'):
    def inner(func):
        upsert(func).add_body_schema(content_type, schema_mapper_factory(schema))
        return func
    return inner


def body_one_of(
    schemas: typing.List[SchemaType],
    content_type='application/json'
):
    def inner(func):
        spec = upsert(func)
        for schema in schemas:
            spec.add_body_schema(content_type, schema_mapper_factory(schema))
        return func
    return inner


def query(schema: SchemaType):
    def inner(func):
        upsert(func).add_parameters(object_schema_to_parameters(schema_mapper_factory(schema)))
        return func
    return inner


def response(
    schema: SchemaType,
    status=200,
    content_type='application/json'
):
    def inner(func):
        upsert(func).add_response_schema(
            status,
            schema_mapper_factory(schema),
            content_type,
            STATUS_TO_DESCRIPTION.get(status, None)
        )
        return func
    return inner


def responses(
    schemas: typing.List[SchemaType],
    status=200,
    content_type='application/json'
):
    def inner(func):
        spec = upsert(func)
        for schema in schemas:
            spec.add_response_schema(
                status,
                schema_mapper_factory(schema),
                content_type,
                STATUS_TO_DESCRIPTION.get(status, None)
            )
        return func
    return inner


def path(
    schema: typing.Union[SchemaType, str],
    path_type: str = None,
    description: str = '',
    enum=None
):
    if isinstance(schema, str):
        parameters = [path_schema_from_raw_parameters(schema, path_type, description, enum)]
    else:
        parameters = object_schema_to_parameters(schema_mapper_factory(schema), OpenapiRouteParameterEnum.path)

    def inner(func):
        upsert(func).add_parameters(parameters)
        return func
    return inner
