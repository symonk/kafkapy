from kafkapy.client import KafkaPyClient
from kafkapy.properties import KafkaProtocolProperties
import typing


def get_client(
    properties: KafkaProtocolProperties,
    bootstrap_servers: typing.Optional[typing.Sequence[str]] = None,
) -> KafkaPyClient:
    """Setup the client within the shared context for use throughout command
    invocations.  This is handled via the main callback.  If not client has
    been set initially, this will create one and attach it to the context.

    :param bootstrap_servers: (Optional) The sequence of broker host:port addresses.
    :param properties: The properties object with librdkafka settings.
    """
    if bootstrap_servers:
        properties["bootstrap.servers"] = ",".join(bootstrap_servers)
    return KafkaPyClient(properties)
