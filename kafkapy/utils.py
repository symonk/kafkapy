from kafkapy.client import KafkaPyClient
from kafkapy.config import Configuration
import typing
from kafkapy.out import die
from kafka.errors import KafkaError
import typer


def client_from_context(
    ctx: typer.Context, config: typing.Optional[Configuration] = None
) -> KafkaPyClient:
    """Setup the client within the shared context for use throughout command
    invocations.  This is handled via the main callback.  If not client has
    been set initially, this will create one and attach it to the context.

    :param ctx: The typer context object.
    :param config: (optional) kafkapy config object, required on initialization only."""
    if ctx.obj is None:
        if config is None:
            # Todo: Make this better..
            die(1, "Critical Error initializing client.")
        try:
            client = KafkaPyClient(brokers=config.brokers, client_id=config.client_id)
        except KafkaError as err:
            die(message=err, code=1)
        ctx.obj = client
    else:
        return ctx.obj
