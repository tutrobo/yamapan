from argparse import Namespace

from yamapan import subcommand
from yamapan.util import run_command


@subcommand("ros2")
def ros2(args: Namespace) -> int:
    return run_command(
        f"ros2 {' '.join(args.args)}",
        ros_env=True,
    )


ros2.add_argument("args", nargs="*", help="passed to ros2")
