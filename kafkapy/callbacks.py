from rich import print 
import typer
from __version__ import __version__
from constants import LibraryMeta

def version_callback(value: bool) -> str:
    """Prints the version of kafkapy and exits."""
    if value:
        print(f"[white][bold]{LibraryMeta.NAME.title()}[/white][/bold] [green][bold]{__version__}[/green][/bold] [yellow][bold]:zap:[/yellow][/bold]")
        raise typer.Exit(code=0)
