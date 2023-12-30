import typer
from kafkapy.deco import set_cmd_description
from kafkapy.constants import CommandDescriptions
from typing_extensions import Annotated
from typing import List
from kafkapy.constants import AppHelp

brokers = typer.Typer(
    name="brokers",
    help=AppHelp.BROKER_DESCRIPTION,
    rich_markup_mode="rich",
)

brokers_id_opt = typer.Option("--broker-id", help="The broker ID to check")


@brokers.command()
@set_cmd_description(CommandDescriptions.BROKER_LIST)
def list(ctx: typer.Context, broker_ids: Annotated[List[str], brokers_id_opt] = None):
    ...
