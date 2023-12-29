

def test_bootstrap_servers_is_handled_correctly(root_app, kafkapytester, kafka_service) -> None:
    result = kafkapytester.invoke(root_app, ("topics", "list", "--bootstrap-servers", "localhost:1234", "--bootstrap-servers", "localhost:4321"))
    assert not result.exit_code 

def test_invalid_bootstrap_servers(root_app, kafkapytester, kafka_service) -> None:
    result = kafkapytester.invoke(root_app, ("topics", "list", "--bootstrap-servers", "local:host:1234"))
    assert result.exit_code == 2 
    assert "Invalid value for '--bootstrap-servers':" in result.stdout
    assert "local:host:1234 can only contain at most a single colon ':'." in result.stdout
