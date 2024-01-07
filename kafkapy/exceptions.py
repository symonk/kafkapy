"""Custom Kafkapy exceptions.  The exception hierarchy of kafkapy is outlined below:
KafkaPyError
    + KafkaConnectionException
    + ...
"""


class KafkaConnectionException:
    """Raised when any IO problems occur connecting to the bootstrap server(s)"""
