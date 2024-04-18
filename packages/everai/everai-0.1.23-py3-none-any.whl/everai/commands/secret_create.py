from . import ClientCommand
from argparse import _SubParsersAction
from everai.secret.secret_manager import SecretManager
from .commands_decorator import command_error


class SecretCreateCommand(ClientCommand):
    def __init__(self, args):
        self.args = args

    @staticmethod
    def setup(parser: _SubParsersAction):
        create_parser = parser.add_parser('create', help='Create Secret from file or literal string')
        create_parser.add_argument('name', help='The secret name')
        create_parser.add_argument(
            '-l',
            '--from-literal',
            action='append',
            type=str,
            help='Create secret from literal, for example: --from-literal name=user'
        )

        create_parser.add_argument(
            '-f',
            '--from-file',
            action='append',
            type=str,
            help='Create secret from file, for example: --from-file filename'
        )

        create_parser.set_defaults(func=SecretCreateCommand)

    @command_error
    def run(self):
        if self.args.from_literal is None and self.args.from_file is None:
            raise ValueError('Please specify either --from-literal, or --from-file arguments')

        if self.args.from_literal is not None and self.args.from_file is not None:
            raise ValueError('Cannot support both --from-literal and --from-file')

        if self.args.from_literal is not None and len(self.args.from_literal) > 0:
            secret = SecretManager().create_from_lines(name=self.args.name, lines=self.args.from_literal)

        if self.args.from_file is not None and len(self.args.from_file) > 0:
            secret = SecretManager().create_from_file(name=self.args.name, file=self.args.from_file)

        print("Secret created successfully")

