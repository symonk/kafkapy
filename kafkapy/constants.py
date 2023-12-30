from dataclasses import dataclass
from typing import NamedTuple


@dataclass
class LibraryMeta:
    """Encapsulation of libary meta data."""

    NAME: str = "kafkapy"
    URL: str = "https://www.github.com/symonk/kafkapy"


class CommandMeta(NamedTuple):
    """Arguments for command descriptions."""

    description: str
    danger: bool = False


class CommandDescriptions:
    """Encapsulation of command descriptions."""

    # broker specifics
    BROKER_LIST = CommandMeta(
        description="Retrieve meta data for some or all brokers", danger=False
    )
    BROKER_VIEW_PARTITIONS = CommandMeta(
        description="Retrieve partitions for which a broker is the leader", danger=False
    )
    BROKER_VIEW_CONSUMER_GROUPS = CommandMeta(
        description="List all consumer groups known to the cluster", danger=False
    )

    # topic specifics
    TOPIC_LIST = CommandMeta(
        description="View the set of known topics, optionally including internal topics"
    )
    TOPIC_DESCRIBE = CommandMeta(description="Describes the topics")
    TOPIC_PARTITIONS = CommandMeta(
        description="View the partitions this broker is a leader of"
    )
    TOPIC_DELETE = CommandMeta(description="Delete a given topic", danger=True)
    TOPIC_DESTROY = CommandMeta(description="Delete ALL topics", danger=True)
    TOPIC_CREATE = CommandMeta(description="Create a new topic")


class OptionDescriptions:
    """Encapsulation of Argument Descriptions."""


APP_NAME__TEMPLATE = "[green][b]{app} Management & Inspection[/green][/b] :star2:"


class AppHelp:
    """Encapsulation of individual app descriptions."""

    ACL_DESCRIPTION = APP_NAME__TEMPLATE.format(app="ACL")
    BROKER_DESCRIPTION = APP_NAME__TEMPLATE.format(app="Broker")
    TOPIC_DESCRIPTION = APP_NAME__TEMPLATE.format(app="Topic")
    CONSUMER_GROUPS_DESCRIPTION = APP_NAME__TEMPLATE.format(app="Consumer Group")


class OptionDefaults:
    """Defaults for reusable options."""

    LOCAL_KAFKA = ["localhost:9092"]
