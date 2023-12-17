import typer
from kafkapy.deco import set_cmd_description
from kafkapy.constants import CommandDescriptions
from kafkapy.utils import client_from_context
from kafkapy.utils import die
from typing_extensions import Annotated
from typing import List
from kafkapy.constants import AppHelp
import rich

brokers = typer.Typer(
    name="brokers",
    help=AppHelp.BROKER_DESCRIPTION,
    rich_markup_mode="rich",
)

brokers_id_opt = typer.Option("--broker-id", help="The broker ID to check")


@brokers.command()
@set_cmd_description(CommandDescriptions.BROKER_LIST)
def list(ctx: typer.Context, broker_ids: Annotated[List[str], brokers_id_opt] = None):
    client = client_from_context(ctx)
    if broker_ids:
        results = [client.fetch_broker_metadata(broker_id) for broker_id in broker_ids]
    else:
        results = [client.fetch_all_brokers_metadata()]
    if results.count(None) == len(results):
        die(code=1, message="No broker meta data available.")
    rich.print(results)
