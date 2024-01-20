import pytest

RequiresDockerKafka = pytest.mark.usefixtures("kafka_container")
