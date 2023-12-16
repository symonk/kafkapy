class KafkaProtocolProperties:
    """An encapsulation of the librdkafka properties."""

    def __init__(self, properties) -> None:
        for key, value in properties.items():
            setattr(self, key, value)
