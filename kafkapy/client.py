from __future__ import annotations
import typing
import types
from confluent_kafka.admin import AdminClient
from confluent_kafka.admin import ClusterMetadata


class KafkaPyClient:
    """Core client for administering the kafka cluster."""

    def __init__(
        self,
        brokers: typing.Sequence[str],
        client_id: str,
        reconnect_backoff_ms: int = 50,
        reconnect_backoff_max_ms: int = 1000,
        request_timeout_ms: int = 30_000,
        # Todo: More options to implement.
    ) -> None:
        self.bootstrap_servers = brokers or ("localhost:9092",)
        self.client_id = client_id
        self.reconnect_backoff_ms = reconnect_backoff_ms
        self.reconnect_backoff_max_ms = reconnect_backoff_max_ms
        self.request_timeout_ms = request_timeout_ms
        self.client = self.initialize_client()
        self.metadata = ClusterMetadata(**{"bootstrap_servers": self.bootstrap_servers})

    def fetch_all_brokers_metadata(self) -> typing.Set:
        """Fetches the meta data for every broker in the cluster."""
        return self.metadata.brokers()

    def fetch_broker_metadata(
        self, broker_id: int
    ) -> typing.Dict[typing.Any, typing.Any]:
        """Fetch meta data for a particular broker in the cluster."""
        return self.metadata.broker_metadata(broker_id)

    def get_partitions_for_broker(
        self, broker_id: int
    ) -> typing.Dict[typing.Any, typing.Any]:
        return self.metadata.partitions_for_broker(broker_id)

    def initialize_client(self) -> AdminClient:
        """Initialize the client."""
        return AdminClient(
            **{"bootstrap_servers": self.bootstrap_servers, "client_id": self.client_id}
        )

    def create_topics(self, name: str):
        """Create new topic(s)."""
        self.client.create_topics(new_topics=[{"name": name}])

    def close(self) -> None:
        """Close the underlying client."""
        self.client.close()

    def __enter__(self) -> KafkaPyClient:
        return self

    def __exit__(
        self,
        exc_type: typing.Optional[typing.Type[BaseException]] = None,
        exc_value: typing.Optional[BaseException] = None,
        traceback: typing.Optional[types.TracebackType] = None,
    ) -> typing.Optional[bool]:
        self.close()

    def retrieve_topics(
        self, include_internal_topics: bool
    ) -> typing.Dict[typing.Any, typing.Any]:
        topics = self.metadata.topics(
            exclude_internal_topics=not include_internal_topics
        )
        return topics

    def delete_topic(self, name: str) -> typing.Any:
        return self.client.delete_topics(name)

    def retrieve_topic_partitions(
        self, topic: str
    ) -> typing.Dict[typing.Any, typing.Any]:
        return self.metadata.partitions_for_topic(topic)
