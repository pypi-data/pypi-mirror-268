import typing

from . import ClientCommand
from argparse import _SubParsersAction, ArgumentParser

from .app_command import app_detect
from .commands_decorator import command_error
from ..app import App
from ..app.app_manager import AppManager


class AppGetCommand(ClientCommand):
    def __init__(self, args):
        self.args = args

    @staticmethod
    @app_detect(optional=True)
    def setup(parser: _SubParsersAction, app: typing.Optional[App]):
        get_parser = parser.add_parser("get", help="Get app information")
        if app is None:
            get_parser.add_argument('name', help='The app name', type=str)

        get_parser.set_defaults(func=AppGetCommand)

    @command_error
    @app_detect(optional=True)
    def run(self, app: App):
        app_name = app.name if app is not None else self.args.name
        resp = AppManager().get(app_name)
        print(resp)
