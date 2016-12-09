"""AVA CLI

    Usage:
      avacli [options] [COMMAND] [ARGS...]
      avacli -h|--help

    Options:
      --verbose         Show more output
      -v, --version     Print version and exit

    Commands:
      login             Authenticate to the AVA Cloud
      version           Show the Ava Cli version information
"""

from docopt import docopt

from .cli.parser import ArgsParser
from .version import __version__

def main():
    arguments = docopt(__doc__, version=__version__)
    parser = ArgsParser(arguments)
    parser.dispatch()
