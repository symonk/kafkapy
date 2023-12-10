import typing


class Text:
    """Represents some renderable text."""

    def __init__(self, text: str) -> None:
        self.text = text

    def render(self) -> str:
        return self.text


class BoldText(Text):
    """Wraps the text in bold."""

    def __init__(self, wrapped: Text) -> None:
        self._wrapped = wrapped

    def render(self) -> str:
        return f"[bold]{self._wrapped.render()}[/bold]"


class ItalicText(Text):
    """Wraps the text in italic."""

    def __init__(self, wrapped: Text) -> None:
        self._wrapped = wrapped

    def render(self) -> str:
        return f"[italic]{self._wrapped.render()}[/italic]"


class ColouredText(Text):
    """Wraps the text in a particular colour."""

    def __init__(self, wrapped: Text, colour: str) -> None:
        self._wrapped = wrapped
        self.colour = colour

    def render(self) -> str:
        return f"[{self.colour}]{self._wrapped.render()}[/{self.colour}]"


def text_wrap(
    text: str,
    colour: typing.Optional[str] = None,
    bold: bool = False,
    italic: bool = False,
) -> str:
    """The entrypoint for generating various pieces of text."""
    tag = Text(text)
    if colour:
        tag = ColouredText(tag, colour=colour)
    if bold:
        tag = BoldText(tag)
    if italic:
        tag = ItalicText(tag)
    return tag.render()
