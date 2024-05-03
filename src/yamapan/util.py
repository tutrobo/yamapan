import subprocess
import sys
from pathlib import Path

import tomli

from yamapan.config import CONFIG_FILENAME, LOCAL_CONFIG_FILENAME, Config, LocalConfig


def get_workspace_path() -> Path:
    def _get_workspace_path(path: Path) -> Path | None:
        config_path = path / CONFIG_FILENAME
        if config_path.is_file():
            return path
        elif path.parent == path:
            return None
        return _get_workspace_path(path.parent)

    workspace_path = _get_workspace_path(Path.cwd())
    if workspace_path is None:
        sys.exit("yamapan: not in a workspace")
    return workspace_path


def load_config() -> Config:
    with open(get_workspace_path() / CONFIG_FILENAME, "rb") as f:
        return Config.model_validate(tomli.load(f))


def load_local_config() -> LocalConfig:
    with open(get_workspace_path() / LOCAL_CONFIG_FILENAME, "rb") as f:
        return LocalConfig.model_validate(tomli.load(f))


def get_setup_sh_path() -> Path:
    setup_sh = get_workspace_path() / "install" / "setup.sh"
    if setup_sh.is_file():
        return setup_sh
    local_config = load_local_config()
    return local_config.ros_install_prefix / "setup.sh"


def run_command(
    command: str,
    ros_env: bool = False,
    cwd: Path | None = None,
    input: bytes | None = None,
) -> int:
    with subprocess.Popen(
        f"{f'. {get_setup_sh_path()} && ' if ros_env else ''}{command}",
        stdin=None if input is None else subprocess.PIPE,
        shell=True,
        cwd=cwd,
    ) as process:
        try:
            process.communicate(input)
        except KeyboardInterrupt:
            process.send_signal(subprocess.signal.SIGINT)
            process.wait()
        except:
            process.kill()
            raise
        return process.poll()
