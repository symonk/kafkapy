from __future__ import annotations
from confluent_kafka.admin import AdminClient
from kafkapy.config import KafkaProtocolProperties


class KafkaPyClient(AdminClient):
    """A Wrapper to interact with kafka resources.  This client
    provides access to all the brokers and all the resource
    types supported by the brokers.
    """

    def __init__(self, configuration: KafkaProtocolProperties):
        super().__init__(configuration.as_dict())
