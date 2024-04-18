from everai.utils import synchronize
import functools


class _Deployment:
    def __init__(self, name: str):
        pass

    def prepare(self):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator

    def clear(self):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator


Deployment = synchronize(_Deployment)
