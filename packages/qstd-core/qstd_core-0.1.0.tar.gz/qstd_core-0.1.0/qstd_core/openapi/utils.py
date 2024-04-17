import typing
import enum

from pydantic import BaseModel

from ..marshmallow import Schema as MarshmallowSchema, List as MarshmallowList
from .spec import OpenapiRoute, OpenapiRouteParameter, OpenapiRouteParameterEnum, OpenapiRouteContent
from ..exceptions.localization import LocalizedException
from ..localization import State
from .mapper_marsmallow import schema_to_openapi as marshmallow_mapper
from .mapper_pydantic import schema_to_openapi as pydantic_mapper

openapi = dict(
    paths={},
    info=dict(title='', version=''),
    openapi="3.0.3",
    tags=[],
    servers=[]
)
handlers = dict()
override_handlers = dict()

type_to_type = {
    'str': lambda: {'type': 'string'},
    'int': lambda: {'type': 'integer'},
    'float': lambda: {'type': 'number'},
    'bool': lambda: {'type': 'boolean'},
    'dict': lambda: {'type': 'dictionary'},
    'list': lambda: {'type': 'array', 'items': {}},
    'enum': lambda: {'type': 'string', 'enum': []}
}


def get_openapi_from_handler(route_handler) -> OpenapiRoute:
    spec: OpenapiRoute = OpenapiRoute()
    while True:
        if route_handler in handlers:
            spec.merge(handlers[route_handler])
        if hasattr(route_handler, '__wrapped__'):
            route_handler = route_handler.__wrapped__
        else:
            return spec


def extract_methods_url(_, route):
    url = ''
    for part in route.parts:
        if part == '':
            continue
        if part.startswith('<'):
            url += '/{' + part.split(':')[0].replace('>', '').replace('<', '') + '}'
        else:
            url += '/' + part
    methods = [*route.methods]
    return url, methods


def extract_handler_view(route, method):
    if hasattr(route[0], 'view_class'):
        view_class = route[0].view_class
        if hasattr(view_class, method):
            return getattr(view_class, method)
    return None


def extract_route_handler(route, method, url):
    handler = route.handler
    if hasattr(handler, 'view_class'):
        view_class = handler.view_class
        if hasattr(view_class, method):
            handler = getattr(view_class, method)
    route_handlers = list(filter(
        lambda h: h is not None,
        [
            override_handlers.get(method + url, None),
            handler
        ]
    ))
    return route_handlers[0]


def assign_doc(doc, openapi_route):
    parts = doc.split('\n')
    openapi_route.summary = ''
    for i, part in enumerate(parts):
        if part != '':
            openapi_route.summary = part
            if i != len(parts) - 1:
                openapi_route.description = '\n'.join(map(lambda s: s.strip(), parts[i + 1::]))
            break


def collect(app):
    tags = set()
    for bg_name in app.blueprints.keys():
        bg = app.blueprints[bg_name]
        for route in bg.routes:
            url, methods = extract_methods_url(bg, route)
            for method in methods:
                method = method.lower()
                if method == 'options':
                    continue
                handler = extract_route_handler(route, method, url)
                openapi_route = get_openapi_from_handler(handler) or OpenapiRoute()
                if openapi_route.exclude is True:
                    continue
                openapi_route.resolve_tags(url, bg_name)
                tags = tags.union(openapi_route.tags)
                assign_doc(handler.__doc__ or '', openapi_route)
                if len(openapi_route.responses) == 0:
                    openapi_route.add_response_content(200, OpenapiRouteContent(description='Ok'))
                if url not in openapi['paths']:
                    openapi['paths'][url] = {method: openapi_route.to_dict()}
                else:
                    openapi['paths'][url][method] = openapi_route.to_dict()
    openapi['tags'] = [dict(name=name) for name in tags]


def upsert(func) -> OpenapiRoute:
    if func not in handlers:
        handlers[func] = OpenapiRoute()
    return handlers[func]


def object_schema_to_parameters(
    schema: dict,
    location: OpenapiRouteParameterEnum = OpenapiRouteParameterEnum.query
) -> typing.List[OpenapiRouteParameter]:
    parameters = []
    required = set(schema.get('required', []))

    for prop in schema['properties'].items():
        name = prop[0]
        item = prop[1]
        parameters.append(
            OpenapiRouteParameter(
                location,
                name,
                name in required,
                item
            )
        )
    return parameters


def exception_schema_to_response(exception):
    if not issubclass(exception, LocalizedException):
        message = {
            'type': 'string',
            'default': exception.message
        }
    else:
        message = {
            'description': exception.localization_key.name,
            'oneOf': []
        }
        for locale, localized_message in State.get_localization_messages(exception.localization_key).items():
            message['oneOf'].append(
                {
                    'title': locale,
                    'type': 'string',
                    'description': localized_message
                }
            )
    schema = {
        'title': exception.__name__,
        'type': 'object',
        'properties': {
            'code': {
                'type': 'integer',
                'default': exception.code
            },
            'error': {
                'type': 'string',
                'default': exception.__name__
            },
            'message': message
        },
        'required': ['message', 'code', 'error']
    }
    annotations = exception.__dict__.get('__annotations__')
    if annotations:
        for field, annotation in annotations.items():
            is_required = True
            if hasattr(annotation, '__origin__'):
                if annotation.__origin__ is typing.Union:
                    field_type = annotation.__args__[0].__name__
                    is_required = False
                else:
                    field_type = annotation.__origin__.__name__
            elif issubclass(annotation, enum.Enum):
                field_type = 'enum'
            else:
                field_type = annotation.__name__
            schema['properties'][field] = type_to_type.get(field_type, lambda: {'type': 'object'})()
            if hasattr(exception, field):
                schema['properties'][field]['default'] = getattr(exception, field)
            if field_type == 'enum':
                schema['properties'][field]['enum'] = [member.value for member in annotation]
            if is_required:
                schema['required'].append(field)
    return schema


def path_schema_from_raw_parameters(name, path_type, description=None, enum_cls=None):
    schema = {
        'type': path_type
    }
    if enum_cls is not None:
        if not isinstance(enum_cls, list):
            enum_cls = list(map(lambda c: c.value, enum_cls))
        schema['enum'] = enum_cls
    return OpenapiRouteParameter(
        OpenapiRouteParameterEnum.path,
        name,
        True,
        schema,
        description
    )


def schema_mapper_factory(schema: typing.Union[MarshmallowSchema, typing.Type[BaseModel]]):
    if isinstance(schema, MarshmallowSchema) or isinstance(schema, MarshmallowList):
        return marshmallow_mapper(schema)
    elif issubclass(schema, BaseModel):
        return pydantic_mapper(schema)
    else:
        return schema
