from marshmallow import Schema as DefaultSchema

from . import validate, Integer, List, fields


class Schema(DefaultSchema):
    @classmethod
    def pagination(cls):
        class PaginationResponse(Schema):
            total = Integer(required=True, validate=validate.Range(min=0))
            page_count = Integer(required=True, validate=validate.Range(min=0))
            data = List(fields.Nested(cls()), required=True)
        return PaginationResponse()



