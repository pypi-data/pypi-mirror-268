from . import ClientCommand
from argparse import _SubParsersAction
from everai.secret.secret_manager import SecretManager
import json

from .commands_decorator import command_error


class SecretGetCommand(ClientCommand):
    def __init__(self, args):
        self.args = args

    @staticmethod
    def setup(parser: _SubParsersAction):
        get_parser = parser.add_parser('get', help='Get secret')
        get_parser.add_argument('name', help='The secret name')
        get_parser.add_argument(
            '-o',
            '--output',
            help='Output type, current support json|table',
            default='table',
            type=str,
        )
        get_parser.set_defaults(func=SecretGetCommand)

    @command_error
    def run(self):
        secret = SecretManager().get(name=self.args.name)
        if self.args.output == 'table':
            print(secret)
        elif self.args.output == 'json':
            print(secret.to_json())
