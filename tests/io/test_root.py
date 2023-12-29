"""Reusable tests shared by multiple commands."""


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
    

def test_bootstrap_servers_is_handled_correctly(root_app, kafkapytester, kafka_service) -> None:
    result = kafkapytester.invoke(root_app, ("topics", "list", "--bootstrap-servers", "localhost:1234", "--bootstrap-servers", "localhost:4321"))
    assert not result.exit_code 

def test_invalid_bootstrap_servers(root_app, kafkapytester, kafka_service) -> None:
    result = kafkapytester.invoke(root_app, ("topics", "list", "--bootstrap-servers", "local:host:1234"))
    assert result.exit_code == 2 
    assert "Invalid value for '--bootstrap-servers':" in result.stdout
    assert "local:host:1234 can only contain at most a single colon ':'." in result.stdout