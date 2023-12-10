import typer
from kafkapy.client import KafkaClient
import sys
from typing import Annotated
import rich

brokers = typer.Typer(
    help=":star2: [green][bold]Broker Inspection & Management[/green][/bold]", rich_markup_mode="rich"
)

brokers_id_opt = typer.Option("--broker-id", help="The broker ID to check")


@brokers.command()
def list_all(ctx: typer.Context) -> None:
    """:star2: [white][b]List all available brokers and exit.[/b][/white]"""
    client: KafkaClient = ctx.obj
    broker_data = client.broker_metadata
    rich.print(broker_data)


@brokers.command()
def list(ctx: typer.Context, broker_id: Annotated[str, brokers_id_opt]):
    """:star2: [white][b]Retrieve information for the given broker id[/b][/white]"""
    client: KafkaClient = ctx.obj
    broker_data = client.get_broker_metadata(broker_id)
    if broker_data is None:
        rich.print(f"No such broker with id: {broker_id}, use brokers list-all to view all available.", file=sys.stderr)
        raise typer.Exit(code=1)
    rich.print(broker_data)


@brokers.command()
def lead_partitions(
    ctx: typer.Context,
    broker_id: Annotated[str, brokers_id_opt],
):
    """:star2: [white][b]Retrieve partitions for which this broker is the leader of.[/white][/b]"""
    client: KafkaClient = ctx.obj
    broker_data = client.get_partitions_for_broker(broker_id)
    if broker_data is None:
        rich.print("broker has no partitions", file=sys.stderr)
        raise typer.Exit(code=1)
    rich.print(broker_data)
