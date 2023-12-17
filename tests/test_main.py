from kafkapy import __version__

def test_main_version_exits(root_app, kafkapytester) -> None:
    result = kafkapytester.invoke(root_app, ("--version"))
    assert not result.exit_code
    assert result.stdout == f"Kafkapy {__version__} ⚡\n"