#!/usr/bin/env python
# @date 2015-02-05

from __future__ import absolute_import, division, print_function, with_statement

import os
import sys

from commitcheck.argutils import git_create_parser, git_get_type
from commitcheck.checkers.gitchecker import Checker
import settings


def main(argv=None):
    argv = sys.argv if argv is None else argv

    # Create parser and parse args.
    parser = git_create_parser(description='IOS commit check')
    args = parser.parse_args(argv[1:])
    check_type = git_get_type(args)
    if check_type is None:
        print('Unknown check type: %s' % (args.type))
        return 1

    # Setup to do check.
    path = os.getcwd()
    patterns = settings.IOS_FULL_PATTERNS
    checker = Checker(path, patterns, settings.IOS_IGNORES, settings.IOS_CHECKS)
    checker.verbose = args.verbose
    return checker.check(check_type, args.revisions)


if __name__ == '__main__':
    sys.exit(main())
