import os
from argparse import Namespace

from yamapan import subcommand
from yamapan.config import (
    CONFIG_FILENAME,
    CONFIG_TEMPLATE,
    GITIGNORE_TEMPLATE,
    LOCAL_CONFIG_FILENAME,
    LOCAL_CONFIG_TEMPLATE,
)


@subcommand("init")
def init(namespace: Namespace, args: list[str]) -> int:
    with open(CONFIG_FILENAME, "w") as f:
        f.write(CONFIG_TEMPLATE)
    with open(LOCAL_CONFIG_FILENAME, "w") as f:
        f.write(LOCAL_CONFIG_TEMPLATE.format(namespace.ros_install_prefix))
    with open(".gitignore", "w") as f:
        f.write(GITIGNORE_TEMPLATE)
    return 0


init.add_argument(
    "--ros-install-prefix",
    default=f"/opt/ros/{os.environ.get('ROS_DISTRO') or 'humble'}",
)
