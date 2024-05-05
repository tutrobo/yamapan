from argparse import Namespace

from yamapan import subcommand
from yamapan.util import run_command


@subcommand("ros2")
def ros2(namespace: Namespace, args: list[str]) -> int:
    return run_command(
        f"ros2 {' '.join(args)}",
        ros_env=True,
    )
