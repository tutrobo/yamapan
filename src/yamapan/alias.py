import sys
from argparse import Namespace

from yamapan import subcommand
from yamapan.util import get_workspace_path, load_config, run_command


@subcommand("alias")
def alias(namespace: Namespace, args: list[str]) -> int:
    workspace_path = get_workspace_path()
    config = load_config()
    alias = config.aliases.get(namespace.name)
    if alias is None:
        sys.exit(f"yamapan: alias not found: '{namespace.name}'")
    return run_command(
        f"{alias} {' '.join(args)}",
        cwd=workspace_path,
    )


alias.add_argument("name", help="alias name")
