import typer
from typing_extensions import Annotated
import pathlib
import typing
from kafkapy.options import PROPERTIES_FILE_OPTION
from kafkapy.properties import KafkaProtocolProperties
from kafkapy.options import BOOTSTRAP_SERVERS_OPTION
from kafkapy.constants import OptionDefaults
from kafkapy.utils import get_client
from kafkapy.constants import CommandDescriptions, AppHelp
from kafkapy.out import write_json_out
from kafkapy.help import generate_help

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


@topics.command(help=generate_help(CommandDescriptions.TOPIC_LIST))
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
    """Fetches topic meta data.  This includes information about the brokers,
    cluster_id and topic partition data, including leader, replic and in sync replica
    data.

    :param bootstrap_servers: The kafka broker addresses for bootstrapping client connections.
    :param properties: The properties.yaml file path, defaults to ~/.kafkapy/properties.yaml.
    :param topic: A specific topic to fetch, if omitted all topic data is returned.
    :param timeout: The timeout for read/connect timeouts, if omitted will try indefinitely."""
    with get_client(
        properties=properties,
        bootstrap_servers=bootstrap_servers,
    ) as client:
        topic_metadata = client.list_topics(
            topic=topic,
            timeout=timeout,
        )
        write_json_out(topic_metadata)


@topics.command(help=generate_help(CommandDescriptions.TOPIC_DESCRIBE))
def describe(
    bootstrap_servers: Annotated[
        typing.List[str], BOOTSTRAP_SERVERS_OPTION
    ] = OptionDefaults.LOCAL_KAFKA,
    properties: Annotated[
        KafkaProtocolProperties, PROPERTIES_FILE_OPTION
    ] = pathlib.Path("~/.kafkapy/properties.yaml"),
) -> None:
    ...


@topics.command(help=generate_help(CommandDescriptions.TOPIC_CREATE))
def create(
    bootstrap_servers: Annotated[
        typing.List[str], BOOTSTRAP_SERVERS_OPTION
    ] = OptionDefaults.LOCAL_KAFKA,
    properties: Annotated[
        KafkaProtocolProperties, PROPERTIES_FILE_OPTION
    ] = pathlib.Path("~/.kafkapy/properties.yaml"),
) -> None:
    ...


@topics.command(help=generate_help(CommandDescriptions.TOPIC_DELETE))
def delete(
    bootstrap_servers: Annotated[
        typing.List[str], BOOTSTRAP_SERVERS_OPTION
    ] = OptionDefaults.LOCAL_KAFKA,
    properties: Annotated[
        KafkaProtocolProperties, PROPERTIES_FILE_OPTION
    ] = pathlib.Path("~/.kafkapy/properties.yaml"),
) -> None:
    ...


@topics.command(help=generate_help(CommandDescriptions.TOPIC_DESTROY))
def destroy(
    bootstrap_servers: Annotated[
        typing.List[str], BOOTSTRAP_SERVERS_OPTION
    ] = OptionDefaults.LOCAL_KAFKA,
    properties: Annotated[
        KafkaProtocolProperties, PROPERTIES_FILE_OPTION
    ] = pathlib.Path("~/.kafkapy/properties.yaml"),
) -> None:
    ...
