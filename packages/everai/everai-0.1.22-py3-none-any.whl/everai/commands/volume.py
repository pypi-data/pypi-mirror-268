from . import ClientCommand
from argparse import _SubParsersAction
from everai.commands.volume_create import VolumeCreateCommand
from everai.commands.volume_delete import VolumeDeleteCommand
from everai.commands.volume_list import VolumeListCommand
from everai.commands.volume_get import VolumeGetCommand
from everai.commands.volume_pull import VolumePullCommand
from everai.commands.volume_push import VolumePushCommand


class VolumeCommand(ClientCommand):
    parser: _SubParsersAction = None

    def __init__(self, args):
        self.args = args

    @staticmethod
    def setup(parser: _SubParsersAction) -> None:
        volume_parser = parser.add_parser('volume', help='Manage volume')
        volume_sub_parser = volume_parser.add_subparsers(help='Volume command help')

        VolumeCreateCommand.setup(volume_sub_parser)
        VolumeListCommand.setup(volume_sub_parser)
        VolumeDeleteCommand.setup(volume_sub_parser)
        VolumeGetCommand.setup(volume_sub_parser)
        VolumePullCommand.setup(volume_sub_parser)
        VolumePushCommand.setup(volume_sub_parser)

        volume_parser.set_defaults(func=VolumeCommand)
        VolumeCommand.parser = volume_parser

    def run(self):
        VolumeCommand.parser.print_help()
        return


