from . import ClientCommand
from argparse import _SubParsersAction
from everai.volume.volume_manager import VolumeManager
from .commands_decorator import command_error


class VolumeGetCommand(ClientCommand):
    def __init__(self, args):
        self.args = args

    @staticmethod
    def setup(parser: _SubParsersAction):
        delete_parser = parser.add_parser('get', help='Get volume')
        delete_parser.add_argument('name', help='The volume name')

        delete_parser.set_defaults(func=VolumeGetCommand)

    @command_error
    def run(self):
        volume_manager = VolumeManager()
        volume = volume_manager.get(self.args.name)
        print(volume)
        print(f'path: {volume_manager.volume_path(volume.id)}')

