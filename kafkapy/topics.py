import typer
from typing_extensions import Annotated
import pathlib
import socket
import typing
from kafkapy.options import OPERATION_TIMEOUT
from kafkapy.options import (
    REQUEST_TIMEOUT,
    TIMEOUT_INDEF_SECONDS_OPTION,
    topic_authorized_operations_option,
    TOPIC_PARTITION_OPTION,
    TOPIC_REPLICATION_FACTOR_OPTION,
    TOPIC_REPLICA_ASSIGNMENT_OPTION,
)
from kafkapy.arguments import TOPIC_NAME_ARGUMENT, TOPIC_CONFIG_ARGUMENT
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


@topics.command(help=generate_help(CommandDescriptions.TOPIC_LIST))
def list(
    bootstrap_servers: Annotated[
        typing.List[str], BOOTSTRAP_SERVERS_OPTION
    ] = OptionDefaults.LOCAL_KAFKA,
    properties: Annotated[
        KafkaProtocolProperties, PROPERTIES_FILE_OPTION
    ] = pathlib.Path("~/.kafkapy/properties.yaml"),
    topic: Annotated[str, TOPIC_NAME_ARGUMENT] = None,
    timeout: Annotated[int, TIMEOUT_INDEF_SECONDS_OPTION] = -1,
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
    topics: Annotated[typing.List[str], TOPIC_NAME_ARGUMENT],
    include_authorized_operations: Annotated[
        bool, topic_authorized_operations_option
    ] = False,
    request_timeout: Annotated[float, REQUEST_TIMEOUT] = socket.timeout.ms * 1000,
    bootstrap_servers: Annotated[
        typing.List[str], BOOTSTRAP_SERVERS_OPTION
    ] = OptionDefaults.LOCAL_KAFKA,
    properties: Annotated[
        KafkaProtocolProperties, PROPERTIES_FILE_OPTION
    ] = pathlib.Path("~/.kafkapy/properties.yaml"),
) -> None:
    """Describe a suite of topic(s)."""
    ...


# Todo: Make it work for one, should allow multiple topics.
@topics.command(help=generate_help(CommandDescriptions.TOPIC_CREATE))
def create(
    topic: Annotated[str, TOPIC_NAME_ARGUMENT],
    operation_timeout: Annotated[float, OPERATION_TIMEOUT] = 0,
    request_timeout: Annotated[float, REQUEST_TIMEOUT] = socket.timeout.ms * 1000,
    topic_config: Annotated[typing.Dict, TOPIC_CONFIG_ARGUMENT] = None,
    partitions: Annotated[int, TOPIC_PARTITION_OPTION] = -1,
    replication_factor: Annotated[int, TOPIC_REPLICATION_FACTOR_OPTION] = -1,
    replica_assignment: Annotated[
        typing.List[typing.List[int]],
        TOPIC_REPLICA_ASSIGNMENT_OPTION,
    ] = None,
    bootstrap_servers: Annotated[
        typing.List[str], BOOTSTRAP_SERVERS_OPTION
    ] = OptionDefaults.LOCAL_KAFKA,
    properties: Annotated[
        KafkaProtocolProperties, PROPERTIES_FILE_OPTION
    ] = pathlib.Path("~/.kafkapy/properties.yaml"),
) -> None:
    """Create a new topic.

    :param topics: (Required) The topic data, this should typically be provided as a
    dictionary where the topic name is stored under a 'name' key and additional topic
    is provided.
    :param operation_timeout: ...
    :param request_timeout: ...
    :param topic_config: ...
    :param partitions: ...
    :param replication_factor: ...
    :param replica_assignment: ...
    :param bootstrap_servers: ...
    :param properties: ...
    """
    ...


@topics.command(help=generate_help(CommandDescriptions.TOPIC_DELETE))
def delete(
    topics: Annotated[typing.List[str], TOPIC_NAME_ARGUMENT],
    operation_timeout: Annotated[float, OPERATION_TIMEOUT] = 0,
    request_timeout: Annotated[float, REQUEST_TIMEOUT] = socket.timeout.ms * 1000,
    bootstrap_servers: Annotated[
        typing.List[str], BOOTSTRAP_SERVERS_OPTION
    ] = OptionDefaults.LOCAL_KAFKA,
    properties: Annotated[
        KafkaProtocolProperties, PROPERTIES_FILE_OPTION
    ] = pathlib.Path("~/.kafkapy/properties.yaml"),
) -> None:
    """Delete one or more topics.

    :param topics: ...
    :param operation_timeout: ...
    :param request_timeout: ...
    :param bootstrap_servers: ...
    :param properties: ..."""
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
    """Delete all topics.

    :param bootstrap_servers: ...
    :param properties: ..."""
