from argparse import ArgumentParser, Namespace
from typing import Callable

parser = ArgumentParser(
    prog="yamapan",
    description="Yet Another MetA worksPAce maNager for ROS 2",
)
parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.0.5")
subparsers = parser.add_subparsers()


def subcommand(name: str):
    def _subcommand(handler: Callable[[Namespace, list[str]], int]):
        parser = subparsers.add_parser(name)
        parser.set_defaults(handler=handler)
        return parser

    return _subcommand


def main() -> int:
    namespace, args = parser.parse_known_args()
    if hasattr(namespace, "handler"):
        return namespace.handler(namespace, args)
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
