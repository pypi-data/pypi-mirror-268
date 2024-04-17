import argparse
import logging
import sys

from . import __version__
from .core import makefile_2_markdown

logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------


def get_parser():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Simple command-line utility that convertys Makefiles to Markdown if specific commenting style is followed."
    )
    parser.add_argument("-p", "--path", required=True, help="Path to the markdown file")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose output",
    )
    parser.add_argument("--version", action="version", version=__version__)

    return parser.parse_args()


def run():
    """Run script."""

    args = get_parser()

    makefile_2_markdown(args.path)

    sys.exit()


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    run()
