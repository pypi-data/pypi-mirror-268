import logging
import sys
import typing

default_log_format = '[%(asctime)s][%(levelname)s][%(pathname)s:%(lineno)d] %(message)s'
default_date_format = '%Y-%m-%d %H:%M:%S'


def set_format(log_fmt: typing.Optional[str] = None, date_fmt: typing.Optional[str] = None):
    log_format = log_fmt or default_log_format
    date_format = date_fmt or default_date_format
    logging.basicConfig(
        format=log_format,
        datefmt=date_format,
        stream=sys.stdout,
    )


Level = typing.Literal[
    'CRITICAL',
    'FATAL',
    'ERROR',
    'WARNING',
    'WARN',
    'INFO',
    'DEBUG',
]


def getLogger(name: typing.Optional[str] = None, level: typing.Optional[Level] = None) -> logging.Logger:
    set_format()
    ret = logging.getLogger(name)
    if level is not None:
        ret.setLevel(level)
    return ret
