import enum


class TargetNameEnum(str, enum.Enum):
    QUERY = 'query',
    BODY = 'body',
    PARAMS = 'params'
    UNION = 'union'
