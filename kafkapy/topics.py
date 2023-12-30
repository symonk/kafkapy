import typer
from typing_extensions import Annotated
import pathlib
import typing
from kafkapy.options import PROPERTIES_FILE_OPTION
from kafkapy.properties import KafkaProtocolProperties
from kafkapy.options import BOOTSTRAP_SERVERS_OPTION
from kafkapy.deco import set_cmd_description
from kafkapy.constants import OptionDefaults
from kafkapy.utils import get_client
from kafkapy.constants import CommandDescriptions, AppHelp
from kafkapy.out import write_out

# Todo:
# describe topics
# create topics
# delete topics


topics = typer.Typer(
    name="topics",
    help=AppHelp.TOPIC_DESCRIPTION,
    rich_markup_mode="rich",
)

topic_name_option = typer.Option(
    "--topic",
    help="The particular topic to lookup information of, all topics if not provided.",
)

timeout_seconds_option = typer.Option(
    "--timeout",
    help="The maximum response time before timing out, forever by default",
)


@set_cmd_description(CommandDescriptions.TOPIC_VIEW)
@topics.command()
def list(
    bootstrap_servers: Annotated[
        typing.List[str], BOOTSTRAP_SERVERS_OPTION
    ] = OptionDefaults.LOCAL_KAFKA,
    properties: Annotated[
        KafkaProtocolProperties, PROPERTIES_FILE_OPTION
    ] = pathlib.Path("~/.kafkapy/properties.yaml"),
    topic: Annotated[str, topic_name_option] = None,
    timeout: Annotated[int, timeout_seconds_option] = -1,
) -> None:
    with get_client(
        properties=properties,
        bootstrap_servers=bootstrap_servers,
    ) as client:
        topic_metadata = client.list_topics(
            topic=topic,
            timeout=timeout,
        )
        write_out(topic_metadata)
