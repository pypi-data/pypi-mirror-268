from . import ClientCommand
from argparse import _SubParsersAction
from everai.volume.volume_manager import VolumeManager
from everai.constants import EVERAI_VOLUME_ROOT
from .commands_decorator import command_error


class VolumePushCommand(ClientCommand):
    def __init__(self, args):
        self.args = args

    @staticmethod
    def setup(parser: _SubParsersAction):
        create_parser = parser.add_parser('push', help='Push volume')
        create_parser.add_argument('name', help='The volume name', type=str)

        create_parser.set_defaults(func=VolumePushCommand)

    @command_error
    def run(self):
        manager = VolumeManager(EVERAI_VOLUME_ROOT)
        volume = manager.push(self.args.name)
        print(volume)
