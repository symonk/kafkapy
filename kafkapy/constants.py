from dataclasses import dataclass


@dataclass
class LibraryMeta:
    """Encapsulation of libary meta data."""

    NAME: str = "kafkapy"
    VERSION: str = "0.1.0"


# Sub Commands
CHECK_COMMAND_HELP = "[green][bold]CHECK COMMAND[/green][/bold]"
