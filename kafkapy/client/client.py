from __future__ import annotations
from confluent_kafka.admin import AdminClient
from confluent_kafka.admin import ClusterMetadata
from .models import SerializableClusterMetaData, TopicMetadata
from ..properties import KafkaProtocolProperties
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
        response: ClusterMetadata = self.client.list_topics(
            topic=topic,
            timeout=timeout,
        )
        return SerializableClusterMetaData(
            brokers=response.brokers,
            cluster_id=response.cluster_id,
            topics=[
                TopicMetadata(
                    topic=name,
                    partitions=meta_data.partitions,
                    error=meta_data.error,
                )
                for name, meta_data in response.topics.items()
            ],
        )

    def __enter__(self) -> KafkaPyClient:
        """Allow the client to be used as a context."""
        return self

    def __exit__(self, *args, **kwargs) -> bool:
        # Todo: Implement types etc.
        return

    def close(self) -> None:
        """Close the underlying client"""
        ...
