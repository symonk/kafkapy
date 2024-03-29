import pytest
import typer

from kafkapy.callbacks import bootstrap_servers_callback


def test_bootstrap_servers_are_split_correctly() -> None:
    result = bootstrap_servers_callback(["localhost:1234", "localhost:4321"])
    assert result == ["localhost:1234", "localhost:4321"]


def test_no_bootstrap_server_returns_empty_list() -> None:
    assert bootstrap_servers_callback(None) is None


def test_invalid_bootstrap_server_errors() -> None:
    with pytest.raises(typer.BadParameter, match="cannot contain more than 1 ':'"):
        bootstrap_servers_callback(["local:host:1234"])
