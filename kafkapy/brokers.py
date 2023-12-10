import typer
from kafkapy.deco import set_cmd_description
from kafkapy.constants import CommandDescriptions
from kafkapy.utils import client_from_context
from kafkapy.utils import die
import sys
from typing_extensions import Annotated
from typing import List
from kafkapy.constants import AppHelp
import rich

brokers = typer.Typer(help=AppHelp.BROKER_DESCRIPTION, rich_markup_mode="rich")

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


@brokers.command()
@set_cmd_description(CommandDescriptions.BROKER_VIEW_PARTITIONS)
def partitions(ctx: typer.Context, broker_id: Annotated[str, brokers_id_opt]):
    client = client_from_context(ctx)
    broker_data = client.get_partitions_for_broker(broker_id)
    if broker_data is None:
        rich.print("broker has no partitions", file=sys.stderr)
        raise typer.Exit(code=1)
    rich.print(broker_data)


@brokers.command()
@set_cmd_description(CommandDescriptions.BROKER_VIEW_CONSUMER_GROUPS)
def view_consumer_groups(
    ctx: typer.Context, broker_ids: Annotated[str, brokers_id_opt] = None
) -> None:
    ...
