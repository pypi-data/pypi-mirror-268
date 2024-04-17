from qstd_async_tools import trace
from sanic import Request


def add_trace_id(_: Request):
    trace.add_trace_id()


