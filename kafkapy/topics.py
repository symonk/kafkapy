import typer
from typing import Annotated
from colors import in_white
from client import KafkaClient
import rich

topics_app = typer.Typer(help="Manage Topics")


@topics_app.command(rich_help_panel=in_white("Topic Inspection & Management :snake:"))
def list(
    ctx: typer.Context,
    include_internal: Annotated[
        bool, typer.Option("--include-internal", help="Include internal kafka topics.")
    ] = False,
) -> None:
    """[blue]List all available topics and exit.[/blue]"""
    client: KafkaClient = ctx.obj
    topics = client.retrieve_topics(include_internal_topics=include_internal)
    rich.print(topics)


@topics_app.command()
def create(ctx: typer.Context):
    ...
