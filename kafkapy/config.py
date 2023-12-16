import typing


class KafkaProtocolProperties:
    """An encapsulation of the librdkafka properties."""

    def __init__(self, properties) -> None:
        self.internal_store = {}
        for key, value in properties.items():
            self.internal_store[key] = value

    def lookup(self, key: str, default=None) -> typing.Any:
        """Look up dotted keys on the store for properties."""
        return self.internal_store.get(key, default)

    def as_dict(self) -> typing.Dict[typing.Any, typing.Any]:
        """Return the internal dictionary"""
        return self.internal_store
