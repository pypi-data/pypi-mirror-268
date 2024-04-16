import argparse
from pathlib import Path
from importlib import metadata

from archerdfu.bmp import CaliberIcon, matrix_to_bmp

try:
    __version__ = metadata.version("archerdfu.bmp")
except metadata.PackageNotFoundError:
    __version__ = 'Unknown'


def get_argparser():
    parser = argparse.ArgumentParser(
        prog='archerdfu bmp processor',
        epilog='Text at the bottom of help',
        conflict_handler='resolve',
        exit_on_error=False,
    )

    parser.add_argument('-v', '--version', action='version', version=f'{parser.prog} v{__version__}')
    parser.add_argument('-d', '--debug', action='store_true', help="run in debug mode")

    add_cli_arguments(parser)
    return parser


def add_cli_arguments(parser):

    if isinstance(parser, argparse._SubParsersAction):
        _parser = parser.add_parser('icon', help="command to create caliber icon")
    else:
        _parser = parser

    parser_group = _parser.add_argument_group("Create icon")
    parser_group.add_argument('-c', '--caliber', action='store', metavar='<str>',
                                   help="Caliber name")
    parser_group.add_argument('-w', '--weight', action='store', metavar='<float>', type=float,
                                   help="Bullet weight")
    parser_group.add_argument('-o', '--output', action='store', metavar='<output dir>',
                                   default='./',
                                   help='output directory')


def create_caliber_icon(commandline_args, logger=None):
    output = commandline_args.output

    dest = Path(output).absolute()
    if not dest.is_dir():
        raise TypeError('Destination must be a directory')

    if not commandline_args.weight:
        raise TypeError('Weight required must be a number')

    if not commandline_args.caliber:
        raise TypeError('Caliber required must be a string')

    filename = f"{commandline_args.caliber}-{commandline_args.weight}gr.bmp"
    matrix = CaliberIcon.create_icon_matrix(commandline_args.caliber, commandline_args.weight)
    matrix_to_bmp(matrix, dest / filename)
    if logger:
        logger.info(f"Icon saved to {dest / filename}")


def main(commandline_args):
    create_caliber_icon(commandline_args)


if __name__ == "__main__":
    COMMANDLINE_PARSER = get_argparser()

    try:
        COMMANDLINE_ARGS, UNKNOWN = COMMANDLINE_PARSER.parse_known_args()
        main(COMMANDLINE_ARGS)
    except Exception as exc:
        COMMANDLINE_PARSER.parse_known_args(('-h',))
