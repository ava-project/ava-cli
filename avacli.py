#!/usr/bin/env python

"""AVA CLI

Usage:
  avacli.py (-h | --help)
  avacli.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

from docopt import docopt


def main():
    arguments = docopt(__doc__, version='AVA CLI 0.1.0')
    print(arguments)

if __name__ == "__main__":
    main()
