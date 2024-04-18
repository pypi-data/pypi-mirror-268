from . import ClientCommand
from argparse import _SubParsersAction
from everai.commands.secret_create import SecretCreateCommand
from everai.commands.secret_delete import SecretDeleteCommand
from everai.commands.secret_list import SecretListCommand
from everai.commands.secret_get import SecretGetCommand


class SecretCommand(ClientCommand):
    parser: _SubParsersAction = None

    def __init__(self, args):
        self.args = args

    @staticmethod
    def setup(parser: _SubParsersAction):
        secret_parser = parser.add_parser('secret', help='Manage secrets')
        secret_sub_parser = secret_parser.add_subparsers(help="Secret command help")

        SecretCreateCommand.setup(secret_sub_parser)
        SecretDeleteCommand.setup(secret_sub_parser)
        SecretListCommand.setup(secret_sub_parser)
        SecretGetCommand.setup(secret_sub_parser)

        secret_parser.set_defaults(func=SecretCommand)
        SecretCommand.parser = secret_parser

    def run(self):
        SecretCommand.parser.print_help()
        return
