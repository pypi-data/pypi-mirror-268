import typing

from marshmallow import validate


class CustomValidation:
    field_name = None


class Length(validate.Length, CustomValidation):
    message_min = "{field_name} must be at least {min} character long."
    message_max = "{field_name} exceeds {max} characters limit."
    message_all = "{field_name} length must be between {min} and {max}."
    message_equal = "{field_name} length must be {equal} characters long."

    def __init__(
        self,
        message_min=None,
        message_max=None,
        message_all=None,
        message_equal=None,
        min: typing.Optional[int] = None,
        max: typing.Optional[int] = None,
        equal: typing.Optional[int] = None,
        error: typing.Optional[str] = None
    ):
        validate.Length.__init__(self, min=min, max=max, equal=equal, error=error)
        if message_min is not None:
            self.message_min = message_min
        if message_max is not None:
            self.message_min = message_max
        if message_all is not None:
            self.message_min = message_all
        if message_equal is not None:
            self.message_min = message_equal

    def _format_error(self, value: typing.Sized, message: str) -> str:
        return (self.error or message).format(
            input=value, min=self.min, max=self.max, equal=self.equal, field_name=self.field_name
        )


class Items(Length):
    message_min = "Shorter than minimum length {min}."
    message_max = "Longer than maximum length {max}."
    message_all = "Length must be between {min} and {max}."
    message_equal = "Length must be {equal}."


class Range(validate.Range, CustomValidation):
    message_min = "{{field_name}} must be {min_op} {{min}}."
    message_max = "{{field_name}} must be {max_op} {{max}}."
    message_all = "{{field_name}} must be {min_op} {{min}} and {max_op} {{max}}."
    message_gte = "greater than or equal to"
    message_gt = "greater than"
    message_lte = "less than or equal to"
    message_lt = "less than"

    def _format_error(self, value, message: str) -> str:
        return (self.error or message).format(input=value, min=self.min, max=self.max, field_name=self.field_name)


class Regexp(validate.Regexp, CustomValidation):
    default_message = "{field_name} must match the regular expression {regex}."

    def _format_error(self, value: typing.Union[str, bytes]) -> str:
        return self.error.format(input=value, regex=self.regex.pattern, field_name=self.field_name)


class OneOf(validate.OneOf, CustomValidation):
    default_message = "{field_name} must be one of: {choices}."

    def _format_error(self, value) -> str:
        return self.error.format(
            input=value, choices=self.choices_text, labels=self.labels_text, field_name=self.field_name
        )

