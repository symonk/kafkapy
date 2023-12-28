import typer
from typing_extensions import Annotated
from kafkapy.constants import LibraryMeta
from kafkapy.topics import topics
from kafkapy.consumer_groups import consumers
from kafkapy.brokers import brokers
from kafkapy.acls import acls
from kafkapy.arg_opts import VERSION_OPTION

app = typer.Typer(
    help="Python CLI for managing kafka clusters.",
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["--help", "-h"]},
)
app.add_typer(topics)
app.add_typer(consumers)
app.add_typer(acls)
app.add_typer(brokers)


root_help = f":star2: [green][bold]Kafkapy Loaded.[/][/] [b]Homepage: [green][b][link={LibraryMeta.URL}]{LibraryMeta.URL}[/link][/][/]"


@app.callback(help=root_help)
def root(
    version: Annotated[bool, VERSION_OPTION] = False,
):
    """The core entrypoint point.  Responsible for basic app initialization
    and handling of commands that typically report and exit.  Right now this is
    only responsible for handling the version and exiting."""


if __name__ == "__main__":
    app()
