from argparse import Namespace

from yamapan import subcommand
from yamapan.util import get_workspace_path, run_command


@subcommand("build")
def build(namespace: Namespace, args: list[str]) -> int:
    workspace_path = get_workspace_path()
    return run_command(
        f"colcon build {'' if namespace.no_symlink else '--symlink-install'} {' '.join(args)}",
        ros_env=True,
        cwd=workspace_path,
    )


build.add_argument(
    "--no-symlink",
    action="store_true",
    help="do not use --symlink-install",
)
