"""AVA CLI

Usage:
  avacli.py (-h | --help)
  avacli.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

from docopt import docopt
from .version import __version__

def main():
    arguments = docopt(__doc__, version=__version__)
    print(arguments)
