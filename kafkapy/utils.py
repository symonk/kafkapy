from kafkapy.client import KafkaPyClient
from kafkapy.config import KafkaProtocolProperties
from kafkapy.types import BootstrapServersTypes, BootstrapServersSplitTypes
import typing


def get_client(
    bootstrap_servers: typing.Optional[typing.Sequence[str]] = None,
    properties: typing.Optional[KafkaProtocolProperties] = None,
) -> KafkaPyClient:
    """Setup the client within the shared context for use throughout command
    invocations.  This is handled via the main callback.  If not client has
    been set initially, this will create one and attach it to the context.

    :param ctx: The typer context object.
    :param config: (optional) kafkapy config object, required on initialization only."""
    return KafkaPyClient(properties)


def split_bootstrap_servers(
    servers: BootstrapServersTypes,
) -> BootstrapServersSplitTypes:
    """Splits the provided bootstrap servers into a tuple of
    (host, port) tuples.

    :param servers: The user provided bootstrap servers."""
