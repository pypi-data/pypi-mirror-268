import enum
import typing

import yaml
from os import listdir
from os.path import isfile, join


class State:
    localization: typing.Dict[str, typing.Dict[str, str]] = dict()
    default_language: str = 'en'

    @classmethod
    def load(cls, resource_path: str):
        cls.localization.clear()
        localization_files = [f for f in listdir(resource_path) if isfile(join(resource_path, f))]
        for filename in localization_files:
            with open(join(resource_path, filename)) as stream:
                cls.localization[filename.replace('.yaml', '')] = yaml.safe_load(stream) or dict()

    @classmethod
    def has_language(cls, lang: str):
        return lang in cls.localization

    @classmethod
    def _key_str(cls, key: typing.Union[str, enum.Enum]):
        return key.name if isinstance(key, enum.Enum) else key

    @classmethod
    def get_template(
        cls,
        languages: typing.Optional[typing.List[str]],
        key: typing.Union[str, enum.Enum]
    ) -> typing.Optional[str]:
        key = cls._key_str(key)
        for lang in languages:
            if lang in cls.localization:
                break
        else:
            lang = cls.default_language
        if cls.has_language(lang):
            lang_template = cls.localization[lang].get(key)
            if lang_template is not None:
                return lang_template
        if cls.has_language(cls.default_language):
            return cls.localization[cls.default_language].get(key)

    @classmethod
    def get_localization_messages(cls, key: typing.Union[str, enum.Enum]):
        key = cls._key_str(key)
        return {locale: messages[key] for locale, messages in cls.localization.items() if key in messages}


def localize(
    key: typing.Union[str, enum.Enum],
    languages: typing.Optional[typing.Union[str, typing.List[str]]] = None,
    params=None
) -> str:
    if languages is not None and isinstance(languages, str):
        languages = [languages]
    template = State.get_template(languages, key)
    if template:
        if params is not None:
            return template.format(**params)
        else:
            return template
    return key

