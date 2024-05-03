from argparse import Namespace

from yamapan import subcommand
from yamapan.util import run_command


@subcommand("rqt")
def rqt(args: Namespace) -> int:
    return run_command(
        f"rqt {' '.join(args.args)}",
        ros_env=True,
    )


rqt.add_argument("args", nargs="*", help="passed to rqt")
