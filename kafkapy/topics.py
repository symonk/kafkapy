import typer
from typing_extensions import Annotated
from kafkapy.deco import set_cmd_description
from kafkapy.utils import client_from_context
from kafkapy.opts import timeout_ms_opt
from kafkapy.constants import CommandDescriptions, AppHelp
import rich

topics = typer.Typer(help=AppHelp.TOPIC_DESCRIPTION, rich_markup_mode="rich")

topics_list_option = typer.Option(
    "--include-internal", help="Display [i]internal[/i] topics in the output."
)

topic_name_option = typer.Option("--name", help="The topic name to delete.")


@set_cmd_description(CommandDescriptions.TOPIC_VIEW)
@topics.command()
def list(
    ctx: typer.Context, include_internal: Annotated[bool, topics_list_option] = False
) -> None:
    client = client_from_context(ctx)
    topics = client.list_topics(include_internal_topics=include_internal)
    rich.print(topics)


@set_cmd_description(CommandDescriptions.TOPIC_PARTITIONS)
@topics.command()
def partitions(
    ctx: typer.Context, topic: Annotated[str, typer.Option(help="The topic to lookup")]
) -> None:
    client = client_from_context(ctx)
    partitions = client.retrieve_topic_partitions(topic)
    rich.print(partitions)


@set_cmd_description(CommandDescriptions.TOPIC_DELETE)
@topics.command()
def delete(
    ctx: typer.Context,
    name: Annotated[str, topic_name_option],
    timeout_ms: Annotated[int, timeout_ms_opt] = 30_000,
) -> None:
    client = client_from_context(ctx)
    response = client.delete_topic(name=name)
    rich.print(response)


@set_cmd_description(CommandDescriptions.TOPIC_DESTROY)
@topics.command()
def destroy(ctx: typer.Context):
    client = client_from_context(ctx)
    client.destroy_topics()


@set_cmd_description(CommandDescriptions.TOPIC_CREATE)
@topics.command()
def create(
    ctx: typer.Context,
    validate_only: Annotated[
        bool, typer.Option("--validate-only", help="Validate Only!")
    ] = False,
):
    client = client_from_context(ctx)
    client.create_topics("foo")
