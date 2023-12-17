import typer
from .out import write_out
from kafkapy.__version__ import __version__
from kafkapy.constants import LibraryMeta


def version_callback(value: bool) -> str:
    """Prints the version of kafkapy and exits."""
    if value:
        write_out(
            f"[white][bold]{LibraryMeta.NAME.title()}[/white][/bold] [green][bold]{__version__}[/green][/bold] [yellow][bold]:zap:[/yellow][/bold]"
        )
        raise typer.Exit(code=0)
