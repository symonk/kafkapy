import typing
from collections import UserDict


class KafkaProtocolProperties(UserDict):
    """An encapsulation of the librdkafka properties."""

    def __init__(self, properties: typing.Dict[str, typing.Any]) -> None:
        super().__init__(properties)
