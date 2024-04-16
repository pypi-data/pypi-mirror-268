import typer

from gitoptim.utils.cli import console
from gitoptim.utils.tag import TagFactory


def command(ctx: typer.Context):
    """
    Creates a start tag in the logs which starts a section. Sections do not need to be closed.
    """

    console.print(TagFactory.create_start_tag(ctx.obj["name"]))
