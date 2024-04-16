import subprocess
from typing import Annotated

import typer

from gitoptim.utils.cli import console
from gitoptim.utils.tag import TagFactory

COMMAND_HELP = "Command to be executed inside section."


def escape_argument(arg: str) -> str:
    # TODO: Improve escaping
    return arg if " " not in arg else f'"{arg}"'


def sh_command_to_str(sh_command: list[str]) -> str:
    return " ".join(map(escape_argument, sh_command))


def command(ctx: typer.Context,
            sh_command: Annotated[list[str], typer.Argument(help=COMMAND_HELP)]):
    """
    Executes a command inside a section.

    The following command:
    $ gitoptim tag --name "name" wrap -- command arg1 [arg2 ...]

    is just a syntax sugar for:
    $ gitoptim tag --name "name" start
    $ command arg1 [arg2 ...]
    $ gitoptim tag --name "name" end
    """

    console.print(TagFactory.create_start_tag(ctx.obj["name"]))
    execution = subprocess.run(sh_command, check=False, capture_output=True, text=True, shell=False)
    console.print(f"$ {sh_command_to_str(sh_command)}")
    console.print(execution.stdout, end="")
    console.print(TagFactory.create_end_tag(ctx.obj["name"]))
