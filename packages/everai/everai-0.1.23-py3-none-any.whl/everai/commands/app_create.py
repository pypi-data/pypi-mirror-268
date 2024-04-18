import typing

from . import ClientCommand
from argparse import _SubParsersAction
from everai.app.app_manager import AppManager, App
from everai.commands.app_command import app_detect
from .commands_decorator import command_error

route_name_description = ('Globally unique route name. '
                          'By default, it is same with the app name. '
                          'Once the application name conflicts, route-name needs to be set explicitly.')


class AppCreateCommand(ClientCommand):
    def __init__(self, args):
        self.args = args

    @staticmethod
    def setup(parser: _SubParsersAction):
        create_parser = parser.add_parser("create", help="Create an app")
        create_parser.add_argument('name', help='The app name', type=str)
        create_parser.add_argument('--route-name', '-r', help=route_name_description, type=str)
        # create_parser.add_argument('--ignore-scaffold', action='store_true',
        #                            help='let everai client do not scaffold, e.g. app2.py')

        create_parser.set_defaults(func=AppCreateCommand)

        AppCreateCommand.parser = create_parser

    @command_error
    def run(self):
        app = AppManager().create(app_name=self.args.name,
                                  app_route_name=self.args.route_name)
        print(app)
