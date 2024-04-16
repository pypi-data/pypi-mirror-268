import typer

from gitoptim.utils.cli import console
from gitoptim.utils.tag import TagFactory


def command(ctx: typer.Context):
    """
    Creates an end tag in the logs which ends a section.
    """

    console.print(TagFactory.create_end_tag(ctx.obj["name"]))
