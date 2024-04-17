# flake8: noqa
import os
from opentelemetry import context as context_api
import json


def _with_tracer_wrapper(func):
    """Helper for providing tracer for wrapper functions."""

    def _with_tracer(tracer, to_wrap):
        def wrapper(wrapped, instance, args, kwargs):
            return func(tracer, to_wrap, wrapped, instance, args, kwargs)

        return wrapper

    return _with_tracer


def should_send_prompts():
    return (
        os.getenv("SYNTRAC_TRACE_CONTENT") or "true"
    ).lower() == "true" or context_api.get_value("override_enable_content_tracing")


def serialise_to_json(value):
    try:
        default = lambda o: f"<<non-serializable: {type(o).__qualname__}>>"
        return json.dumps(value, default=default)
    except Exception as e:
        print(e)
        return value
