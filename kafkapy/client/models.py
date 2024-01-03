import json
import typing
from dataclasses import asdict
from dataclasses import dataclass

from confluent_kafka import KafkaException
from confluent_kafka.admin import BrokerMetadata


@dataclass(frozen=True)
class SerializableBrokerMetaData:
    """Serializable Broker Meta Data."""

    host: str
    port: int
    broker_id: int


@dataclass(frozen=True)
class SerializablePartitionmetaData:
    """Serializable Partition Meta Data."""

    partition_id: int
    leader: int
    replicas: typing.List[int]
    in_sync_replicas: typing.List[int]
    error: typing.Optional[KafkaException] = None


@dataclass(frozen=True)
class SerializableTopicMetaData:
    """Serializable Topic Meta Data."""

    topic: str
    partitions: typing.List[SerializablePartitionmetaData]
    error: typing.Optional[KafkaException]


@dataclass(frozen=True)
class SerializableClusterMetaData:
    """Serializable container for Topic Meta Data."""

    brokers: typing.Dict[int, BrokerMetadata]
    cluster_id: str
    topics: typing.List[SerializableTopicMetaData]

    def as_json(self) -> str:
        return json.dumps(asdict(self))
