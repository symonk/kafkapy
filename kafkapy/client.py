from __future__ import annotations
from dataclasses import dataclass
from confluent_kafka.admin import AdminClient
from confluent_kafka.error import KafkaException
from kafkapy.properties import KafkaProtocolProperties
import typing


class KafkaPyClient:
    """A Wrapper to interact with kafka resources.  This client
    provides access to all the brokers and all the resource
    types supported by the brokers.  This client implements
    json serializable types to allow seamless of piping kafkapy
    output into various other tools, such as `jq` etc.
    """

    def __init__(
        self,
        properties: KafkaProtocolProperties,
    ):
        self.client = AdminClient(properties.data)

    def list_topics(
        self,
        topic: typing.Optional[str] = None,
        timeout: float = -1,
    ) -> typing.List[SerializableClusterMetaData]:
        """Fetch topic meta data from the cluster.

        :param topic: (Optional) topic name to fetch only the data for, otherwise fetches all topics.
        :param timeout: The timeout for read/connect operations to the cluster, defaults to infinite (-1).
        """
        response = self.client.list_topics(
            topic=topic,
            timeout=timeout,
        )
        return response

    def __enter__(self) -> KafkaPyClient:
        """Allow the client to be used as a context."""
        return self

    def __exit__(self, *args, **kwargs) -> bool:
        # Todo: Implement types etc.
        return

    def close(self) -> None:
        """Close the underlying client"""
        ...


@dataclass(frozen=True)
class TopicMetadata:
    """A Serializable piece of topic meta data."""

    error: KafkaException
    partitions: int
    topic: str


@dataclass(frozen=True)
class SerializableClusterMetaData:
    """Json serializable topic meta data."""

    brokers: typing.Dict
    cluster_id: str
    topics: typing.List[TopicMetadata]
