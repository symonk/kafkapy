import typing
from dataclasses import dataclass

from confluent_kafka import KafkaException
from pydantic import BaseModel
from pydantic import ConfigDict


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
class SerializableTopicMetaData:
    """Serializable Topic Meta Data."""

    topic: str
    partitions: typing.List[PartitionMeta]
    error: typing.Optional[KafkaException]


class ClusterMetaData(BaseModel):
    """Serializable container for Topic Meta Data."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    brokers: typing.List[BrokerMeta]
    cluster_id: str
    topics: typing.List[SerializableTopicMetaData]
