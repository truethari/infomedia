from .run       import Worker
from .version   import __version__
import argparse

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="infomedia {}".format(__version__)
    )
    parser.add_argument("input", help="File path")

    parser.add_argument(
        "-i",
        "--info",
        type=str,
        default="False",
        help="Get information about",
    )

    parser.add_argument(
        "-s",
        "--save-path",
        type=str,
        default="False",
        help="A file path to save the data file",
    )

    parser.add_argument(
        "-of",
        "--output-format",
        type=str,
        default="False",
        choices=["json", "ini"],
        help="Data file format",
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
        cli_args.input,
        cli_args.info,
        cli_args.output_format,
        cli_args.save_path
    )

    worker._application()

if __name__ == '__main__':
    main()