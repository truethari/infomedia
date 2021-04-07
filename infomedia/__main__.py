import argparse

from .run       import Worker
from .version   import __version__

class MyHelpFormatter(argparse.ArgumentDefaultsHelpFormatter):
    def _get_help_string(self, action):
        return action.help

def main():
    parser = argparse.ArgumentParser(
        formatter_class=MyHelpFormatter,
        description="infomedia {}".format(__version__)
    )

    parser.print_usage = parser.print_help

    parser.add_argument("file", help="path to file")

    parser.add_argument(
        "-i",
        "--info",
        type=str,
        default="False",
        help="get information about",
    )

    parser.add_argument(
        "-s",
        "--save-path",
        type=str,
        default="False",
        help="a file path to save the data file",
    )

    parser.add_argument(
        "-of",
        "--output-format",
        type=str,
        default="False",
        choices=["json", "ini", "xml", "csv", "flat"],
        help="data file format",
    )

    parser.add_argument(
        "-v",
        "--version",
        action='version',
        version=__version__,
        help="infomedia version",
    )

    cli_args = parser.parse_args()

    worker = Worker(
        cli_args.file,
        cli_args.info,
        cli_args.output_format,
        cli_args.save_path
    )

    worker._application()

if __name__ == '__main__':
    main()