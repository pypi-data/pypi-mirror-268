import functools

from everai.app import App
from everai.runner import find_right_target


def app_detect(optional: bool = True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            app = find_right_target(target_type=App)
            if not optional and app is None:
                raise Exception('No app found in app.py')
            return func(app=app, *args, **kwargs)

        return wrapper
    return decorator


def app_name(optional: bool = True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            app = find_right_target(target_type=App)
            if not optional and app is None:
                raise Exception('No app found in app.py')

            return func(name=app.name, *args, **kwargs)

        return wrapper
    return decorator
