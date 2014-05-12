# -*- coding: utf-8 -*-
import sys
from argparse import ArgumentParser

from .__version__ import __version__, __build__
from .baidusuggest import (text_sink, spooler, source)

__all__ = []

description = '''A simple research tool for getting Baidu suggestions.'''

epilog = '''....'''


def main():
    '''
    Main Entry point for translator and argument parser
    '''
    version = ''.join([__version__, __build__])

    # Version
    parser.add_argument(
        '-v', '--version', action='version',
        version="%s v%s" % ('translate', version))
    args = parser.parse_args()

if __name__ == '__main__':
    sys.exit(main())
