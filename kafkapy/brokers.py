import typer
from kafkapy.text import text_wrap
from kafkapy.client import KafkaClient
from typing import Annotated
import rich

brokers_app = typer.Typer(help="Manage Brokers")


@brokers_app.command(rich_help_panel=text_wrap("Topic Inspection & Management :snake:"))
def list_all(ctx: typer.Context) -> None:
    """[blue]List all available brokers and exit.[/blue]"""
    client: KafkaClient = ctx.obj
    broker_data = client.broker_metadata
    rich.print(broker_data)


@brokers_app.command()
def list(ctx: typer.Context, broker_id: Annotated[str, typer.Option(help="The broker ID to check")]):
    client: KafkaClient = ctx.obj
    broker_data = client.get_broker_metadata(broker_id)
    rich.print(broker_data)
