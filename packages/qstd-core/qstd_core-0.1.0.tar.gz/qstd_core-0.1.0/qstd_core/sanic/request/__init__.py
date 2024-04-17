import typing

from sanic import Request


def locale_to_language(locale):
    return locale.strip().split('-')[0].lower()


def get_languages(request: Request) -> typing.Optional[typing.List[str]]:
    accept_language = request.headers.get('accept-language')
    if accept_language is None:
        return []
    languages = accept_language.split(",")
    locale_q_pairs = []

    for language in languages:
        if language.split(";")[0] == language:
            locale_q_pairs.append(dict(language=locale_to_language(language), q=1))
        else:
            locale = locale_to_language(language.split(";")[0])
            q = language.split(";")[1].split("=")[1]
            locale_q_pairs.append(dict(language=locale, q=float(q)))
    return list(map(lambda pair: pair['language'], sorted(locale_q_pairs, key=lambda d: d['q'], reverse=True)))
