from argparse import Namespace

from yamapan import subcommand
from yamapan.util import get_workspace_path, run_command


@subcommand("build")
def build(args: Namespace) -> int:
    workspace_path = get_workspace_path()
    return run_command(
        f"colcon build {'' if args.no_symlink else '--symlink-install'} {' '.join(args.args)}",
        ros_env=True,
        cwd=workspace_path,
    )


build.add_argument(
    "--no-symlink",
    action="store_true",
    help="do not use --symlink-install",
)
build.add_argument("args", nargs="*", help="passed to colcon build")
