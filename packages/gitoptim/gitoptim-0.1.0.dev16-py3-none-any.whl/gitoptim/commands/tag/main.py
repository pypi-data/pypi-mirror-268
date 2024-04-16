from typing import Annotated

import typer

from gitoptim.utils import validator
from gitoptim.utils.cli import should_callback_execute

from .end import command as end
from .start import command as start
from .wrap import command as wrap

app = typer.Typer(rich_markup_mode="rich")


@app.callback()
def main(ctx: typer.Context, name: Annotated[str, typer.Option(help="name", callback=validator.validate_name)] = None):
    """
    Creates sections in the logs to be used for analysis.

    Example:
    $ gitoptim tag --name "all" start
    $ gitoptim tag --name "install" start
    $ npm install
    $ gitoptim tag --name "install" end
    $ gitoptim tag start
    $ npm run test
    $ gitoptim tag end
    $ gitoptim analyse logs --last-section
    $ gitoptim analyse logs --name "install"
    $ gitoptim analyse logs --name "all"

    In the example first execution of `gitoptim analyse` will analyse logs from `npm run test`. Second execution of
    `gitoptim analyse` will analyse logs from `npm install`. Last execution of `gitoptim analyse` will analyse all the
    logs. Note that the same can be accomplished by using just `gitoptim analyse logs` as this is the default behaviour.
    """

    if not should_callback_execute():
        return

    ctx.obj = {"name": name}


app.command(name="start")(start)
app.command(name="end")(end)
app.command(name="wrap")(wrap)
