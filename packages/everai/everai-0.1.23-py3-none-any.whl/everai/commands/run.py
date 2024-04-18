from . import ClientCommand
from argparse import _SubParsersAction, Namespace

from .app_command import app_detect
from everai.app import AppManager, App
from .commands_decorator import command_error


class RunCommand(ClientCommand):
    def __init__(self, args: Namespace):
        self.args = args

    @staticmethod
    def setup(parser: _SubParsersAction) -> None:
        run_parser = parser.add_parser('run', help='Local run a everai application for test')
        run_parser.add_argument('--port', type=int, default=8866, help='The port to bind to')
        run_parser.add_argument('--listen', type=str, default='0.0.0.0', help='The interface to bind to')

        run_parser.set_defaults(func=RunCommand)

    @command_error
    @app_detect(optional=False)
    def run(self, app: App):
        AppManager().run(app=app,
                         port=self.args.port,
                         listen=self.args.listen,)

