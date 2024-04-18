from . import ClientCommand
from argparse import _SubParsersAction, ArgumentParser

from .app_command import app_detect
from .commands_decorator import command_error
from everai.app import App, AppManager
from everai.logger.logger import getLogger

logger = getLogger(__name__)


class AppDeployCommand(ClientCommand):
    def __init__(self, args):
        self.args = args

    @staticmethod
    def setup(parser: _SubParsersAction):
        deploy_parser = parser.add_parser("deploy", help="Deploy an app to serving status")

        deploy_parser.set_defaults(func=AppDeployCommand)

    @command_error
    @app_detect(optional=False)
    def run(self, app: App):
        AppManager().deploy(app)
