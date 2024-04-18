import importlib
import os
import sys
import typing

from everai.app import App
from everai.logger import getLogger

T = typing.TypeVar('T')

logger = getLogger(__name__)


class _TypeChecker(typing.Generic[T]):
    def is_right_type(self, x: typing.Any) -> bool:
        # print(self.__orig_class__.__args__[0])
        # print(type(x))
        return isinstance(x, self.__orig_class__.__args__[0])


def find_object(file: str | os.PathLike, t: T, name: str) -> typing.Optional[T]:
    try:
        module = importlib.import_module(prepare_import_path(file))
    except Exception as e:
        logger.debug(e)
        return None

    logger.debug(f'import {file} success')
    attr = getattr(module, name, None)
    if _TypeChecker[t]().is_right_type(attr):
        return attr

    matches = [v for v in module.__dict__.values() if _TypeChecker[t]().is_right_type(v)]
    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        raise Exception(f'More than one {t.__name__} in module')
    else:
        return None


def prepare_import_path(path: str) -> str:
    path = os.path.realpath(path)
    filename, ext = os.path.splitext(path)
    if ext == ".py":
        path = filename

    if os.path.basename(path) == "__init__":
        path = os.path.dirname(path)

    module_name = []
    while True:
        path, name = os.path.split(path)
        module_name.append(name)

        if not os.path.exists(os.path.join(path, "__init__.py")):
            break

    if sys.path[0] != path:
        sys.path.insert(0, path)
    result = ".".join(module_name[::-1])
    return result


def find_right_target(search_files: list[str] = None, target_type: type = None, target_name: str = None):
    search_files = ['app.py'] if search_files is None else search_files
    target_name = 'app' if not target_name else target_name
    target_type = App if target_type is None else target_type

    target = None
    for path in search_files:
        target = find_object(path, target_type, target_name)
        if target is not None:
            break

    return target


def must_find_right_target(search_files: list[str] = None, target_type: type = None, target_name: str = None):
    target = find_right_target(search_files, target_type, target_name)

    if target is None:
        raise Exception(f'Cloud not find any {target_type.__name__} in {search_files}')
    return target
