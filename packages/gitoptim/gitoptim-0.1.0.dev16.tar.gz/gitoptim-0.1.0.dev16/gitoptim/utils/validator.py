from typing import Optional

import typer

from gitoptim.utils.cli import error_console


def validate_name(name: Optional[str]):
    if name is not None and len(name) == 0:
        error_console.print("Name cannot be empty.")
        raise typer.Exit(code=1)

    if name is not None and name.isalnum() is False:
        error_console.print("Name can only contain letters and numbers.")
        raise typer.Exit(code=1)

    return name
