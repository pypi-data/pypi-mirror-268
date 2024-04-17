import typing
from enum import Enum

from marshmallow import fields, Schema, validate, utils


types = [fields.String, fields.Integer, fields.Number, fields.Boolean, fields.DateTime, fields.Date, fields.Dict]
type_to_type = {
    fields.String: lambda: {'type': 'string'},
    fields.Integer: lambda: {'type': 'integer'},
    fields.Number: lambda: {'type': 'number'},
    fields.Boolean: lambda: {'type': 'boolean'},
    fields.DateTime: lambda: {'type': 'string', "format": "date-time"},
    fields.Date: lambda: {'type': 'string', "format": "date"},
    fields.Dict: lambda: {'type': 'dictionary'}
}


def _get_parent_type(actual):
    for expected in types:
        if isinstance(actual, expected):
            return expected
    return None


def _get_attr(schema, attr: str):
    if hasattr(schema, attr):
        return getattr(schema, attr)
    else:
        return None


def schema_to_openapi(schema: typing.Any, parent_schema: dict = None):
    if isinstance(schema, Schema):
        openapi: dict = {
            'title': type(schema).__name__,
            'type': 'object',
            'properties': {},
            'required': []
        }
        for name in schema.fields:
            openapi_name = schema.fields[name].data_key or name
            openapi['properties'][openapi_name] = schema_to_openapi(schema.fields[name], openapi)
        if len(openapi['required']) == 0:
            del openapi['required']
        if schema.many is True:
            openapi = {
                'type': 'array',
                'items': openapi
            }
    elif hasattr(schema, 'meta_one_of') and schema.meta_one_of is not None:
        openapi = {
            'oneOf': [schema_to_openapi(one_of_schema) for one_of_schema in schema.meta_one_of]
        }
        if schema.required is True:
            parent_schema['required'].append(schema.name)
    elif isinstance(schema, fields.Nested):
        if schema.required is True:
            parent_schema['required'].append(schema.name)
        openapi = schema_to_openapi(schema.schema, parent_schema)
    elif isinstance(schema, fields.List):
        openapi = {
            'type': 'array',
            'items': {}
        }
        if schema.required is True:
            parent_schema['required'].append(schema.name)
        if hasattr(schema, 'get_validation'):
            validation = schema.get_validation()
            for v in validation:
                if isinstance(v, validate.Length):
                    if v.min is not None:
                        openapi['minItems'] = v.min
                    if v.max is not None:
                        openapi['maxItems'] = v.max
        openapi['items'] = schema_to_openapi(schema.inner, openapi['items'])
    elif isinstance(schema, fields.Nested):
        if _get_attr(schema, 'required') is True:
            parent_schema['required'].append(schema.name)
        return schema_to_openapi(schema.schema, parent_schema)
    else:
        parent_type = _get_parent_type(schema)
        if parent_type is not None:
            openapi = type_to_type[parent_type]()
            if schema.allow_none is True:
                openapi['nullable'] = True
            if schema.missing != utils.missing:
                openapi['default'] = schema.missing.name if isinstance(schema.missing, Enum) else schema.missing
            elif schema.dump_default != utils.missing:
                openapi['default'] = schema.dump_default
            elif schema.default != utils.missing:
                openapi['default'] = schema.default
            deprecated = _get_attr(schema, 'deprecated')
            if deprecated is not None and deprecated is True:
                openapi['deprecated'] = True
            description = _get_attr(schema, 'description')
            if description is not None:
                openapi['description'] = description
            if hasattr(schema, 'get_validation'):
                validation = schema.get_validation()
            else:
                validation = None
            enum: typing.Optional[typing.Union[list, typing.Type[Enum]]] = _get_attr(schema, 'enum')
            if enum is not None:
                if not isinstance(enum, list):
                    enum = list(map(lambda c: c.value, enum))
                openapi['enum'] = enum
            if _get_attr(schema, 'required') is True:
                parent_schema['required'].append(schema.name)
            if validation is not None:
                for v in validation:
                    if isinstance(v, validate.Regexp):
                        openapi['pattern'] = v.regex.pattern
                    elif isinstance(v, validate.Length):
                        if v.min is not None:
                            openapi['minLength'] = v.min
                        if v.max is not None:
                            openapi['maxLength'] = v.max
                    elif isinstance(v, validate.Range):
                        if v.min is not None:
                            openapi['minimum'] = v.min
                        if v.max is not None:
                            openapi['maximum'] = v.max
                    elif isinstance(v, validate.OneOf):
                        openapi['enum'] = v.choices
        else:
            print('Warn! Not supported marshmallow schema item', schema)
            openapi = {}
    return openapi
