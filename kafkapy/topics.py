import typer
from typing import Annotated
from kafkapy.client import KafkaClient
import rich

topics = typer.Typer(help=":star2: [green][bold]Topic Inspection & Management[/green][/bold]", rich_markup_mode="rich")

topics_list_option = typer.Option("--include-internal", help="Display [i]internal[/i] topics in the output.")


@topics.command()
def list(
    ctx: typer.Context,
    include_internal: Annotated[bool, topics_list_option] = False,
) -> None:
    """[b][white]View the set of known topics, optionally including internal topics.[/white][b]."""
    client: KafkaClient = ctx.obj
    topics = client.retrieve_topics(include_internal_topics=include_internal)
    rich.print(topics)


@topics.command()
def partitions(ctx: typer.Context, topic: Annotated[str, typer.Option(help="The topic to lookup")]) -> None:
    """[b][white]List all partitions for the topic (whether available or not)[/b][/white]."""
    client: KafkaClient = ctx.obj
    partitions = client.retrieve_topic_partitions(topic)
    rich.print(partitions)


@topics.command()
def delete():
    ...


@topics.command()
def create(ctx: typer.Context):
    """[b][white]Create new topics[/b][/white]"""
