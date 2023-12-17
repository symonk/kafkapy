from kafkapy.client import KafkaPyClient
from kafkapy.config import KafkaProtocolProperties
import typing
from kafkapy.out import die
from confluent_kafka.error import KafkaError
import typer


def client_from_context(
    ctx: typer.Context, properties: typing.Optional[KafkaProtocolProperties] = None
) -> KafkaPyClient:
    """Setup the client within the shared context for use throughout command
    invocations.  This is handled via the main callback.  If not client has
    been set initially, this will create one and attach it to the context.

    :param ctx: The typer context object.
    :param config: (optional) kafkapy config object, required on initialization only."""
    return KafkaPyClient(properties)
    if ctx.obj is None:
        if properties is None:
            # Todo: Make this better..
            die(1, "Critical Error initializing client.")
        try:
            client = KafkaPyClient(properties)
        except KafkaError as err:
            die(message=err, code=1)
        ctx.obj = client
        return client
    else:
        return ctx.obj
