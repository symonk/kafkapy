from dataclasses import dataclass
from typing import NamedTuple


@dataclass
class LibraryMeta:
    """Encapsulation of libary meta data."""

    NAME: str = "kafkapy"


class CommandMeta(NamedTuple):
    """Arguments for command descriptions."""

    description: str
    danger: bool = False


class CommandDescriptions:
    """Encapsulation of command descriptions."""

    # broker specifics
    BROKER_VIEW = CommandMeta(description="Retrieve meta data for some or all brokers", danger=False)
    BROKER_VIEW_PARTITIONS = CommandMeta(
        description="Retrieve partitions for which a broker is the leader", danger=False
    )
    BROKER_VIEW_CONSUMER_GROUPS = CommandMeta(description="List all consumer groups known to the cluster", danger=False)

    # topic specifics
    TOPIC_VIEW = CommandMeta(description="View the set of known topics, optionally including internal topics")
    TOPIC_PARTITIONS = CommandMeta(description="View the partitions this broker is a leader of")
    TOPIC_DELETE = CommandMeta(description="Delete a given topic", danger=True)
    TOPIC_DESTROY = CommandMeta(description="Delete ALL topics", danger=True)
    TOPIC_CREATE = CommandMeta(description="Create a new topic")


# Sub Commands
CHECK_COMMAND_HELP = "[green][bold]CHECK COMMAND[/green][/bold]"
