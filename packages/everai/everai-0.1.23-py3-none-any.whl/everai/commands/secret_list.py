from . import ClientCommand
from argparse import _SubParsersAction
from everai.secret.secret_manager import SecretManager
import json
from typing import List, Dict

from .commands_decorator import command_error


class SecretListCommand(ClientCommand):
    def __init__(self, args):
        self.args = args

    @staticmethod
    def setup(parser: _SubParsersAction):
        list_parser = parser.add_parser('list', help='List secret')
        list_parser.add_argument(
            '-o',
            '--output',
            help='Output type, current support json|table',
            default='table',
            type=str,
        )
        list_parser.set_defaults(func=SecretListCommand)

    @command_error
    def run(self):
        list_secrets = SecretManager().list()
        if self.args.output == 'table':
            for secret in list_secrets:
                print(secret)
        elif self.args.output == 'json':
            json_out_data: List[Dict[str, str | Dict[str, str]]] = []
            for v in list_secrets:
                json_out_data.append({
                    'secret_name': v.name,
                    'data': v.data
                })

            print(json.dumps(json_out_data, ensure_ascii=False))

