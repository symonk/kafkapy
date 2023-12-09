import typing
from collections import namedtuple
from kafka import KafkaAdminClient

class BootstrapServer(namedtuple):
    """An encapsulation of meta data to talk to a broker."""
    host: str = "localhost"
    port: int = 9092

class KafkaClient:
    """Core client for administering the kafka cluster."""

    def __init__(self,
                 bootstrap_servers: typing.Sequence[BootstrapServer],
                 client_id: str,
                 reconnect_backoff_ms: int = 50,
                 reconnect_backoff_max_ms: int = 1000,
                 request_timeout_ms: int = 30_000
                 # Todo: More options to implement.
                 ) -> None:
        self.bootstrap_servers = bootstrap_servers or (BootstrapServer(),)
        self.client_id = client_id
        self.reconnect_backoff_ms = reconnect_backoff_ms
        self.reconnect_backoff_max_ms = reconnect_backoff_max_ms
        self.request_timeout_ms = request_timeout_ms
        self.client = KafkaAdminClient()

    def initialize_client(self) -> KafkaAdminClient:
        """Initialize the client."""
        return KafkaAdminClient(
            self.bootstrap_servers,
            self.client_id,
        )

    def close(self) -> None:
        """Close the underlying client."""
        self.client.close()

    def __enter__():
        ...

    def __exit__():
        ...

    def retrieve_topics() -> ...:
        ...

