from typing import AnyStr

from marshmallow import fields, ValidationError
from marshmallow_enum import EnumField


class CustomField(fields.Field):
    field_name = None
    deprecated = None

    default_error_messages = {
        "required": "{field_name} is required field.",
        "null": "{field_name} can not be empty.",
        "validator_failed": "Invalid value.",
    }

    @property
    def name(self):
        return self.field_name

    @name.setter
    def name(self, value):
        self.field_name = self.data_key or value
        for validation in self.get_validation():
            validation.field_name = self.field_name

    def __init__(
            self,
            transform=None,
            transform_after=None,
            description: str = None,
            meta_one_of=None,
            deprecated=None,
            cls_or_instance=None,
            **kwargs
    ):
        if cls_or_instance:
            super().__init__(cls_or_instance, **kwargs)
        else:
            super().__init__(**kwargs)
        self._transform = transform
        self._transform_after = transform_after
        self.description = description
        self.meta_one_of = meta_one_of
        self.deprecated = deprecated

    def get_validation(self):
        if self.validate is None:
            return []
        elif type(self.validate) is list:
            return self.validate
        else:
            return [self.validate]

    def transform(self, value):
        if self._transform is not None:
            if isinstance(self._transform, list):
                for f in self._transform:
                    value = f(value)
            else:
                value = self._transform(value)
        return value

    def transform_after(self, value):
        if self._transform_after is not None:
            if isinstance(self._transform_after, list):
                for f in self._transform_after:
                    value = f(value)
            else:
                value = self._transform_after(value)
        return value

    def make_error(self, key: str, **kwargs) -> ValidationError:
        return super().make_error(key, field_name=self.field_name, **kwargs)

    def _deserialize(self, value, attr, data, **kwargs) -> AnyStr:
        return self.transform_after(super()._deserialize(self.transform(value), attr, data, **kwargs))

    def _serialize(self, value, attr, obj, **kwargs) -> AnyStr:
        return self.transform_after(super().serialize(self.transform(value), attr, obj, **kwargs))


class String(CustomField, fields.String):
    default_error_messages = {
        "invalid": "{field_name} must be string.",
        "invalid_utf8": "{field_name} must be utf-8 string."
    }

    def __init__(self, **kwargs):
        fields.String.__init__(self, **kwargs)
        CustomField.__init__(self, **kwargs)


class Date(CustomField, fields.Date):
    default_error_messages = {
        "invalid": "Invalid date.",
        "format": '"{input}" cannot be formatted as a date.'
    }

    def __init__(self, **kwargs):
        fields.Date.__init__(self, **kwargs)
        CustomField.__init__(self, **kwargs)


class Integer(CustomField, fields.Integer):
    default_error_messages = {"invalid": "{field_name} must be integer."}

    def __init__(self, **kwargs):
        fields.Integer.__init__(self, **kwargs)
        CustomField.__init__(self, **kwargs)


class Enum(EnumField, String):
    default_error_messages = {
        'by_name': 'Invalid enum member {input}. Allowed values: {names}.',
        'by_value': 'Invalid enum value {input}. Allowed values: {values}.',
        'must_be_string': 'Enum name must be string. Allowed values: {values}.'
    }

    def __init__(self, **kwargs):
        EnumField.__init__(self, **kwargs)
        String.__init__(self, **kwargs)


class Boolean(CustomField, fields.Boolean):
    default_error_messages = {"invalid": "{field_name} must be boolean."}

    def __init__(self, **kwargs):
        fields.Boolean.__init__(self, **kwargs)
        CustomField.__init__(self, **kwargs)


class Number(CustomField, fields.Number):
    default_error_messages = {
        "invalid": "{field_name} must be number.",
        "too_large": "Number too large."
    }

    def __init__(self, **kwargs):
        fields.Number.__init__(self, **kwargs)
        CustomField.__init__(self, **kwargs)


class List(CustomField, fields.List):
    default_error_messages = {"invalid": "{field_name} are not a valid list."}

    def __init__(self, item, **kwargs):
        fields.List.__init__(self, item, **kwargs)
        CustomField.__init__(self, **kwargs, cls_or_instance=item)


class Nested(fields.Nested, CustomField):
    default_error_messages = {"type": "{filed_name} contain invalid data type"}

    def __init__(self, nested, **kwargs):
        fields.Nested.__init__(self, nested, **kwargs)
        CustomField.__init__(self, **kwargs)


class Float(fields.Float, CustomField):
    default_error_messages = {
        "special": "Special numeric values (nan or infinity) are not permitted.",
        "invalid": "{field_name} must be a float number.",
        "too_large": "Number too large."
    }

    def __init__(self, **kwargs):
        fields.Float.__init__(self, **kwargs)
        CustomField.__init__(self, **kwargs)
