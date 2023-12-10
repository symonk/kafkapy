import typer
from kafkapy.client import KafkaClient
from kafkapy.deco import set_cmd_description
from kafkapy.constants import CommandDescriptions
import sys
from typing_extensions import Annotated
from kafkapy.constants import AppHelp
import rich

brokers = typer.Typer(help=AppHelp.BROKER_DESCRIPTION, rich_markup_mode="rich")

brokers_id_opt = typer.Option("--broker-id", help="The broker ID to check")


@set_cmd_description(CommandDescriptions.BROKER_VIEW)
@brokers.command()
def list(ctx: typer.Context, broker_id: Annotated[str, brokers_id_opt] = None):
    client: KafkaClient = ctx.obj
    fn = (
        client.broker_metadata
        if broker_id is None
        else client.get_broker_metadata(broker_id)
    )
    broker_data = fn()
    if broker_data is None:
        rich.print(
            f"No such broker with id: {broker_id}, use brokers list-all to view all available.",
            file=sys.stderr,
        )
        raise typer.Exit(code=1)
    rich.print(broker_data)


@set_cmd_description(CommandDescriptions.BROKER_VIEW_PARTITIONS)
@brokers.command()
def partitions(ctx: typer.Context, broker_id: Annotated[str, brokers_id_opt]):
    client: KafkaClient = ctx.obj
    broker_data = client.get_partitions_for_broker(broker_id)
    if broker_data is None:
        rich.print("broker has no partitions", file=sys.stderr)
        raise typer.Exit(code=1)
    rich.print(broker_data)


@set_cmd_description(CommandDescriptions.BROKER_VIEW_CONSUMER_GROUPS)
@brokers.command()
def view_consumer_groups(
    ctx: typer.Context, broker_ids: Annotated[str, brokers_id_opt] = None
) -> None:
    ...
