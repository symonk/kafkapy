from __future__ import annotations

import typing
from dataclasses import dataclass

from confluent_kafka import KafkaException
from pydantic import BaseModel
from pydantic import ConfigDict

from ..types import StringDictTypes


class BrokerMeta(BaseModel):
    """A Serializable"""

    host: str
    port: int
    broker_id: int


class PartitionMeta(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    partition_id: int
    leader: int
    replicas: typing.List[int]
    in_sync_replicas: typing.List[int]
    error: typing.Optional[KafkaException] = None


@dataclass(frozen=True)
class TopicMetaData:
    """Serializable Topic Meta Data."""

    topic: str
    partitions: typing.List[PartitionMeta]
    error: typing.Optional[KafkaException]


class ClusterMetaData(BaseModel):
    """Serializable container for Topic Meta Data."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    brokers: typing.List[BrokerMeta]
    cluster_id: str
    topics: typing.List[TopicMetaData]

    @classmethod
    def from_response(cls, response: typing.Any) -> ClusterMetaData:
        return ClusterMetaData(
            cluster_id=response.cluster_id,
            brokers=[
                BrokerMeta(host=broker.host, port=broker.port, broker_id=broker.id)
                for broker in response.brokers.values()
            ],
            topics=[
                TopicMetaData(
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


class DeletedTopicsModel(BaseModel):
    """The topics deleted by a call to the delete subcommand of topics.

    :param successes: The topics, successfully deleted.
    :param failures: The topics which failed to delete."""

    successes: StringDictTypes
    failures: StringDictTypes
