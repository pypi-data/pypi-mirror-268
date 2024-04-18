import argparse
from . import UBitLogger, NoUBitFound, __version__


def cli() -> None:

    parser = argparse.ArgumentParser(
        prog='ubitlogger',
        description="micro:bit serial port logger",
        epilog='https://github.com/p4irin/ubitlogger'
    )

    parser.add_argument(
        '-V',
        '--version',
        action='version',
        version=f'{__version__}',
        help='show version and exit.'
    )

    sub_parsers = parser.add_subparsers(
        title='Sub commands',
        dest='command'
    )

    sp_start = sub_parsers.add_parser(
        'start',
        help="start logging",
    )

    sp_start.add_argument(
        '-d',
        '--debug',
        action='store_true',
        help='show debugging output'
    )
    sp_start.add_argument(
        '-t',
        '--timeout',
        action='store',
        type=float,
        help='set a timeout (float)'
    )

    args = parser.parse_args()
    kwargs = {}
    if args.command == 'start':
        if args.debug:
            debug_flag = True
        else:
            debug_flag = False
        kwargs['debug'] = debug_flag
        if args.timeout:
            timeout_flag = args.timeout
            kwargs['timeout'] = timeout_flag

    try:
        ubitlogger = UBitLogger(**kwargs)
        ubitlogger.start()
    except NoUBitFound:
        print("No micro:bit found ! Is it plugged in ?")
