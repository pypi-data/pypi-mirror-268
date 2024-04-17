from sanic import Blueprint, response as sanic_response

from . import utils
from .decorators import exclude


openapi_router = Blueprint('openapi')


@openapi_router.listener('after_server_start')
def collect(app, _):
    utils.collect(app)


@exclude()
async def get_spec(_):
    return sanic_response.json(utils.openapi)


openapi_router.add_route(get_spec, '/openapi', ['GET'])
