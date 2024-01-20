from __future__ import annotations

import types
import typing
from concurrent.futures import CancelledError
from concurrent.futures import TimeoutError

from confluent_kafka.admin import AdminClient
from confluent_kafka.admin import KafkaException

from ..properties import KafkaProtocolProperties
from .models import ClusterMetaData
from .models import DeletedTopicsModel


class KafkaPyClient:
    """A Wrapper to interact with kafka resources.  This client
    provides access to all the brokers and all the resource
    types supported by the brokers.  This client implements
    json serializable types to allow seamless of piping kafkapy
    output into various other tools, such as `jq` etc.
    """

    def __init__(
        self,
        bootstrap_servers: typing.Optional[typing.Sequence[str]],
        properties: KafkaProtocolProperties,
    ):
        self.properties = self.merge_bootstrap_servers(properties, bootstrap_servers)
        self.client = AdminClient(self.properties.data)

    def merge_bootstrap_servers(
        self,
        properties: KafkaProtocolProperties,
        bootstrap_servers: typing.Optional[typing.Sequence[str]],
    ) -> KafkaProtocolProperties:
        """Updates properties in place if bootstrap_servers has been provided by the user.

        :param bootstrap_servers: The sequence of broker addresses.
        """
        if not bootstrap_servers:
            # They might of only been provided in the properties file and not on the CLI.
            return properties
        properties["bootstrap.servers"] = ",".join(bootstrap_servers)
        return properties

    def describe_topics(self) -> None:
        """Describe Some topics...
        Todo: impl"""

    def list_topics(
        self,
        topic: typing.Optional[str] = None,
        timeout: float = -1.0,
    ) -> ClusterMetaData:
        """Fetch topic meta data from the cluster.

        :param topic: (Optional) topic name to fetch only the data for, otherwise fetches all topics.
        :param timeout: The timeout for read/connect operations to the cluster, defaults to infinite (-1).

        # Todo: This is not sufficient, futures may not be finished?
        """
        return ClusterMetaData.from_response(
            self.client.list_topics(
                topic=topic,
                timeout=timeout,
            )
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

    def __exit__(
        self,
        exc_type: typing.Optional[typing.Type[BaseException]] = None,
        exc: typing.Optional[BaseException] = None,
        traceback: typing.Optional[types.TracebackType] = None,
    ) -> typing.Optional[bool]:
        # Todo: Does the underlying client need closed? nothing in it's public API for now.
        ...
