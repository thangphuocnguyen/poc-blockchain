""" Implementation of the command line interface.

"""
from argparse import ArgumentParser
from inspect import getfullargspec

from . import __version__
from .api import cmd
from .api import demo
from .api import signature_demo

from .core import config
from .core import logger


__all__ = "main",


def main(argv=None):
    """ Execute the application CLI.

    Arguments are taken from sys.argv by default.

    """
    args = _args(argv)
    logger.start(args.warn)
    logger.debug("starting execution")
    config.load(args.config)
    config.core.logging = args.warn
    command = args.command

    args = vars(args)

    spec = getfullargspec(command)

    if not spec.varkw:
        # No kwargs, remove unexpected arguments.
        args = {key: args[key] for key in args if key in spec.args}
    try:
        command(**args)
    except RuntimeError as err:
        logger.critical(err)
        return 1
    logger.debug("successful completion")
    return 0
 

def _args(argv=None):
    """ Parse command line arguments.

    """
    parser = ArgumentParser()
    parser.add_argument("-c", "--config", action="append",
            help="config file [etc/config.yml]")
    parser.add_argument("-v", "--version", action="version",
            version="app {:s}".format(__version__),
            help="print version and exit")
    parser.add_argument("-w", "--warn", default="WARN",
            help="logger warning level [WARN]")

    common = ArgumentParser(add_help=False)  # common subcommand arguments
    common.add_argument("--name", "-n", default="World", help="greeting name")
    
    subparsers = parser.add_subparsers(title="subcommands")
    
    _cmd(subparsers, common)
    _cmd_demo(subparsers, common)
    _signature_demo(subparsers, common)
    
    args = parser.parse_args(argv)
    if not args.config:
        # Don't specify this as an argument default or else it will always be
        # included in the list.
        args.config = "etc/config.yml"
    return args
 

def _cmd(subparsers, common):
    """ CLI adaptor for the api.cmd command.

    """
    parser = subparsers.add_parser("cmd", parents=[common])
    parser.set_defaults(command=cmd)
    return

def _cmd_demo(subparsers, common):
    parser = subparsers.add_parser("demo", parents=[common])
    parser.set_defaults(command=demo)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    return

def _signature_demo(subparsers, common):
    parser = subparsers.add_parser("signature", parents=[common])
    parser.set_defaults(command=signature_demo)
    return


# Make the module executable.

if __name__ == "__main__":
    try:
        status = main()
    except:
        logger.critical("shutting down due to fatal error")
        raise  # print stack trace
    else:
        raise SystemExit(status)
