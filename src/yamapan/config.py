from pathlib import Path
from typing import Any

from pydantic import BaseModel

CONFIG_FILENAME = "yamapan.toml"
CONFIG_TEMPLATE = """[aliases]
# build = "yamapan build -- --cmake-args -DCMAKE_C_COMPILER_LAUNCHER=ccache -DCMAKE_CXX_COMPILER_LAUNCHER=ccache"

[repositories]
# "ext/voicevox_ros2" = { type = "git", url = "https://github.com/tutrobo/voicevox_ros2.git", version = "master" }
"""

LOCAL_CONFIG_FILENAME = "yamapan.local.toml"
LOCAL_CONFIG_TEMPLATE = """ros_install_prefix = "{}"
"""

GITIGNORE_TEMPLATE = """yamapan.local.toml
build/
install/
log/
"""


class Config(BaseModel):
    aliases: dict[str, str]
    repositories: dict[str, Any]


class LocalConfig(BaseModel):
    ros_install_prefix: Path
