from kafkapy.main import root_application
from typer.testing import CliRunner
import pathlib
import pytest
import typing
from pytest_docker.plugin import Services
from confluent_kafka.admin import KafkaException
from kafkapy import KafkaPyClient
from kafkapy import KafkaProtocolProperties
test_runner = CliRunner(mix_stderr=True)


@pytest.fixture()
def kafkapytester() -> CliRunner:
    """Return the cli runner utility that can be used for executing
    the application in a subprocess and interrogating exit and std 
    streams etc."""
    return test_runner


@pytest.fixture()
def root_app():
    """Return the root (parent) app of kafkapy."""
    return root_application


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig: pytest.Config):
    """Custom fixture for allowing the docker-compose.yml to reside outside
     of the tests directory.
     
     :param pytestconfig: The pytest.Config object (auto injected)."""
    return pathlib.Path(str(pytestconfig.rootdir)) / "docker-compose.yml"

@pytest.fixture(scope="session")
def kafka_container(docker_ip: str, docker_services: Services):
    """Ensure that the kafka service is up and responsive.
    This will be guaranteed before dependent tests will run.
    
    :param docker_ip: The IP addreses for TCP connectivity to the docker service(s)
    :param docker_services: The wrapper to interact with services directly."""
    port = docker_services.port_for("kafka0", 9092)
    expected = ("first", "second", "third")
    docker_services.wait_until_responsive(timeout=30.0, pause=2.0, check=lambda: has_topics_in_response(f"localhost:{port}", expected))

@pytest.fixture(scope="session")
def docker_cleanup() -> str:
    """A Custom docker cleanup command that will tear down associated kafka volumes.
    Overrwrites the default from pytest-docker.""" 
    return "down --volumes --remove-orphans"

def has_topics_in_response(addr: str, topics: typing.Tuple[str]) -> bool:
    """Predicate for checking topics exist on the cluster.
    
    :param addr: The address (TCP) to talk to the cluster.
    :param topics: The sequence of topics that must exist."""
    with KafkaPyClient(properties=KafkaProtocolProperties({f"bootstrap.servers": addr})) as client:
        try:
            topics_response = client.list_topics(timeout=5)
            parsed_topics = set([t.topic for t in topics_response.topics])
            return all(topic in parsed_topics for topic in parsed_topics)
        except KafkaException:
            return False