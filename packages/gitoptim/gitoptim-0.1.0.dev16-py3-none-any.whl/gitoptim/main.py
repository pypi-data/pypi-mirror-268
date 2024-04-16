import typer

from gitoptim import commands
from gitoptim.utils.cli import should_callback_execute

app = typer.Typer(rich_markup_mode="rich")
app.add_typer(commands.analyse.app, name="analyse")
app.add_typer(commands.tag.app, name="tag")


@app.callback()
def main():
    """
    Gitoptim SDK
    """

    if not should_callback_execute():
        return


app.command(name="memlab")(commands.memlab)
