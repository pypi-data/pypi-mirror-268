from . import ClientCommand
from argparse import _SubParsersAction

from .app_create import AppCreateCommand
from .app_get import AppGetCommand
from .app_deploy import AppDeployCommand
from .app_pause import AppPauseCommand
from .app_upgrade import AppUpgradeCommand
from .app_prepare import AppPrepareCommand


class AppCommand(ClientCommand):
    parser: _SubParsersAction = None

    def __init__(self, args):
        self.args = args

    @staticmethod
    def setup(parser: _SubParsersAction):
        app_parser = parser.add_parser('app', help='Manage app')
        app_sub_parser = app_parser.add_subparsers(help='App command help')

        AppCreateCommand.setup(app_sub_parser)
        AppGetCommand.setup(app_sub_parser)
        AppUpgradeCommand.setup(app_sub_parser)
        AppPauseCommand.setup(app_sub_parser)
        AppDeployCommand.setup(app_sub_parser)
        AppPauseCommand.setup(app_sub_parser)
        AppPrepareCommand.setup(app_sub_parser)

        app_parser.set_defaults(func=AppCommand)
        AppCommand.parser = app_parser

    def run(self):
        AppCommand.parser.print_help()
