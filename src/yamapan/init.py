from argparse import Namespace

from yamapan import subcommand
from yamapan.config import (
    CONFIG_FILENAME,
    CONFIG_TEMPLATE,
    GITIGNORE_TEMPLATE,
)


@subcommand("init")
def init(namespace: Namespace, args: list[str]) -> int:
    with open(CONFIG_FILENAME, "w") as f:
        f.write(CONFIG_TEMPLATE)
    with open(".gitignore", "w") as f:
        f.write(GITIGNORE_TEMPLATE)
    return 0
