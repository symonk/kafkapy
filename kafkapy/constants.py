from dataclasses import dataclass


@dataclass
class LibraryMeta:
    """Encapsulation of libary meta data."""

    NAME: str = "kafkapy"


# Sub Commands
CHECK_COMMAND_HELP = "[green][bold]CHECK COMMAND[/green][/bold]"
