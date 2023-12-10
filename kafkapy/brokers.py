import typer
from kafkapy.client import KafkaClient
import sys
from typing import Annotated
import rich

brokers_app = typer.Typer(
    help=":star2: [green][bold]Broker Inspection & Management[/green][/bold]", rich_markup_mode="rich"
)


@brokers_app.command()
def list_all(ctx: typer.Context) -> None:
    """:star2: [white][b]List all available brokers and exit.[/b][/white]"""
    client: KafkaClient = ctx.obj
    broker_data = client.broker_metadata
    rich.print(broker_data)


@brokers_app.command()
def list(ctx: typer.Context, broker_id: Annotated[str, typer.Option(help="The broker ID to check")]):
    """:star2: [white][b]Retrieve information for the given broker id[/b][/white]"""
    client: KafkaClient = ctx.obj
    broker_data = client.get_broker_metadata(broker_id)
    if broker_data is None:
        rich.print(f"No such broker with id: {broker_id}, use brokers list-all to view all available.", file=sys.stderr)
        raise typer.Exit(code=1)
    rich.print(broker_data)
