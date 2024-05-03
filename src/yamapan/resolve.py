from argparse import Namespace

import yaml

from yamapan import subcommand
from yamapan.util import get_workspace_path, load_config, run_command


@subcommand("resolve")
def resolve(_: Namespace) -> int:
    workspace_path = get_workspace_path()
    config = load_config()
    ret = run_command(
        "vcs import",
        cwd=workspace_path,
        input=yaml.dump({"repositories": config.repositories}).encode(),
    )
    if ret != 0:
        return ret
    ret = run_command("rosdep update")
    if ret != 0:
        return ret
    return run_command(
        "rosdep install -y --from-paths . --ignore-src --rosdistro $ROS_DISTRO",
        ros_env=True,
        cwd=workspace_path,
    )
