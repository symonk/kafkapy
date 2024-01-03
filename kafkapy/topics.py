import pathlib
import socket
import typing

import typer
from typing_extensions import Annotated

from .constants import AppHelp
from .constants import CommandDescriptions
from .constants import OptionDefaults
from .help import generate_help
from .options import BOOTSTRAP_SERVERS_OPTION
from .options import OPERATION_TIMEOUT
from .options import PROPERTIES_FILE_OPTION
from .options import REQUEST_TIMEOUT
from .options import TIMEOUT_INDEF_SECONDS_OPTION
from .options import TOPIC_AUTHORIZED_OPERATIONS_OPTION
from .options import TOPIC_CONFIG_OPTION
from .options import TOPIC_NAME_OPTION
from .options import TOPIC_PARTITION_OPTION
from .options import TOPIC_REPLICA_ASSIGNMENT_OPTION
from .options import TOPIC_REPLICATION_FACTOR_OPTION
from .out import write_json_out
from .properties import KafkaProtocolProperties
from .utils import get_client

topics_application = typer.Typer(
    name="topics",
    help=AppHelp.TOPIC_DESCRIPTION,
    rich_markup_mode="rich",
)


@topics_application.command(help=generate_help(CommandDescriptions.TOPIC_LIST))
def list(
    topic: Annotated[str, TOPIC_NAME_OPTION],
    bootstrap_servers: Annotated[
        typing.List[str], BOOTSTRAP_SERVERS_OPTION
    ] = OptionDefaults.LOCAL_KAFKA,
    properties: Annotated[
        KafkaProtocolProperties, PROPERTIES_FILE_OPTION
    ] = pathlib.Path("~/.kafkapy/properties.yaml"),
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


@topics_application.command(help=generate_help(CommandDescriptions.TOPIC_DESCRIBE))
def describe(
    topics: Annotated[typing.List[str], TOPIC_NAME_OPTION],
    include_authorized_operations: Annotated[
        bool, TOPIC_AUTHORIZED_OPERATIONS_OPTION
    ] = False,
    request_timeout: Annotated[float, REQUEST_TIMEOUT] = socket.timeout.ms * 1000,
    bootstrap_servers: Annotated[
        typing.List[str], BOOTSTRAP_SERVERS_OPTION
    ] = OptionDefaults.LOCAL_KAFKA,
    properties: Annotated[
        KafkaProtocolProperties, PROPERTIES_FILE_OPTION
    ] = pathlib.Path("~/.kafkapy/properties.yaml"),
) -> None:
    """Describe a suite of topic(s).

    :param topics: (Required) ...
    :param include_authorized_operations: ...
    :param request_timeout: ...
    :param bootstrap_servers: ...
    :param properties: ...
    """
    ...


# Todo: Make it work for one, should allow multiple topics.
@topics_application.command(help=generate_help(CommandDescriptions.TOPIC_CREATE))
def create(
    topic_config: Annotated[typing.Dict, TOPIC_CONFIG_OPTION],
    topic: Annotated[str, TOPIC_NAME_OPTION],
    operation_timeout: Annotated[float, OPERATION_TIMEOUT] = 0,
    request_timeout: Annotated[float, REQUEST_TIMEOUT] = socket.timeout.ms * 1000,
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


@topics_application.command(help=generate_help(CommandDescriptions.TOPIC_DELETE))
def delete(
    topics: Annotated[typing.List[str], TOPIC_NAME_OPTION],
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


@topics_application.command(help=generate_help(CommandDescriptions.TOPIC_DESTROY))
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
