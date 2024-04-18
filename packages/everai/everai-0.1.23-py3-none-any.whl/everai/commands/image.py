from . import ClientCommand
from argparse import _SubParsersAction
from everai.constants import COMMAND_ENTRY
from everai.runner import must_find_right_target
from everai.image import Builder
from .commands_decorator import command_error


class ImageBuildCommand(ClientCommand):
    def __init__(self, args):
        self.args = args

    @staticmethod
    def setup(parser: _SubParsersAction) -> None:
        image_build_parser = parser.add_parser('build', help='Image build')
        image_build_parser.set_defaults(func=ImageBuildCommand)

    @command_error
    def run(self):
        print('Start compiling the image ...')
        builder = must_find_right_target(search_files=['image.py', 'image_builder.py'], target_type=Builder, target_name='image_builder')
        builder.run()


class ImagePushCommand(ClientCommand):
    def __init__(self, args):
        self.args = args

    @staticmethod
    def setup(parser: _SubParsersAction) -> None:
        image_push_parser = parser.add_parser('push', help='Push image build')
        image_push_parser.set_defaults(func=ImagePushCommand)

    @command_error
    def run(self):
        print('push')


class ImageCommand(ClientCommand):
    parser: _SubParsersAction = None

    def __init__(self, args):
        self.args = args

    @staticmethod
    def setup(parser: _SubParsersAction) -> None:
        image_parser = parser.add_parser('image', help='Image management')
        image_subparsers = image_parser.add_subparsers(help=f'{COMMAND_ENTRY} image command helps')

        ImageBuildCommand.setup(image_subparsers)
        ImagePushCommand.setup(image_subparsers)

        image_parser.set_defaults(func=ImageCommand)
        ImageCommand.parser = image_parser

    def run(self):
        ImageCommand.parser.print_help()
