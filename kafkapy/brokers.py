from typing import List

import typer
from typing_extensions import Annotated

from .constants import AppHelp
from .constants import CommandDescriptions
from .help import generate_help

brokers_application = typer.Typer(
    name="brokers",
    help=AppHelp.BROKER_DESCRIPTION,
    rich_markup_mode="rich",
)

brokers_id_opt = typer.Option("--broker-id", help="The broker ID to check")


@brokers_application.command(help=generate_help(CommandDescriptions.BROKER_LIST))
def list(ctx: typer.Context, broker_ids: Annotated[List[str], brokers_id_opt] = None):
    ...
