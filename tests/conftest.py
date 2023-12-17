from kafkapy.main import app
from typer.testing import CliRunner
import pytest
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
