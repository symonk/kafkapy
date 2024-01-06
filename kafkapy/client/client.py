from __future__ import annotations

import typing
from concurrent.futures import CancelledError
from concurrent.futures import TimeoutError

from confluent_kafka.admin import AdminClient
from confluent_kafka.admin import ClusterMetadata
from confluent_kafka.admin import KafkaException

from ..properties import KafkaProtocolProperties
from .models import BrokerMeta
from .models import ClusterMetaData
from .models import DeletedTopicsModel
from .models import PartitionMeta
from .models import SerializableTopicMetaData


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
    ) -> typing.List[ClusterMetaData]:
        """Fetch topic meta data from the cluster.

        :param topic: (Optional) topic name to fetch only the data for, otherwise fetches all topics.
        :param timeout: The timeout for read/connect operations to the cluster, defaults to infinite (-1).

        # Todo: This is not sufficient, futures may not be finished?
        """
        response: ClusterMetadata = self.client.list_topics(
            topic=topic,
            timeout=timeout,
        )
        return ClusterMetaData(
            cluster_id=response.cluster_id,
            brokers=[
                BrokerMeta(host=broker.host, port=broker.port, broker_id=broker.id)
                for broker in response.brokers.values()
            ],
            topics=[
                SerializableTopicMetaData(
                    topic=name,
                    partitions=[
                        PartitionMeta(
                            partition_id=partition.id,
                            leader=partition.leader,
                            replicas=partition.replicas,
                            in_sync_replicas=partition.isrs,
                            error=partition.error,
                        )
                        for partition in meta_data.partitions.values()
                    ],
                    error=meta_data.error,
                )
                for name, meta_data in response.topics.items()
            ],
        )

    def delete_topics(
        self,
        topics: typing.List[str],
        operation_timeout: float,
        request_timeout: float,
    ) -> DeletedTopicsModel:
        """Delete one or more topics.

        :param topics: The sequence of topics to delete.
        :param operation_timeout: The operation timeout in seconds, controlling how long the request will
        block on the broker waiting for the topic deletion to propagate in the cluster.
        :param request_timeout: The overall request timeout in seconds, including broker lookup,
        request transmission, operation time on broker and response.  Default 30 seconds.
        """
        successful, failures = {}, {}
        response = self.client.delete_topics(
            topics=topics,
            operation_timeout=operation_timeout,
            request_timeout=request_timeout,
        )
        for topic, future in response.items():
            try:
                _ = future.result()
            except (KafkaException, TimeoutError, CancelledError) as exc:
                failures[topic] = str(exc)
            else:
                successful[topic] = ""
        return DeletedTopicsModel(successes=successful, failures=failures)

    def __enter__(self) -> KafkaPyClient:
        """Allow the client to be used as a context."""
        return self

    def __exit__(self, *args, **kwargs) -> bool:
        # Todo: Implement types etc.
        return

    def close(self) -> None:
        """Close the underlying client"""
        ...
