from kafkapy import __version__

def test_main_version_exits(root_app, kafkapytester) -> None:
    result = kafkapytester.invoke(root_app, ("--version"))
    assert not result.exit_code
    assert result.stdout == f"Kafkapy {__version__} ⚡\n"


def test_dash_dash_help(root_app, kafkapytester) -> None:
    result = kafkapytester.invoke(root_app, ("--help"))
    assert result.stderr_bytes is None
    assert not result.exit_code


def test_dash_h_is_enabled(root_app, kafkapytester) -> None:
    result = kafkapytester.invoke(root_app, ("-h"))
    assert not result.exit_code