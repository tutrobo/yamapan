import shutil
from argparse import Namespace

from yamapan import subcommand
from yamapan.util import get_workspace_path


@subcommand("clean")
def clean(_: Namespace) -> int:
    workspace_path = get_workspace_path()
    shutil.rmtree(workspace_path / "build", ignore_errors=True)
    shutil.rmtree(workspace_path / "install", ignore_errors=True)
    shutil.rmtree(workspace_path / "log", ignore_errors=True)
    return 0
