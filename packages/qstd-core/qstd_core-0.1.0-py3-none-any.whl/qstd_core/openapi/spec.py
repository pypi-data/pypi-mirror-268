from __future__ import annotations

import enum
import typing


class OpenapiRouteParameterEnum(enum.Enum):
    query = 'query',
    path = 'path'


class OpenapiRouteContentSchema:
    schema: dict

    def __init__(self, schema: dict = None):
        self.schema = schema

    def to_dict(self):
        result = dict(schema=self.schema)
        return result


class OpenapiRouteContent:
    description: str
    content: typing.Optional[typing.Dict[str, OpenapiRouteContentSchema]]

    def __init__(self, content: typing.Dict[str, OpenapiRouteContentSchema] = None, description: str = None):
        self.description = description
        self.content = content

    def add_schema(self, content_type: str, schema: dict) -> OpenapiRouteContent:
        if content_type not in self.content:
            self.content[content_type] = OpenapiRouteContentSchema(schema)
        elif self.content[content_type].schema == schema:
            return self
        else:
            current_content = self.content[content_type]
            if 'oneOf' in current_content.schema:
                if 'oneOf' in schema:
                    for child_schema in schema['oneOf']:
                        self.content[content_type].schema['oneOf'].append(child_schema)
                else:
                    self.content[content_type].schema['oneOf'].append(schema)
            else:
                schemas = []
                if 'oneOf' in schema:
                    schemas = schema['oneOf']
                else:
                    schemas.append(schema)
                self.content[content_type] = OpenapiRouteContentSchema(
                    {'oneOf': [*schemas, current_content.schema]}
                )
        return self

    def merge(self, content: OpenapiRouteContent) -> OpenapiRouteContent:
        if content is None:
            return self
        if content.content is not None:
            for content_type in typing.cast(typing.Dict, content.content):
                target_content = typing.cast(typing.Dict, content.content)[content_type]
                self.add_schema(content_type, target_content.schema)
        if self.description is None and content.description is not None:
            self.description = content.description
        return self

    def to_dict(self):
        content = {}
        if self.content is not None:
            for key in self.content.keys():
                content[key] = self.content[key].to_dict()
        result = dict(content=content)
        if self.description is not None:
            result['description'] = self.description
        return result


class OpenapiRouteParameter:
    location: OpenapiRouteParameterEnum
    name: str
    required: bool
    schema: typing.Dict
    description: str

    def __init__(
            self,
            location: OpenapiRouteParameterEnum,
            name: str,
            required: bool,
            schema: dict,
            description: str = None
    ):
        self.location = location
        self.name = name
        self.required = required
        self.schema = schema
        self.description = description

    def to_dict(self):
        result = {
            'in': self.location.name,
            'name': self.name,
            'required': self.required,
            'schema': self.schema
        }
        if self.description is not None:
            result['description'] = self.description
        return result


class OpenapiRouteTagOptions:
    name: str
    includes: str
    excludes: str

    def __init__(
            self,
            name: str,
            includes: str = None,
            excludes: str = None
    ):
        self.name = name
        self.includes = includes
        self.excludes = excludes


class OpenapiRoute:
    responses: typing.Dict[int, OpenapiRouteContent]
    summary: str or None
    description: str or None
    tags: typing.Set[str]
    requestBody: OpenapiRouteContent or None
    exclude: bool
    deprecated: bool
    parameters: typing.Set[OpenapiRouteParameter]
    tags_options: typing.List[OpenapiRouteTagOptions]

    def __init__(self):
        self.responses = {}
        self.summary = ''
        self.description = None
        self.requestBody = None
        self.exclude = False
        self.deprecated = False
        self.tags = set()
        self.parameters = set()
        self.tags_options = []

    def add_parameters(
            self,
            parameters: typing.List[OpenapiRouteParameter]
    ) -> OpenapiRoute:
        self.parameters = self.parameters.union(parameters)
        return self

    def add_tag_fabric(
            self,
            name: str,
            includes: str,
            excludes: str
    ) -> OpenapiRoute:
        if includes is not None or excludes is not None:
            return self.add_tag_options(name, includes, excludes)
        else:
            return self.add_tag(name)

    def add_tag(
            self,
            name: str
    ):
        self.tags.add(name)
        return self

    def add_tag_options(
            self,
            name: str,
            includes: str,
            excludes: str
    ) -> OpenapiRoute:
        self.tags_options.append(OpenapiRouteTagOptions(name, includes, excludes))
        return self

    def add_response_schema(
            self,
            status: int,
            schema: dict,
            content_type: str,
            description: str = None
    ):
        return self.add_response_content(
            status,
            OpenapiRouteContent(
                {content_type: OpenapiRouteContentSchema(schema)},
                description
            )
        )

    def add_response_content(
            self,
            status: int,
            content: OpenapiRouteContent
    ) -> OpenapiRoute:
        if status not in self.responses:
            self.responses[status] = content
        else:
            self.responses[status].merge(content)
        return self

    def add_body_schema(
            self,
            content_type: str,
            schema: dict
    ) -> OpenapiRoute:
        if self.requestBody is None:
            self.requestBody = OpenapiRouteContent(
                {content_type: OpenapiRouteContentSchema(schema)}
            )
        else:
            self.requestBody.add_schema(content_type, schema)
        return self

    def merge(
            self,
            route: OpenapiRoute
    ) -> OpenapiRoute:
        if route.summary:
            self.summary = route.summary
        if route.description:
            self.description = route.description
        self.parameters = self.parameters.union(route.parameters)
        self.tags = self.tags.union(route.tags)
        self.tags_options = self.tags_options + route.tags_options
        if self.requestBody is not None:
            self.requestBody.merge(route.requestBody)
        else:
            self.requestBody = route.requestBody
        if route.exclude is not False:
            self.exclude = route.exclude
        if route.deprecated is not False:
            self.deprecated = route.deprecated
        for code, content in route.responses.items():
            if code not in self.responses:
                self.responses[code] = content
            else:
                self.responses[code].merge(content)
        return self

    def resolve_tags(
            self,
            url: str,
            default_tag: str
    ) -> OpenapiRoute:
        if len(self.tags) == 0 and len(self.tags_options) == 0:
            self.tags.add(default_tag)
        elif len(self.tags_options) != 0:
            for options in self.tags_options:
                if options.excludes is not None and options.includes is not None:
                    if options.excludes not in url and options.includes in url:
                        self.tags.add(options.name)
                else:
                    if options.excludes is not None:
                        if options.excludes not in url:
                            self.tags.add(options.name)
                    elif options.includes is not None:
                        if options.includes in url:
                            self.tags.add(options.name)
        return self

    def to_dict(self):
        responses = {}
        for status in self.responses.keys():
            responses[status] = self.responses[status].to_dict()
        result = dict(
            summary=self.summary,
            tags=list(self.tags),
            responses=responses
        )
        if self.deprecated is True:
            result['deprecated'] = True
        if len(self.parameters) != 0:
            result['parameters'] = [parameter.to_dict() for parameter in self.parameters]
        if self.requestBody is not None:
            result['requestBody'] = self.requestBody.to_dict()
        if self.description is not None:
            result['description'] = self.description
        return result
