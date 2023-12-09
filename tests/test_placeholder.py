from kafkapy.main import app
from typer.testing import CliRunner

runner = CliRunner()

def test_placeholder():
    result = runner.invoke(app, ("check", "--help"))
    assert not result.exit_code