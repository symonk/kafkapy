import pytest
from confluent_kafka.admin import KafkaException

from tests.markers import RequiresDockerKafka

pytestmark = pytest.mark.requires_kafka

def test_omitted_bootstrap_servers_reads_from_config() -> None:
    ...

def test_provided_bootstrap_servers_overwrite_config() -> None:
    ...

def test_if_no_properties_file_is_provided_look_in_default_dir() -> None:
    ...

def test_if_default_config_exists_and_not_provided_default_is_used() -> None:
    ...

def test_default_properties_dir_is_overwritable_from_environment() -> None:
    # Todo: This is not possible right now.
    ...
    

@RequiresDockerKafka
def test_bootstrap_servers_is_handled_correctly(root_app, kafkapytester) -> None:
    with pytest.raises(KafkaException, match=r".*Failed to get metadata: Local: Broker transport failure"):
        result = kafkapytester.invoke(root_app, ("topics", "list", "--bootstrap-servers", "localhost:1234", "--bootstrap-servers", "localhost:4321", "--timeout", "5.0"), catch_exceptions=False)
        assert result.exit_code == 1
        assert result.return_value is None

@RequiresDockerKafka
def test_invalid_bootstrap_servers(root_app, kafkapytester) -> None:
    result = kafkapytester.invoke(root_app, ("topics", "list", "--bootstrap-servers", "local:host:1234", "--timeout", "5.0"))
    assert result.exit_code
    assert "Invalid value for '--bootstrap-servers':" in result.stdout