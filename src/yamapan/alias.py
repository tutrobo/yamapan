import sys
from argparse import Namespace

from yamapan import subcommand
from yamapan.util import get_workspace_path, load_config, run_command


@subcommand("alias")
def alias(args: Namespace) -> int:
    workspace_path = get_workspace_path()
    config = load_config()
    alias = config.aliases.get(args.name)
    if alias is None:
        sys.exit(f"yamapan: alias not found: '{args.name}'")
    return run_command(
        f"{alias} {' '.join(args.args)}",
        cwd=workspace_path,
    )


alias.add_argument("name", help="alias name")
alias.add_argument("args", nargs="*", help="passed to the aliased command")
