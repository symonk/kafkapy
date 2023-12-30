import typing
from dataclasses import dataclass
from confluent_kafka import KafkaException


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
