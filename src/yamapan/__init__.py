from argparse import ArgumentParser, Namespace
from typing import Callable

parser = ArgumentParser(
    prog="yamapan",
    description="Yet Another MetA worksPAce maNager for ROS 2",
)
parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.0.1")
subparsers = parser.add_subparsers()


def subcommand(name: str):
    def _subcommand(handler: Callable[[Namespace], int]):
        parser = subparsers.add_parser(name)
        parser.set_defaults(handler=handler)
        return parser

    return _subcommand


def main() -> int:
    args = parser.parse_args()
    if hasattr(args, "handler"):
        return args.handler(args)
    else:
        parser.print_help()
        return 1


import yamapan.alias as _
import yamapan.build as _
import yamapan.clean as _
import yamapan.init as _
import yamapan.resolve as _
import yamapan.ros2 as _
import yamapan.rqt as _
