import typer
from typing_extensions import Annotated

from .acls import acls_application
from .brokers import brokers_application
from .constants import LibraryMeta
from .consumer_groups import consumer_groups_application
from .options import VERSION_OPTION
from .topics import topics_application

root_application = typer.Typer(
    help="Python CLI for managing kafka clusters.",
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["--help", "-h"]},
)
root_application.add_typer(topics_application)
root_application.add_typer(consumer_groups_application)
root_application.add_typer(acls_application)
root_application.add_typer(brokers_application)


root_help = f":star2: [green][bold]Kafkapy Loaded.[/][/] [b]Homepage: [green][b][link={LibraryMeta.URL}]{LibraryMeta.URL}[/link][/][/]"


@root_application.callback(help=root_help)
def root(
    version: Annotated[bool, VERSION_OPTION] = False,
):
    """The core entrypoint point.  Responsible for basic app initialization
    and handling of commands that typically report and exit.  Right now this is
    only responsible for handling the version and exiting."""
