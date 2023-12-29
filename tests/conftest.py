from kafkapy.main import app
from typer.testing import CliRunner
import pathlib
import pytest
from pytest_docker.plugin import Services
test_runner = CliRunner()


@pytest.fixture()
def kafkapytester() -> CliRunner:
    """Return the cli runner utility that can be used for executing
    the application in a subprocess and interrogating exit and std 
    streams etc."""
    return test_runner


@pytest.fixture()
def root_app():
    """Return the root (parent) app of kafkapy."""
    return app


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig: pytest.Config):
    """Custom fixture for allowing the docker-compose.yml to reside outside
     of the tests directory."""
    return pathlib.Path(str(pytestconfig.rootdir)) / "docker-compose.yml"

@pytest.fixture(scope="session")
def kafka_service(docker_ip: str, docker_services: Services):
    """Ensure that the kafka service is up and responsive."""
    port = docker_services.port_for("kafka0", 9092)
    # Todo: Add health check support for kafka services.
