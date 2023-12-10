import typer
from typing import Annotated
from kafkapy.deco import set_cmd_description
from kafkapy.client import KafkaClient
from kafkapy.constants import CommandDescriptions, AppHelp
import rich

topics = typer.Typer(help=AppHelp.TOPIC_DESCRIPTION, rich_markup_mode="rich")

topics_list_option = typer.Option("--include-internal", help="Display [i]internal[/i] topics in the output.")


@set_cmd_description(CommandDescriptions.TOPIC_VIEW)
@topics.command()
def list(
    ctx: typer.Context,
    include_internal: Annotated[bool, topics_list_option] = False,
) -> None:
    client: KafkaClient = ctx.obj
    topics = client.retrieve_topics(include_internal_topics=include_internal)
    rich.print(topics)


@set_cmd_description(CommandDescriptions.TOPIC_PARTITIONS)
@topics.command()
def partitions(ctx: typer.Context, topic: Annotated[str, typer.Option(help="The topic to lookup")]) -> None:
    client: KafkaClient = ctx.obj
    partitions = client.retrieve_topic_partitions(topic)
    rich.print(partitions)


@set_cmd_description(CommandDescriptions.TOPIC_DELETE)
@topics.command()
def delete():
    ...


@set_cmd_description(CommandDescriptions.TOPIC_DESTROY)
@topics.command()
def destroy():
    ...


@set_cmd_description(CommandDescriptions.TOPIC_CREATE)
@topics.command()
def create(ctx: typer.Context):
    ...
