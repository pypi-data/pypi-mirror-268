from . import ClientCommand
from argparse import _SubParsersAction
from everai.token_manager import TokenManager
from .commands_decorator import command_error


class LogoutCommand(ClientCommand):
    def __init__(self,args):
        self.args = args

    @staticmethod
    def setup(parser: _SubParsersAction):
        logout_parser = parser.add_parser('logout', help='Logout')
        logout_parser.set_defaults(func=LogoutCommand)

    @command_error
    def run(self):
        TokenManager.delete_token()
        print('Logout successful')

