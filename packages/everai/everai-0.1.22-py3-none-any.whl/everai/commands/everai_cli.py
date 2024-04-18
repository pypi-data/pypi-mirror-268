from argparse import ArgumentParser
from everai.commands.app import AppCommand
from everai.commands.config import ConfigCommand
from everai.commands.login import LoginCommand
from everai.commands.logout import LogoutCommand
from everai.commands.run import RunCommand
from everai.commands.image import ImageCommand
from everai.commands.secret import SecretCommand
from everai.commands.volume import VolumeCommand
from everai.constants import COMMAND_ENTRY
import everai.utils.verbose as vb


def main():
    parser = ArgumentParser(
        COMMAND_ENTRY,
        description='EverAI Client for manage your EverAI application and other asserts'
    )

    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='Verbose output',
    )
    commands_parser = parser.add_subparsers(help=f'Valid subcommands for {COMMAND_ENTRY}')
    LoginCommand.setup(commands_parser)
    LogoutCommand.setup(commands_parser)
    ConfigCommand.setup(commands_parser)
    ImageCommand.setup(commands_parser)
    RunCommand.setup(commands_parser)
    AppCommand.setup(commands_parser)
    SecretCommand.setup(commands_parser)
    VolumeCommand.setup(commands_parser)

    args = parser.parse_args()
    if not hasattr(args, "func"):
        parser.print_help()
        exit(1)
    vb.is_verbose = args.verbose
    service = args.func(args)
    service.run()
    pass


if __name__ == "__main__":
    main()
