import sys

from rich.console import Console

SUBCOMMAND_NAMES = ["analyse"]


def should_callback_execute():
    """
    Makes sure callback logic is not executed when running commands like:
    - `gitoptim`
    - `gitoptim --help`
    - `gitoptim analyse`
    """
    return "--help" not in sys.argv and sys.argv[-1] not in SUBCOMMAND_NAMES


console = Console()
error_console = Console(stderr=True, style="bold red")
