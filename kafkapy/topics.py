import typer
from typing import Annotated
from kafkapy.client import KafkaClient
import rich

topics_app = typer.Typer(
    help=":star2: [green][bold]Topic Inspection & Management[/green][/bold]", rich_markup_mode="rich"
)

topics_list_option = typer.Option("--include-internal", help="Display [i]internal[/i] topics in the output.")


@topics_app.command()
def list(
    ctx: typer.Context,
    include_internal: Annotated[bool, topics_list_option] = False,
) -> None:
    """[b][white]View the set of known topics, optionally including internal topics.[/white][b]"""
    client: KafkaClient = ctx.obj
    topics = client.retrieve_topics(include_internal_topics=include_internal)
    rich.print(topics)


@topics_app.command()
def delete():
    ...


@topics_app.command()
def create(ctx: typer.Context):
    """[b][white]Create new topics[/b][/white]"""
