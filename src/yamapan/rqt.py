from argparse import Namespace

from yamapan import subcommand
from yamapan.util import run_command


@subcommand("rqt")
def rqt(namespace: Namespace, args: list[str]) -> int:
    return run_command(
        f"rqt {' '.join(args)}",
        ros_env=True,
    )
