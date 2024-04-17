from pydantic import BaseModel, ValidationError

from .ValidatorABS import ValidatorABS
from .exceptions import SchemaValidationException


class ValidatorPydantic(ValidatorABS):
    schema: BaseModel

    def validate(self, payload: dict):
        try:
            return self.schema.parse_obj(payload)
        except ValidationError as ex:
            raise self.errors_mapper(ex)

    def errors_mapper(self, ex: ValidationError):
        errors_list = []
        for error in ex.errors():
            loc = error['loc']
            errors_list.append(
                SchemaValidationException.SchemaValidationItemException(
                    self.format_error_message(error['msg'], loc[len(loc) - 1]),
                    location=loc
                )
            )
        return SchemaValidationException(
            self.target_name,
            errors_list
        )

    @classmethod
    def format_error_message(cls, message: str, field_name: str) -> str:
        return message.format(field_name=field_name)
