from kafkapy.text import text_wrap

def test_plain_text() -> None:
    assert text_wrap("foo") == "foo"


def test_bold_text() -> None:
    assert text_wrap("foo", bold=True) == "[bold]foo[/bold]"


def test_italic_text() -> None:
    assert text_wrap("foo", italic=True) == "[italic]foo[/italic]"


def test_coloured_text() -> None:
    assert text_wrap("foo", colour="white") == "[white]foo[/white]"


def test_multiple_wrappers() -> None:
    actual = text_wrap(text="foo", colour="blue", bold=True, italic=True)
    assert actual == "[italic][bold][blue]foo[/blue][/bold][/italic]"