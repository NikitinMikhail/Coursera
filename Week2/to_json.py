import functools
import json


def to_json(func):
    @functools.wraps(func)
    def inner_function(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))

    return inner_function
