import typer
from typing_extensions import Annotated
import typing
from kafkapy.deco import set_cmd_description
from kafkapy.utils import client_from_context
from kafkapy.constants import CommandDescriptions, AppHelp
from kafkapy.out import write_out

# Todo:
# list_topics
# describe topics
# create topics
# delete topics


topics = typer.Typer(help=AppHelp.TOPIC_DESCRIPTION, rich_markup_mode="rich")

topics_list_option = typer.Option(
    "--include-internal", help="Display [i]internal[/i] topics in the output."
)

topic_name_option = typer.Option(
    "--topic",
    help="The particular topic to lookup information of, all topics if not provided.",
)

timeout_seconds_option = typer.Option(
    "--timeout", help="The maximum response time before timing out, forever by default"
)


@set_cmd_description(CommandDescriptions.TOPIC_VIEW)
@topics.command()
def list(
    ctx: typer.Context,
    topic: Annotated[str, topic_name_option] = None,
    timeout: Annotated[int, timeout_seconds_option] = -1,
) -> None:
    client = client_from_context(ctx)
    topics = client.list_topics(topic=topic, timeout=timeout)
    write_out(topics.topics)


@set_cmd_description(CommandDescriptions.TOPIC_DESCRIBE)
@topics.command()
def describe(
    ctx: typer.Context,
    topics: Annotated[typing.List[str], typer.Option("--topics")] = None,
    timeout: Annotated[int, timeout_seconds_option] = 30_000,
):
    client = client_from_context(ctx)
    topic_response = client.describe_topics()
    write_out(topic_response)
