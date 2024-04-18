from . import ClientCommand
from argparse import _SubParsersAction, ArgumentParser

from .commands_decorator import command_error
from ..app.app_manager import AppManager


class AppPauseCommand(ClientCommand):
    def __init__(self, args):
        self.args = args

    @staticmethod
    def setup(parser: _SubParsersAction):
        pause_parser = parser.add_parser("pause", help="Pause an app, all worker will be stopped")
        pause_parser.add_argument('name', help='The app name', type=str)

        pause_parser.set_defaults(func=AppPauseCommand)

    @command_error
    def run(self):
        AppManager().pause(self.args.name)
