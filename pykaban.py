#!/usr/bin/env python
import sys
from optparse import OptionParser

def get_option_parser():
    parser = OptionParser(usage='usage: %prog [options] database_name')
    ao = parser.add_option
    ao('-H', '--host', dest='host')
    ao('-p', '--port', dest='port', type='int')
    ao('-u', '--user', dest='user')
    ao('-P', '--password', dest='password', action='store_true')
    ao('-o', '--preserve-order', action='store_true', dest='preserve_order',
       help='Model definition column ordering matches source table.')
    return parser

def err(msg):
    sys.stderr.write('\033[91m%s\033[0m\n' % msg)
    sys.stderr.flush()

if __name__ == '__main__':
    raw_argv = sys.argv

    parser = get_option_parser()
    options, args = parser.parse_args()

    if len(args) < 1:
        err('Missing required parameter "database"')
        parser.print_help()
        sys.exit(1)

    print(options.info)
